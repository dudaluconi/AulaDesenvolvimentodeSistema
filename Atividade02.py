
3- n1 = int(input("Digite o primeiro número: "))


for numero in range (1,11):
    print(f'{n1} X {numero} = {n1*numero}')


#1
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
Soma = n1 + n2 + n3 + n4 + n5


print("A soma dos 5 números é de ", Soma)


#2
 n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
maior = n1


if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
   
menor = n1


if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
   
print(f"O menor número é {menor} e o maior número é {maior}")




#3
palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
quantidade = 0




while palavra:
    if palavra[0] in vogais:
        quantidade += 1
    palavra = palavra[1:]
print(f"A palavra tem {quantidade} vogais.")




#4
contador = 0    
numeros_pares = []




while contador < 6:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    contador += 1




print("Os números pares digitados foram:", numeros_pares)
print("Números pares digitados:", numeros_pares)




#5




nota1 = float(input('Digite sua nota'))
nota2 = float(input('Digite sua nota'))
nota3 = float(input('Digite sua nota'))
nota4 = float(input('Digite sua nota'))




media = nota1+nota2 + nota3 + nota4
print(f'Sua média é: {media/4}')






#6
n1 = int(input("Digite o primeiro número: "))


for numero in range (1,11):
    print(f'{n1} X {numero} = {n1*numero}')




#7
n1 = int(input("Digite um número: "))


n2 = 1
while n2 <= n1:
    print(n2)
    n2 += 1




#8
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]
print(palavra_invertida)




#9
numero = int(input("Digite um número: "))




if numero % 3 == 0:
    print("O número é múltiplo de 3.")
else:
    print("O número não é múltiplo de 3.")




#10
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")


nomes = [nome1, nome2, nome3]


nomes.sort()


print("Nomes em ordem alfabética:")
print(nomes[0])
print(nomes[1])
print(nomes[2])

