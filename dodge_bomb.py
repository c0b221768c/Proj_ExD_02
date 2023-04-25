import random
import sys
import time
import math
import pygame as pg
from tkinter import messagebox

move_key_list = {
         pg.K_UP : (0,-1),
         pg.K_DOWN :(0,+1),
         pg.K_LEFT :(-1,0),
         pg.K_RIGHT :(+1,0)
         }


def check_bound(screen_rect:pg.Rect,obj_rect:pg.Rect) -> tuple[bool,bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値(True,False)を判定し、真理値タプルを返す関数
    引数1:画面SurfaceのRect
    引数2:こうかとん、または、爆弾SurfaceのRect
    戻り値:横方向、縦方向のはみだし判定結果(画面内:True/画面外:False)
    """
    
    horizontal, vertical = True, True
    if obj_rect.left< screen_rect.left or screen_rect.right < obj_rect.right:
        horizontal = False
    if obj_rect.top < screen_rect.top or screen_rect.bottom < obj_rect.bottom:
        vertical =False
    return horizontal,vertical


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1200, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("./fig/pg_bg.jpg")
    kk_img = pg.image.load("./fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center =900,400



    bomb_img = pg.Surface((20,20))
    pg.draw.circle(bomb_img,(255,0,0),(10,10),10)
    bomb_img.set_colorkey((0,0,0))
    vx,vy=+1,+1 # 練習3
    bomb_rect = bomb_img.get_rect() # 練習3
    bomb_rect.center =random.randint(0, 1200),random.randint(0, 900) # 練習3
    tmr = 0 # 練習3

    # Make timer
    start_timer = time.time()
 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        tmr += 1



        key_lst = pg.key.get_pressed()
        for k,mv in move_key_list.items():
            if key_lst[k]:
                kk_rect.move_ip(mv)
        if check_bound(screen.get_rect(),kk_rect) != (True,True):
            for k,mv in move_key_list.items():
                if key_lst[k]:
                    kk_rect.move_ip(-mv[0],-mv[1])    


        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bomb_rect.move_ip(vx,vy) # 練習3
        horizontal,vertical = check_bound(screen.get_rect(),bomb_rect)
        if not horizontal: # 横方向にはみ出ていたら
            vx *= -1
        if not vertical: # 縦方向にはみ出ていたら
            vy *= -1
        screen.blit(bomb_img,bomb_rect) # 練習3
        if kk_rect.colliderect(bomb_rect): # 練習6
            # Show timer result
            stop_timer = time.time()
            result = math.floor(stop_timer-start_timer)
            messagebox.showinfo('結果発表',str(result)+'秒！')
            return


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()