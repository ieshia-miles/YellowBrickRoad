import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Oval import Oval


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='mintcream')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):
        #self.wall = Square(canvas=self.canvas, size=100, color="red", fill="red", line=2)
        self.wall = Square(canvas=self.canvas, size=200, color="black", fill="linen", line=2)
        self.wall.move_horizontal(50)
        self.wall.move_vertical(80)
        self.wall.make_visible()

         #self.roof = Triangle(canvas=self.canvas, height=75, width=150, color="green", fill="green", line=2)
        # Horizontal 35, Vertical 113
        self.roof = Triangle(canvas=self.canvas, height=75, width=200, color="black", fill="SkyBlue3", line=2)
        self.roof.move_horizontal(60)
        self.roof.move_vertical(113)
        self.roof.make_visible()

        #self.door = Rectangle(canvas=self.canvas, height=100, width=40, color="black", fill="Red", line=2)
        #hor=152, vert=200
        self.door = Rectangle(canvas=self.canvas, height=100, width=40, color="black", fill="Red", line=2)
        self.door.move_horizontal(133)
        self.door.move_vertical(200)
        self.door.make_visible()

        self.doorknob = Circle(canvas=self.canvas, diameter=5, color="red", fill="white", line=1)
        self.doorknob.move_horizontal(200)
        self.doorknob.move_vertical(220)
        self.doorknob.make_visible()

        self.garage = Square(canvas=self.canvas, size=100, color="black", fill="linen", line=2)
        self.garage.move_horizontal(-50)
        self.garage.move_vertical(180)
        self.garage.make_visible()

        self.garage_door = Square(canvas=self.canvas, size=70, color="SkyBlue3", fill="white", line=2)
        self.garage_door.move_horizontal(-35)
        self.garage_door.move_vertical(220)
        self.garage_door.make_visible()

        self.garage_roof = Triangle(canvas=self.canvas, height=50, width=100, color="black", fill="SkyBlue3", line=2)
        self.garage_roof.move_horizontal(-40)
        self.garage_roof.move_vertical(215)
        self.garage_roof.make_visible()

        self.shutters = Rectangle(canvas=self.canvas, height=30, width=50, color="SkyBlue2", fill="Skyblue2", line=2)
        self.shutters.move_horizontal(60)
        self.shutters.move_vertical(100)
        self.shutters.make_visible()

        self.shutters1 = Rectangle(canvas=self.canvas, height=30, width=50, color="SkyBlue2", fill="Skyblue2", line=2)
        self.shutters1.move_horizontal(60)
        self.shutters1.move_vertical(220)
        self.shutters1.make_visible()

        self.shutters2 = Rectangle(canvas=self.canvas, height=30, width=50, color="SkyBlue2", fill="Skyblue2", line=2)
        self.shutters2.move_horizontal(190)
        self.shutters2.move_vertical(220)
        self.shutters2.make_visible()

        self.shutters3 = Rectangle(canvas=self.canvas, height=30, width=50, color="SkyBlue2", fill="Skyblue2", line=2)
        self.shutters3.move_horizontal(190)
        self.shutters3.move_vertical(100)
        self.shutters3.make_visible()

        #self.window = Square(canvas=self.canvas, size=30, color="black", fill="black", line=1)
        #horizontal(80), vertical(100)
        self.window = Square(canvas=self.canvas, size=30, color="black", fill="white", line=1)
        self.window.move_horizontal(70)
        self.window.move_vertical(100)
        self.window.make_visible()

        self.window1 = Square(canvas=self.canvas, size=30, color="black", fill="white", line=1)
        self.window1.move_horizontal(70)
        self.window1.move_vertical(220)
        self.window1.make_visible()

        self.window2 = Square(canvas=self.canvas, size=30, color="black", fill="white", line=1)
        self.window2.move_horizontal(200)
        self.window2.move_vertical(220)
        self.window2.make_visible()

        self.window3 = Square(canvas=self.canvas, size=30, color="black", fill="white", line=1)
        self.window3.move_horizontal(200)
        self.window3.move_vertical(100)
        self.window3.make_visible()

        #self.sun = Circle(canvas=self.canvas, diameter=60, color="yellow", fill="yellow", line=1)
        #horizontal 200, vert -10
        self.sun = Circle(canvas=self.canvas, diameter=84, color="yellow", fill="yellow", line=1)
        self.sun.move_horizontal(440)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

        self.sun_smile = Circle(canvas=self.canvas, diameter=44, color="white", fill="white", line=1)
        self.sun_smile.move_horizontal(458)
        self.sun_smile.move_vertical(15)
        self.sun_smile.make_visible()

        self.sun_smile1 = Circle(canvas=self.canvas, diameter=38, color="yellow", fill="yellow", line=1)
        self.sun_smile1.move_horizontal(462)
        self.sun_smile1.move_vertical(11)
        self.sun_smile1.make_visible()

        self.sun_eye = Circle(canvas=self.canvas, diameter=10, color="white", fill="black", line=1)
        self.sun_eye.move_horizontal(458)
        self.sun_eye.move_vertical(10)
        self.sun_eye.make_visible()

        self.sun_eye1 = Circle(canvas=self.canvas, diameter=10, color="white", fill="black", line=1)
        self.sun_eye1.move_horizontal(488)
        self.sun_eye1.move_vertical(10)
        self.sun_eye1.make_visible()

        self.bush = Circle(canvas=self.canvas, diameter=50, color="green", fill="green", line=1)
        self.bush.move_horizontal(360)
        self.bush.move_vertical(200)
        self.bush.make_visible()

        self.bush_base = Triangle(canvas=self.canvas, height=25, width=10, color="black", fill="brown", line=2)
        self.bush_base.move_horizontal(350)
        self.bush_base.move_vertical(315)
        self.bush_base.make_visible()

        self.bush1 = Circle(canvas=self.canvas, diameter=50, color="green", fill="green", line=1)
        self.bush1.move_horizontal(410)
        self.bush1.move_vertical(200)
        self.bush1.make_visible()

        self.apple = Circle(canvas=self.canvas, diameter=5, color="red", fill="red", line=1)
        self.apple.move_horizontal(375)
        self.apple.move_vertical(230)
        self.apple.make_visible()

        self.apple1 = Circle(canvas=self.canvas, diameter=5, color="red", fill="red", line=1)
        self.apple1.move_horizontal(390)
        self.apple1.move_vertical(215)
        self.apple1.make_visible()

        self.apple2 = Circle(canvas=self.canvas, diameter=5, color="red", fill="red", line=1)
        self.apple2.move_horizontal(445)
        self.apple2.move_vertical(230)
        self.apple2.make_visible()

        self.apple3 = Circle(canvas=self.canvas, diameter=5, color="red", fill="red", line=1)
        self.apple3.move_horizontal(430)
        self.apple3.move_vertical(210)
        self.apple3.make_visible()

        self.bush_base1 = Triangle(canvas=self.canvas, height=25, width=10, color="black", fill="brown", line=2)
        self.bush_base1.move_horizontal(400)
        self.bush_base1.move_vertical(315)
        self.bush_base1.make_visible()

        self.bush2 = Circle(canvas=self.canvas, diameter=50, color="green", fill="green", line=1)
        self.bush2.move_horizontal(460)
        self.bush2.move_vertical(200)
        self.bush2.make_visible()

        self.bush_base2 = Triangle(canvas=self.canvas, height=25, width=10, color="black", fill="brown", line=2)
        self.bush_base2.move_horizontal(450)
        self.bush_base2.move_vertical(315)
        self.bush_base2.make_visible()

        self.apple4 = Circle(canvas=self.canvas, diameter=5, color="red", fill="red", line=1)
        self.apple4.move_horizontal(466)
        self.apple4.move_vertical(220)
        self.apple4.make_visible()

        self.lawn = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn.move_horizontal(100)
        self.lawn.move_vertical(280)
        self.lawn.make_visible()

        self.lawn1 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn1.move_horizontal(20)
        self.lawn1.move_vertical(280)
        self.lawn1.make_visible()

        self.lawn2 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn2.move_horizontal(-60)
        self.lawn2.move_vertical(280)
        self.lawn2.make_visible()

        self.lawn3 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn3.move_horizontal(180)
        self.lawn3.move_vertical(280)
        self.lawn3.make_visible()

        self.lawn4 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn4.move_horizontal(260)
        self.lawn4.move_vertical(280)
        self.lawn4.make_visible()

        self.lawn5 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn5.move_horizontal(340)
        self.lawn5.move_vertical(280)
        self.lawn5.make_visible()

        self.lawn6 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn6.move_horizontal(420)
        self.lawn6.move_vertical(280)
        self.lawn6.make_visible()

        self.lawn7 = Square(canvas=self.canvas, size=80, color="green", fill="green", line=1)
        self.lawn7.move_horizontal(500)
        self.lawn7.move_vertical(280)
        self.lawn7.make_visible()

        self.driveway = Rectangle(canvas=self.canvas, height=80, width=45, color="gray", fill="gray", line=1)
        self.driveway.move_horizontal(-23)
        self.driveway.move_vertical(280)
        self.driveway.make_visible()

        self.lake = Circle(canvas=self.canvas, diameter=90, color="lightblue", fill="lightblue", line=1)
        self.lake.move_horizontal(500)
        self.lake.move_vertical(290)
        self.lake.make_visible()

        #Duck
        self.duke_body =Oval(canvas=self.canvas, height=6, width=9, color="yellow", fill="yellow", line=1)
        self.duke_body.move_horizontal(535)
        self.duke_body.move_vertical(324)
        self.duke_body.make_visible()

        self.duck_head = Circle(canvas=self.canvas, diameter=6, color="yellow", fill="yellow", line=1)
        self.duck_head.move_horizontal(540)
        self.duck_head.move_vertical(320)
        self.duck_head.make_visible()

        self.pavement = Rectangle(canvas=self.canvas, height=10, width=50, color="burlywood1", fill="burlywood1", line=2)
        self.pavement.move_horizontal(128)
        self.pavement.move_vertical(290)
        self.pavement.make_visible()

        self.pavement1 = Rectangle(canvas=self.canvas, height=10, width=50, color="burlywood1", fill="burlywood1", line=2)
        self.pavement1.move_horizontal(128)
        self.pavement1.move_vertical(310)
        self.pavement1.make_visible()

        self.pavement2 = Rectangle(canvas=self.canvas, height=10, width=50, color="burlywood1", fill="burlywood1", line=2)
        self.pavement2.move_horizontal(128)
        self.pavement2.move_vertical(330)
        self.pavement2.make_visible()

        self.pavement3 = Rectangle(canvas=self.canvas, height=10, width=50, color="burlywood1", fill="burlywood1", line=2)
        self.pavement3.move_horizontal(128)
        self.pavement3.move_vertical(350)
        self.pavement3.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
