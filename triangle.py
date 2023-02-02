
def main_triangle():
    FRONT = "*************************"
    i = 0
    length = len(FRONT)
    for x in FRONT:
        i +=1
        s = length-i
        c = " "*s
        #UTILIZADO PARA DAR O ESPAÇAMENTO NO TRIANGULO, FAZENDO ELE ALINHAR AO MEIO DA TELA!
        t = i*2
        cd = "t"*t

        #O 'c' é utilizado para dar o espaçamento e alinhamento central.
        #Quando colocado o 'cd' ele gera a metade de um triângulo.
        #Ao concatenar c+cd o "cd" além de criar um triangulo do lado direito, também cria um do lado esquerdo, pois o espaçamento vai diminuindo conforme o loop passa.

        #No inicio setamos o espaçamento como "s=length-i" isso significa que o espaçamento começara no tamanho da string "FRONT" e diminuira 1 caractere até chegar ao final dela. É como se começarmos pela ultima letra e irmos colocando as que antecedem ela.

        #Após isso o "cd" vai sendo criado apartir do ponto C se ele for 0 então o cd começara em 0, se for 10, começara em 10. No nosso exemplo o 'cd' iniciara em na ultima letra da string "FRONT" e ira aumentando conforme o loop passa.

        print(c,cd)

main_triangle()
