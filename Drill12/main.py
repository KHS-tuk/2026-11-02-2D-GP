from pico2d import *
from ball import Ball
from boy import Boy
from grass import Grass

import game_world

# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            direction = boy.handle_event(event)
            if direction is not None:
                print('오른쪽 발사' if direction == 1 else '왼쪽 발사')
                x, y = boy.get_position()
                game_world.add_object(Ball(x + direction * 50, y, direction), 1)



def reset_world():
    global grass, boy

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass()
    game_world.add_object(grass)


def update_world():
    game_world.update_world()

def render_world():
    clear_canvas()
    game_world.render_world()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
