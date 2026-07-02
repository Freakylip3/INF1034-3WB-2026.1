from pygame import *
import sys

init()

window = display.set_mode((1280, 720))

window.fill((160, 103, 97))

Vader_img = image.load('./Atividade-5./assets/Darth-Vader-PNG.png')
Vader_img = transform.scale(Vader_img, (300, 300))
tie_img = image.load('./Atividade-5./assets/Tie.png')
tie_img = transform.scale(tie_img,(85, 85))
x= 100

#starWars font
StarF= font.Font("./Atividade-5./assets/Starjhol.ttf", 30)
Y = 50 + 0.067

mixer.music.load('./Atividade-5./assets/imperial_march.mp3')
mixer.music.play(-1)
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    #desenhar apartir daqui
    window.fill((160, 103, 97))
    draw.rect(window, ((243, 205, 146)), (0, 600, 1280,120))
    draw.rect(window, ((141, 98, 120)), (300, 340, 260,260))
    draw.rect(window, ((120, 77, 26)), (435, 400, 110, 200))
    draw.circle(window,((0, 0, 0)), (450, 500), 8)
    draw.circle(window,((247, 219, 181)), (140, 100), 65)
    draw.circle(window,((232, 86, 41)), (230, 100), 65)
    draw.polygon(window, (46, 56, 90), ((290, 340), (440, 220), (580, 340)))
    draw.circle(window,((207, 207, 205)), (370, 450), 40)
    #r2d2 abaixo

    draw.rect(window, ((207, 207, 205)), (750, 140, 100 ,150))
    draw.circle(window, ((207, 207, 205)), (800, 160), 53)
    draw.circle(window, ((230, 116, 108)), (800, 160), 5)
    draw.rect(window, ((23, 76, 162)), (793, 138, 14 ,14))
    draw.rect(window, ((23, 76, 162)), (793, 155, 14 ,14))
    draw.rect(window, ((23, 76, 162)), (761, 155, 13 ,14))
    draw.rect(window, ((23, 76, 162)), (777, 155, 13 ,14))
    draw.rect(window, ((23, 76, 162)), (809, 155, 13 ,14))
    draw.rect(window, ((23, 76, 162)), (825, 155, 13 ,14)) #a   
    draw.rect(window, ((23, 76, 162)), (774, 185, 50 ,5))
    draw.rect(window, ((23, 76, 162)), (774, 120, 50 ,6))
    draw.rect(window, ((23, 76, 162)), (776, 114, 45 ,6)) #a
    draw.rect(window, ((23, 76, 162)), (775, 195, 50 ,5))
    draw.rect(window, ((23, 76, 162)), (790, 210, 20 ,35))
    draw.rect(window, ((23, 76, 162)), (790, 255, 20 ,20))
    draw.line(window, ((207, 207, 205)), (798,127), (798,113), 3 )
    draw.line(window, ((128, 127, 126)), (800,273), (800,255), 3 )
    draw.line(window, ((128, 127, 126)), (790,265), (809,265), 3 )
    draw.circle(window, ((128, 127, 126)), (800, 218), 7)
    draw.circle(window, ((128, 127, 126)), (800, 235), 7)    
    draw.circle(window, ((230, 116, 108)), (800, 160), 5)
    draw.circle(window, ((0, 0, 0)), (800, 145), 6)
        #braco r2
    draw.rect(window, ((207, 207, 205)), (725, 175, 20 ,140))
    draw.rect(window, ((207, 207, 205)), (855, 175, 20 ,140))
    draw.polygon(window, (207, 180, 205), ((700, 345), (735, 315), (770, 345)))
    draw.polygon(window, (207, 180, 205), ((830, 345), (865, 315), (900, 345)))
    draw.polygon(window, (207, 180, 205), ((775, 315), (800, 295), (830, 315)))
    draw.line(window, ((23, 76, 162)), (730,180), (730,300), 3 )
    draw.line(window, ((23, 76, 162)), (870,180), (870,300), 3 )
    
    #imagem

    window.blit (Vader_img, (980, 300))
    
    StarText=  StarF.render("You don't know the power of the dark side", True, (0,0,0))
    window.blit(StarText, (400, 650))
    
    window.blit (tie_img, (x, 18 ))
    x= x+ 0.1
    if x>1200:
        x=100

    display.update()

