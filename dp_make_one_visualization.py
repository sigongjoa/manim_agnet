"""
백준 1463번 - 1로 만들기
동적계획법을 이용한 최소 연산 횟수 시각화
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class DPMakeOneVisualization(VoiceoverScene):
    """1로 만들기 - DP 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("백준 1463번 - 1로 만들기", font_size=44, font="NanumGothic").to_edge(UP)
        subtitle = Text("동적계획법을 이용한 최소 연산 횟수", font_size=28, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="백준 1463번 1로 만들기 문제입니다. 정수 N을 1로 만드는 최소 연산 횟수를 구합니다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 문제 설명
        with self.voiceover(text="세 가지 연산이 있습니다. 첫째, n을 3으로 나누기. 둘째, n을 2로 나누기. 셋째, n에서 1을 빼기. 단, n은 각 연산을 수행할 수 있을 때만 나누어집니다."):
            ops = [
                Text("연산 1: n ÷ 3 (n이 3의 배수일 때)", font_size=24, font="NanumGothic"),
                Text("연산 2: n ÷ 2 (n이 2의 배수일 때)", font_size=24, font="NanumGothic"),
                Text("연산 3: n - 1", font_size=24, font="NanumGothic"),
            ]

            for i, op in enumerate(ops):
                op.move_to(UP * (2 - i * 0.7))
                self.play(Write(op))
                self.wait(0.3)

            self.wait(0.5)

        # DP 배열 생성 (n=10 예제)
        n = 10
        with self.voiceover(text="N이 10인 경우를 예시로 살펴봅시다. DP 배열을 만들어 각 수에서의 최소 연산 횟수를 저장합니다."):
            # DP 배열 시각화
            dp_boxes = VGroup()
            for i in range(1, n + 1):
                box = Rectangle(width=0.5, height=0.5, color=BLUE, stroke_width=1.5)
                num_text = Text(str(i), font_size=16, font="NanumGothic", color=WHITE)
                box_group = VGroup(box, num_text)
                box_group.shift((i - 5.5) * 0.6 * RIGHT + UP * 0.5)
                dp_boxes.add(box_group)

            self.play(Create(dp_boxes))
            self.wait(0.5)

        # DP 계산 과정 (BFS 기반)
        with self.voiceover(text="동적계획법을 사용하여 각 수에 도달하는 최소 횟수를 계산합니다."):
            dp_values = [0] * 11
            dp_values[1] = 0

            # 1의 최소값 표시
            value_text = Text("dp[1] = 0", font_size=20, font="NanumGothic", color=GREEN)
            value_text.move_to(DOWN * 0.5)
            self.play(Write(value_text))
            self.wait(0.3)

        # 점진적으로 값 채우기
        with self.voiceover(text="2부터 10까지 차례대로 계산합니다."):
            # dp[2] = dp[1] + 1 = 1
            dp_values[2] = 1
            value_text_2 = Text("dp[2] = 1 (2-1)", font_size=20, font="NanumGothic", color=GREEN)
            value_text_2.move_to(DOWN * 0.5)
            self.play(Transform(value_text, value_text_2))
            self.wait(0.3)

            # dp[3] = min(dp[3/3] + 1, dp[3-1] + 1) = 1
            dp_values[3] = 1
            value_text_3 = Text("dp[3] = 1 (3÷3)", font_size=20, font="NanumGothic", color=GREEN)
            value_text_3.move_to(DOWN * 0.5)
            self.play(Transform(value_text_2, value_text_3))
            self.wait(0.3)

        # 10에 도달하는 경로 시각화
        with self.voiceover(text="계속 계산하면 dp[10]은 3이 됩니다. 경로를 보면 10에서 2로 나누어 5가 되고, 5에서 1을 빼 4가 되고, 4를 2로 나누어 2가 되고, 2를 2로 나누어 1이 됩니다."):
            path = Text("경로: 10 → 5 → 4 → 2 → 1", font_size=26, font="NanumGothic", color=YELLOW)
            path.move_to(ORIGIN)
            self.play(Write(path))
            self.wait(0.5)

            ops_count = Text("총 3번의 연산", font_size=26, font="NanumGothic", color=YELLOW)
            ops_count.move_to(DOWN * 0.8)
            self.play(Write(ops_count))
            self.wait(1)

        with self.voiceover(text="이처럼 동적계획법을 사용하면 최소 연산 횟수를 효율적으로 구할 수 있습니다. 시청해주셔서 감사합니다!"):
            self.wait(2)


class DPMakeOneTreeVisualization(VoiceoverScene):
    """1로 만들기 - 트리 구조로 경로 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        title = Text("1로 만들기 - 경로 트리", font_size=44, font="NanumGothic").to_edge(UP)

        with self.voiceover(text="N에서 1로 가는 모든 경로를 트리 형태로 시각화해봅시다."):
            self.play(Write(title))
            self.wait(0.5)

        self.play(FadeOut(title))

        # 루트: 10
        with self.voiceover(text="10에서 시작합니다."):
            root = Circle(radius=0.3, color=RED, fill_opacity=0.6)
            root.move_to(ORIGIN)
            root_label = Text("10", font_size=20, font="NanumGothic", color=WHITE)
            root_label.move_to(ORIGIN)
            self.play(Create(root), Write(root_label))
            self.wait(0.3)

        # 10에서 가능한 연산: 10/2=5, 10-1=9
        with self.voiceover(text="10은 2의 배수이므로 2로 나눌 수 있고, 10에서 1을 뺄 수도 있습니다."):
            # 10/2 = 5
            node_5 = Circle(radius=0.3, color=BLUE, fill_opacity=0.6)
            node_5.move_to(LEFT * 2 + DOWN * 1.2)
            label_5 = Text("5", font_size=20, font="NanumGothic", color=WHITE)
            label_5.move_to(LEFT * 2 + DOWN * 1.2)
            line_5 = Line(root.get_center(), node_5.get_center(), color=WHITE)

            # 10-1 = 9
            node_9 = Circle(radius=0.3, color=BLUE, fill_opacity=0.6)
            node_9.move_to(RIGHT * 2 + DOWN * 1.2)
            label_9 = Text("9", font_size=20, font="NanumGothic", color=WHITE)
            label_9.move_to(RIGHT * 2 + DOWN * 1.2)
            line_9 = Line(root.get_center(), node_9.get_center(), color=WHITE)

            self.play(Create(line_5), Create(node_5), Write(label_5))
            self.play(Create(line_9), Create(node_9), Write(label_9))
            self.wait(0.5)

        # 5에서 가능한 연산: 5-1=4
        with self.voiceover(text="5에서는 1을 빼 4를 만들 수 있습니다."):
            node_4 = Circle(radius=0.3, color=GREEN, fill_opacity=0.6)
            node_4.move_to(LEFT * 2.5 + DOWN * 2.4)
            label_4 = Text("4", font_size=20, font="NanumGothic", color=WHITE)
            label_4.move_to(LEFT * 2.5 + DOWN * 2.4)
            line_4 = Line(node_5.get_center(), node_4.get_center(), color=WHITE)

            self.play(Create(line_4), Create(node_4), Write(label_4))
            self.wait(0.3)

        # 4에서 가능한 연산: 4/2=2
        with self.voiceover(text="4를 2로 나누면 2가 됩니다."):
            node_2 = Circle(radius=0.3, color=YELLOW, fill_opacity=0.6)
            node_2.move_to(LEFT * 2.5 + DOWN * 3.6)
            label_2 = Text("2", font_size=20, font="NanumGothic", color=WHITE)
            label_2.move_to(LEFT * 2.5 + DOWN * 3.6)
            line_2 = Line(node_4.get_center(), node_2.get_center(), color=WHITE)

            self.play(Create(line_2), Create(node_2), Write(label_2))
            self.wait(0.3)

        # 2에서 1로
        with self.voiceover(text="마지막으로 2를 2로 나누면 1에 도달합니다."):
            node_1 = Circle(radius=0.3, color=ORANGE, fill_opacity=0.6)
            node_1.move_to(LEFT * 2.5 + DOWN * 4.8)
            label_1 = Text("1", font_size=20, font="NanumGothic", color=WHITE)
            label_1.move_to(LEFT * 2.5 + DOWN * 4.8)
            line_1 = Line(node_2.get_center(), node_1.get_center(), color=WHITE)

            self.play(Create(line_1), Create(node_1), Write(label_1))
            self.wait(0.5)

        # 최종 경로 강조
        with self.voiceover(text="가장 빠른 경로는 총 3번의 연산입니다: 10에서 2로 나누기, 5에서 1 빼기, 4에서 2로 나누기, 2에서 2로 나누기."):
            path_text = Text("최단 경로: 10 → 5 → 4 → 2 → 1 (3번)", font_size=24, font="NanumGothic", color=GREEN)
            path_text.move_to(DOWN * 0.5 + RIGHT * 3)
            self.play(Write(path_text))
            self.wait(2)
