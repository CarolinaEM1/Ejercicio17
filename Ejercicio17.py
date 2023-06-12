#Mostrar una frase sin espacio y contar

frase = input("Digite una frase -> ")
frase2 = ""

for i in frase:
    if i!= " ":
        frase2 += i

frase = frase2

print(f"\nFrase final: {frase}")
print(f"Numero de caracteres: {len(frase)}")

#Carolina EM
