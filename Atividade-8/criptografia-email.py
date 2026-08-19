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


