from manim import *
config.background_color = "#fbfbfb"


class scene(Scene):
    def construct(self):
        # corona = ImageMobject("./media/images/board3legs.png")
        # corona.scale(1.2)
        # corona.to_edge(RIGHT, buff=1)
        # self.play(FadeIn(corona))
        board = Rectangle(color="#00186e", height=3, width=6, stroke_width=1)
        self.play(Create(board))

        middle_leg_top = Rectangle(color="#00186e", height=0.3,
                                   width=0.2, stroke_width=1).shift(1.65*DOWN)
        middle_leg_bottom = Rectangle(color="#00186e", height=1,
                                      width=0.2, stroke_width=1).shift(2.3*DOWN)
        self.play(Create(middle_leg_top), Create(middle_leg_bottom))

        left_leg_top = Rectangle(color="#00186e", height=0.3,
                                 width=0.2, stroke_width=1).shift(1.65*DOWN + 0.3*LEFT)
        left_leg_bottom = Rectangle(color="#00186e", height=1,
                                    width=0.2, stroke_width=1).shift(2.3*DOWN + 0.3*LEFT)
        self.play(Create(left_leg_top), Create(left_leg_bottom))

        right_leg_top = Rectangle(color="#00186e", height=0.3,
                                  width=0.2, stroke_width=1).shift(1.65*DOWN + 0.3*RIGHT)
        right_leg_bottom = Rectangle(color="#00186e", height=1,
                                     width=0.2, stroke_width=1).shift(2.3*DOWN + 0.3*RIGHT)
        self.play(Create(right_leg_top), Create(right_leg_bottom))

        line = Line(start=2.8*DOWN+1.5*LEFT, end=2.8 *
                    DOWN+1.5*RIGHT, color="#00186e", stroke_width=1)
        self.play(Create(line))

        slide3 = Group(board, middle_leg_top, middle_leg_bottom, left_leg_bottom,
                       left_leg_top, right_leg_top, right_leg_bottom, line)
        slide3.scale(1.4)

        board_words = Text(
            "\\center {The math behind cryptography utilizes modular arithmetic, a subset of number theory. Some of its modern uses include error correcting codes, DVDs, and satellites.}", color=BLACK)
        board_words.scale(0.45)
        self.play(FadeIn(board_words))


class ModularArithmetic(Scene):
    def construct(self):
        # slide 1 - title
        title = Tex(r'Modular Arithmetic', color=BLACK, font_size=144)
        self.play(Write(title), run_time=6)
        self.play(FadeOut(title))

        # slide2 - Warm Up
        subtitle = Tex(r'Warm Up', color="#13152f", font_size=72)
        subtitle.generate_target().shift(5*LEFT + 3*UP)
        self.play(MoveToTarget(subtitle))

        warm_up_problem = Tex(
            "\\justifying {What is the largest positive integer that divides 40 and 78?\nWhat about the smallest positive integer divisible by 40 and 78?}", color=BLACK)
        warm_up_problem.scale(0.75)
        warm_up_problem.shift(UP)
        self.play(FadeIn(warm_up_problem))
        self.wait(1)
        self.play(FadeOut(warm_up_problem), FadeOut(subtitle))

        # slide3
        board = Rectangle(color="#00186e", height=3, width=6, stroke_width=1)
        self.play(Create(board))

        middle_leg_top = Rectangle(color="#00186e", height=0.3,
                                   width=0.2, stroke_width=1).shift(1.65*DOWN)
        middle_leg_bottom = Rectangle(color="#00186e", height=1,
                                      width=0.2, stroke_width=1).shift(2.3*DOWN)
        self.play(Create(middle_leg_top), Create(middle_leg_bottom))

        left_leg_top = Rectangle(color="#00186e", height=0.3,
                                 width=0.2, stroke_width=1).shift(1.65*DOWN + 0.3*LEFT)
        left_leg_bottom = Rectangle(color="#00186e", height=1,
                                    width=0.2, stroke_width=1).shift(2.3*DOWN + 0.3*LEFT)
        self.play(Create(left_leg_top), Create(left_leg_bottom))

        right_leg_top = Rectangle(color="#00186e", height=0.3,
                                  width=0.2, stroke_width=1).shift(1.65*DOWN + 0.3*RIGHT)
        right_leg_bottom = Rectangle(color="#00186e", height=1,
                                     width=0.2, stroke_width=1).shift(2.3*DOWN + 0.3*RIGHT)
        self.play(Create(right_leg_top), Create(right_leg_bottom))

        line = Line(start=2.8*DOWN+1.5*LEFT, end=2.8 *
                    DOWN+1.5*RIGHT, color="#00186e", stroke_width=1)
        self.play(Create(line))

        slide3 = Group(board, middle_leg_top, middle_leg_bottom, left_leg_bottom,
                       left_leg_top, right_leg_top, right_leg_bottom, line)
        slide3.scale(1.4)

        # board_words = Text(
        #     "\\center {The math behind cryptography utilizes modular arithmetic, a subset of number theory. Some of its modern uses include error correcting codes, DVDs, and satellites.}", color=BLACK)
        # board_words.scale(0.45)
        # self.play(FadeIn(board_words))
