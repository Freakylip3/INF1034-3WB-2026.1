from pygame import *
import sys

init()

clock= time.Clock()
window = display.set_mode((800, 720))
background_color =(123, 108, 145)
display.set_caption("Animations.pygame")
curr_frame_n = 0
anim_time = 0
dino_sheet= image.load("./Atividade-11./Dinoi.png")


#var dino
fonte = font.SysFont("Arial", 30)
dinox ,dinoy= 300, 300
speed_dinox= 0
speed_dinoy= 0
mov_speed= 5
jump= -15
gravidade=0.7
dinoGreen_walk = False
ground_check= True
chao_dino=500
curr_frame_n = 0
anim_time = 0
LARGURA_FRAME = 24
ALTURA_FRAME = 100
dt = clock.get_time()
olhando_para_direita = True




while True:
    dt = clock.tick(60)
    window.fill(background_color)
    keys = key.get_pressed()
    for ev in event.get():
        if ev.type== QUIT:
            sys.exit()
    retangulo_do_frame = (curr_frame_n * LARGURA_FRAME, 0, LARGURA_FRAME, ALTURA_FRAME)

    
    # Tecla A e D
    speed_dinox = 0
    walking = False
    if keys[K_a]:
        speed_dinox = -mov_speed
        walking = True
        olhando_para_direita = False
    if keys[K_d]:
        speed_dinox = mov_speed
        walking = True
        olhando_para_direita = True
        
        # Jump
    if keys[K_SPACE] and ground_check:
        speed_dinoy = jump
        ground_check = False
        curr_frame_n = 12
    
    speed_dinoy += gravidade
    dinox += speed_dinox
    dinoy += speed_dinoy

    if dinoy >= chao_dino:
        dinoy = chao_dino
        speed_dinoy = 0
        ground_check = True


    dino_surf = Surface((LARGURA_FRAME, ALTURA_FRAME), SRCALPHA).convert_alpha()
    pos_sheet = curr_frame_n * LARGURA_FRAME
    area_do_frame = (pos_sheet, 0, LARGURA_FRAME, ALTURA_FRAME)
    dino_surf.blit(dino_sheet, (0, 0), area_do_frame)
    
    if not olhando_para_direita:
        dino_surf = transform.flip(dino_surf, True, False)
    anim_time += dt
    if ground_check:
        if walking: 
            if anim_time > 100: 
                curr_frame_n += 1
                if curr_frame_n > 9: 
                    curr_frame_n = 0
                anim_time = 0
        else:
            curr_frame_n = 0 
    elif not ground_check:    
        
        if speed_dinoy < 0:
            curr_frame_n = 12 
        else:
            curr_frame_n = 13
    draw.rect(window, ((243, 205, 146)), (0, 520, 1280,300))
    draw.circle(window,((214, 63, 13)), (100, 100), 50)
    text = fonte.render("Run Dino!", True, (8, 7, 7))
    window.blit(text, (400, 620))

    pos_sheet = curr_frame_n * LARGURA_FRAME
    window.blit(dino_surf, (dinox, dinoy))
    display.flip()
