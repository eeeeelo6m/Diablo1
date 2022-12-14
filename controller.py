import pygame, model
from pygame import event

pygame.key.set_repeat(50, 50)


def control():
    e = event.get()
    for r in e:
        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_d:
            model.go_right()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_a:
            model.go_left()

        if r.type == pygame.KEYDOWN and r.key == pygame.K_w:
            model.go_top()

        if r.type == pygame.KEYDOWN and r.key == pygame.K_s:
            model.go_down()

        if r.type == pygame.KEYUP and pygame.K_e == r.key:
            model.next_lvl()

