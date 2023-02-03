
#O 'c' é utilizado para dar o espaçamento e alinhamento central.
#Quando colocado o 'cd' ele gera a metade de um triângulo.
#Ao concatenar c+cd o "cd" além de criar um triangulo do lado direito, também cria um do lado esquerdo, pois o espaçamento vai diminuindo conforme o loop passa.

#No inicio setamos o espaçamento como "s=length-i" isso significa que o espaçamento começara no tamanho da string "FRONT" e diminuira 1 caractere até chegar ao final dela. É como se começarmos pela ultima letra e irmos colocando as que antecedem ela.

#Após isso o "cd" vai sendo criado apartir do ponto C se ele for 0 então o cd começara em 0, se for 10, começara em 10. No nosso exemplo o 'cd' iniciara em na ultima letra da string "FRONT" e ira aumentando conforme o loop passa.

def main_triangle():
    FRONT = "*************************"
    SHADOW = ".........................."
    i = 0
    length = len(FRONT)
    print(length)
    tam_sombra =  0
    xxD = -5
    h = 0
    g = 0
    for x in FRONT: #CRIA UM LOOP DO TAMANHO DA STRINGG (FRONT)
        i +=1  #A cara vez que o loop for executado ira aumentar + 1
        
        ''' TRIÂNGULO'''
        
        s = length-i #Pegamos o valor de "length" ou tamanho da string, e diminuimos em "i" ou seja, -1 a caada loop
        c = " "*s #UTILIZADO PARA DAR O ESPAÇAMENTO NO TRIANGULO, FAZENDO ELE ALINHAR AO MEIO DA TELA!
        t = i*2 #Utilizado para proporcionar um formato triângular do tamanho da string
        cd = "."
        xxt= "#"*i+"." #LADO DIREITO DO TRIANGLE
        ce = xxt
        ''' SOMBRA '''
        sombra = "X"*i+"."  #LADO ESQUERDO DO TRIANGLE
        if i >= 20:
            h +=8
            fg = 15
            fg -=1
            g +=4
            xe = "X"*(i-g)+"." #PARTE ESQUERDA DA BASE
            xd = " "*(h)+"."#27 #BASE
            xxD  += 3
            cer = "#"*round(length-12-xxD)+"."


            #print(c+cd+xe+xd)
            sombra = " "*i+"."
            print(c+cd+xe+xd+cer)
        else:
            print(c+cd+sombra+ce)
    print("."*54)

main_triangle()

