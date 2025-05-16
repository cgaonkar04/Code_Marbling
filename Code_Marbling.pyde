add_library('vecmath')  # Ensure PVector is fully functional in Python mode

from marbling_utils import *
from marbling_drop import MarblingDrop

# Modes
MODE_BLANK = 0
MODE_CREATE = 1
MODE_TINELINE = 2
current_mode = MODE_BLANK

# Interaction
drag_start = None
M = PVector(1, 0)
drops = []

#canvas setup
def setup():
    size(800, 600)
    background(240)
    noLoop()
    textSize(16)

def draw():
    background(240)

    for drop in drops:
        drop.display()

    if current_mode == MODE_TINELINE and drag_start:
        stroke(255, 0, 0)
        line(drag_start.x, drag_start.y, mouseX, mouseY)
        noStroke()

    fill(0)
    text("Mode: " + ["BLANK", "CREATE", "TINELINE"][current_mode], 20, 30)
    text("Keys: 1-Create  2-Tineline  0-Reset", 20, 60)

# dragging mouse to indicate tineline vector
def mousePressed():
    global drag_start
    if current_mode == MODE_CREATE:
        create_new_drop(mouseX, mouseY, drops)
        redraw()
    elif current_mode == MODE_TINELINE:
        drag_start = PVector(mouseX, mouseY)

def mouseReleased():
    global drag_start, M
    if current_mode == MODE_TINELINE and drag_start:
        B = drag_start.copy()
        end_point = PVector(mouseX, mouseY)
        M = PVector.sub(end_point, B)
        if M.mag() > 0:
            mag = M.mag() * 0.01  # deformation proportional to drag length
            M.normalize()
            tine_deform(drops, M, B.x, B.y, mag, 2)
        drag_start = None
        redraw()

def keyPressed():
    global current_mode, drops
    if key == '0':
        current_mode = MODE_BLANK
        drops = []
        redraw()
    elif key == '1':
        current_mode = MODE_CREATE
    elif key == '2':
        current_mode = MODE_TINELINE
    redraw()
