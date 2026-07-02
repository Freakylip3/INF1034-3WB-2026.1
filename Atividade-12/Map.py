import  sys
from pygame import*
init()
largura_tela =1260
largura_mapa= 3600
screen = display.set_mode((largura_tela, 720))
display.set_caption('Sad Dino')
clock = time.Clock()
fonte= font.SysFont("Times New Roman",30)
sorry=fonte.render("Thank you Dino! But our princess is in another castle!", True, (255, 255, 255))
tile_size = 60
tile_size_joguinho =60
tileset = image.load("./Atividade-12/assets/TileSet.png")
tileset= transform.scale(tileset, (20 * tile_size_joguinho, 12 * tile_size_joguinho)) 
placaP = image.load("Atividade-12/assets/7.png")
placaP = transform.scale(placaP, (tile_size_joguinho, tile_size_joguinho))
fundo= image.load("Atividade-12/assets/2.png")
fundo= transform.scale(fundo, (3600, 720))
fundo2=image.load("Atividade-12/assets/3.png")
fundo2= transform.scale(fundo2, (3600, 720))
castelo= image.load("Atividade-12/assets/castelo.png")
castelo= transform.scale(castelo, (600, 400))
encostouCastelo= False

#dino
dino_sheet= image.load("./Atividade-12/assets/Dinoi.png")
dino_sheet= transform.scale(dino_sheet, (14*60, 60))
dinox ,dinoy= 000, 300
speed_dinox= 0
speed_dinoy= 0
mov_speed= 5
jump= -15
gravidade=0.40
dinoGreen_walk = False
ground_check= True
curr_frame_n = 0
anim_time = 0
LARGURA_FRAME = 24
ALTURA_FRAME = 100
dt = clock.get_time()
olhando_para_direita = True

arq = open("./Atividade-12/assets/Map.txt", "r")
mapa_joguinho = []
for linha in arq:
    mapa_joguinho.append(linha.rstrip(".\n "))
arq.close()



tiles = {
    'B': (60, 60),   #bloco pedra
    'G': (60, 0),    #grama
    'D': (300, 0),   #borda direita
    'C': (0, 0),     #canto sup esquerdo
}
colisoes = {'B', 'G', 'D', 'C'}




while True:
    keys = key.get_pressed()
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    clock.tick(60)
    dt = clock.get_time()

    old_dinox = dinox
    old_dinoy = dinoy
    
    camera_x = dinox - largura_tela // 2
    camera_x = max(0, camera_x) 
    camera_x = min(camera_x, largura_mapa - largura_tela)

    screen.fill((152,209,250))
    screen.blit(fundo, (0 - camera_x, 0))
    screen.blit(fundo2, (0 - camera_x, 0))


    def checar_colisao(mapa, collider_dino, colisoes, tile_size):
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] in colisoes:
                    collider_tile = Rect(j * tile_size, i * tile_size, tile_size, tile_size)
                    if collider_dino.colliderect(collider_tile):
                        return True
                
        return False
    
    for i in range(len(mapa_joguinho)): 
        for j in range(len(mapa_joguinho[i])): 

            if mapa_joguinho[i][j] == "P":
                screen.blit(placaP, (j * tile_size_joguinho - camera_x, i * tile_size_joguinho))
        
            if mapa_joguinho[i][j] == "S":
                screen.blit(castelo, (j * tile_size_joguinho - camera_x, i * tile_size_joguinho -240))
                collider_castelo = Rect(j * tile_size_joguinho, i * tile_size_joguinho - 215, 500, 240)
                

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
        curr_frame_n = 13
    
    
    old_dinox = dinox
    old_dinoy = dinoy

    dinox += speed_dinox
    collider_dino = Rect(dinox + 15, dinoy + 10, 30, 40)
    if checar_colisao(mapa_joguinho, collider_dino, colisoes, tile_size_joguinho):
        dinox = old_dinox

    dinoy += speed_dinoy
    speed_dinoy += gravidade
    collider_dino = Rect(dinox + 15, dinoy + 10, 30, 40)
    if checar_colisao(mapa_joguinho, collider_dino, colisoes, tile_size_joguinho):
        dinoy = old_dinoy
        speed_dinoy = 0
        ground_check = True

    dino_surf = Surface((60, 60), SRCALPHA).convert_alpha()
    pos_sheet = curr_frame_n * 60
    area_do_frame = (pos_sheet, 0, 60, 60)
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

    if collider_dino.colliderect(collider_castelo):        
        encostou_castelo = True
        if encostou_castelo == True:
            screen.blit(sorry, (100, 100))
            
    for i in range(len(mapa_joguinho)):
        for j in range(len(mapa_joguinho[i])):
            if mapa_joguinho[i][j] in tiles:
                col, lin = tiles[mapa_joguinho[i][j]]
                screen.blit(tileset, (j * tile_size_joguinho - camera_x, i * tile_size_joguinho), (col, lin, tile_size_joguinho, tile_size_joguinho))
                collider_tile = Rect(j * tile_size_joguinho, i * tile_size_joguinho, tile_size_joguinho, tile_size_joguinho)
    
    
    screen.blit(dino_surf, (dinox - camera_x, dinoy))
    display.flip()
        
    