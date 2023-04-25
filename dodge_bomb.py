import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1200, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("./fig/pg_bg.jpg")
    kk_img = pg.image.load("./fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0
    # make a bomb Ex.01
    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img,(255,0,0),(10,10),10)
    bomb_img.set_colorkey((0,0,0))
    
    # set random number Ex.02
    rdm_num_horizontal = random.randint(0,1200)
    rdm_num_vertical = random.randint(0,900)
    # move a bomb Ex.03
    vx,vy = +1,+1
    bomb_rect = bomb_img.get_rect()
    bomb_rect.center = rdm_num_horizontal,rdm_num_vertical

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb_img, bomb_rect)


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()