from pygame import*
import random

init()

#var
background_color =(247, 247, 213)
window = display.set_mode((1280, 720))
running= True   
clock = time.Clock()
fonte= font.SysFont('arial', 25)
fonteT= font.SysFont('arial', 50, bold=True)
foco= "email"
telaMomento= "bloqueio"
texto_email="" 
texto_senha=""
running = True
papel_img= image.load("./Atividade-8/assets/hand-paper.png")
pedra_img= image.load("./Atividade-8/assets/hand.png")
tesoura_img= image.load("./Atividade-8/assets/scissors.png")
reset_img= image.load("./Atividade-8/assets/reset.png")
escolhas=["pedra", "papel", "tesoura"]
pontos= 0
sua_escolha=""
inimigo_escolha=""
running = True
window = display.set_mode((1280, 720))
background_colorppt =(19, 108, 145)
clock = time.Clock()
texto_muda= "Faça sua jogada!"
c3po_cabeca_img  = transform.scale(image.load("./Atividade-8/assets/c3po-cabeça.png"),(70, 70))
c3po_tronco1_img = transform.scale(image.load("./Atividade-8/assets/c3po-tronco1.PNG"),(115, 70))
c3po_tronco2_img = transform.scale(image.load("./Atividade-8/assets/c3po-tronco2.PNG"),(113, 70))
c3po_tronco3_img = transform.scale(image.load("./Atividade-8/assets/c3po-tronco3.PNG"),(113, 70))
c3po_pernas1_img = transform.scale(image.load("./Atividade-8/assets/c3po-pernas-1.PNG"),(113, 50))
c3po_pernas2_img = transform.scale(image.load("./Atividade-8/assets/c3po-pernas-2.PNG"),(113, 50))
lista_St= ["jedi", "vader", "luke", "yoda", "skywalker", "anakin", "solo", "sith", "leia", "padme", "chewbacca"]
palavra_escolhida= random.choice(lista_St)
palavra_forca = '_' * len(palavra_escolhida)
letras_usadas=[]
erros_f = 0
window = display.set_mode((1280, 720))
background_colorst =(1, 1, 38)
chute= ""
running= True
StarF= font.Font("./Atividade-8/assets/Starjhol.ttf", 30)
clock= time.Clock()
Vader_img = image.load('./Atividade-8/assets/Darth-Vader-PNG.png')
Vader_img = transform.scale(Vader_img, (300, 300))
tie_img = image.load('./Atividade-8/assets/Tie.png')
tie_img = transform.scale(tie_img,(85, 85))
x= 100
        


#cripto
def valida_email(email): #verifica se os ultimos 7 digitos do email
    return email[-7:] == "puc.com"
        
    

def possuiMaiuscula(palavra): #verifica se tem palavra maiuscula 
    for caracter in palavra:
        if caracter.isupper():
            return True
    return False   

def possuiMinuscula(palavra): #verifica se tem palavra minuscula
    for caracter in palavra:
        if caracter.islower():
            return True
    return False
    
def possuiNumero(palavra):  #verifica se possui numero
    for caracter in palavra:
        if caracter.isdigit():
            return True
    return False
    



def valida_senha(senha):  #junta todas as verificacoes e coloca para validar uma senha
    check_tamanho= len(senha) >=8
    check_maiuscula= possuiMaiuscula(senha)
    check_minuscula= possuiMinuscula(senha)
    check_numero= possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero



def criptografa_senha(senha):        #criptografia de cesar usando a tabela ASCII
    senha_cripto= ""                 
    ref= 65
    for char in senha:
        if char.isdigit():
            ref= ord("0")  #etapa1 #obtem o vcalor na tabela
            pos_alpha = ord(char) - ref #etapa2   
            pos_cesar = pos_alpha + 3  #etapa3 obtem o caractere criptografado
            pos_cesar = pos_cesar % 10 #etapa 4 faz com que ao chegar no 9, caso seja um numero volte ao 0, e caso seja uma letra ao chegar no 25 volta ao comeco
            letra_cesar = chr(ref + pos_cesar) #etapa 5 transforma novamente para um caractere da tabela
            senha_cripto += letra_cesar #etapa 6 adiciona o caractere criptografado a string vazia criada anteriormente 
        elif char.isupper():
            ref= ord("A") #65 #etapa1
            pos_alpha = ord(char) - ref #etapa2
            pos_cesar = pos_alpha + 3  #etapa3
            pos_cesar = pos_cesar % 26 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar #etapa 6
           
        elif char.islower():
            ref= ord("a") #65 #etapa1
            pos_alpha = ord(char) - ref #etapa2
            pos_cesar = pos_alpha + 3  #etapa3
            pos_cesar = pos_cesar % 26 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar #etapa 6

        else:
            senha_cripto += char
    return senha_cripto


botao_enter = Rect(540, 550, 200, 60)
caixa_email = Rect(210, 130, 900, 80 )
caixa_senha = Rect(210, 400, 900, 80 )
botao_ppt = Rect(100, 300, 300, 200)
botao_forca = Rect(490, 300, 300, 200)
botao_casitaultimate = Rect(880, 300, 300, 200)

while running:
    for evento in event.get():
        if evento.type == QUIT:
            running = False
        if evento.type == MOUSEBUTTONDOWN:
            if telaMomento == "bloqueio":
                if caixa_email.collidepoint(evento.pos):
                    foco = "email"
                elif caixa_senha.collidepoint(evento.pos):
                    foco = "senha"
                elif botao_enter.collidepoint(evento.pos):
                    if valida_email(texto_email) and valida_senha(texto_senha):
                        resultado_cripto = criptografa_senha(texto_senha)
                        senha_final = texto_senha
                        telaMomento = "principal"
            
            elif telaMomento == "principal":
                if botao_ppt.collidepoint(evento.pos):
                    telaMomento = "ppt"
                elif botao_forca.collidepoint(evento.pos):
                    # Inicia/Reseta o jogo ao entrar na tela
                    letras_usadas = []
                    erros_f = 0
                    palavra_escolhida = random.choice(lista_St)
                    telaMomento = "forca"
                elif botao_casitaultimate.collidepoint(evento.pos):
                    telaMomento = "casita"
                
                elif botao_casitaultimate.collidepoint(evento.pos):
                        telaMomento= "casita"
        elif evento.type == KEYDOWN:
            nome_tecla= key.name(evento.key)
            mods= key.get_mods()
            shift_press= mods & KMOD_SHIFT or mods & KMOD_LSHIFT
            tecla_final=nome_tecla
            caractere_novo= ""
            if nome_tecla == "backspace":
                if foco == "email":
                    texto_email = texto_email[:-1]
                else:
                    texto_senha = texto_senha[:-1]
                
            elif nome_tecla == "2" and shift_press:
                caractere_novo= "@"
                if caractere_novo != "":
                    if foco == "email":
                        texto_email += caractere_novo
                    else:
                        texto_senha += caractere_novo
            
            elif len(tecla_final)== 1:
                if shift_press:
                    tecla_final= nome_tecla.upper()
                else:
                    tecla_final= nome_tecla
                    
                if foco== "email":
                    texto_email+=tecla_final
                else:
                    texto_senha+=tecla_final
            if telaMomento == "forca":
                para_vencer = all(letra in letras_usadas for letra in palavra_escolhida)
                if not para_vencer and erros_f < 6:
                    if K_a <= evento.key <= K_z:
                        letra = key.name(evento.key).lower()
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)
                            if letra not in palavra_escolhida:
                                erros_f += 1

    window.fill(background_color)
    
    if telaMomento== 'bloqueio':
        draw.rect(window, ((214, 214, 214)), (35, 10, 1210, 700))
        draw.rect(window, (255, 255, 255), caixa_email)
        draw.rect(window, (255, 255, 255), caixa_senha)
        draw.rect(window, (50, 50, 50), botao_enter)
        draw.rect(window, (255, 0, 0), botao_enter)
        enter_palavra= fonte.render("Entrar", True, (87, 245, 66))
        window.blit(enter_palavra, (botao_enter.x + 55, botao_enter.y + 15))    

        mostra_email= fonte.render(f"Email: {texto_email}", True, (0, 0, 0))
        window.blit(mostra_email, (caixa_email.x + 10, caixa_email.y + 25))
        mostra_senha= fonte.render(f"Senha: {texto_senha}", True, (0, 0, 0))
        window.blit(mostra_senha, (caixa_senha.x + 10, caixa_senha.y + 25))

    elif telaMomento == "principal":
        msg = fonteT.render("BEM-VINDO!", True, (255, 255, 255))
        window.blit(msg,(30,30))
        senha_og= fonte.render( senha_final, True, (200, 200, 200))
        senha_cripto= fonte.render(resultado_cripto, True, (87, 245, 66))
        window.blit(senha_og,(50,120))
        window.blit(senha_cripto,(50,160))
        
        draw.rect(window, (0, 150, 255), botao_ppt) # Azul
        draw.rect(window, (0, 255, 150), botao_forca) # Verde
        draw.rect(window, (255, 150, 0), botao_casitaultimate)

        ppt = fonte.render("ppt", True, (255, 255, 255))
        forca = fonte.render("forca", True, (255, 255, 255))
        casita = fonte.render("casita", True, (255, 255, 255))
        
        window.blit(ppt, (botao_ppt.x + 110, botao_ppt.y + 85))
        window.blit(forca, (botao_forca.x + 110, botao_forca.y + 85))
        window.blit(casita, (botao_casitaultimate.x + 110, botao_casitaultimate.y + 85))


    elif telaMomento == "ppt":
        from pygame import*
        import random
        import sys 


        #lista e var
        

        #img
        papel_img= image.load("./Atividade-8/hand-paper.png")
        pedra_img= image.load("./Atividade-8/hand.png")
        tesoura_img= image.load("./Atividade-8/scissors.png")
        reset_img= image.load("./Atividade-8/reset.png")


        def jogada():

                
            global pontos
            if sua_escolha == inimigo_escolha:
                return "empate"
            elif sua_escolha == "papel" and inimigo_escolha == "pedra" or sua_escolha == "pedra" and inimigo_escolha == "tesoura" or sua_escolha == "tesoura" and  inimigo_escolha == "papel":
                pontos+=1
                return "jogador venceu!"
            else:
                return "jogador perdeu :["
                           
        window.fill(background_colorppt)
        

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
                
    elif telaMomento== "forca": 

        def forca(erros_f, palavra_forca, letras_U):

            draw.line(window, ((151, 175, 194)), (130, 800), (200, 300), 3)
            draw.line(window, ((151, 175, 194)), (200, 300), (300, 300), 3)
            draw.line(window, ((151, 175, 194)), (300, 300), (300, 350), 3)

            if erros_f >= 1:  
                window.blit(c3po_cabeca_img, (262, 340))
            if erros_f >= 2:
                window.blit(c3po_tronco1_img, (238, 408))
            if erros_f >= 3:
                window.blit(c3po_tronco2_img, (237, 475))
            if erros_f >= 4:
                window.blit(c3po_tronco3_img, (238.5, 545))
            if erros_f >= 5:
                window.blit(c3po_pernas1_img, (238.5, 595))
            if erros_f >= 6:
                window.blit(c3po_pernas2_img, (238.5, 645))
                
            usadas=""
            for letra in palavra_escolhida: 
                if letra.lower() in letras_U:
                    usadas += letra.upper() + " "
                else:
                    usadas += "_ "
            ###
            chances_restantes= fonte.render(f'Erros feitos:{erros_f}', True, (204, 157, 2))
            window.blit(chances_restantes, (100, 100))

            letras_usadas= fonte.render(f'Letras usadas:{','.join(letras_U)}', True, (204, 157, 2))
            window.blit(letras_usadas, (600, 600))
            palavra_acertando = fonte.render(usadas, True, (204, 157, 2))
            window.blit(palavra_acertando, (450, 400))
        
        window.fill(background_colorst)
        forca(erros_f, palavra_forca, letras_usadas)
        

        para_vencer = all(letra in letras_usadas for letra in palavra_escolhida)
        if para_vencer:
            window.blit(fonte.render("Venceu!", True, (0,255,0)), (450, 200))
        if erros_f >= 6:
            window.blit(fonte.render(f"Perdeu! Era: {palavra_escolhida}", True, (255,0,0)), (450, 200))
        

    elif telaMomento=="casita":
        from pygame import *
        import sys



        window.fill((160, 103, 97))

        
        Y = 50 + 0.067

        mixer.music.load('imperial_march.mp3')
        mixer.music.play(-1)
        
    
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

    display.flip()
    clock.tick(60)

quit()