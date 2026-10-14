from jupyturtle import penup, pendown
from jupyturtle import left, right,forward
from jupyturtle import make_turtle
import math
#from math import*
就可以导入所有关于math的了

def jump(length):
    """向前移动`length`的距离，不留下踪迹。
    
    后置条件：将笔落下。
    """
    penup()
    forward(length)
    pendown()

def rectangle(width,height):
  """矩形"""
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
make_turtle()
rectangle(80, 40)


def rhombus(length,angle):
  """菱形"""
    for i in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(180-angle)
make_turtle()
rhombus(50, 60)


def parallelogram(width,length,angle):
  """通用版"""
    for i in range(2):
        forward(length)
        left(angle)
        forward(width)
        left(180-angle)


def triangle(length,angle):
    base_length=2*length*math.sin(math.radians(angle)/2)
    forward(length)
    left(180 - (180 - angle) / 2) 
    forward(base_length)
    left(180 - (180 - angle) / 2) 
    forward(length)
def draw_pie(count,size):
  """多边形pie"""
    angle=360/count
    for i in range(count):
        triangle(size,angle)
        left(180)


#花朵
def jump(length):
    penup()
    forward(length)
    pendown()
def polyline(n,length,angle):
    for i in range(n):
        forward(length)
        left(angle)
def arc(r,angle):
    newc=2*math.pi*r*angle/360
    n=30
    step=newc/n
    sangle=angle/n
    polyline(n,step,sangle)
def pedal(r,angle):
    arc(r,angle)
    left(180-angle)
    arc(r,angle)
    left(180-angle)
def flower(n,r,a):
    for i in range(n):
        pedal(r,a)
        left(360/n)
make_turtle(delay=0)




