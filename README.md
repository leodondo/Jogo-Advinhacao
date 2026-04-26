# Jogo-Advinhacao
Função: O desafio que fizemos em sala de aula consistia em criar um jogo onde o computador escolhe um número aleatório de 0 a 100 e se caso o usuário errar ele fala se o número é maior ou menor daquele que digitamos e pergunta outro palpite até o usuário acertar.
## Nome dos integrantes
Leonardo Hiroshi Dondo de Freitas
Gabriel Marinho Sarrão
Caio Alexandre da Silva Tavares
Murtllo Henrick Rosario Loiola Nascimento
Ricardo Polachini Mayer Gomes Marques
Victor Emanuel da Cruz Nardo
## Pré-requisitos
Python 3.14
## Como usar
Para usar, é necessário salvar o código em um arquivo com a extensão .py, por exemplo: jogo_advinhacao.py, após isso, é preciso abrir o terminal ou o prompt de comando e achar a pasta na qual você salvou. Para executar o programa, é necessário um comando, como: python jogo_advinhacao.py, ao iniciar o programa, irá aparecer uma mensagem falando para o usuário adivinhar um número de 0 a 100. Digite um número inteiro dentro esse intervalo e clica a tecla (enter). O programa informará se o número que você digitou é maior ou menor do que o número secreto. O programa irá continuar com as tentativas até o usuário acertar, quando acertar, exibirá uma mensagem te parabenizando e dizendo que você acertou. 
## Explicação Técnica
O programa que criamos utiliza a função randint (0,100) da biblioteca (random) para gerar um número aleatório entre 0 e 100. Já o laço (while True)  faz com que o jogo continue rodando até o usuário acertar o número. O comando (input) captura o palpite do usuário após responder à pergunta que aparece através do comando (print), e o comando (int) converte o valor digitado para número inteiro. As estruturas condicionais que usamos foram (if, elif e else) e servem para: validar se o número está entre 0 e 100, comparar o número digitado com o número secreto e informar se o valor correto é maior ou menor. O (break) encerra o loop quando o usuário acerta o número secreto, finalizando o nosso programa. 
## Links Github
Leonardo Hiroshi Dondo de Freitas 
https://github.com/leodondo 

Gabriel Marinho Sarrão 
https://github.com/gabrielmarinhosrr-art 

Caio Alexandre da Silva Tavares 
https://github.com/Tavares-Developer
 
Muryllo Henrick Rosario Loiola Nascimento 
https://github.com/pecinhadomal123 

Ricardo Polachini Mayer Gomes Marques 
https://github.com/ricardopolachini 

Victor Emanuel da Cruz Nardo 
https://github.com/vnardo
## Código usado para rodar o nosso programa
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
