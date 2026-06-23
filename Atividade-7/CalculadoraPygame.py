from pygame import *
import sys
 
init()
 
window = display.set_mode((420, 600))
background_color = (19, 108, 145)
running = True
clock = time.Clock()
fonte = font.SysFont('arial', 25)
prim_num = ""
seg_num = ""
num_salvo = 0
operacao = ""
resul = ""
window.fill(background_color)
 
 
def calculadora(n1, n2, op):
    if op == "+":
        return str(n1 + n2)
    elif op == "-":
        return str(n1 - n2)
    elif op == "*":
        return str(n1 * n2)
    elif op == "/":
        if n2 == 0:
            return "erro"
        return str(n1 / n2)
    else:
        return "erro"
 
 
calc = transform.scale(image.load("./Atividade-7/assets/calculating-machine.png"), (420, 600))
 
 
while running:
    window.fill(background_color)
 
    window.blit(calc, (0, 0))
    window.blit(fonte.render('1', True, (255, 255, 255)), (106, 220))
    window.blit(fonte.render('2', True, (255, 255, 255)), (170, 220))
    window.blit(fonte.render('3', True, (255, 255, 255)), (234, 220))
    window.blit(fonte.render('x', True, (255, 255, 255)), (302, 220))
    window.blit(fonte.render('4', True, (255, 255, 255)), (106, 315))
    window.blit(fonte.render('5', True, (255, 255, 255)), (170, 315))
    window.blit(fonte.render('6', True, (255, 255, 255)), (234, 315))
    window.blit(fonte.render('/', True, (255, 255, 255)), (302, 315))
    window.blit(fonte.render('7', True, (255, 255, 255)), (106, 410))
    window.blit(fonte.render('8', True, (255, 255, 255)), (170, 410))
    window.blit(fonte.render('9', True, (255, 255, 255)), (234, 410))
    window.blit(fonte.render('=', True, (255, 255, 255)), (302, 445))
    window.blit(fonte.render('+', True, (255, 255, 255)), (106, 502))
    window.blit(fonte.render('0', True, (255, 255, 255)), (170, 502))
    window.blit(fonte.render('-', True, (255, 255, 255)), (240, 502))
 
    for evento in event.get():
 
        if evento.type == QUIT:
            running = False
 
        if evento.type == KEYDOWN:
            tecla = evento.unicode 
 
            if tecla in "0123456789":
                prim_num += tecla
 
            elif tecla in "+-*/":
                if prim_num != "":
                    num_salvo = float(prim_num)
                    operacao = tecla
                    prim_num = ""
 
            elif evento.key == K_RETURN:
                if prim_num != "" and operacao != "":
                    n2 = float(prim_num)
                    resultado = calculadora(num_salvo, n2, operacao)
                    prim_num = str(resultado)
                    operacao = ""
 
            elif evento.key == K_BACKSPACE:
                prim_num = prim_num[:-1]
 
    
    if operacao != "":
        mostra = f'{num_salvo}{operacao}{prim_num}'
    else:
        mostra = prim_num if prim_num != "" else "0"
 
    tela = fonte.render(mostra, True, (255, 255, 255))
    window.blit(tela, (100, 130))
    clock.tick(60)
    display.update()
 
quit()
sys.exit()
