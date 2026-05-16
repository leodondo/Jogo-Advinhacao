from random import * 
numero_secreto = randint (0,100)
print ("Tente advinhar o número entre 0 e 100!")

while True:
    palpite = int(input("Digite o seu palpite: "))

    if palpite < 0 or palpite > 100:
        print ("Digite um número entre 0 e 100!!")

    elif palpite < numero_secreto:
        print ("O número é maior!")

    elif palpite > numero_secreto:
        print ("O número é menor!")

    else:
        print ("Parabéns! Você acertou")

        break