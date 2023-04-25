import pygame as pg
import sys

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
    # set bomb randomly
    # rdm_num = 
    #get_bomb_position = bomb_img.


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bomb_img, [900, 600])

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()