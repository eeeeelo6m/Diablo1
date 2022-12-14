# 1366,768
import pygame,os

os.environ['SDL_VIDEO_WINDOW_POS'] = "341,192"

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
# screen = pygame.display.set_mode([683, 384])
# screen = pygame.display.set_mode([1366,768])
# print(screen.get_rect())
import model, stenaputi, fullscreen, settings, time
from pygame import display, draw


minimap_size_h = screen.get_height() / settings.PERCENTMINIMAP
minimap_size_w = screen.get_width() / settings.PERCENTMINIMAP
rect_minimap = pygame.Rect(screen.get_width() - minimap_size_w - 30, 30, minimap_size_w, minimap_size_h)
minimap = pygame.Surface([rect_minimap.w, rect_minimap.h])
perehod = pygame.Surface([screen.get_width(), screen.get_height()], pygame.SRCALPHA)
perehod.fill([0, 0, 0, 0])


def world(what, minimap):
    mul = 'minimap' if minimap else 'map'

    pygame.draw.rect(what, [0, 0, 0],
                     fullscreen.fullscreen_rect(model.exit,what,mul ))
    for stenaputi in model.obshie:
        stenaputi.draw(what, minimap)
    model.igroc.draw(what, minimap)


def veiw():
    screen.fill([30, 255, 30])
    world(screen, False)
    minimap.fill([73, 97, 0])
    world(minimap, True)
    screen.blit(minimap, rect_minimap)

    if model.sostoynie == model.SOSTOYNIE_POTEMNENIE or model.sostoynie == model.SOSTOYNIE_POTEMNENIE_WAR  and time.time() - model.go_to_next_lvl < 2.5:
        screen.blit(perehod, [0, 0])

        perehod.fill([0, 0, 0, (time.time() - model.go_to_next_lvl) * 100])
    if model.sostoynie == model.SOSTOYNIE_OSVETLENIE and 2.5 - (time.time() - model.go_to_next_lvl) > 0:
        screen.blit(perehod, [0, 0])
        perehod.fill([0, 0, 0, 250 - (time.time() - model.go_to_next_lvl) * 100])

    if (model.sostoynie == model.SOSTOYNIE_POTEMNENIE or model.sostoynie == model.SOSTOYNIE_POTEMNENIE_WAR) and time.time() - model.go_to_next_lvl > 2.5:
        perehod.fill([0, 0, 0, 255])
        screen.blit(perehod, [0, 0])

    if model.sostoynie == model.SOSTOYNIE_PEREGENERACIY:
        perehod.fill([0, 0, 0, 255])
        screen.blit(perehod, [0, 0])

    display.flip()
