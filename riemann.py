from manim import *

class test(Scene):
    def construct(self):
        # self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))
        ax = Axes(
            x_range=[-2, 10],
            x_length=10,
            y_range=[-2, 10],
            y_length=5,

        )
        quadratic = ax.plot(
                lambda x: 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5,
                x_range=[-0.3, 10],
                color=GREEN
        )

        self.play(FadeIn(ax), FadeIn(quadratic))

        rects = VGroup()

        for dx in np.arange(0.2, 0.05, -0.05):
            rect = ax.get_riemann_rectangles(
                quadratic,
       			x_range=[2, 8],
                dx=dx,
                stroke_width=4*dx,
            )
            rects.add(rect)

       	self.play(
       			DrawBorderThenFill(
       				rects[0],
       				run_time=2,
       				rate_func=smooth,
       				lag_ratio=0.5,
       			),
       		)
       	self.wait()

       	for rect in rects[1:]:
       		self.play(
       			Transform(
       				rects[0], rect,
       				run_time=2,
       				rate_func=smooth,
       				lag_ratio=0.5,
       			),
       		)

