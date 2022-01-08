from manim_pptx import *
from manim import *

class intro(PPTXScene):
    def construct(self):
        riemann = Text("Das Riemann Integral", font_size=60)
        name = Text("Bernhard Steidl", font_size=20)
        name.next_to(riemann, DOWN)
        self.add(riemann)
        self.play(Create(name))
        self.endSlide()
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        # self.play(Create(circle))  # show the circle on screen
        ax = Axes(
            x_range=[-2, 10],
            x_length=10,
            y_range=[-2, 10],
            y_length=5,

        )
        question = Tex(r"Fläche im Intervall $[1;8]$", font_size=40)
        question_sign = Text("?", font_size=60)
                # rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        question.next_to(ax, UP)
        question_sign.next_to(question, RIGHT, buff=0.5)
        quadratic = ax.plot(
                lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5,
                x_range=[-0.3, 10],
                color=GREEN
        )

        e = ValueTracker(1) #Tracks the end value of both functions

        # the rectangles are constructed from their top right corner.
        # passing an iterable to `color` produces a gradient
        rects_right = always_redraw(
                lambda: ax.get_riemann_rectangles(
                    quadratic,
                    x_range=[2, 8],
                    dx=e.get_value(),
                    # color=(TEAL, RED_B, RED),
                    input_sample_type="left",
            )
        )

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=5)
        self.play(LaggedStart(
            FadeIn(ax), FadeIn(quadratic), FadeIn(question), FadeIn(question_sign),
            run_time=3, lag_ratio=1.0)
            # run_time=0.1, lag_ratio=0.1)
        )
        self.endSlide(shownextnotes=True)
        self.wait(4)
        self.play(Create(rects_right))

        self.wait(3)
        self.play(e.animate.set_value(0.04), run_time = 10, rate_func = linear)
        self.endSlide(notes="Next Animation displays Bye")
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=5)

        t2 = Tex("Bye!")
        self.play(Write(t2, run_time=5))
        self.endSlide()


# class intro(Scene):
#     def construct(self):
#         text = Text("Hello world", font_size=144)
#         self.add(text)
