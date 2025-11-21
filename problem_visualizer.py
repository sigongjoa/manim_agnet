"""
AI-powered Coding Problem Visualizer with Manim
자동으로 코딩 문제의 해법을 분석하고 시각화하는 시스템
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from typing import Dict, List, Tuple
import json


class ProblemVisualizer:
    """문제와 해법을 받아서 시각화 정보를 생성하는 클래스"""

    def __init__(self, problem_name: str, problem_type: str, language: str = "ko"):
        self.problem_name = problem_name
        self.problem_type = problem_type  # "array", "tree", "dp", "sort" 등
        self.language = language
        self.visualization_data = {}

    def generate_visualization(self) -> Dict:
        """문제 유형별로 시각화 데이터를 생성"""
        if self.problem_type == "array_hashmap":
            return self._generate_two_sum_viz()
        elif self.problem_type == "tree_bfs":
            return self._generate_tree_level_order_viz()
        elif self.problem_type == "dp":
            return self._generate_dp_viz()
        elif self.problem_type == "sort":
            return self._generate_sort_viz()
        else:
            raise ValueError(f"Unknown problem type: {self.problem_type}")

    def _generate_two_sum_viz(self) -> Dict:
        """Two Sum 문제 시각화 데이터"""
        return {
            "problem_name": "Two Sum",
            "description": "주어진 배열에서 두 개의 수를 더해 target이 되는 인덱스를 찾기",
            "example": {
                "nums": [2, 7, 11, 15],
                "target": 9,
                "output": [0, 1]
            },
            "algorithm": "HashMap",
            "steps": [
                {"step": 1, "description": "빈 HashMap 생성", "action": "create_hashmap"},
                {"step": 2, "description": "배열의 각 원소를 순회하면서 complement(target - num) 찾기", "action": "iterate_array"},
                {"step": 3, "description": "complement가 HashMap에 있으면 답 반환", "action": "find_complement"},
                {"step": 4, "description": "없으면 현재 수를 HashMap에 저장", "action": "store_in_hashmap"}
            ],
            "narration": {
                "ko": [
                    "안녕하세요! 오늘은 Two Sum 문제를 시각화해보겠습니다.",
                    "주어진 배열 [2, 7, 11, 15]에서 합이 9가 되는 두 수의 인덱스를 찾아야 합니다.",
                    "HashMap을 사용하는 효율적인 해법을 보여드리겠습니다.",
                    "먼저 빈 HashMap을 생성합니다.",
                    "배열의 첫 번째 요소 2를 확인합니다. 9 - 2 = 7인데 HashMap에 7이 없으므로 2를 저장합니다.",
                    "다음 요소 7을 확인합니다. 9 - 7 = 2이고, HashMap에 2가 있습니다!",
                    "따라서 인덱스 0과 1이 답입니다. 시청해 주셔서 감사합니다!"
                ]
            }
        }

    def _generate_tree_level_order_viz(self) -> Dict:
        """Binary Tree Level Order Traversal 시각화 데이터"""
        return {
            "problem_name": "Binary Tree Level Order Traversal",
            "description": "이진 트리를 레벨 순서로 순회하여 결과를 리스트로 반환",
            "example": {
                "tree": [3, 9, 20, None, None, 15, 7],
                "output": [[3], [9, 20], [15, 7]]
            },
            "algorithm": "BFS with Queue",
            "steps": [
                {"step": 1, "description": "루트 노드를 큐에 추가", "action": "enqueue_root"},
                {"step": 2, "description": "큐가 빌 때까지 반복", "action": "while_queue_not_empty"},
                {"step": 3, "description": "현재 레벨의 노드 개수를 파악", "action": "get_level_size"},
                {"step": 4, "description": "해당 개수만큼 노드를 꺼내고 자식을 큐에 추가", "action": "process_level"},
            ],
            "narration": {
                "ko": [
                    "이진 트리의 레벨 순서 순회 문제입니다.",
                    "BFS(너비 우선 탐색) 알고리즘을 사용합니다.",
                    "큐(Queue) 자료구조를 이용하여 같은 레벨의 노드들을 한 번에 처리합니다.",
                    "루트 노드부터 시작합니다.",
                    "각 레벨별로 노드들을 순회하고 결과를 저장합니다.",
                    "최종적으로 레벨별 노드 값 리스트를 반환합니다."
                ]
            }
        }

    def _generate_dp_viz(self) -> Dict:
        """동적계획법 - 1로 만들기 시각화 데이터"""
        return {
            "problem_name": "1로 만들기",
            "description": "주어진 정수 N에서 3가지 연산(n/3, n/2, n-1)으로 1을 만드는 최소 횟수",
            "example": {
                "n": 10,
                "output": 3  # 10 -> 9 -> 3 -> 1
            },
            "algorithm": "Dynamic Programming (BFS)",
            "steps": [
                {"step": 1, "description": "DP 배열 초기화", "action": "init_dp"},
                {"step": 2, "description": "N부터 1까지 각 수에 대해 최소 연산 횟수 계산", "action": "fill_dp"},
                {"step": 3, "description": "3으로 나누어떨어지면 dp[n/3] + 1과 비교", "action": "check_div3"},
                {"step": 4, "description": "2로 나누어떨어지면 dp[n/2] + 1과 비교", "action": "check_div2"},
                {"step": 5, "description": "n-1일 때 dp[n-1] + 1과 비교", "action": "check_minus1"},
            ],
            "narration": {
                "ko": [
                    "백준 1463번 1로 만들기 문제입니다.",
                    "정수 N을 1로 만드는 최소 연산 횟수를 구하는 문제입니다.",
                    "3가지 연산이 있습니다: n을 3으로 나누기, n을 2로 나누기, n에서 1 빼기.",
                    "동적계획법을 사용하여 각 수에서의 최소 연산 횟수를 저장합니다.",
                    "N이 10인 경우를 예시로 보겠습니다.",
                    "10에서 2로 나누어 5를 만들고, 5에서 1을 빼 4를 만들고, 4를 2로 나누어 2를 만들고, 2를 2로 나누어 1을 만듭니다.",
                    "총 3번의 연산이 필요합니다."
                ]
            }
        }

    def _generate_sort_viz(self) -> Dict:
        """정렬 시각화 데이터"""
        return {
            "problem_name": "수 정렬하기",
            "description": "주어진 N개의 정수를 오름차순으로 정렬",
            "example": {
                "numbers": [5, 2, 8, 1, 9],
                "output": [1, 2, 5, 8, 9]
            },
            "algorithm": "Bubble Sort (시각화 친화적)",
            "steps": [
                {"step": 1, "description": "배열의 처음부터 끝까지 순회", "action": "outer_loop"},
                {"step": 2, "description": "인접한 두 원소를 비교", "action": "compare"},
                {"step": 3, "description": "왼쪽이 오른쪽보다 크면 교환", "action": "swap"},
                {"step": 4, "description": "다음 쌍으로 이동", "action": "next_pair"},
            ],
            "narration": {
                "ko": [
                    "백준 2750번 수 정렬하기 문제입니다.",
                    "정렬 알고리즘을 시각화해보겠습니다.",
                    "버블 정렬을 사용하여 단계별 정렬 과정을 보여드리겠습니다.",
                    "배열 [5, 2, 8, 1, 9]를 예시로 들어보겠습니다.",
                    "인접한 두 수를 비교하면서 큰 수를 오른쪽으로 옮깁니다.",
                    "이 과정을 반복하면 결국 작은 수들이 왼쪽으로 이동하게 됩니다.",
                    "최종적으로 [1, 2, 5, 8, 9]로 정렬됩니다."
                ]
            }
        }


# ==============================================================================
# Manim Scene들
# ==============================================================================

class TwoSumVisualization(VoiceoverScene):
    """Two Sum 문제 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 문제 제목
        title = Text("LeetCode 1번 - Two Sum", font_size=48, font="NanumGothic").to_edge(UP)
        subtitle = Text("HashMap을 이용한 O(n) 해법", font_size=32, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="안녕하세요! 오늘은 Two Sum 문제를 시각화해보겠습니다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 배열 시각화
        nums = [2, 7, 11, 15]
        target = 9

        with self.voiceover(text="주어진 배열은 [2, 7, 11, 15]이고, 목표 합은 9입니다."):
            # 배열 그리기
            array_elements = VGroup()
            for i, num in enumerate(nums):
                box = Rectangle(width=0.8, height=0.8, color=BLUE)
                text = Text(str(num), font_size=32, font="NanumGothic")
                element = VGroup(box, text)
                element.arrange_in_grid(rows=1, cols=1, buff=0.1)
                element.shift(i * 1.0 * RIGHT - 1.5 * RIGHT)
                array_elements.add(element)

            self.play(*[Create(el) for el in array_elements])
            self.wait(1)

        # HashMap 시각화
        with self.voiceover(text="빈 HashMap을 생성합니다."):
            hashmap_label = Text("HashMap: {}", font_size=28, font="NanumGothic").move_to(DOWN * 2)
            self.play(Write(hashmap_label))
            self.wait(0.5)

        # 알고리즘 실행
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num

            if i == 0:
                with self.voiceover(text=f"첫 번째 요소 {num}을 확인합니다. 목표에서 {num}을 뺀 {complement}를 찾아야 합니다."):
                    self.play(array_elements[i].animate.set_color(YELLOW))
                    self.wait(0.5)
                    new_hashmap_text = Text(f"HashMap: {{{num}: 0}}", font_size=28, font="NanumGothic").move_to(DOWN * 2)
                    self.play(Transform(hashmap_label, new_hashmap_text))
                    hashmap[num] = i
                    self.wait(0.5)
                    self.play(array_elements[i].animate.set_color(BLUE))

            elif i == 1:
                with self.voiceover(text=f"다음 요소 {num}을 확인합니다. {complement}가 HashMap에 있습니다!"):
                    self.play(array_elements[i].animate.set_color(YELLOW))
                    self.wait(0.5)
                    self.wait(1)

                    result_text = Text(f"답: 인덱스 {hashmap[complement]}와 {i}", font_size=32, font="NanumGothic").move_to(ORIGIN)
                    self.play(Write(result_text))
                    self.wait(1)
                    break

        with self.voiceover(text="시청해 주셔서 감사합니다!"):
            self.wait(1)


class BinaryTreeLevelOrderVisualization(VoiceoverScene):
    """Binary Tree Level Order Traversal 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("LeetCode 102번 - Binary Tree Level Order", font_size=40, font="NanumGothic").to_edge(UP)
        subtitle = Text("BFS를 이용한 레벨 순회", font_size=28, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="이진 트리의 레벨 순서 순회 문제입니다. BFS 알고리즘을 사용합니다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 트리 구조 표현
        with self.voiceover(text="루트 노드 3부터 시작하여 각 레벨의 노드들을 순회합니다."):
            # 루트
            root = Circle(radius=0.4, color=RED).move_to(UP * 2)
            root_label = Text("3", font_size=24, font="NanumGothic").move_to(UP * 2)
            self.play(Create(root), Write(root_label))
            self.wait(0.5)

        with self.voiceover(text="레벨 2의 노드들입니다."):
            # 레벨 2
            left_child = Circle(radius=0.4, color=BLUE).move_to(LEFT * 2 + UP * 0.5)
            right_child = Circle(radius=0.4, color=BLUE).move_to(RIGHT * 2 + UP * 0.5)
            left_label = Text("9", font_size=24, font="NanumGothic").move_to(LEFT * 2 + UP * 0.5)
            right_label = Text("20", font_size=24, font="NanumGothic").move_to(RIGHT * 2 + UP * 0.5)

            # 선
            line_left = Line(root.get_center(), left_child.get_center(), color=WHITE)
            line_right = Line(root.get_center(), right_child.get_center(), color=WHITE)

            self.play(Create(line_left), Create(line_right))
            self.play(Create(left_child), Create(right_child))
            self.play(Write(left_label), Write(right_label))
            self.wait(0.5)

        with self.voiceover(text="그리고 레벨 3의 노드들입니다."):
            # 레벨 3
            left_grandchild = Circle(radius=0.4, color=GREEN).move_to(RIGHT * 1.5 + DOWN * 1)
            right_grandchild = Circle(radius=0.4, color=GREEN).move_to(RIGHT * 3.5 + DOWN * 1)
            left_gc_label = Text("15", font_size=24, font="NanumGothic").move_to(RIGHT * 1.5 + DOWN * 1)
            right_gc_label = Text("7", font_size=24, font="NanumGothic").move_to(RIGHT * 3.5 + DOWN * 1)

            line_left_gc = Line(right_child.get_center(), left_grandchild.get_center(), color=WHITE)
            line_right_gc = Line(right_child.get_center(), right_grandchild.get_center(), color=WHITE)

            self.play(Create(line_left_gc), Create(line_right_gc))
            self.play(Create(left_grandchild), Create(right_grandchild))
            self.play(Write(left_gc_label), Write(right_gc_label))
            self.wait(0.5)

        with self.voiceover(text="최종 결과는 [[3], [9, 20], [15, 7]]입니다."):
            result = Text("결과: [[3], [9, 20], [15, 7]]", font_size=28, font="NanumGothic").move_to(DOWN * 3)
            self.play(Write(result))
            self.wait(1)

        with self.voiceover(text="시청해 주셔서 감사합니다!"):
            self.wait(1)


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
        with self.voiceover(text="3가지 연산이 있습니다: n을 3으로 나누기, n을 2로 나누기, n에서 1 빼기"):
            ops_text = Text("연산: n/3, n/2, n-1", font_size=28, font="NanumGothic").move_to(UP * 2)
            self.play(Write(ops_text))
            self.wait(1)

        # DP 배열 시각화 (n=10 예제)
        with self.voiceover(text="N이 10인 경우를 예시로 보겠습니다. DP 배열을 만들어 각 수에서의 최소 연산 횟수를 저장합니다."):
            dp = [0] * 11
            dp[1] = 0

            # DP 배열 표시
            dp_display = VGroup()
            for i in range(1, 11):
                box = Rectangle(width=0.6, height=0.6, color=BLUE)
                num = Text(str(i), font_size=20, font="NanumGothic")
                box_group = VGroup(box, num)
                box_group.move_to((i - 5.5) * 0.7 * RIGHT + UP * 0.5)
                dp_display.add(box_group)

            self.play(Create(dp_display))
            self.wait(1)

        # DP 계산 과정
        with self.voiceover(text="10에서 2로 나누어 5를 만듭니다. 5에서 1을 빼 4를 만듭니다. 4를 2로 나누어 2를 만듭니다. 2를 2로 나누어 1을 만듭니다. 총 3번의 연산이 필요합니다."):
            path_text = Text("10 → 5 → 4 → 2 → 1 (3번 연산)", font_size=24, font="NanumGothic").move_to(DOWN * 2)
            self.play(Write(path_text))
            self.wait(2)

        with self.voiceover(text="시청해 주셔서 감사합니다!"):
            self.wait(1)


class SortVisualization(VoiceoverScene):
    """수 정렬하기 - 버블 정렬 시각화"""

    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 제목
        title = Text("백준 2750번 - 수 정렬하기", font_size=44, font="NanumGothic").to_edge(UP)
        subtitle = Text("버블 정렬 알고리즘", font_size=28, font="NanumGothic").next_to(title, DOWN)

        with self.voiceover(text="백준 2750번 수 정렬하기 문제입니다. 버블 정렬 알고리즘을 시각화해보겠습니다."):
            self.play(Write(title), Write(subtitle))
            self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle))

        # 배열 시각화
        nums = [5, 2, 8, 1, 9]

        with self.voiceover(text="배열 [5, 2, 8, 1, 9]를 정렬합니다."):
            array_elements = VGroup()
            for i, num in enumerate(nums):
                box = Rectangle(width=0.8, height=0.8, color=BLUE)
                text = Text(str(num), font_size=32, font="NanumGothic")
                element = VGroup(box, text)
                element.shift(i * 1.0 * RIGHT - 2.0 * RIGHT)
                array_elements.add(element)

            self.play(*[Create(el) for el in array_elements])
            self.wait(0.5)

        # 정렬 과정
        current_nums = nums.copy()

        with self.voiceover(text="첫 번째 비교: 5와 2를 비교합니다. 5가 더 크므로 교환합니다."):
            self.play(array_elements[0].animate.set_color(YELLOW), array_elements[1].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(Swap(array_elements[0], array_elements[1]))
            current_nums[0], current_nums[1] = current_nums[1], current_nums[0]
            self.wait(0.3)
            self.play(array_elements[0].animate.set_color(BLUE), array_elements[1].animate.set_color(BLUE))

        with self.voiceover(text="계속해서 다음 쌍들을 비교합니다."):
            # 비교: 5와 8
            self.play(array_elements[1].animate.set_color(YELLOW), array_elements[2].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(array_elements[1].animate.set_color(BLUE), array_elements[2].animate.set_color(BLUE))
            self.wait(0.3)

            # 비교: 8과 1
            self.play(array_elements[2].animate.set_color(YELLOW), array_elements[3].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(Swap(array_elements[2], array_elements[3]))
            self.wait(0.3)
            self.play(array_elements[2].animate.set_color(BLUE), array_elements[3].animate.set_color(BLUE))
            self.wait(0.3)

            # 비교: 8과 9
            self.play(array_elements[3].animate.set_color(YELLOW), array_elements[4].animate.set_color(YELLOW))
            self.wait(0.3)
            self.play(array_elements[3].animate.set_color(BLUE), array_elements[4].animate.set_color(BLUE))
            self.wait(0.5)

        with self.voiceover(text="이 과정을 반복하면 결국 배열이 정렬됩니다. 최종 결과는 [1, 2, 5, 8, 9]입니다."):
            final_text = Text("정렬 완료: [1, 2, 5, 8, 9]", font_size=32, font="NanumGothic").move_to(DOWN * 2)
            self.play(Write(final_text))
            self.wait(2)

        with self.voiceover(text="시청해 주셔서 감사합니다!"):
            self.wait(1)


if __name__ == "__main__":
    print("=" * 60)
    print("AI-Powered Coding Problem Visualizer")
    print("=" * 60)

    # 각 문제별 시각화 정보 생성
    problems = [
        ("Two Sum", "array_hashmap"),
        ("Binary Tree Level Order", "tree_bfs"),
        ("1로 만들기", "dp"),
        ("수 정렬하기", "sort")
    ]

    for problem_name, problem_type in problems:
        visualizer = ProblemVisualizer(problem_name, problem_type, language="ko")
        data = visualizer.generate_visualization()
        print(f"\n[{problem_name}]")
        print(f"Description: {data['description']}")
        print(f"Algorithm: {data['algorithm']}")
        print(f"Steps: {len(data['steps'])} 단계")
        print(f"Example: {data['example']}")
