from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class KoreanMathProblem(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="ko", tld="com"))

        # 1. Introduction
        self.voiceover(text="안녕하세요, 여러분! 오늘은 한국 고등학생들이 자주 마주하는 수학 문제, 바로 이차방정식 풀이에 대해 알아보겠습니다.")
        title = Text("한국 고등학생들의 수학 문제", font_size=48, font="NanumGothic").to_edge(UP)
        subtitle = Text("이차방정식 풀이", font_size=36, font="NanumGothic").next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(0.5)

        # 2. Quadratic Equation Form
        self.voiceover(text="이차방정식은 ax² + bx + c = 0 형태로 나타나며, 여기서 a는 0이 아닙니다.")
        quadratic_eq = MathTex(r"ax^2 + bx + c = 0", font_size=60).move_to(ORIGIN)
        a_not_zero = Text("a \neq 0", font_size=30, font="NanumGothic").next_to(quadratic_eq, RIGHT, buff=0.5)
        self.play(Write(quadratic_eq))
        self.play(Write(a_not_zero))
        self.wait(1)

        # 3. Quadratic Formula
        self.voiceover(text="이 방정식을 풀기 위해 우리는 근의 공식을 사용합니다. 근의 공식은 x = [-b ± sqrt(b² - 4ac)] / 2a 입니다.")
        quadratic_formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", font_size=60).move_to(ORIGIN)
        self.play(TransformMatchingTex(quadratic_eq, quadratic_formula), FadeOut(a_not_zero))
        self.wait(1)

        # 4. Example Problem
        self.voiceover(text="예를 들어, x² - 4x + 3 = 0 이라는 방정식을 풀어볼까요? 여기서 a는 1, b는 -4, c는 3입니다.")
        example_eq = MathTex(r"x^2 - 4x + 3 = 0", font_size=60).move_to(UP)
        abc_values = Text("a = 1, b = -4, c = 3", font_size=36, font="NanumGothic").next_to(example_eq, DOWN)
        self.play(TransformMatchingTex(quadratic_formula, example_eq))
        self.play(Write(abc_values))
        self.wait(1)

        # 5. Substitution
        self.voiceover(text="이 값들을 근의 공식에 대입하면, x = [4 ± sqrt((-4)² - 4*1*3)] / 2*1 이 됩니다.")
        substituted_formula = MathTex(
            r"x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(3)}}{2(1)}",
            font_size=60
        ).move_to(ORIGIN)
        self.play(TransformMatchingTex(example_eq, substituted_formula), FadeOut(abc_values))
        self.wait(1)

        # 6. Calculation Step 1
        self.voiceover(text="계산하면 x = [4 ± sqrt(16 - 12)] / 2, 즉 x = [4 ± sqrt(4)] / 2 가 됩니다.")
        calc_step1 = MathTex(r"x = \frac{4 \pm \sqrt{16 - 12}}{2}", font_size=60).move_to(ORIGIN)
        self.play(TransformMatchingTex(substituted_formula, calc_step1))
        self.wait(0.5)
        calc_step2 = MathTex(r"x = \frac{4 \pm \sqrt{4}}{2}", font_size=60).move_to(ORIGIN)
        self.play(TransformMatchingTex(calc_step1, calc_step2))
        self.wait(1)

        # 7. Solutions
        self.voiceover(text="따라서 x = [4 ± 2] / 2 이고, 해는 x = 3 또는 x = 1 입니다.")
        calc_step3 = MathTex(r"x = \frac{4 \pm 2}{2}", font_size=60).move_to(ORIGIN)
        self.play(TransformMatchingTex(calc_step2, calc_step3))
        self.wait(0.5)
        solution1 = MathTex("x = 3", font_size=60).shift(LEFT * 2)
        solution2 = MathTex("x = 1", font_size=60).shift(RIGHT * 2)
        self.play(TransformMatchingTex(calc_step3, VGroup(solution1, solution2)))
        self.wait(1)

        # 8. Conclusion
        self.voiceover(text="이렇게 근의 공식을 사용하면 어떤 이차방정식도 쉽게 풀 수 있습니다. 시청해 주셔서 감사합니다!")
        self.play(FadeOut(solution1), FadeOut(solution2))
        thanks_text = Text("시청해 주셔서 감사합니다!", font_size=48, font="NanumGothic").move_to(ORIGIN)
        self.play(Write(thanks_text))
        self.wait(2)
