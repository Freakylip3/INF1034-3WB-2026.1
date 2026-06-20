from pygame import*
import random
import sys 

init()

#lista e var
escolhas=["pedra", "papel", "tesoura"]
pontos= 0
sua_escolha=""
inimigo_escolha=""
running = True
window = display.set_mode((1280, 720))
background_color =(19, 108, 145)
clock = time.Clock()
fonte= font.SysFont("comicsansms", 30)
texto_muda= "Faça sua jogada!"

#img
papel_img= image.load("./Atividade-7/hand-paper.png")
pedra_img= image.load("./Atividade-7/hand.png")
tesoura_img= image.load("./Atividade-7/scissors.png")
reset_img= image.load("./Atividade-7/reset.png")


def jogada():

        
    global pontos
    if sua_escolha == inimigo_escolha:
        return "empate"
    elif sua_escolha == "papel" and inimigo_escolha == "pedra" or sua_escolha == "pedra" and inimigo_escolha == "tesoura" or sua_escolha == "tesoura" and  inimigo_escolha == "papel":
        pontos+=1
        return "jogador venceu!"
    else:
        return "jogador perdeu :["
    
    






while running:
        
        window.fill(background_color)
        
        papel_img= image.load("./Atividade-7/hand-paper.png")
        pedra_img= image.load("./Atividade-7/hand.png")
        tesoura_img= image.load("./Atividade-7/scissors.png")
        reset_img= image.load("./Atividade-7/reset.png")


        draw.rect(window, ((136, 148, 153)), (100, 370, 175, 225)) 
        pedra_img= transform.scale(pedra_img, (120,113))
        window.blit(pedra_img, (127, 420))
        draw.rect(window, ((228, 236, 240)), (300, 370, 175, 225)) 
        papel_img= transform.scale(papel_img, (120, 110))
        window.blit(papel_img, (320, 430))
        draw.rect(window, ((166, 58, 41)),   (500, 370, 175, 225)) 
        tesoura_img= transform.scale(tesoura_img, (120, 110))
        window.blit(tesoura_img, (530, 430))
        draw.rect(window, ((10, 143, 45)), (700, 370, 175, 225))
        reset_img= transform.scale(reset_img, (120, 110))
        window.blit(reset_img, (730, 430))

        rect_pedra = Rect(100, 370, 175, 225)
        rect_papel = Rect(300, 370, 175, 225)
        rect_tesoura = Rect(500, 370, 175, 225)
        rect_reset = Rect(700, 370, 175, 225)


        window.blit(fonte.render(f'Pontos: {pontos}', True, (22, 28, 24)), (80, 85))
        window.blit(fonte.render(texto_muda, True, (22, 28, 24)), (50, 50))
        window.blit(fonte.render(f'Inimgo escolheu:{inimigo_escolha}', True, (22, 28, 24)), (600, 200))
        
        escolha= ""
        for evento_atual in event.get():
            if evento_atual.type == QUIT:
                running = False
            
            if evento_atual.type == MOUSEBUTTONDOWN:
                pos= mouse.get_pos()
                if rect_pedra.collidepoint(pos):
                    escolha = "pedra"
                    texto_muda =True
                elif rect_papel.collidepoint(pos):
                    escolha = "papel"
                    texto_muda= True
                elif rect_tesoura.collidepoint(pos):
                    escolha = "tesoura"
                    texto_muda =True
                elif rect_reset.collidepoint(pos):
                    pontos= 0
                    texto_muda= "Faça sua jogada"

    
        

        if escolha:
            sua_escolha = escolha
            inimigo_escolha= random.choice(escolhas)
            status= jogada()
            texto_muda = f'Você escolheu {sua_escolha}! {status}'
            
        
        

        display.flip()

quit()
sys.exit()