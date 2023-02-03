FRONT = "***************" # = 20CARACTERES, 20
i = 0 #PARAMETRO PARA UM LOOP 
for x in FRONT:
    i+=1
    s = len(FRONT) - i
    d = i - 1 # USADO PARA FAZER 
    print(" "*s+""+"x"*(i+i)+""+"#"*d)
#print("."*(len(FRONT)*2+3))
