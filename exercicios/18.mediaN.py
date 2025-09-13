qtd_nota= int(input("quantas notas seram adiconadas: "))
soma=0
for i in range(1,qtd_nota+1):
    nota= float(input(f"digite a nota {i}: "))
    soma= nota+soma
media = soma/qtd_nota
print("media: ",media)    