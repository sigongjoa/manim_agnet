
from manim import *

class NavierStokesScene(Scene):
    def construct(self):
        # 1. Intro
        title = Tex("Navier-Stokes Equation", font_size=60)
        self.play(Write(title))
        self.wait(1)

        eq = MathTex(
            r"\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} = -\frac{1}{\rho} \nabla p + \nu \nabla^2 \mathbf{u} + \mathbf{g}",
            font_size=48
        )
        question = Tex("What on earth is this?", font_size=48).next_to(eq, DOWN, buff=0.5)

        self.play(ReplacementTransform(title, eq), FadeIn(question, shift=UP))
        self.wait(2)

        explanation = Tex("An equation describing the motion of fluids", font_size=48)
        self.play(ReplacementTransform(VGroup(eq, question), explanation))
        self.wait(2)
        self.play(FadeOut(explanation))

        # 2. Term-by-term explanation
        eq_full = MathTex(
            r"\frac{\partial \mathbf{u}}{\partial t}",  # 0: Time derivative
            r"+ (\mathbf{u} \cdot \nabla) \mathbf{u}", # 1: Convection
            r" = -\frac{1}{\rho} \nabla p",             # 2: Pressure
            r"+ \nu \nabla^2 \mathbf{u}",               # 3: Viscosity
            r"+ \mathbf{g}",                             # 4: External forces
            font_size=48
        ).move_to(UP * 2.5)

        terms = [
            Tex("Time Derivative: Acceleration", font_size=36),
            Tex("Convection: Movement with the flow", font_size=36),
            Tex("Pressure Gradient: Force from high to low pressure", font_size=36),
            Tex("Viscosity: Internal friction", font_size=36),
            Tex("External Forces: e.g., Gravity", font_size=36)
        ]

        self.play(Write(eq_full))
        self.wait(1)

        # Time Derivative
        self.play(eq_full[0].animate.set_color(YELLOW))
        term_explanation = terms[0].next_to(eq_full, DOWN, buff=1)
        arrow = Arrow(eq_full[0].get_bottom(), term_explanation.get_top(), buff=0.2)
        dot = Dot(point=LEFT*2, radius=0.1, color=BLUE)
        self.play(FadeIn(term_explanation), Create(arrow), FadeIn(dot))
        self.play(dot.animate.shift(RIGHT*4).set_color(RED), rate_func=smooth, run_time=2)
        self.wait(1)
        self.play(FadeOut(term_explanation), FadeOut(arrow), FadeOut(dot))
        self.play(eq_full[0].animate.set_color(WHITE))


        # Convection
        self.play(eq_full[1].animate.set_color(YELLOW))
        term_explanation = terms[1].next_to(eq_full, DOWN, buff=1)
        arrow = Arrow(eq_full[1].get_bottom(), term_explanation.get_top(), buff=0.2)
        pipe = VGroup(
            Line(LEFT*4 + UP, RIGHT*4 + UP),
            Line(LEFT*4 + DOWN, LEFT*1 + DOWN),
            Line(LEFT*1 + DOWN, LEFT*1 + DOWN*1.5),
            Line(RIGHT*1 + DOWN*1.5, RIGHT*1 + DOWN),
            Line(RIGHT*1 + DOWN, RIGHT*4 + DOWN)
        )
        dots = VGroup(*[Dot(point=LEFT*4 + (UP*0.8 - UP*i*0.4), radius=0.1, color=BLUE) for i in range(5)])
        self.play(FadeIn(term_explanation), Create(arrow), Create(pipe))
        self.play(dots.animate.shift(RIGHT*3).scale(0.8), run_time=2)
        self.play(dots.animate.shift(RIGHT*2).scale(1.5), run_time=1)
        self.play(dots.animate.shift(RIGHT*3).scale(1), run_time=2)
        self.wait(1)
        self.play(FadeOut(term_explanation), FadeOut(arrow), FadeOut(pipe), FadeOut(dots))
        self.play(eq_full[1].animate.set_color(WHITE))

        # Pressure
        self.play(eq_full[2].animate.set_color(YELLOW))
        term_explanation = terms[2].next_to(eq_full, DOWN, buff=1)
        arrow = Arrow(eq_full[2].get_bottom(), term_explanation.get_top(), buff=0.2)
        
        pressure_rect = Rectangle(height=3, width=6).set_fill(color=[RED, BLUE], opacity=0.5)
        high_pressure = Tex("High P", font_size=36).move_to(LEFT*4)
        low_pressure = Tex("Low P", font_size=36).move_to(RIGHT*4)
        dots = VGroup(*[Dot(point=LEFT*2.5 + (UP*1 - UP*i*0.5), radius=0.1, color=WHITE) for i in range(5)])
        self.play(FadeIn(term_explanation), Create(arrow), FadeIn(pressure_rect), FadeIn(high_pressure), FadeIn(low_pressure), FadeIn(dots))
        self.play(dots.animate.shift(RIGHT*5), run_time=3)
        self.wait(1)
        self.play(FadeOut(term_explanation), FadeOut(arrow), FadeOut(pressure_rect), FadeOut(high_pressure), FadeOut(low_pressure), FadeOut(dots))
        self.play(eq_full[2].animate.set_color(WHITE))

        # Viscosity
        self.play(eq_full[3].animate.set_color(YELLOW))
        term_explanation = terms[3].next_to(eq_full, DOWN, buff=1)
        arrow = Arrow(eq_full[3].get_bottom(), term_explanation.get_top(), buff=0.2)
        
        honey = Rectangle(height=3, width=3, color=YELLOW, fill_opacity=0.5).move_to(LEFT*2)
        water = Rectangle(height=3, width=3, color=BLUE, fill_opacity=0.5).move_to(RIGHT*2)
        honey_label = Tex("High Viscosity").next_to(honey, DOWN)
        water_label = Tex("Low Viscosity").next_to(water, DOWN)
        
        sphere_honey = Sphere(radius=0.2, color=RED).move_to(LEFT*2 + UP*1)
        sphere_water = Sphere(radius=0.2, color=RED).move_to(RIGHT*2 + UP*1)

        self.play(FadeIn(term_explanation), Create(arrow), FadeIn(honey), FadeIn(water), FadeIn(honey_label), FadeIn(water_label), FadeIn(sphere_honey), FadeIn(sphere_water))
        self.play(sphere_honey.animate.shift(DOWN*2), run_time=4)
        self.play(sphere_water.animate.shift(DOWN*2), run_time=1)
        self.wait(1)
        self.play(FadeOut(term_explanation), FadeOut(arrow), FadeOut(honey), FadeOut(water), FadeOut(honey_label), FadeOut(water_label), FadeOut(sphere_honey), FadeOut(sphere_water))
        self.play(eq_full[3].animate.set_color(WHITE))

        # External Forces
        self.play(eq_full[4].animate.set_color(YELLOW))
        term_explanation = terms[4].next_to(eq_full, DOWN, buff=1)
        arrow = Arrow(eq_full[4].get_bottom(), term_explanation.get_top(), buff=0.2)
        
        dots = VGroup(*[Dot(point=np.random.rand(3)*4-2, radius=0.1, color=BLUE) for i in range(20)])
        self.play(FadeIn(term_explanation), Create(arrow), FadeIn(dots))
        self.play(dots.animate.shift(DOWN*3), run_time=2)
        self.wait(1)
        self.play(FadeOut(term_explanation), FadeOut(arrow), FadeOut(dots))
        self.play(eq_full[4].animate.set_color(WHITE))

        # 3. Outro
        self.play(FadeOut(eq_full))
        
        outro_text = Tex("These terms combine to create the beautiful motion of fluids", font_size=48)
        self.play(Write(outro_text))
        self.wait(2)

        # Dynamic vortex animation
        dots = VGroup(*[Dot(radius=0.05, color=BLUE).move_to(point) for point in self.get_vortex_points(200, 3)])
        self.play(ReplacementTransform(outro_text, dots))
        self.play(
            Rotate(dots, angle=4*PI, about_point=ORIGIN, run_time=10, rate_func=linear),
            dots.animate.scale(0.2).set_opacity(0)
        )
        self.wait(1)

        final_text = Tex("Visualized with Manim", font_size=48)
        self.play(FadeIn(final_text))
        self.wait(2)
        self.play(FadeOut(final_text))

    def get_vortex_points(self, n_points, max_radius=2):
        return [
            np.array([
                r * np.cos(2 * PI * r / max_radius + 2 * PI * i / n_points),
                r * np.sin(2 * PI * r / max_radius + 2 * PI * i / n_points),
                0
            ])
            for i, r in enumerate(np.linspace(0.1, max_radius, n_points))
        ]


