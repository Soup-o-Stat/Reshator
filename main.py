from time import *
import pygame
import os
import button
from param import *
from config import *
from pygame.locals import *
import sys
from save import *
import random


#Версия
ver='Alpha 0.1.3'

particles = []

#Создает окно
pygame.init()
SCREEN_WIDTH = 1180
SCREEN_HEIGHT = 740
pygame.display.set_caption('Решатор')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Настройка ФПС
clock = pygame.time.Clock()

save_data=Save()

custom1=save_data.get('custom1')
custom2=save_data.get('custom2')
custom3=save_data.get('custom3')
custom4=save_data.get('custom4')

idle_run = random.randint(1, 5)

#Полный экран
pygame.display.flip()
fullscreen = True
screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)

#Цвета
white=(255,255,255)
black=(0,0,0)
red=(255, 0, 0)
green=(0,255,0)
dark_green=(12,79,26)
blue=(0,0,255)
yellow=(255,255,0)
cyan=(20, 20, 60)

color1=random.randint(1,10)
if color1 in range(1,4):
    color2=green
if color1 in range(3,7):
    color2=blue
if color1 in range(6,10):
    color2=red
if color1==10:
    color2=cyan

text_timer_1=100
stop_button=25
towel_away=300
towa=False

#Цвета и фон к окошкам для ввода
COLOR_INACTIVE = pygame.Color(black)
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

#Изменение курсора
cursor = pygame.image.load('cursor.png')
pygame.mouse.set_visible(False)
coord = pygame.mouse.get_pos()

#Главный цикл
start=True
start_intro=True

#Значения True False
start_choose=True
work=False
meha_work=False
kriv_work=False
main_menu=True
settings_menu=False
spravochnik=False
credits_menu=False
choose_bg_menu=False
list_1=True
qmode=False

error=False

#шрифты
font1=pygame.font.Font('font/droid.ttf', 20)
font2=pygame.font.Font('font/comic.ttf', 60)
font3=pygame.font.Font('font/comic.ttf', 40)
font4=pygame.font.Font('font/comic.ttf', 30)
font5=pygame.font.Font('font/comic.ttf', 20)
font6=pygame.font.Font('font/south_park.ttf', 90)

#Загрузка изображений
bg_1_img = pygame.image.load('img/bg/bg-1.png').convert_alpha()
bazinga_img = pygame.image.load('img/bg/bazinga.jpg').convert_alpha()
bg_2_img=pygame.image.load('img/bg/bg-2.png').convert_alpha()
bg_3_img=pygame.image.load('img/bg/bg-3.jpg').convert_alpha()
bg_2_dark_img=pygame.image.load('img/bg/bg-2_dark.png').convert_alpha()
choose_bg_img=pygame.image.load('img/bg/choose_bg.jpg').convert_alpha()
run_bg_img=pygame.image.load('img/bg/run_bg1.png').convert_alpha()
q1_img=pygame.image.load('img/other/q1.png').convert_alpha()

gid_img=pygame.image.load('img/other/gid.png').convert_alpha()
cloud_img=pygame.image.load('img/other/cloud.png').convert_alpha()

custom_1_img=pygame.image.load('img/bg/custom/1.png').convert_alpha()
custom_2_img=pygame.image.load('img/bg/custom/2.png').convert_alpha()
custom_3_img=pygame.image.load('img/bg/custom/3.png').convert_alpha()
custom_4_img=pygame.image.load('img/bg/custom/4.png').convert_alpha()

grey_false_img=pygame.image.load('img/buttons/grey_false.png').convert_alpha()
grey_true_img=pygame.image.load('img/buttons/grey_true.png').convert_alpha()

empty_violet_img=pygame.image.load('img/buttons/empty/violet.png').convert_alpha()

start_img = pygame.image.load('img/buttons/start.png').convert_alpha()
start_1_img = pygame.image.load('img/buttons/start_1.png').convert_alpha()
sprav_img = pygame.image.load('img/buttons/Справочник.png').convert_alpha()
sprav_tab=pygame.image.load('img/buttons/sprav.png').convert_alpha()
meha_img = pygame.image.load('img/buttons/механика.png').convert_alpha()
kriv_img=pygame.image.load('img/buttons/kriv.png').convert_alpha()
settings_img = pygame.image.load('img/buttons/settings.png').convert_alpha()
exit_img=pygame.image.load('img/buttons/exit.png').convert_alpha()
back_img=pygame.image.load('img/buttons/back.png').convert_alpha()
next_img=pygame.image.load('img/buttons/arrow_red.png').convert_alpha()
back_img_1=pygame.image.load('img/buttons/arrow_red_1.png').convert_alpha()
arrow_red_img=pygame.image.load('img/buttons/arrow_red.png').convert_alpha()
form7_img=pygame.image.load('img/formuls/form7.jpg').convert_alpha()
form8_img=pygame.image.load('img/formuls/form8.jpg').convert_alpha()
form9_img=pygame.image.load('img/formuls/form9.jpg').convert_alpha()

"""
sleep создана для небольшой оптимизации
"""

if first_start==1:
    cut1=1

#Рисует текст
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

sleep(0.03)

#Поле с титрами
def credits():
    global settings_menu, main_menu, credits_menu
    if credits_menu==True:
        screen.fill(white)

sleep(0.07)

def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        draw_text('Загрузка...', font6, white, screen.get_width() - 100 - screen.get_width() / 1.65, SCREEN_HEIGHT//2)
        pygame.display.update()
        pygame.time.delay(3)

#Справочник
def sprav_menu():
    global main_menu, spravochnik, list_1, list_2, custom1, custom2, custom3, custom4, text_timer_1
    if spravochnik==True:
        if custom1 == 0 and custom2 == 0 and custom3 == 0 and custom4 == 0:
            if bg_1.draw(screen):
                pass
        if custom1 == 1:
            if custom_1.draw(screen):
                pass
        if custom2 == 1:
            if custom_2.draw(screen):
                pass
        if custom3 == 1:
            if custom_3.draw(screen):
                pass
        if custom4 == 1:
            if custom_4.draw(screen):
                pass
        if list_1==True:
            if form7.draw(screen):
                pass
            if form8.draw(screen):
                pass
            if next_button.draw(screen):
                list_1=False
            if back_button_1.draw(screen):
                list_1=False
        if list_1==False:
            if form9.draw(screen):
                pass
            if next_button.draw(screen):
                list_1=True
            if back_button_1.draw(screen):
                list_1=True
        if back_button.draw(screen):
            spravochnik=False
            main_menu=True
            text_timer_1=100

sleep(0.05)

#Подраздел
def start_menu():
    global work, main_menu, settings_menu, spravochnik, meha_work, ans, text_timer_1, cut3,  cut4, first_start, kriv_work, stop_button
    if work==True:
        if bg_3.draw(screen):
            pass
        stop_button-=1
        if back_button.draw(screen):
            work=False
            main_menu=True
            text_timer_1=100
        draw_text('Выберите раздел:', font2, black, 400, 25)
        draw_text('Раздел криволинейное движение находится в разработке...', font3, red, 10, 700)
        if meha_button.draw(screen):
            meha_work=True
            work=False
            ans=False
            cut3=0
            if first_start==1:
                cut4=1
        if kriv_button.draw(screen):
            #if stop_button<=0:
                #kriv_work = True
                #work = False
                #ans = False
            pass
        if cut3==1:
            if gid_3.draw(screen):
                pass
            if cloud2.draw(screen):
                pass
            draw_text('Выбери раздел "Механика"', font5, black, 305, 508)


sleep(0.1)

#Выбор фона
def choose_bg():
    global settings_menu, choose_bg_menu, custom1, custom2, custom3, custom4
    if choose_bg_menu==True:
        if choose_bg_bg.draw(screen):
            pass
        if back_button.draw(screen):
            choose_bg_menu=False
            settings_menu=True
        if custom_1_button.draw(screen):
            custom1=1
            custom2=0
            custom3=0
            custom4=0
        if custom_2_button.draw(screen):
            custom1 = 0
            custom2 = 1
            custom3 = 0
            custom4 = 0
        if custom_3_button.draw(screen):
            custom1=0
            custom2=0
            custom3=1
            custom4=0
        if custom_4_button.draw(screen):
            custom1 = 0
            custom2 = 0
            custom3 = 0
            custom4 = 1
        draw_text('F9 - сбросить фон к стандартному', font4, black, 100,10)

#Меню настроек
def settings():
    global main_menu, settings_menu, credits_menu, choose_bg_menu, custom1, custom2, custom3, custom4, FPS, text_timer_1
    if settings_menu==True:
        if custom1==0 and custom2==0 and custom3==0 and custom4==0:
            if bg_1.draw(screen):
                pass
        if custom1==1:
            if custom_1.draw(screen):
                pass
        if custom2==1:
            if custom_2.draw(screen):
                pass
        if custom3==1:
            if custom_3.draw(screen):
                pass
        if custom4==1:
            if custom_4.draw(screen):
                pass
        draw_text(f'ver. {ver}', font1, white, 1050, 740)
        draw_text(f'FPS:. {FPS}', font1, white, 1180, 740)
        draw_text('60 FPS', font4, white, 50, 200)
        draw_text('Для эффектов курсора нажмите: F1; F2; F3;', font4, white,20,720)
        #draw_text('Танцующее чудо', font4, white, 50, 300)
        if FPS==60:
            if fps_true_button.draw(screen):
                FPS=144
        if FPS==144:
            if fps_false_button.draw(screen):
                FPS=60
        if back_button.draw(screen):
            settings_menu=False
            main_menu=True
            text_timer_1=100
            save_data.save()
            save_data.add('FPS', FPS)
            save_data.add('mouse_effect', mouse_effect)
            save_data.add('custom1', custom1)
            save_data.add('custom2', custom2)
            save_data.add('custom3', custom3)
            save_data.add('custom4', custom4)
        if empty_violet.draw(screen):
            settings_menu=False
            choose_bg_menu=True
        draw_text('Изменить фон', font4, white, 990, 25)

sleep(0.1)

#Главнре меню
def main():
    global main_menu, settings_menu, spravochnik, work, start_choose, light_mode, list_1, text_timer_1, first_start, cut1, cut2, cut3, cut4, cut5, stop_button
    if main_menu==True:
        if light_mode==1:
                if bg_2.draw(screen):
                    pass
                text_timer_1-=1
                if text_timer_1 in range(91,100):
                    draw_text('Р_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 in range(81,91):
                    draw_text('Ре_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65,screen.get_width() / 10)
                if text_timer_1 in range(71,81):
                    draw_text('Реш_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 in range(61,71):
                    draw_text('Решa_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 in range(51,61):
                    draw_text('Решaт_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 in range(41,51):
                    draw_text('Решaт_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 in range(31,41):
                    draw_text('Решaтo_', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 <=30:
                    draw_text('Решaтop', font6, black, screen.get_width() - 90 - screen.get_width() / 1.65, screen.get_width() / 10)
                if text_timer_1 in range(26,31):
                    draw_text('B_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(21,26):
                    draw_text('By_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(16,21):
                    draw_text('By _', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(11,16):
                    draw_text('By I_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(6,11):
                    draw_text('By IT_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(1,6):
                    draw_text('By IT__', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(-6,1):
                    draw_text('By IT_D_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(-11,-6):
                    draw_text('By IT_DA_', font1, black, screen.get_width() - 50- screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(-16,-11):
                    draw_text('By IT_D_', font1, black, screen.get_width() - 50- screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(-21,-16):
                    draw_text('By IT_DU_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(-26,-21):
                    draw_text('By IT_DUM_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 in range(-31,-26):
                    draw_text('By IT_DUMP_', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
                if text_timer_1 <=-30:
                    draw_text('By IT_DUMPS', font1, black, screen.get_width() - 50 - screen.get_width() / 14, screen.get_width() / 1.75)
        if sprav_button.draw(screen):
            if first_start==0:
                list_1=True
                start_choose=False
                main_menu = False
                spravochnik = True
        if cut1==1:
            if gid_1.draw(screen):
                cut1=0
                cut2=1
            if cloud1.draw(screen):
                pass
            draw_text('Привет!', font5, black, 520, 428)
            draw_text('Я твой гид по Решатору.', font5, black, 455, 458)
            draw_text('Кликни на меня, чтобы', font5, black, 455, 488)
            draw_text('начать обучение!', font5, black, 455, 518)
        if cut2==1:
            if gid_2.draw(screen):
                pass
            if cloud1.draw(screen):
                pass
            draw_text('Отлично!!', font5, black, 520, 428)
            draw_text('Теперь нажми на кнопку', font5, black, 455, 458)
            draw_text('Решить задачу.', font5, black, 455, 488)
        if start_button.draw(screen):
            if first_start == 0 or cut1==0:
                sleep(0.15)
                start_choose=True
                fade(SCREEN_WIDTH*2,SCREEN_HEIGHT*2)
                work=True
                stop_button=25
                main_menu=False
                if cut2==1:
                    cut2=0
                    cut3=1
        if settings_button.draw(screen):
            if first_start == 0:
                main_menu=False
                settings_menu=True
        if start_choose==True:
            if arrow_red_1.draw(screen):
                pass
        if start_choose==False:
            if arrow_red_2.draw(screen):
                pass
        if exit_button.draw(screen):
            exit()

sleep(0.05)

#Поле для ввода
class InputBox_V:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global v_pass, v
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        int(self.text)
                        self.color=green
                        v=int(self.text)
                        print(v)
                        v_pass = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            v_pass=True
                        else:
                            print('error')
                            self.color=red
                            v_pass=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class InputBox_S:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global s_pass, s
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        int(self.text)
                        self.color=green
                        s=int(self.text)
                        print('s=',s)
                        s_pass = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            s_pass=True
                        else:
                            print('error')
                            self.color=red
                            s_pass=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class InputBox_t:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global t_pass, t, kriv_work, meha_work
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        if meha_work==True:
                            self.color=green
                            t=int(self.text)
                            print(t)
                            t_pass = False
                        if kriv_work==True:
                            self.color = green
                            t = int(self.text)
                            print(t)
                            t_pass = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            t_pass=True
                        else:
                            print('error')
                            self.color=red
                            t_pass=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

sleep(0.2)

class InputBox_A:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global a_pass, a, meha_work
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        if meha_work == True:
                            self.color=green
                            a=int(self.text)
                            print(a)
                            a_pass = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            a_pass=True
                        else:
                            print('error')
                            self.color=red
                            a_pass=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

sleep(0.2)

class InputBox_V0:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global v0_pass, v0, meha_work
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.color=green
                        v0=int(self.text)
                        print(v0)
                        v0_pass = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            v0_pass=True
                        else:
                            print('error')
                            self.color=red
                            v0_pass=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class InputBox_N:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global N_pass1, N
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.color=green
                        N=int(self.text)
                        print(T)
                        N_pass1 = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            N_pass1=True
                        else:
                            print('error')
                            self.color=red
                            N_pass1=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class InputBox_T:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global T_pass1, T
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.color=green
                        T=int(self.text)
                        print(T)
                        T_pass1 = False
                    except:
                        if self.text =='?' or self.text=='-':
                            print('pass')
                            self.color=black
                            T_pass1=True
                        else:
                            print('error')
                            self.color=red
                            T_pass1=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class Find:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global find_v, find_t, find_a, find_l, find_r, find_s, find_v0, find1_N, find1_T, find1_r, find1_s, find1_t, find1_v, find1_ѵ, meha_work,\
                kriv_work
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.color=dark_green
                        find=str(self.text)
                        print(find)
                        if meha_work==True:
                            if find=='V' or find=='v':
                                find_a=False
                                find_l=False
                                find_r=False
                                find_v0 = False
                                find_s=False
                                find_t=False
                                find_v=True
                            if find=='s' or find=='S':
                                find_a=False
                                find_l=False
                                find_r=False
                                find_s=True
                                find_t=False
                                find_v0 = False
                                find_v=False
                            if find=='T' or find=='t':
                                find_a=False
                                find_l=False
                                find_r=False
                                find_s=False
                                find_t=True
                                find_v0 = False
                                find_v=False
                            if find=='r' or find=='R':
                                find_a=False
                                find_l=False
                                find_r=True
                                find_s=False
                                find_t=False
                                find_v=False
                                find_v0 = False
                            if find == 'l' or find == 'L':
                                find_a = False
                                find_l = True
                                find_r = False
                                find_s = False
                                find_t = False
                                find_v = False
                                find_v0 = False
                            if find=='a' or find=='A':
                                find_a=True
                                find_l=False
                                find_r=False
                                find_s=False
                                find_t=False
                                find_v=False
                                find_v0 = False
                            if find=='v0' or find=='V0':
                                find_a=False
                                find_l=False
                                find_r=False
                                find_s=False
                                find_t=False
                                find_v=False
                                find_v0=True
                            if find=='s' or find=='S':
                                find_a = False
                                find_l = False
                                find_r = False
                                find_s = True
                                find_t = False
                                find_v = False
                                find_v0 = False
                        if kriv_work==True:
                            if find=='v':
                                find1_ѵ=False
                                find1_v=True
                                find1_t=True
                                find1_r=False
                                find1_T=False
                                find1_N=False
                                find1_s=False
                            if find=='s' or find=='S':
                                find1_ѵ=False
                                find1_v=False
                                find1_t=True
                                find1_r=False
                                find1_T=False
                                find1_N=False
                                find1_s=True
                            if find=='V':
                                find1_ѵ=True
                                find1_v=False
                                find1_t=False
                                find1_r=False
                                find1_T=False
                                find1_N=False
                                find1_s=False
                            if find=='t':
                                find1_ѵ=False
                                find1_v=False
                                find1_t=True
                                find1_r=False
                                find1_T=False
                                find1_N=False
                                find1_s=False
                            if find=='r' or find=='R':
                                find1_ѵ=False
                                find1_v=False
                                find1_t=False
                                find1_r=True
                                find1_T=False
                                find1_N=False
                                find1_s=False
                            if find=='T':
                                find1_ѵ=False
                                find1_v=False
                                find1_t=False
                                find1_r=False
                                find1_T=True
                                find1_N=False
                                find1_s=False
                            if find=='N' or find=='n':
                                find1_ѵ=False
                                find1_v=False
                                find1_t=False
                                find1_r=False
                                find1_T=False
                                find1_N=True
                                find1_s=False
                    except:
                        print('error to find')
                        self.color=red
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

sleep(0.05)

def que1():
    global qmode, meha_work
    if qmode==True:
        if q1.draw(screen):
            pass

def kriv_run():
    global kriv_work, work, error, v_pass1, r_pass1, ѵ_pass1, s_pass1, T_pass1, t_pass1, N_pass1, start_num, t, T, N, v, T1_answer, v1_answer, t1_answer
    if kriv_work==True:
        screen.fill(white)
        work=False
        if run_bg.draw(screen):
            pass
        draw_text('V=', font3, black, 10, 85)
        draw_text('S=', font3, black, 10, 135)
        draw_text('t=', font3, black, 10, 185)
        draw_text('T=', font3, black, 10, 235)
        draw_text('N=', font3, black, 10, 285)

        draw_text('м/с', font3, black, 350, 85)
        draw_text('м', font3, black, 375, 135)
        draw_text('c', font3, black, 375, 185)
        draw_text('с', font3, black, 375, 235)
        draw_text('-', font3, black, 375, 285)

        if T1_answer==1:
            draw_text('T=t/N', font3, black, 500, 100)
            draw_text(f'T={t}/{N}', font3, black, 500, 200)
            draw_text(f'T={T} с', font3, black, 500, 300)
            draw_text(f'T={T} c', font3, black, 595, 680)

        if t1_answer==1:
            draw_text('t=N*T', font3, black, 500, 100)
            draw_text(f't={N}*{T}', font3, black, 500, 200)
            draw_text(f't={t} с', font3, black, 500, 300)
            draw_text(f't={t} c', font3, black, 595, 680)

        if start_1_button.draw(screen):
            if start_num==1:
                start_num=0
            if error==True:
                pass
            else:
                if find1_T == True and T_pass1 == True:
                    T=t/N
                    T1_answer=1
                    t1_answer = 0
                if find1_t == True and t_pass1 == True:
                    t=N*T
                    t1_answer=1
                    T1_answer = 0

        input_box1.draw(screen)
        input_box2.draw(screen)
        input_box3.draw(screen)
        input_box4.draw(screen)
        input_box7.draw(screen)
        input_box8.draw(screen)

#Механика
def meha_run():
    global meha_work, work, error, towa, spravochnik, towel_away, \
        s_pass, v_pass, t_pass,\
        ans_v, ans_t, ans_s, ans_v0, ans_a,\
        t, v, s, v0, a,\
        v_ravnomer, t_ravnomer, s_ravnomer, a_answer_1, v0_answer_1, s_pramolinein,\
        find_v, find_t, find_a, find_l, find_r, find_s, \
        start_num, cut4, qmode, cut5, first_start, Soldier
    if meha_work==True:
        screen.fill(white)
        work=False
        if towa==True:
            towel_away-=1
        if run_bg.draw(screen):
            pass
        draw_text('V=', font3, black, 10, 85)
        draw_text('S=', font3, black, 10, 135)
        draw_text('t=', font3, black, 10, 185)
        draw_text('V₀=', font3, black, 3, 235)
        draw_text('a=', font3, black, 10, 285)

        draw_text('м/с', font3, black, 350, 85)
        draw_text('м', font3, black, 375, 135)
        draw_text('c', font3, black, 375, 185)
        draw_text('м/с', font3, black, 350, 235)
        draw_text('м/с²', font3, black, 350, 285)

        if v_ravnomer==1:
            draw_text('V=S/t', font3, black, 500, 100)
            draw_text(f'V={s}/{t}', font3, black, 500, 200)
            draw_text(f'V={v}', font3, black, 500, 300)

        elif s_ravnomer==1:
            draw_text('S=V*t', font3, black, 500, 100)
            draw_text(f'S={v}*{t}', font3, black, 500, 200)
            draw_text(f'S={s}', font3, black, 500, 300)

        elif t_ravnomer==1:
            draw_text('t=S/V', font3, black, 500, 100)
            draw_text(f't={s}/{v}', font3, black, 500, 200)
            draw_text(f't={t}', font3, black, 500, 300)

        elif a_answer_1==1:
            draw_text('a=(V-V₀)/t', font3, black, 500, 100)
            draw_text(f'a=({v}-{v0})/{t}', font3, black, 500, 200)
            draw_text(f'a={a}', font3, black, 500, 300)

        elif v0_answer_1==1:
            draw_text('V₀=at-V', font3, black, 500, 100)
            draw_text(f'V₀={a}*{t}-{v}', font3, black, 500, 200)
            draw_text(f'V₀={v0}', font3, black, 500, 300)

        elif s_pramolinein==1:
            draw_text('S=V₀*t+at/2', font3, black, 500, 100)
            draw_text(f'S={v0}*{t}+{a} {t}/2', font3, black, 500, 200)
            draw_text(f'S={s}', font3, black, 500, 300)

        if start_1_button.draw(screen):
            if start_num==1:
                start_num=0
            if cut4==1:
                cut5=1
                cut4=0
                towa=True
            if error==True:
                pass
            else:

                if find_v==True and v_pass==True:
                    v=s/t
                    ans_v0=False
                    ans_a=False
                    ans_s = False
                    ans_v = True
                    ans_t = False
                    print('v=',v, 'м/с')
                    if a_pass==True and v0_pass==True:
                        v_ravnomer=1
                        a_answer_1 = 0
                        v0_answer_1 = 0
                        s_ravnomer=0
                        t_ravnomer=0
                        s_pramolinein = 0

                if find_s==True and s_pass==True:
                    s=t*v
                    ans_v0 = False
                    ans_a = False
                    ans_v = False
                    ans_t = False
                    ans_s=True
                    print('s=',s, 'м')
                    if a_pass == True and v0_pass == True:
                        a_answer_1 = 0
                        v_ravnomer = 0
                        s_ravnomer = 1
                        v0_answer_1 = 0
                        t_ravnomer = 0
                        s_pramolinein = 0

                if find_s==True and s_pass==True and v_pass==True:
                    s=v0*t+(a*t*t)/2
                    ans_v0 = False
                    ans_a = False
                    ans_v = False
                    ans_t = False
                    ans_s=True
                    print('s=', s, 'м')
                    a_answer_1 = 0
                    v_ravnomer = 0
                    s_ravnomer = 0
                    v0_answer_1 = 0
                    t_ravnomer = 0
                    s_pramolinein=1

                if find_t==True and t_pass==True:
                    t=s/v
                    ans_v0 = False
                    ans_a = False
                    ans_s=False
                    ans_v=False
                    ans_t=True
                    print('t=',t, 'с')
                    if a_pass == True and v0_pass == True:
                        a_answer_1 = 0
                        v_ravnomer = 0
                        v0_answer_1 = 0
                        s_ravnomer = 0
                        t_ravnomer = 1
                        s_pramolinein = 0

                if find_a==True:
                    a=(v-v0)/t
                    ans_v0 = False
                    ans_a = True
                    ans_s = False
                    ans_v = False
                    ans_t = False
                    print(f'a={a}')
                    a_answer_1=1
                    v_ravnomer = 0
                    v0_answer_1 = 0
                    s_ravnomer = 0
                    t_ravnomer = 0
                    s_pramolinein = 0

                if find_v0==True:
                    v0=a*t-v
                    ans_v0 = True
                    ans_a = False
                    ans_s = False
                    ans_v = False
                    ans_t = False
                    print(f'V0={v0}')
                    a_answer_1=0
                    v0_answer_1=1
                    v_ravnomer = 0
                    s_ravnomer = 0
                    t_ravnomer = 0
                    s_pramolinein = 0

        if ans_s==True:
            draw_text(f'S={s} м', font3, black, 595, 680)
        if ans_v==True:
            draw_text(f'V={v} м/c', font3, black, 595, 680)
        if ans_t==True:
            draw_text(f'T={t} с', font3, black, 595, 680)
        if ans_v0==True:
            draw_text(f'V₀={v0} м/с', font3, black, 595, 680)
        if ans_a==True:
            draw_text(f'a={a} м/с²', font3, black, 595, 680)

        input_box1.draw(screen)
        input_box2.draw(screen)
        input_box3.draw(screen)
        input_box4.draw(screen)
        input_box5.draw(screen)
        input_box6.draw(screen)

        if cut4==True:
            if gid_4.draw(screen):
                pass
            if cloud3.draw(screen):
                pass
            draw_text('Теперь реши задачу.', font5, black, 975, 460)
            if empty_violet.draw(screen):
                meha_work=False
                qmode=True
        if cut5==True:
            if towel_away>=0:
                if gid_4.draw(screen):
                    pass
                if cloud3.draw(screen):
                    pass
                draw_text('Молодец!', font5, black, 995, 428)
                draw_text('Теперь ты можешь ', font5, black, 955, 458)
                draw_text('решать задачи', font5, black, 955, 488)
                draw_text('А еще не забудь взять ', font5, black, 955, 518)
                draw_text(' с собой полотенце!', font5, black, 955, 548)
                first_start=0

sleep(0.1)

#Клас танцующего медведя в дано. На название Soldier не обращай внимание: взято из Lovebeer
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['Idle', 'Idle_1', 'Idle_2', 'Idle_3']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'dance/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'dance/{animation}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            self.image = self.animation_list[self.action][self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def update_animation(self):
        global idle_run
        if idle_run!=4:
            ANIMATION_COOLDOWN = 35
        else:
            ANIMATION_COOLDOWN = 150
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

if idle_run == 1:
    player = Soldier('player', 525, 645, 2)
if idle_run == 2:
    player = Soldier('player', 515, 638, 1)
if idle_run == 3:
    player = Soldier('player', 520, 630, 0.5)
if idle_run == 4:
    player = Soldier('player', 545, 640, 3)

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

class ScreenFade():
	def __init__(self, direction, colour, speed):
		self.direction = direction
		self.colour = colour
		self.speed = speed
		self.fade_counter = 0


	def fade(self):
		fade_complete = False
		self.fade_counter += self.speed
		if self.direction == 1:
			pygame.draw.rect(screen, self.colour, (0 - self.fade_counter, 0, SCREEN_WIDTH // 0.8, SCREEN_HEIGHT*2))
		if self.direction == 2:
			pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
		if self.fade_counter >= SCREEN_WIDTH+10000000:
			fade_complete = True

		return fade_complete

#create screen fades
intro_fade = ScreenFade(1, black, 15)

#Кнопки
sprav_button = button.Button(510, 430, sprav_img, 1)
sprav_tab_button=button.Button(1600, 0, sprav_tab, 3.3)
start_button = button.Button(470, 300, start_img, 0.8)
start_1_button = button.Button(7,570, start_1_img, 1)

empty_violet=button.Button(900, 5, empty_violet_img, 0.8)

meha_button=button.Button(100, 200, meha_img, 1)
kriv_button=button.Button(100, 300, kriv_img, 1)
settings_button = button.Button(25, 700, settings_img, 1.2)
exit_button=button.Button(1170, 20, exit_img, 0.3)

bg_1 = button.Button(0, 0, bg_1_img ,0.8) #2.4
bazinga_bg = button.Button(0, 0, bazinga_img ,1)
bg_2 = button.Button(0, 0, bg_2_img,  1)  #1.5
bg_3 = button.Button(0, 0, bg_3_img,  1)
bg_2_dark = button.Button(0, 0, bg_2_dark_img,  2.4)
choose_bg_bg = button.Button(0, 0, choose_bg_img,  1)
run_bg = button.Button(0, 0, run_bg_img,  1.1)
q1 = button.Button(0, 0, q1_img,  1.1)

custom_1=button.Button(0,0, custom_1_img, 1.7)
custom_2=button.Button(0,0, custom_2_img, 1.7)
custom_3=button.Button(0,0, custom_3_img, 1.7)
custom_4=button.Button(0,0, custom_4_img, 1.7)

gid_1=button.Button(200,500, gid_img, 0.75)
gid_2=button.Button(200,500, gid_img, 0.75)
gid_3=button.Button(70,500, gid_img, 0.75)
gid_4=button.Button(700,500, gid_img, 0.75)

cloud1=button.Button(400,400, cloud_img, 0.4)
cloud2=button.Button(270,400, cloud_img, 0.4)
cloud3=button.Button(900,400, cloud_img, 0.4)

custom_1_button=button.Button(150,150, custom_1_img, 0.3)
custom_2_button=button.Button(550,150, custom_2_img, 0.3)
custom_3_button=button.Button(950,150, custom_3_img, 0.3)
custom_4_button=button.Button(1350,150, custom_4_img, 0.3)

fps_true_button=button.Button(200, 200, grey_true_img, 3)
fps_false_button=button.Button(200, 200, grey_false_img, 3)

next_button=button.Button(40, 300, next_img, 0.2)
back_button_1=button.Button(15, 300, back_img_1, 0.2)
arrow_red_1=button.Button(370,300, arrow_red_img, 0.09)
arrow_red_2=button.Button(370,430, arrow_red_img, 0.09)
back_button=button.Button(25, 30, back_img, 0.3)

form7=button.Button(150, 100, form7_img, 0.4)
form8=button.Button(700, 100, form8_img, 0.84)
form9=button.Button(450, 70, form9_img, 0.84)

input_box1 = InputBox_V(60, 100, 70, 32)
input_box2 = InputBox_S(60, 150, 70, 32)
input_box3 = InputBox_t(60, 200,70, 32)
input_box4 = Find(40, 700,70, 32)
input_box5 = InputBox_V0(60, 250,70, 32)
input_box6 = InputBox_A(60, 300,70, 32)

input_box7 = InputBox_T(60, 250,70, 32)
input_box8 = InputBox_N(60, 300,70, 32)

input_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5, input_box6, input_box7, input_box8]

#Главный цикл
run = True
while run==True:
    clock.tick(FPS)


    mx, my = pygame.mouse.get_pos()

    for box in input_boxes:
        box.update()

    if start==True:
        main()
        start_menu()
        settings()
        credits()
        sprav_menu()
        choose_bg()
        meha_run()
        que1()
        kriv_run()
    else:
        pass
    if meha_work==True:
        if dancing_dude != 0:
            player.draw()
            player.update_animation()
            if player.alive:
                if idle_run == 1:
                    player.update_action(0)
                if idle_run == 2:
                    player.update_action(1)
                if idle_run == 3:
                    player.update_action(2)
                if idle_run == 4:
                    player.update_action(3)

    if mouse_effect==1:
        particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            if meha_work==True or kriv_work==True:
                pygame.draw.circle(screen, (black), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            else:
                pygame.draw.circle(screen, (white), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

    if mouse_effect==2:
        mx, my = pygame.mouse.get_pos()
        particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.15
            if meha_work == True or kriv_work == True:
                pygame.draw.circle(screen, (black), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            else:
                pygame.draw.circle(screen, (white), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

            radius = particle[2] * 2
            screen.blit(circle_surf(radius, (color2)), (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                        special_flags=BLEND_RGB_ADD)

            if particle[2] <= 0:
                particles.remove(particle)

    if start_intro == True:
        if intro_fade.fade():
            start_intro = False
            intro_fade.fade_counter = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        for box in input_boxes:
            box.handle_event(event)

        #Клавиатура
        key = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                first_start=0
            if event.key == pygame.K_t:
                first_start=1
            if event.key == pygame.K_ESCAPE:
                if main_menu==True:
                    exit()
                if settings_menu==True:
                    settings_menu=False
                    main_menu=True
                    text_timer_1 = 100
                    save_data.save()
                    save_data.add('FPS', FPS)
                    save_data.add('mouse_effect', mouse_effect)
                    save_data.add('custom1', custom1)
                    save_data.add('custom2', custom2)
                    save_data.add('custom3', custom3)
                    save_data.add('custom4', custom4)
                if credits_menu==True:
                    settings_menu=True
                    credits_menu=False
                if qmode==True:
                    qmode=False
                    meha_work=True
                if spravochnik==True:
                    spravochnik=False
                    main_menu=True
                if work==True:
                    work=False
                    main_menu=True
                    text_timer_1=100
                if meha_work==True:
                    meha_work=False
                    work=True
                if kriv_work == True:
                    kriv_work = False
                    work = True
                    if cut5==1:
                        first_start=0
                        cut5=0
                if choose_bg_menu==True:
                    choose_bg_menu=False
                    settings_menu=True
            if event.key==pygame.K_F1:
                if fullscreen==True:
                    fullscreen=False
                    continue
                if fullscreen==False:
                    fullscreen=True
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                if start_choose==True:
                    start_choose=False
                    continue
                if start_choose==False:
                    start_choose=True
                    continue
            if event.key == pygame.K_RETURN:
                if start_choose==True:
                    if main_menu==True:
                        fade(SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2)
                        main_menu=False
                        work=True
                if start_choose==False:
                    if main_menu==True:
                        main_menu=False
                        spravochnik=True
            if event.key==pygame.K_LEFT:
                if spravochnik==True:
                    if list_1==True:
                        list_1=False
                        continue
                    if list_1==False:
                        list_1=True
            if event.key==pygame.K_RIGHT:
                if spravochnik==True:
                    if list_1==True:
                        list_1=False
                        continue
                    if list_1==False:
                        list_1=True
            if event.key==pygame.K_F9:
                custom1=0
                custom2=0
                custom3=0
                custom4=0
            if event.key==pygame.K_F1:
                mouse_effect=0
            if event.key==pygame.K_F2:
                mouse_effect=1
            if event.key==pygame.K_F3:
                mouse_effect=2

        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    #Обновление курсора, монитора
    if mouse_effect==0:
        screen.blit( cursor, ( pygame.mouse.get_pos() ) )
    pygame.display.update()

#При закрытии программы
pygame.quit()
sys.exit()