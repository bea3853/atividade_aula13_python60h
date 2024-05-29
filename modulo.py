def calculo_do_produto(x):
    lista = []
    for n in range(1,11):
        lista.append(n)
        resulta =  x * n
        lista.append(resulta)
        print(resulta)
    print(lista)