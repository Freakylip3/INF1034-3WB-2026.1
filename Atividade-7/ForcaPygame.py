from pygame import *
import sys
import random


init()

#var

lista_St= ["jedi", "vader", "luke", "yoda", "skywalker", "anakin", "solo", "sith", "leia", "padme", "chewbacca"]
palavra_escolhida= random.choice(lista_St)
palavra_forca = '_' * len(palavra_escolhida)
letras_usadas=[]
erros = 0
window = display.set_mode((1280, 720))
background_color =(1, 1, 38)
chute= ""
running= True
clock= time.Clock()
fonte= font.SysFont('arial', 25)



c3po_cabeca_img  = transform.scale(image.load("./Atividade-7/c3po-cabeça.png"),(70, 70))
c3po_tronco1_img = transform.scale(image.load("./Atividade-7/c3po-tronco1.PNG"),(115, 70))
c3po_tronco2_img = transform.scale(image.load("./Atividade-7/c3po-tronco2.PNG"),(113, 70))
c3po_tronco3_img = transform.scale(image.load("./Atividade-7/c3po-tronco3.PNG"),(113, 70))
c3po_pernas1_img = transform.scale(image.load("./Atividade-7/c3po-pernas-1.PNG"),(113, 50))
c3po_pernas2_img = transform.scale(image.load("./Atividade-7/c3po-pernas-2.PNG"),(113, 50))

def forca(erros, palavra_forca, letras_U):

    draw.line(window, ((151, 175, 194)), (130, 800), (200, 300), 3)
    draw.line(window, ((151, 175, 194)), (200, 300), (300, 300), 3)
    draw.line(window, ((151, 175, 194)), (300, 300), (300, 350), 3)
    


    if erros >= 1:  
        window.blit(c3po_cabeca_img, (262, 340))
    if erros >= 2:
        window.blit(c3po_tronco1_img, (238, 408))
    if erros >= 3:
        window.blit(c3po_tronco2_img, (237, 475))
    if erros >= 4:
        window.blit(c3po_tronco3_img, (238.5, 545))
    if erros >= 5:
        window.blit(c3po_pernas1_img, (238.5, 595))
    if erros >= 6:
        window.blit(c3po_pernas2_img, (238.5, 645))
        
    usadas=""
    for letra in palavra_escolhida: 
        if letra.lower() in letras_U:
            usadas += letra.upper() + " "
        else:
            usadas += "_ "
    ###
    chances_restantes= fonte.render(f'Erros feitos:{erros}', True, (204, 157, 2))
    window.blit(chances_restantes, (100, 100))

    letras_usadas= fonte.render(f'Letras usadas:{','.join(letras_U)}', True, (204, 157, 2))
    window.blit(letras_usadas, (600, 600))
    palavra_acertando = fonte.render(usadas, True, (204, 157, 2))
    window.blit(palavra_acertando, (450, 400))

def reset_jogo():
    global palavra_escolhida, palavra_forca, letras_usadas, erros
    palavra_escolhida= random.choice(lista_St)
    palavra_forca = '_' * len(palavra_escolhida)
    letras_usadas=[]
    erros= 0
    


while running:
    window.fill(background_color)
    forca(erros, palavra_forca, letras_usadas)
    

    para_vencer= all(letra in letras_usadas for letra in palavra_escolhida)
    if para_vencer:
        aviso = fonte.render("Você venceu e salvou o C3pO!", True, (204, 157, 2))
        window.blit(aviso, (450, 200))
    if erros>=6:
        aviso = fonte.render(f"Você perdeu! A palavra era: {palavra_escolhida}", True, (255, 0, 0))
        window.blit(aviso, (450, 200))
    

    for evento in event.get():
        if evento.type == QUIT:
            running= False
            sys.exit()

        if evento.type == KEYDOWN and not para_vencer and erros<6:            
            if K_a <= evento.key <= K_z:
                letra = key.name(evento.key).lower()
            if letra not in letras_usadas:
                letras_usadas.append(letra)
                if letra not in palavra_escolhida:
                    erros +=1
            if evento.key == K_SPACE:
                chute= ""
            elif evento.key == K_RETURN:
                if chute== palavra_escolhida:
                    letras_usadas = list(palavra_escolhida)
                else:
                    erros +=1
    clock.tick(60)
    display.update()
