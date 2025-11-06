from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class CircleAngleScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))
        with self.voiceover(text="안녕하세요. 오늘은 원과 각에 대한 수학 문제를 시각화해보겠습니다. 원의 중심 O와 원 위의 세 점 A, B, P가 있습니다. 각 점들을 연결하는 선분들을 그려보겠습니다."):
            circle = Circle(radius=2, color=WHITE)
            O = ORIGIN
            A = circle.point_at_angle(150 * DEGREES)
            B = circle.point_at_angle(40 * DEGREES)
            P = circle.point_at_angle(110 * DEGREES)

            dots = [Dot(pt, color=c) for pt, c in zip([O, A, B, P],
                        [YELLOW, BLUE, BLUE, RED])]
            labels = [
                MathTex("O").next_to(dots[0], DOWN),
                MathTex("A").next_to(dots[1], LEFT),
                MathTex("B").next_to(dots[2], RIGHT),
                MathTex("P").next_to(dots[3], UP)
            ]

            # 2️⃣ 기본 도형 표시
            self.play(Create(circle))
            self.play(*[FadeIn(d) for d in dots])
            self.play(*[Write(l) for l in labels])

            OA, OB, OP = [Line(O, pt, color=YELLOW) for pt in [A, B, P]]
            AP, BP = [Line(pt1, pt2, color=BLUE) for pt1, pt2 in [(A, P), (B, P)]]
            self.play(Create(OA), Create(OB), Create(OP), Create(AP), Create(BP))
            self.wait(1)

        # 3️⃣ 중심각 110°
        arc_AOB = Arc(radius=0.7, start_angle=150*DEGREES, angle=-110*DEGREES, color=GREEN)
        label_110 = MathTex("110^{\circ}").move_to(0.8*LEFT + 0.3*DOWN)
        self.play(Create(arc_AOB), Write(label_110))
        self.wait(1)

        # 4️⃣ ∠PAO = 70°
        with self.voiceover(text="그리고 각 PAO는 70도입니다."):
            arc_70 = ArcBetweenPoints(
                A + 0.3*(O - A)/np.linalg.norm(O - A),
                A + 0.3*(P - A)/np.linalg.norm(P - A),
                radius=0.3, color=ORANGE)
            label_70 = MathTex("70^{\circ}").next_to(A, UP+0.2*RIGHT)
            self.play(Create(arc_70), Write(label_70))
            self.wait(1)

        # 5️⃣ 설명 텍스트
        with self.voiceover(text="삼각형 OAP를 살펴보면, OA와 OP는 원의 반지름이므로 길이가 같습니다. 따라서 삼각형 OAP는 이등변삼각형입니다. 각 PAO가 70도이므로, 각 OPA도 70도입니다. 삼각형 내각의 합은 180도이므로, 중심각 AOP는 180도에서 70도 두 개를 뺀 40도가 됩니다."):
            explain1 = Text("△OAP: 밑각 70°이므로 중심각 AOP = 40°", font="/usr/share/fonts/truetype/nanum/NanumGothic.ttf").to_edge(DOWN)
            self.play(Write(explain1))
            self.wait(1)

            # 6️⃣ 중심각 AOP = 40°
            arc_AOP = Arc(radius=0.5, start_angle=150*DEGREES, angle=-40*DEGREES, color=PURPLE)
            label_40 = MathTex("40^{\circ}").move_to(0.4*LEFT + 0.3*UP)
            self.play(Create(arc_AOP), Write(label_40))
            self.wait(1)

        # 7️⃣ 중심각 분할 관계
        with self.voiceover(text="이제 전체 중심각 AOB는 AOP와 POB의 합으로 이루어집니다. AOB가 110도이고 AOP가 40도이므로, 각 POB는 110도에서 40도를 뺀 70도가 됩니다."):
            explain2 = Text("AOB = AOP + POB → POB = 70°", font="/usr/share/fonts/truetype/nanum/NanumGothic.ttf").next_to(explain1, UP)
            self.play(Write(explain2))
            arc_POB = Arc(radius=0.5, start_angle=110*DEGREES, angle=-70*DEGREES, color=RED)
            label_70b = MathTex("70^{\circ}").move_to(0.5*RIGHT + 0.4*UP)
            self.play(Create(arc_POB), Write(label_70b))
            self.wait(1)

        # 8️⃣ 최종 x각
        with self.voiceover(text="마지막으로 삼각형 OBP를 보겠습니다. OB와 OP 역시 원의 반지름이므로 이등변삼각형입니다. 각 POB가 70도이므로, 나머지 두 밑각인 각 OPB와 각 OBP는 각각 55도가 됩니다. 따라서 우리가 구하고자 하는 각 x는 55도입니다."):
            explain3 = Text("△OBP: 이등변 → 2x + 70° = 180° → x = 55°", font="/usr/share/fonts/truetype/nanum/NanumGothic.ttf").next_to(explain2, UP)
            self.play(Write(explain3))
            arc_x = ArcBetweenPoints(
                B + 0.3*(O - B)/np.linalg.norm(O - B),
                B + 0.3*(P - B)/np.linalg.norm(P - B),
                radius=0.3, color=YELLOW)
            label_x = MathTex("x = 55^{\circ}").next_to(B, DOWN+0.2*LEFT)
            self.play(Create(arc_x), Write(label_x))
            self.wait(2)
