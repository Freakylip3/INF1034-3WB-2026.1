from pygame import*
import sys
import random

init()
nums = [    100, 120, 130, 120, 150,  100, 160, 200, 190, 110, 115, 125, 135, 170, 130]
lista1 = [random.randint(100, 200) for _ in range(50)]
num_cat1 = 5
lista2_base = [100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130]
lista2 = [random.choice(lista2_base) + random.randint(-15, 15) for _ in range(len(lista2_base))]
num_cat2 = 5
lista3 = []
num_cat3 = 5
running=  True
window = display.set_mode((1280, 720))
fonte = font.SysFont("Arial", 15)
texto_input = ""
input_ativo = True
caixa_input = Rect(540, 300, 200, 45)
tela_atual=0 



def contabiliza_totais(nums, num_cat):
    if not nums:
        return [0] * num_cat
        
    num_min = min(nums)
    num_max = max(nums)
    tam_cat = (num_max - num_min) / num_cat
    
    if tam_cat == 0: 
        tam_cat = 1
    lista_total = [0] * num_cat

    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue
        
        for i_cat in range(num_cat):
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total


def desenho(screen, lista_total, cores_categorias, titulo):
    screen_h = screen.get_height()
    base_y = screen_h - 150  
    x_offset = 400          


    txt_menu = fonte.render("<    >", True, (0, 255, 255))
    screen.blit(txt_menu, (380, screen_h - 60))

    draw.line(screen, (200, 200, 200), (x_offset - 10, base_y), (x_offset - 10, base_y - 350), 2)
    comprimento_eixo = len(lista_total) * 80 + 20
    draw.line(screen, (200, 200, 200), (x_offset - 10, base_y), (x_offset - 10 + comprimento_eixo, base_y), 2)

    for i in range(len(lista_total)):
        x = x_offset + i * 80
        h = 20 * lista_total[i] 
        cor_barra = cores_categorias
        if h > 0:
            draw.rect(screen, cor_barra, (x, base_y - h, 50, h))
        
        # Marcações
        texto_qtd = fonte.render(str(lista_total[i]), True, (255, 255, 255))
        screen.blit(texto_qtd, (x + 18, base_y - h - 20))
        
        texto_faixa = fonte.render(f"Faixa {i+1}", True, (150, 150, 150))
        screen.blit(texto_faixa, (x + 5, base_y + 15))

cores_h1 =((252, 3, 223))
cores_h2 =((18, 199, 8))
cores_h3 =((252, 186, 3))

totais1 = contabiliza_totais(lista1, num_cat1)
totais2 = contabiliza_totais(lista2, num_cat2)
totais3 = [0] * num_cat3

relogio = time.Clock()

while running:
    relogio.tick(60)  
    
    for evento in event.get():
        if evento.type == QUIT:
            running = False
            
        elif evento.type == KEYDOWN:
            
            if evento.key == K_RIGHT and tela_atual > 0:
                tela_atual = tela_atual + 1 if tela_atual < 3 else 1
            elif evento.key == K_LEFT and tela_atual > 0:
                tela_atual = tela_atual - 1 if tela_atual > 1 else 3
            elif tela_atual == 0 and input_ativo:
                if evento.key == K_RETURN:
                    if texto_input != "":
                        lista3.append(int(texto_input))
                    texto_input = "" 
                elif evento.key == K_BACKSPACE:
                    texto_input = texto_input[:-1]
                elif evento.key == K_SPACE: 
                    if len(lista3) > 0:
                        totais3 = contabiliza_totais(lista3, num_cat3)
                        tela_atual = 1 
                        input_ativo = False
                elif evento.key == K_0: texto_input += "0"
                elif evento.key == K_1: texto_input += "1"
                elif evento.key == K_2: texto_input += "2"
                elif evento.key == K_3: texto_input += "3"
                elif evento.key == K_4: texto_input += "4"
                elif evento.key == K_5: texto_input += "5"
                elif evento.key == K_6: texto_input += "6"
                elif evento.key == K_7: texto_input += "7"
                elif evento.key == K_8: texto_input += "8"
                elif evento.key == K_9: texto_input += "9"

    window.fill((20, 20, 20))
    lista_total = totais1
    if tela_atual == 0:
        txt_aviso = fonte.render("Digite numeros e de enter para validá-los. Depois, aperte espaço para ver os graficos:", True, (255, 255, 255))
        window.blit(txt_aviso, (400, 250)) 
                
        draw.rect(window, (50, 50, 50), caixa_input, 0, 5)
        draw.rect(window, (0, 255, 255), caixa_input, 2, 5)
        txt_digitado = fonte.render(texto_input, True, (255, 255, 255))
        window.blit(txt_digitado, (caixa_input.x + 15, caixa_input.y + 15))
    elif tela_atual == 1:
        desenho(window, totais1, cores_h1, "Histograma 1")
    elif tela_atual == 2:
        desenho(window, totais2, cores_h2, "Histograma 2")
    elif tela_atual == 3:
        desenho(window, totais3, cores_h3, "Histograma 3")
    display.flip()

QUIT()