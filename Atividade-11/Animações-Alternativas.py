from pygame import *
import sys

init()

fonte = font.SysFont("Arial", 30)
clock= time.Clock()
window = display.set_mode((800, 720))
background_color =(123, 108, 145)
display.set_caption("Animations.pygame")
curr_frame_n = 0
anim_time = 0


cav_x, cav_y = 100, 100
curr_frame_cav = 0
anim_time_s = 0
vel_cav_x = 4
cav_direita = True
cav_walk= image.load("./Atividade-11/assets/RUN.png") 
necrom= image.load("./Atividade-11/assets/necromancer.png") 
run_animation = True
anim_time_necro = 0

while True:
    window.fill(background_color)
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()
    speed_cav = 0   
    cav_andando = False
    keys = key.get_pressed()
    if keys[K_RIGHT]:  
        speed_cav = vel_cav_x
        cav_direita = True
        cav_andando = True
    elif keys[K_LEFT]:  
        speed_cav = -vel_cav_x
        cav_direita = False
        cav_andando = True

    
    cav_x += speed_cav

    if cav_andando:
        anim_time_s += dt
        if anim_time_s >=100:
            curr_frame_cav += 1
            if curr_frame_cav > 7:  
                curr_frame_cav = 0
            anim_time_s = 0
    else:
        curr_frame_cav = 0  

    anim_time = anim_time + dt
    anim_time_sec = anim_time/100


    if run_animation:
        anim_time_necro = anim_time_necro + dt
        anim_time_necro_sec = anim_time_necro/1000

        if anim_time_necro_sec > 0.1:
            curr_frame_n = curr_frame_n + 1
            if curr_frame_n > 8:
                curr_frame_n = 0
            anim_time_necro = 0

    cavaleiro = Surface((100, 100), SRCALPHA)
    cavaleiro.blit(cav_walk, (0, 0), (96 * (curr_frame_cav % 8), 96 * (curr_frame_cav // 8), 96, 96))
        
    if not cav_direita:
            cavaleiro = transform.flip(cavaleiro, True, False)
        
    window.blit(cavaleiro, (cav_x, cav_y))
    window.blit(necrom, (400, 500), (149 * curr_frame_n, 0, 149, 93))
    text = fonte.render("Use < > para mover o cavaleiro!", True, (8, 7, 7))
    window.blit(text, (300, 620))

    display.flip()
