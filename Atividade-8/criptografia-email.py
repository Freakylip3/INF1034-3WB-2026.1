from pygame import*

init()

#var
background_color =(189, 0, 0)
window = display.set_mode((1280, 720))
running= True   
clock = time.Clock()
fonte= font.SysFont('arial', 25)
fonteT= font.SysFont('arial', 50, bold=True)
#fonte= font.SysFont("Courier New", 30)


def valida_email(email):
    return email[-8:] == "@puc.com"
        
    

def possuiMaiuscula(palavra):
    for caracter in palavra:
        if caracter.isupper():
            return True
    return False   

def possuiMinuscula(palavra):
    for caracter in palavra:
        if caracter.islower():
            return True
    return False
    
def possuiNumero(palavra):
    for caracter in palavra:
        if caracter.isdigit():
            return True
    return False
    



def valida_senha(senha):
    check_tamanho= len(senha) >=8
    check_maiuscula= possuiMaiuscula(senha)
    check_minuscula= possuiMinuscula(senha)
    check_numero= possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero



def criptografa_senha(senha):
    senha_cripto= ""
    ref= 65
    for char in senha:
        if char.isdigit():
            ref= ord("0")  #etapa1
            pos_alpha = ord(char) - ref #etapa2
            pos_cesar = pos_alpha + 3  #etapa3
            pos_cesar = pos_cesar % 10 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar #etapa 6
        elif char.isupper():
            ref= ord("A") #65 #etapa1
            pos_alpha = ord(char) - ref #etapa2
            pos_cesar = pos_alpha + 3  #etapa3
            pos_cesar = pos_cesar % 26 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar #etapa 6
           
        elif char.islower():
            #copiar logica do maiusculo, trocando ref para "a"
            ref= ord("a") #65 #etapa1
            pos_alpha = ord(char) - ref #etapa2
            pos_cesar = pos_alpha + 3  #etapa3
            pos_cesar = pos_cesar % 26 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar #etapa 6

        else:
            senha_cripto += char
    return senha_cripto


print(criptografa_senha("FreakyLip3"))


while running:     
    window.fill(background_color)
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev .type == KEYDOWN:
            if K_a <= ev.key <= K_z:
                letra = key.name(ev.key).lower()
    draw.rect(window, ((214, 214, 214)), (35, 10, 1210, 700))
    draw.rect(window, ((147, 149, 150)), (200, 130, 900, 80 )) #email
    draw.rect(window, ((82, 82, 82)), (200, 400, 900, 80 )) #senha
    
    caixa_email= Rect(210, 130, 900, 80 )
    caixa_senha= Rect(210, 400, 900, 80 )

    text_email= fonte.render.email, True, 255, 255, 255
    text_senha= fonte.render.email, True, 255, 255, 255

    window.blit(text_email, (caixa_email, 255, 255, 255))
    window.blit(text_senha, (caixa_senha, 255, 255, 255))


    display.flip()