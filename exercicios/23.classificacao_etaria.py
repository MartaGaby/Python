# 23. Classificação etária

idade= int(input("qual a sua idade: "))

if(idade<=12):
    print("infantil")
elif(idade>12)and(idade<17):
    print("adulto")      
elif(idade>18)and(idade<65):
    print("adulto") 
else:
    print("idoso")       