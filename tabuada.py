tabuada=int(input("Digite um numero para saber a tabuada:"))
for count in range(1, 11):
    print('{} x {:2} = {}' .format(tabuada, count, tabuada*count))
