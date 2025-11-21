"""
LeetCode 1번 - Two Sum
HashMap을 이용한 O(n) 해법 시각화
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class TwoSumVisualization(VoiceoverScene):
    """Two Sum 문제 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("LeetCode 1번 - Two Sum", font_size=48, font="NanumGothic").to_edge(UP)
        subtitle = Text("HashMap을 이용한 O(n) 해법", font_size=32, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="안녕하세요! 오늘은 LeetCode의 대표 문제인 Two Sum을 시각화해보겠습니다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 문제 설명
        problem_desc = Text("주어진 배열에서 두 수의 합이 target이 되는 인덱스 찾기",
                           font_size=28, font="NanumGothic").move_to(UP * 2.5)
        self.play(Write(problem_desc))
        self.wait(0.5)

        # 배열 시각화
        nums = [2, 7, 11, 15]
        target = 9

        with self.voiceover(text="배열은 2, 7, 11, 15이고, 목표 합은 9입니다."):
            # 배열 상자 만들기
            array_group = VGroup()
            boxes = []
            for i, num in enumerate(nums):
                box = Rectangle(width=0.8, height=0.8, color=BLUE, stroke_width=2)
                text = Text(str(num), font_size=32, font="NanumGothic", color=WHITE)
                element = VGroup(box, text)
                element.shift((i * 1.2 - 1.8) * RIGHT + DOWN * 0.5)
                array_group.add(element)
                boxes.append(element)

            self.play(Create(array_group))
            self.wait(1)

        # HashMap 초기화
        with self.voiceover(text="HashMap을 사용하여 각 수와 그 인덱스를 저장합니다."):
            hashmap_title = Text("HashMap", font_size=28, font="NanumGothic").move_to(DOWN * 1.5)
            hashmap_content = Text("{}", font_size=24, font="NanumGothic").move_to(DOWN * 2.2)
            self.play(Write(hashmap_title), Write(hashmap_content))
            self.wait(0.5)

        # 알고리즘 실행
        hashmap = {}

        with self.voiceover(text="첫 번째 수 2를 봅니다. 9 - 2 = 7인데, HashMap에 7이 없으므로 2를 저장합니다."):
            self.play(boxes[0].animate.set_color(YELLOW))
            self.wait(0.5)
            new_hashmap = Text("{2: 0}", font_size=24, font="NanumGothic").move_to(DOWN * 2.2)
            self.play(Transform(hashmap_content, new_hashmap))
            hashmap[2] = 0
            self.wait(0.5)
            self.play(boxes[0].animate.set_color(BLUE))

        with self.voiceover(text="두 번째 수 7을 봅니다. 9 - 7 = 2이고, HashMap에 2가 있습니다!"):
            self.play(boxes[1].animate.set_color(YELLOW))
            self.wait(0.5)

            # 답 찾음
            result_box = Text("2 + 7 = 9 ✓", font_size=32, font="NanumGothic", color=GREEN).move_to(ORIGIN)
            indices_text = Text("인덱스: [0, 1]", font_size=28, font="NanumGothic", color=GREEN).move_to(DOWN * 0.8)

            self.play(Write(result_box))
            self.play(Write(indices_text))
            self.wait(2)

        with self.voiceover(text="HashMap을 사용하면 O(n) 시간에 답을 찾을 수 있습니다. 시청해주셔서 감사합니다!"):
            self.wait(2)


class TwoSumVisualizationExtended(VoiceoverScene):
    """Two Sum 문제 확장 시각화 - 여러 예제"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("Two Sum - 상세 분석", font_size=48, font="NanumGothic").to_edge(UP)

        with self.voiceover(text="Two Sum 문제의 더 자세한 분석을 보겠습니다."):
            self.play(Write(title))
            self.wait(1)

        self.play(FadeOut(title))

        # 알고리즘 설명
        algo_steps = [
            "1단계: 빈 HashMap 생성",
            "2단계: 배열 순회 시작",
            "3단계: 각 수에 대해 complement = target - num 계산",
            "4단계: complement가 HashMap에 있으면 답 반환",
            "5단계: 없으면 현재 수를 HashMap에 저장"
        ]

        for i, step in enumerate(algo_steps):
            step_text = Text(step, font_size=24, font="NanumGothic")
            if i == 0:
                step_text.move_to(UP * 2)
                self.play(Write(step_text))
            else:
                step_text.move_to(UP * (2 - i * 0.6))
                with self.voiceover(text=step):
                    self.play(Write(step_text))
            self.wait(0.3)

        self.wait(1)
