lado1 = float(input("digite o comprimento do primeiro lado"))
lado2 = float(input("digite o comprimento do segundo lado"))
lado3 = float(input("digite o comprimento do terceiro lado"))
if(lado1<lado2+lado3)and (lado2< lado1+lado3) and(lado3<lado1+lado2):
    print("os lados não foram um triangulo")
else:
    print("Os lados não forman um triangulo.")
if lado1== lado2== lado3:
    print("O triangulo é equilatero.")
elif lado1 == lado2 or lado1==lado3 or lado2 ==lado3:
    print("o triangulo é isóscels.")
else:
    print("O triangulo é escaleno" )                