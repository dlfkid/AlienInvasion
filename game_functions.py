import sys

import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

#检测按键
def check_events(ship,settings,bullets,screen):
    #相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event,ship,settings,bullets,screen)
        elif event.type == pygame.KEYUP:
            check_key_up(event,ship)

#更新屏幕
def update_screen(settings,screen,ship,bullets,aliens):
    #更新屏幕图像，并切换到新屏幕
    screen.fill(settings.bg_color)

    #重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #让屏幕刷新
    pygame.display.flip()

def check_key_down(event,ship,settings,bullets,screen):
    if event.key == pygame.K_RIGHT:
    # 移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_forward = True
    if event.key == pygame.K_DOWN:
        ship.moving_backward = True
    #开火
    if event.key == pygame.K_SPACE:
        fire_bullets(bullets,settings,screen,ship)
    #退出
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_forward = False
    if event.key == pygame.K_DOWN:
        ship.moving_backward = False

def update_bullets(settings,bullets,aliens,ship,screen):
    # 更新子弹移动状态
    bullets.update()
    check_bullet_alien_collide(bullets,aliens)
    alien_spawn(bullets,settings,aliens,ship,screen)
    #删除已经到达顶端的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(bullets,settings,screen,ship):
    # 创建一颗子弹，并把子弹加入bullets编组中
    if len(bullets) < settings.bullet_maximun:
        new_bullet = Bullet(settings=settings, screen=screen, ship=ship)
        bullets.add(new_bullet)

def check_bullet_alien_collide(bullets,aliens):
    # 检查是否有子弹击中外星人
    pygame.sprite.groupcollide(bullets, aliens, False, True)


#外星人相关

def alien_spawn(bullets,settings,aliens,ship,screen):
    #刷新外星人
    if len(aliens) == 0:
        #删除现有的子弹并刷新外星人
        bullets.empty()
        create_alien_fleet(settings=settings,aliens=aliens,ship=ship,screen=screen)

def create_alien_fleet(settings,screen,aliens,ship):
    #创建外星人群
    alien = Alien(settings,screen)
    number_aliens_x = get_number_aliens_x(settings,alien)
    number_rows_fleet = get_number_rows(settings,ship.rect.height,alien.rect.height)
    for row in range(number_rows_fleet):
        create_aliens(settings,screen,aliens,number_aliens_x,row)


def get_number_aliens_x(settings,alien):
    alien_width = alien.rect.width
    avaliable_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def create_aliens(settings,screen,aliens,number_aliens_x,row):
    # 创建一行外星人
    for alien_number in range(number_aliens_x):
        # 创建一个外星人实例并加入到外星人队列中
        alien = Alien(screen=screen,settings=settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        aliens.add(alien)

def get_number_rows(settings,ship_height,alien_height):
    #计算总共能容纳多少行外星人
    avaliable_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows

def check_fleet_reach_edges(settings,aliens):
    #判断有没有外星人碰到屏幕边缘
    for alien in aliens.sprites():
        if alien.is_reach_edge():
            change_fleet_direction(settings,aliens)
            break

def change_fleet_direction(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    #碰到边缘的外星人下移后反方向移动
    settings.fleet_direction *= -1

def check_ship_been_hit(settings,screen,aliens,ship,bullets,state):
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Ship was hit!")
        ship_hit(settings=settings,aliens=aliens,ship=ship,screen=screen,state=state,bullets=bullets)

def update_aliens(settings,aliens,ship,game_state,screen,bullets):
    #更新每个外星人的位置
    check_fleet_reach_edges(settings=settings,aliens=aliens)
    check_ship_been_hit(settings,screen,aliens,ship,state=game_state,bullets=bullets)
    aliens.update()

def ship_hit(settings,state,screen,ship,bullets,aliens):
    #响应被外星人撞到的飞船
    state.ships_left -= 1

    #清空外星人和子弹列表
    aliens.empty()
    bullets.empty()

    #创建新的外星人舰队,重置飞船位置
    create_alien_fleet(settings=settings,aliens=aliens,screen=screen,ship=ship)
    ship.replace_space_ship()

    #暂停
    sleep(1)
