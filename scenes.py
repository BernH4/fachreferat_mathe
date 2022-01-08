from manim import *

class intro(Scene):
    def construct(self):
        riemann = Text("Das Riemann Integral", font_size=60)
        name = Text("Bernhard Steidl", font_size=20)
        name.next_to(riemann, DOWN)
        self.add(riemann)
        self.play(Create(name))
        self.wait(3)
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        # self.play(Create(circle))  # show the circle on screen
class whats_riemann(Scene):
    def construct(self):
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

        rects = VGroup()
        # the rectangles are constructed from their top right corner.
        # passing an iterable to `color` produces a gradient
        for dx in np.arange(0.2, 0.05, -0.05):
            rect = ax.get_riemann_rectangles(
                quadratic,
                            x_range=[2, 8],
                dx=dx,
                stroke_width=4*dx,
                # color=(TEAL, RED_B, RED),
                input_sample_type="left",
            )
            rects.add(rect)


        self.play(LaggedStart(
            FadeIn(ax), FadeIn(quadratic), FadeIn(question), FadeIn(question_sign),
            run_time=3, lag_ratio=1.0)
            # run_time=0.1, lag_ratio=0.1)
        )
        self.wait(3)
        # Riemann Rechtecke einblenden
        self.play(
            DrawBorderThenFill(
                    rects[0],
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )
        self.wait()

        # Anzahl erhöhen
        for rect in rects[1:]:
            self.play(
                Transform(
                    rects[0], rect,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )




# class intro(Scene):
#     def construct(self):
#         text = Text("Hello world", font_size=144)
#         self.add(text)
