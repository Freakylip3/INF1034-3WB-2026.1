from pygame import *

init()

running = True
clock = time.Clock()
timer = 0
x= 100
pos_x = 300
sun_x = 100
sun_y = 200
dia = Color((160, 103, 97))
tarde= Color((16, 73, 154))
noite= Color((7, 10, 54))
background_color = dia
text= "You dont know the power of the dark side"
tieDir= 'right'
window = display.set_mode((1280, 720)) #425
window.fill((160, 103, 97))


#fonte png e musica
Vader_img = image.load('./Atividade-6/assets/Darth-Vader-PNG.png')
Vader_img = transform.scale(Vader_img, (300, 300))
tie_img = image.load('./Atividade-6/assets/Tie.png')
tie_img = transform.scale(tie_img,(85, 85))

StarF= font.Font("./Atividade-6/assets/Starjhol.ttf", 30)
Y = 50 + 0.067

#som
mixer.music.load('./Atividade-6/assets/imperial_march.mp3')
mixer.music.play(-1)
r2d2scream_sfx= mixer.Sound('./Atividade-6/assets/r2d2_scream_converted.mp3')
VaderBreath_sfx= mixer.Sound('./Atividade-6/assets/darth-vader.mp3')
TieRoar_sfx= mixer.Sound('./Atividade-6/assets/tie-fighter-roar.mp3')



while running:
    clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                if sun_x < 640:
                    r2d2scream_sfx.play()
                elif sun_x < 880:
                    VaderBreath_sfx.play()
                else:
                    TieRoar_sfx.play()


    #  update  #
    dt = clock.get_time()/1000
    keys = key.get_pressed()
    pos_x = pos_x + 1 *dt


    #pressionar teclas
    if keys[K_d]:
        pos_x = pos_x + 100*dt

    elif keys[K_a]:
        pos_x = pos_x - 100*dt


    #mouse
    keys = key.get_pressed()

    if mouse.get_focused()== False:
        if keys[K_d] or keys[K_RIGHT]:
            sun_x=sun_x+100 * dt
        elif keys[K_a] or keys[K_LEFT]:
            sun_x = sun_x - 100 * dt
        if keys[K_w] or keys[K_UP]:
            sun_y = sun_y - 100 * dt
        elif keys[K_s] or keys[K_DOWN]:
            sun_y = sun_y + 100 * dt
    else:
        sun_x, sun_y = mouse.get_pos()


    window.fill(background_color)
     #2Sol
    draw.circle(window,((247, 219, 181)), (sun_x, sun_y), 63) #
    draw.circle(window,((232, 86, 41)), (sun_x+ 90, sun_y), 63)#       
        
        #desenhar apartir daqui
    draw.rect(window, ((243, 205, 146)), (0, 600, 1280,120))
    draw.rect(window, ((141, 98, 120)), (300, 340, 260,260))
    draw.rect(window, ((120, 77, 26)), (435, 400, 110, 200))
    draw.circle(window,((0, 0, 0)), (450, 500), 8)
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

    
    
    #nao deixar sol sair da borda

    if sun_y < 100:
        sun_y = 100
    if sun_y > 630:
        sun_y = 630
    if sun_x > 1140:
        sun_x = 1140
    if sun_x < 40:
        sun_x = 40
    
    #mudando
    if sun_x < 640:
        background_color = dia.lerp(tarde, (sun_x)/640)
        text = "You dont know the power of the dark side"
    else:
        background_color = tarde.lerp(noite, (sun_x-640)/640)
        if sun_x < 880:
            text = "i find your lack of faith disturbing"
        else:
            text = "No Luke, i am your Father"

    
   


    #imagem e texto
    textoA =StarF.render(text,True,(0,0,0))
    window.blit(textoA, (400,620))
    window.blit (Vader_img, (980, 300))

    

    window.blit (tie_img, (pos_x, 18 ))
    
    if tieDir == "right":
        pos_x = pos_x  +100* dt
        if pos_x > 1200:
            tieDir = "left"
    elif tieDir == 'left':
        pos_x = pos_x - 100 * dt
        if pos_x < 10:
            tieDir= "right"

    display.update()

