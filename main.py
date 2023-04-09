import pygame
from constants import WIDTH, HEIGHT, FPS

pygame.init()
pygame.display.set_caption("Platformer")
window = pygame.display.set_mode((WIDTH, HEIGHT))

from get_background import get_background
from draw import draw
from handle_move import handle_move
from fire import Fire
from player import Player
from block import Block
from level_maker import LevelMaker



def main(window):
    block_size = 96

    level1 = LevelMaker(1, "background.png", "block.png",[
        Block(0, HEIGHT - block_size * 2, block_size),
        Block(block_size * 3, HEIGHT - block_size * 3, block_size),
        Block(block_size * 4, HEIGHT - block_size * 4, block_size),
        Block(block_size * 5, HEIGHT - block_size * 5, block_size),
        Block(block_size * 6, HEIGHT - block_size * 6, block_size),
    ], [
        Fire(100, HEIGHT - block_size - 64, 16, 32,),
        Fire(200, HEIGHT - block_size - 64, 16, 32,),
    ])


    clock = pygame.time.Clock()

    player = Player(150, 600, 50, 50)
    if player.invincible == True:
        player.invincible_timer -= 1
    if player.invincible_timer <= 0:
        player.invincible = False



    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        if player.invincible_timer > 0:
            player.invincible_timer -= 1
        if player.invincible_timer == 0:
            player.invincible = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        handle_move(player, level1.objects)
        draw(window, level1.level_background, level1.bg_image, player, level1.objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
