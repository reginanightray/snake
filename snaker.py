from tkinter import *
from time import *
from random import *


def draw_circle(centerX, centerY, r, color):
    canvas.create_oval(centerX - r, centerY - r, centerX + r, centerY + r, fill=color)


def draw_field():
    canvas.create_rectangle([0, 0], [canvasWidth, canvasHeight], fill='tomato4')
    canvas.create_rectangle([frame_width_pixels, frame_width_pixels],
                            [canvasWidth - frame_width_pixels, canvasHeight - frame_width_pixels], fill='OliveDrab4')


def draw_snake():
    i = 0
    while i < len(body_part_x):
        draw_object(body_part_x[i], body_part_y[i], 'gold')
        i += 1

def draw_object(field_x, field_y, color):
    draw_circle(field_x * cellWidthPixels + cellWidthPixels/2 + frame_width_pixels , field_y * cellWidthPixels + cellWidthPixels/2 + frame_width_pixels, cellWidthPixels / 2, color)


def draw_bonus():
    draw_object(apple_x, apple_y, 'red')


def draw_count():
    Label(canvas, text='Яблочки: ' + str(apple_ate_count), bg='tomato4', fg='white').place(
        x=canvasWidth - 2 * cellWidthPixels, y=3)


def draw_all():
    draw_field()
    draw_snake()
    draw_bonus()
    draw_count()
    canvas.update()


def left(event):
    global step_dx, step_dy
    step_dx = -1
    step_dy = 0


def right(event):
    global step_dx, step_dy
    step_dx = 1
    step_dy = 0


def up(event):
    global step_dx, step_dy
    step_dx = 0
    step_dy = -1


def down(event):
    global step_dx, step_dy
    step_dx = 0
    step_dy = 1


def game_over():
    draw_field()
    draw_snake()
    draw_bonus()
    draw_count()
    lab = Label(canvas, text='Змейка умерла!', bg='bisque2', font='Arial 48', fg='black', borderwidth=2,
                relief='solid').place(x=cellWidthPixels * 6, y=cellWidthPixels * 2)
    canvas.update()
    root.mainloop()



fieldWidth = 20
fieldHeight = 10
cellWidthPixels = 50
frame_width_pixels = cellWidthPixels / 2
canvasWidth = cellWidthPixels * (fieldWidth + 1)
canvasHeight = cellWidthPixels * (fieldHeight + 1)
turn_length_sec = .2

root = Tk()
root.title('Змейка')
canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
canvas.pack()

root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

body_part_x = [6, 7, 8, 9]
body_part_y = [2, 2, 2, 2]


apple_x, apple_y, = randrange(0, fieldWidth - 1, 1), randrange(0, fieldHeight - 1, 1)

step_dx = -1
step_dy = 0

apple_ate_count = 0


suicide = False
while True:
    canvas.update()
    if (body_part_x[0] == 0) and (step_dx == -1):
        body_part_x.insert(0, fieldWidth - 1)
        body_part_y.insert(0, body_part_y[0] + step_dy)
    elif (body_part_x[0] == fieldWidth - 1) and (step_dx == 1):
        body_part_x.insert(0, 0)
        body_part_y.insert(0, body_part_y[0] + step_dy)
    elif (body_part_y[0] == 0) and (step_dy == -1):
        body_part_x.insert(0, body_part_x[0] + step_dx)
        body_part_y.insert(0, fieldHeight - 1)
    elif (body_part_y[0] == fieldHeight - 1) and (step_dy == 1):
        body_part_x.insert(0, body_part_x[0] + step_dx)
        body_part_y.insert(0, 0)
    else:
        body_part_x.insert(0, body_part_x[0] + step_dx)
        body_part_y.insert(0, body_part_y[0] + step_dy)

    if (body_part_x[0] == apple_x) and (body_part_y[0] == apple_y):
        apple_x, apple_y, = randrange(0, fieldWidth - 1, 1), randrange(0, fieldHeight - 1, 1)
        apple_ate_count += 1
    else:
        body_part_x.pop()
        body_part_y.pop()

    for i in range(1, len(body_part_x)):
        if (body_part_x[0] == body_part_x[i]) and (body_part_y[0] == body_part_y[i]):
            suicide = True
            break
    if suicide:
        break
    else:
        draw_all()
    sleep(turn_length_sec)
game_over()

