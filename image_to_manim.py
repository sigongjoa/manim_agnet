import cv2
import numpy as np
from manim import * # Assuming manim is installed and available

class ImageToManim:
    def __init__(self, image_path: str, **config):
        self.image_path = image_path
        self.config = {
            "class_name": "VectorizedScene",
            "max_lines": 500,
            "line_color": WHITE, # Use Manim's WHITE
            "animation_style": "Create", # Or ShowCreation
            **config
        }
        self.lines_data = [] # To store transformed Manim line data

    def generate_script(self, output_path: str):
        # 1. Load image
        gray_image = self._load_image()
        img_height, img_width = gray_image.shape[:2]

        # 2. Detect lines
        raw_lines = self._detect_lines(gray_image)

        # Sort lines by length and take top N if max_lines is set
        if self.config["max_lines"] and len(raw_lines) > self.config["max_lines"]:
            # Calculate length for each line to sort
            # Line format: [x1, y1, x2, y2]
            line_lengths = [
                np.sqrt((line[2] - line[0])**2 + (line[3] - line[1])**2)
                for line in raw_lines
            ]
            # Sort by length in descending order and get indices
            sorted_indices = np.argsort(line_lengths)[::-1]
            raw_lines = [raw_lines[i] for i in sorted_indices[:self.config["max_lines"]]]

        # 3. Transform coordinates
        self.lines_data = self._transform_coordinates(raw_lines, img_height, img_width)

        # 4. Generate Manim script content
        class_name = self.config["class_name"]
        line_color = self.config["line_color"]
        animation_style = self.config["animation_style"]

        if not self.lines_data:
            # Handle no lines detected scenario
            script_content = (
                f"from manim import *\n"
                f"import numpy as np\n\n"
                f"class {class_name}(Scene):\n"
                f"    def construct(self):\n"
                f'        text = Text("No lines detected in the image.", font_size=24)\n'
                f"        self.play(Write(text))\n"
                f"        self.wait()\n"
            )
        else:
            # Format line data for embedding in the script
            formatted_line_data = []
            for start_point, end_point in self.lines_data:
                formatted_line_data.append(
                    f"[np.array([{start_point[0]:.4f}, {start_point[1]:.4f}, {start_point[2]:.4f}]), "
                    f"np.array([{end_point[0]:.4f}, {end_point[1]:.4f}, {end_point[2]:.4f}])],"
                )
            lines_str = "\n                ".join(formatted_line_data)

            script_content = f"""from manim import *
import numpy as np

class {class_name}(Scene):
    def construct(self):
        line_data = [
                {lines_str}
        ]

        lines = VGroup(*[
            Line(start, end, color={line_color}) for start, end in line_data
        ])

        self.play({animation_style}(lines), run_time=3)
        self.wait()
"""

        # 5. Write script to file
        with open(output_path, "w") as f:
            f.write(script_content)

        print(f"Manim script generated successfully at {output_path}")

    def _load_image(self) -> np.ndarray:
        """
        Loads the image from self.image_path and converts it to grayscale.
        Raises FileNotFoundError if the image does not exist.
        Raises ValueError if the image cannot be read or is in an unsupported format.
        """
        image = cv2.imread(self.image_path)
        if image is None:
            # Check if file exists to differentiate between FileNotFoundError and ValueError
            try:
                with open(self.image_path, 'rb') as f:
                    pass # File exists but couldn't be read by opencv
                raise ValueError(f"Could not read image file: {self.image_path}. It might be corrupted or in an unsupported format.")
            except FileNotFoundError:
                raise FileNotFoundError(f"Image file not found: {self.image_path}")

        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def _detect_lines(self, image: np.ndarray) -> list:
        """
        Detects line segments in the given grayscale image using OpenCV's LSD.
        Returns a list of detected lines, each as [x1, y1, x2, y2].
        """
        lsd = cv2.createLineSegmentDetector(0)
        lines = lsd.detect(image)[0] # lines is an array of shape (N, 1, 4)
        if lines is None:
            return []
        # Reshape to (N, 4) for easier processing
        return lines.reshape(-1, 4).tolist()

    def _transform_coordinates(self, lines: list, img_height: int, img_width: int) -> list:
        """
        Transforms OpenCV pixel coordinates to Manim's coordinate system.
        Includes centering, y-axis inversion, and scaling to fit Manim's frame.
        """
        transformed_lines = []
        manim_frame_height = config.frame_height # Default 8.0

        # Calculate scale factor to fit the image height into Manim's frame height
        scale_factor = manim_frame_height / img_height

        for x1, y1, x2, y2 in lines:
            # Transform point 1
            mx1 = (x1 - img_width / 2) * scale_factor
            my1 = (img_height / 2 - y1) * scale_factor # Invert Y-axis

            # Transform point 2
            mx2 = (x2 - img_width / 2) * scale_factor
            my2 = (img_height / 2 - y2) * scale_factor # Invert Y-axis

            transformed_lines.append([
                np.array([mx1, my1, 0.]),
                np.array([mx2, my2, 0.])
            ])
        return transformed_lines
