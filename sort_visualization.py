"""
백준 2750번 - 수 정렬하기
버블 정렬 알고리즘의 단계별 시각화
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np


class SortVisualization(VoiceoverScene):
    """수 정렬하기 - 버블 정렬 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("백준 2750번 - 수 정렬하기", font_size=44, font="NanumGothic").to_edge(UP)
        subtitle = Text("버블 정렬 알고리즘의 시각화", font_size=28, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="백준 2750번 수 정렬하기 문제입니다. 버블 정렬 알고리즘을 시각화해봅시다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 배열 시각화
        nums = [5, 2, 8, 1, 9]

        with self.voiceover(text="배열 [5, 2, 8, 1, 9]를 오름차순으로 정렬합니다."):
            array_group = self._create_array_visual(nums, -2)
            self.play(Create(array_group))
            self.wait(0.5)

        # 알고리즘 설명
        with self.voiceover(text="버블 정렬은 인접한 두 원소를 비교하여 큰 원소를 오른쪽으로 이동시키는 알고리즘입니다."):
            algo_text = Text("인접한 원소 비교 → 교환 → 반복", font_size=24, font="NanumGothic", color=YELLOW)
            algo_text.move_to(UP * 1.5)
            self.play(Write(algo_text))
            self.wait(0.5)

        current_nums = nums.copy()
        boxes = self._get_current_boxes(array_group)

        # 첫 번째 Pass
        with self.voiceover(text="첫 번째 패스를 시작합니다. 첫 번째 비교: 5와 2를 비교합니다. 5가 더 크므로 교환합니다."):
            # 5와 2 비교 및 교환
            self.play(boxes[0].animate.set_color(YELLOW), boxes[1].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(Swap(boxes[0], boxes[1]))
            current_nums[0], current_nums[1] = 2, 5
            self.wait(0.3)
            self.play(boxes[0].animate.set_color(BLUE), boxes[1].animate.set_color(BLUE))

        with self.voiceover(text="다음 비교: 5와 8을 비교합니다. 5가 작으므로 교환하지 않습니다."):
            # 5와 8 비교 (교환 안 함)
            self.play(boxes[1].animate.set_color(YELLOW), boxes[2].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(boxes[1].animate.set_color(BLUE), boxes[2].animate.set_color(BLUE))

        with self.voiceover(text="다음 비교: 8과 1을 비교합니다. 8이 더 크므로 교환합니다."):
            # 8과 1 교환
            self.play(boxes[2].animate.set_color(YELLOW), boxes[3].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(Swap(boxes[2], boxes[3]))
            current_nums[2], current_nums[3] = 1, 8
            self.wait(0.3)
            self.play(boxes[2].animate.set_color(BLUE), boxes[3].animate.set_color(BLUE))

        with self.voiceover(text="마지막 비교: 8과 9를 비교합니다. 8이 작으므로 교환하지 않습니다."):
            # 8과 9 비교 (교환 안 함)
            self.play(boxes[3].animate.set_color(YELLOW), boxes[4].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(boxes[3].animate.set_color(BLUE), boxes[4].animate.set_color(BLUE))
            self.wait(0.5)

        # 첫 번째 Pass 완료 - 가장 큰 원소가 끝에 정렬됨
        with self.voiceover(text="첫 번째 패스가 완료되었습니다. 가장 큰 원소 9가 맨 끝에 위치했습니다. 9는 이제 정렬된 것으로 표시합니다."):
            self.play(boxes[4].animate.set_color(GREEN))
            self.wait(0.5)

        # 빠른 진행을 위해 나머지 과정 요약
        with self.voiceover(text="같은 방식으로 계속 진행하면 배열이 정렬됩니다."):
            # 각 Pass마다 한 번씩
            remaining_steps = [
                ("두 번째 패스", [0, 1, 2, 3]),  # 8 정렬됨
                ("세 번째 패스", [0, 1, 2]),      # 5 정렬됨
                ("네 번째 패스", [0, 1]),         # 2 정렬됨
            ]

            for step_name, indices in remaining_steps:
                with self.voiceover(text=f"{step_name}"):
                    for idx in indices:
                        self.play(boxes[idx].animate.set_color(YELLOW), run_time=0.2)
                        self.play(boxes[idx].animate.set_color(BLUE), run_time=0.2)
                    self.wait(0.2)

        # 최종 정렬 결과
        with self.voiceover(text="모든 원소가 정렬되었습니다. 최종 결과는 [1, 2, 5, 8, 9]입니다."):
            for i in range(5):
                self.play(boxes[i].animate.set_color(GREEN))

            result_text = Text("정렬 완료: [1, 2, 5, 8, 9]", font_size=32, font="NanumGothic", color=GREEN)
            result_text.move_to(DOWN * 2)
            self.play(Write(result_text))
            self.wait(2)

        with self.voiceover(text="시청해주셔서 감사합니다!"):
            self.wait(1)

    def _create_array_visual(self, nums, y_pos):
        """배열을 시각화하는 헬퍼 함수"""
        group = VGroup()
        for i, num in enumerate(nums):
            box = Rectangle(width=0.8, height=0.8, color=BLUE, stroke_width=2)
            text = Text(str(num), font_size=28, font="NanumGothic", color=WHITE)
            element = VGroup(box, text)
            element.shift((i * 1.0 - 2.0) * RIGHT + y_pos * UP)
            group.add(element)
        return group

    def _get_current_boxes(self, array_group):
        """현재 배열의 박스들을 반환"""
        boxes = []
        for element in array_group:
            boxes.append(element)
        return boxes


class SortSelectionVisualization(VoiceoverScene):
    """선택 정렬로도 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        title = Text("정렬 알고리즘 비교", font_size=44, font="NanumGothic").to_edge(UP)

        with self.voiceover(text="다양한 정렬 알고리즘이 있습니다. 각각의 특징을 알아봅시다."):
            self.play(Write(title))
            self.wait(0.5)

        self.play(FadeOut(title))

        # 알고리즘 비교
        algorithms = [
            ("버블 정렬", "O(n²)", "간단하지만 느림"),
            ("선택 정렬", "O(n²)", "최소값을 찾아 교환"),
            ("삽입 정렬", "O(n²)", "손으로 카드 정렬하는 방식"),
            ("병합 정렬", "O(n log n)", "분할 정복 방식"),
        ]

        y_pos = UP * 2
        for algo_name, complexity, description in algorithms:
            name_text = Text(algo_name, font_size=24, font="NanumGothic", color=YELLOW)
            complexity_text = Text(f"시간복잡도: {complexity}", font_size=20, font="NanumGothic")
            desc_text = Text(description, font_size=18, font="NanumGothic", color=BLUE)

            name_text.move_to(y_pos)
            complexity_text.move_to(y_pos - DOWN * 0.4)
            desc_text.move_to(y_pos - DOWN * 0.8)

            with self.voiceover(text=f"{algo_name}, {description}"):
                self.play(Write(name_text), Write(complexity_text), Write(desc_text))
                self.wait(0.4)

            y_pos -= DOWN * 1.2

        self.wait(1)
