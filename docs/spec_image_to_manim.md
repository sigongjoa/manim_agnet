# 명세: 이미지의 벡터화를 통한 Manim 씬 생성 도구

## 1. 개요

본 문서는 래스터 이미지(PNG, JPG 등)를 분석하여 선분(line segment)을 추출하고, 이를 기반으로 Manim 파이썬 스크립트를 자동 생성하는 도구의 기능 및 기술 사양을 정의합니다.

---

## 2. 기능 명세 (Functional Specification)

### 2.1. 핵심 기능
- 지정된 이미지 파일에서 선분을 검출한다.
- 검출된 선분을 Manim 좌표계에 맞게 변환한다.
- 변환된 데이터를 사용하여, 선분들을 그리는 애니메이션이 포함된 Manim `Scene` 클래스 코드를 파이썬 파일(`.py`)로 생성한다.

### 2.2. 입력 (Inputs)

- **`image_path` (str)**: 필수. 처리할 이미지의 경로.
- **`output_path` (str)**: 필수. 생성될 Manim 스크립트 파일의 경로.
- **`config` (dict)**: 선택. 세부 동작을 제어하는 설정 객체.
    - **`class_name` (str)**: 생성될 Manim 씬의 클래스 이름. 기본값: `VectorizedScene`.
    - **`max_lines` (int)**: 처리할 최대 선분 수. 검출된 선분이 이보다 많을 경우, 길이가 긴 순서대로 상위 N개만 사용한다. 기본값: `500`.
    - **`line_color` (str)**: Manim에서 그려질 선의 색상. 기본값: `manim.WHITE`.
    - **`animation_style` (str)**: 선을 그리는 애니메이션 스타일. `Create` 또는 `ShowCreation` 중 선택. 기본값: `Create`.

### 2.3. 출력 (Output)

- 지정된 `output_path`에 파이썬 파일이 생성된다.
- 파일 내용은 다음과 같은 구조를 가진다:
    ```python
    from manim import *
    import numpy as np

    class VectorizedScene(Scene):
        def construct(self):
            # 좌표 변환을 통해 생성된 라인 데이터
            line_data = [
                # [start_point, end_point], ...
                [np.array([-2., 1., 0.]), np.array([2., -1., 0.])],
                # ...
            ]

            lines = VGroup(*[
                Line(start, end, color=WHITE) for start, end in line_data
            ])

            self.play(Create(lines), run_time=3)
            self.wait()
    ```

### 2.4. 예외 처리 (Error Handling)

- **`FileNotFoundError`**: `image_path`에 해당하는 파일이 없을 경우 발생.
- **`ValueError`**: 지원하지 않는 이미지 형식이거나, 이미지 파일을 읽을 수 없을 때 발생.
- **선분 미검출**: 이미지에서 선분을 하나도 찾지 못했을 경우, 빈 씬 대신 "No lines detected in the image."라는 `Text` 객체를 표시하는 Manim 스크립트를 생성한다.

---

## 3. 기술 명세 (Technical Specification)

### 3.1. 주요 컴포넌트: `ImageToManim` 클래스

전체 로직은 `ImageToManim` 클래스 하나로 캡슐화한다.

```python
class ImageToManim:
    def __init__(self, image_path: str, **config):
        # ...

    def generate_script(self, output_path: str):
        # ...

    def _load_image(self) -> np.ndarray:
        # ...

    def _detect_lines(self, image: np.ndarray) -> list:
        # ...

    def _transform_coordinates(self, lines: list, img_height: int, img_width: int) -> list:
        # ...
```

### 3.2. 좌표 변환 알고리즘 (매우 중요)

OpenCV의 좌표계(좌상단 원점, y축 아래로 증가)를 Manim의 좌표계(중앙 원점, y축 위로 증가)로 변환하고, Manim 카메라 뷰에 맞게 스케일링한다.

1.  **이미지 차원**: 입력 이미지의 높이를 `H_img`, 너비를 `W_img`로 가져온다.
2.  **Manim 프레임 차원**: Manim의 기본 프레임 높이는 `config.frame_height` (기본값 8.0)이다.
3.  **스케일링 팩터 계산**:
    - 이미지의 가로세로 비율을 유지하면서 Manim 프레임에 맞추기 위해 스케일 팩터를 계산한다.
    - `scale_factor = config.frame_height / H_img`
4.  **좌표 변환 공식**:
    - OpenCV 좌표점 `(px, py)`에 대해 Manim 좌표점 `(mx, my)`를 계산한다.
    - **a. 원점 이동**: 이미지의 중심을 원점으로 이동: `(px - W_img / 2, py - H_img / 2)`
    - **b. Y축 반전**: Manim 좌표계에 맞게 Y축을 뒤집는다: `(px - W_img / 2, -(py - H_img / 2))` -> `(px - W_img / 2, H_img / 2 - py)`
    - **c. 스케일링 적용**:
        - `mx = (px - W_img / 2) * scale_factor`
        - `my = (H_img / 2 - py) * scale_factor`
    - **d. 최종 3D 좌표**: Manim은 3D 공간을 사용하므로 z축 값을 0으로 추가: `[mx, my, 0]`

### 3.3. 스크립트 생성 로직

- `generate_script` 메소드는 최종 변환된 라인 데이터 리스트를 파이썬 코드 문자열로 포매팅한다.
- 이 데이터를 `2.3.`에서 정의한 템플릿에 삽입하여 완전한 Manim 스크립트 문자열을 만든다.
- 완성된 문자열을 `output_path`에 파일로 쓴다.

---

## 4. 사용 예시

```python
# main.py
from image_to_manim import ImageToManim

# 설정 정의
config = {
    "class_name": "MyVectorAnimation",
    "max_lines": 300,
    "line_color": "manim.BLUE",
}

# 변환기 생성 및 스크립트 생성
converter = ImageToManim("path/to/my_drawing.png", **config)
converter.generate_script("generated_scene.py")

# 터미널에서 Manim 실행
# manim -pql generated_scene.py MyVectorAnimation
```
