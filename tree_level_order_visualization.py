"""
LeetCode 102번 - Binary Tree Level Order Traversal
BFS를 이용한 레벨 순서 순회 시각화
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class BinaryTreeLevelOrderVisualization(VoiceoverScene):
    """Binary Tree Level Order Traversal 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("LeetCode 102번 - Binary Tree Level Order", font_size=40, font="NanumGothic").to_edge(UP)
        subtitle = Text("BFS를 이용한 레벨 순회", font_size=28, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="이진 트리의 레벨 순서 순회 문제를 시각화합니다. BFS 알고리즘을 사용합니다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 트리 구조 생성
        # 루트 노드
        root_circle = Circle(radius=0.35, color=RED, fill_opacity=0.5)
        root_circle.move_to(UP * 2.5)
        root_label = Text("3", font_size=24, font="NanumGothic", color=WHITE)
        root_label.move_to(UP * 2.5)

        with self.voiceover(text="루트 노드 3부터 시작합니다."):
            self.play(Create(root_circle), Write(root_label))
            self.wait(0.5)

        # 레벨 2 노드들
        left_circle = Circle(radius=0.35, color=BLUE, fill_opacity=0.5)
        left_circle.move_to(LEFT * 2 + UP * 0.8)
        left_label = Text("9", font_size=24, font="NanumGothic", color=WHITE)
        left_label.move_to(LEFT * 2 + UP * 0.8)

        right_circle = Circle(radius=0.35, color=BLUE, fill_opacity=0.5)
        right_circle.move_to(RIGHT * 2 + UP * 0.8)
        right_label = Text("20", font_size=24, font="NanumGothic", color=WHITE)
        right_label.move_to(RIGHT * 2 + UP * 0.8)

        # 루트에서 자식으로 가는 선
        line_left = Line(root_circle.get_center(), left_circle.get_center(), color=WHITE)
        line_right = Line(root_circle.get_center(), right_circle.get_center(), color=WHITE)

        with self.voiceover(text="레벨 2의 노드들: 9와 20입니다."):
            self.play(Create(line_left), Create(line_right))
            self.play(Create(left_circle), Create(right_circle))
            self.play(Write(left_label), Write(right_label))
            self.wait(0.5)

        # 레벨 3 노드들
        left_grand = Circle(radius=0.35, color=GREEN, fill_opacity=0.5)
        left_grand.move_to(RIGHT * 0.8 + DOWN * 1.2)
        left_grand_label = Text("15", font_size=24, font="NanumGothic", color=WHITE)
        left_grand_label.move_to(RIGHT * 0.8 + DOWN * 1.2)

        right_grand = Circle(radius=0.35, color=GREEN, fill_opacity=0.5)
        right_grand.move_to(RIGHT * 3.2 + DOWN * 1.2)
        right_grand_label = Text("7", font_size=24, font="NanumGothic", color=WHITE)
        right_grand_label.move_to(RIGHT * 3.2 + DOWN * 1.2)

        # 20에서 자식으로 가는 선
        line_left_grand = Line(right_circle.get_center(), left_grand.get_center(), color=WHITE)
        line_right_grand = Line(right_circle.get_center(), right_grand.get_center(), color=WHITE)

        with self.voiceover(text="레벨 3의 노드들: 15와 7입니다. 이들은 노드 20의 자식입니다."):
            self.play(Create(line_left_grand), Create(line_right_grand))
            self.play(Create(left_grand), Create(right_grand))
            self.play(Write(left_grand_label), Write(right_grand_label))
            self.wait(0.5)

        # 순회 결과
        with self.voiceover(text="BFS 방식으로 순회하면 각 레벨별로 노드들을 처리합니다."):
            queue_text = Text("Queue 기반 순회", font_size=24, font="NanumGothic").move_to(DOWN * 1.5)
            self.play(Write(queue_text))
            self.wait(0.5)

        with self.voiceover(text="최종 결과는 레벨별 노드들의 값입니다: 3, 그 다음 9와 20, 마지막으로 15와 7입니다."):
            result = Text("결과: [[3], [9, 20], [15, 7]]", font_size=28, font="NanumGothic", color=GREEN).move_to(DOWN * 2.5)
            self.play(Write(result))
            self.wait(2)

        with self.voiceover(text="시청해주셔서 감사합니다!"):
            self.wait(1)


class BinaryTreeBFSDetailed(VoiceoverScene):
    """BFS 알고리즘 상세 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        title = Text("BFS 알고리즘 상세 분석", font_size=44, font="NanumGothic").to_edge(UP)

        with self.voiceover(text="BFS 알고리즘의 상세한 동작 방식을 살펴봅시다."):
            self.play(Write(title))
            self.wait(0.5)

        self.play(FadeOut(title))

        # 알고리즘 스텝
        steps = [
            ("1단계: 루트를 큐에 추가", "queue = [3]"),
            ("2단계: 큐에서 노드를 하나씩 꺼내기", "queue = []"),
            ("3단계: 꺼낸 노드의 자식들을 큐에 추가", "queue = [9, 20]"),
            ("4단계: 다시 반복하기", "queue = [20, 15, 7]"),
            ("5단계: 큐가 빌 때까지 반복", "완료!"),
        ]

        y_pos = UP * 2
        for i, (step, queue_state) in enumerate(steps):
            step_text = Text(step, font_size=24, font="NanumGothic")
            queue_text = Text(queue_state, font_size=20, font="NanumGothic", color=BLUE)

            step_text.move_to(y_pos)
            queue_text.move_to(y_pos - DOWN * 0.5)

            with self.voiceover(text=step):
                self.play(Write(step_text), Write(queue_text))
                self.wait(0.5)

            y_pos -= DOWN * 1.2

        self.wait(1)
