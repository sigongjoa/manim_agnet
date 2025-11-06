import pytest
import os
import cv2
import numpy as np
from manim import *

from image_to_manim import ImageToManim

# Fixture to create a temporary directory for test files
@pytest.fixture
def tmp_path(tmpdir):
    return str(tmpdir)

# Helper to create a test image with a line
def create_test_image(path, with_line=True):
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    if with_line:
        # Draw a white diagonal line from (10, 10) to (190, 90)
        cv2.line(img, (10, 10), (190, 90), (255, 255, 255), 2)
    cv2.imwrite(path, img)
    return path

# --- Test Cases ---

def test_load_image_success(tmp_path):
    """Test successful image loading and conversion to grayscale."""
    img_path = os.path.join(tmp_path, "line.png")
    create_test_image(img_path)
    converter = ImageToManim(image_path=img_path)
    gray_image = converter._load_image()
    assert isinstance(gray_image, np.ndarray)
    assert len(gray_image.shape) == 2 # Should be grayscale

def test_load_image_not_found():
    """Test FileNotFoundError for non-existent image."""
    converter = ImageToManim(image_path="non_existent_file.png")
    with pytest.raises(FileNotFoundError):
        converter._load_image()

def test_detect_lines_found(tmp_path):
    """Test that lines are detected in an image that has them."""
    img_path = os.path.join(tmp_path, "line.png")
    create_test_image(img_path, with_line=True)
    converter = ImageToManim(image_path=img_path)
    gray_image = converter._load_image()
    lines = converter._detect_lines(gray_image)
    assert isinstance(lines, list)
    assert len(lines) > 0

def test_detect_lines_none(tmp_path):
    """Test that no lines are detected in a blank image."""
    img_path = os.path.join(tmp_path, "blank.png")
    create_test_image(img_path, with_line=False)
    converter = ImageToManim(image_path=img_path)
    gray_image = converter._load_image()
    lines = converter._detect_lines(gray_image)
    assert isinstance(lines, list)
    assert len(lines) == 0

def test_transform_coordinates():
    """Test the coordinate transformation logic with predictable values."""
    converter = ImageToManim(image_path="dummy.png")
    # Image: 200W x 100H. Manim frame height is 8.
    # Scale factor = 8 / 100 = 0.08
    # Line from (10, 10) to (190, 90)
    lines = [[10, 10, 190, 90]]
    img_height, img_width = 100, 200
    transformed = converter._transform_coordinates(lines, img_height, img_width)

    expected_start = np.array([ (10 - 100) * 0.08, (50 - 10) * 0.08, 0 ]) # [-7.2, 3.2, 0]
    expected_end = np.array([ (190 - 100) * 0.08, (50 - 90) * 0.08, 0 ])   # [7.2, -3.2, 0]

    assert len(transformed) == 1
    np.testing.assert_allclose(transformed[0][0], expected_start, atol=1e-4)
    np.testing.assert_allclose(transformed[0][1], expected_end, atol=1e-4)

def test_generate_script_success(tmp_path):
    """Integration test: check if a valid script is generated."""
    img_path = os.path.join(tmp_path, "line.png")
    script_path = os.path.join(tmp_path, "gen_scene.py")
    create_test_image(img_path)

    converter = ImageToManim(image_path=img_path, class_name="TestScene")
    converter.generate_script(output_path=script_path)

    assert os.path.exists(script_path)
    with open(script_path, "r") as f:
        content = f.read()
        assert "class TestScene(Scene):" in content
        assert "line_data = [" in content
        assert "np.array" in content # Check for line data


def test_generate_script_no_lines(tmp_path):
    """Test script generation for an image with no lines."""
    img_path = os.path.join(tmp_path, "blank.png")
    script_path = os.path.join(tmp_path, "gen_scene_no_lines.py")
    create_test_image(img_path, with_line=False)

    converter = ImageToManim(image_path=img_path)
    converter.generate_script(output_path=script_path)

    assert os.path.exists(script_path)
    with open(script_path, "r") as f:
        content = f.read()
        assert 'Text("No lines detected in the image."' in content
