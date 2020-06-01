# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = paddle2_pos = HEIGHT / 2
paddle1_vel = paddle2_vel = 0

score1 = score2 = 0

ball_speed = 60.0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left


def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction:
        direction = 1
    else:
        direction = -1
    ball_vel = [direction *
                random.randrange(120, 240), - random.randrange(60, 180)]

# define event handlers


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel , ball_speed
    global score1, score2  # these are ints
    score1 = score2 = 0
    ball_speed = 60
    spawn_ball(random.randrange(0, 2))


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, ball_speed

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    ball_pos[0] += ball_vel[0] / ball_speed
    ball_pos[1] += ball_vel[1] / ball_speed

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, "white", "white")
    # update paddle's vertical position, keep paddle on the screen

    # PAddle Left
    if paddle1_pos + paddle1_vel <= HALF_PAD_HEIGHT - 5:
        paddle1_pos = paddle1_pos
    elif paddle1_pos + paddle1_vel >= HEIGHT - HALF_PAD_HEIGHT + 5:
        paddle1_pos = paddle1_pos
    else:
        paddle1_pos += paddle1_vel
    # Paddle Right
    if paddle2_pos + paddle2_vel <= HALF_PAD_HEIGHT - 5:
        paddle2_pos = paddle2_pos
    elif paddle2_pos + paddle2_vel >= HEIGHT - HALF_PAD_HEIGHT + 5:
        paddle2_pos = paddle2_pos
    else:
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                     [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "white")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [
                     WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "white")
    # determine whether paddle and ball collide
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_speed -= 1.5
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            ball_speed -= 1.5
        else:
            score1 += 1
            spawn_ball(LEFT)

    if ball_speed >= 1:
        ball_speed = 60.0
    # draw scores
    canvas.draw_text("Score: " + str(score1), [100, 25], 30, "white")
    canvas.draw_text("Score: " + str(score2), [WIDTH - 200, 25], 30, "white")


def keydown(key):
    global paddle1_vel, paddle2_vel
    speed = 5

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = - speed
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = speed
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = - speed
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = speed


def keyup(key):
    global paddle1_vel, paddle2_vel, ball_speed

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
