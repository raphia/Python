# Primeiros Passos
O nosso primeiro comando será o “print” [Impressão] escrito todo de minúsculo uma vez que Python linguagem sensitiva, ela considera “A” diferentes do “a” letras maiúsculas e minúsculas são diferentes, claro que sim, o problema na linguagem humana, pessoas terminam entendendo que a palavra melancia é a mesma que Melancia, pois para nossa linguagem que é bastante complexa esse nome se refere a uma fruta. 
Quando se trata de Python o computador não sabe que melancia é uma fruta, para ele Melancia diferente de melancia por que o “M” é diferente de “m”, pode ter certeza que Melancia , melancia , mElancia, MELANCIA, mELAncia são todas palavras diferentes, para o Python terão significados diferentes, algumas linguagens de programação como Pascal iria ignorar o caso sensitivo, mas no caso de Python de proposito ele não ignora, já para você ter oportunidade de organizar o código de forma mais padrão, para não virar uma bagunça! 
 O comando print ele é um objeto que suporta uma entrada de outro objeto ou uma variável. 
Tipo de uma palavra representado por aspas simples ou dupla. 

EX:

``` "Olá, Mundo!" ```

O mesmo pode ser representado por aspa simples

``` 'Olá, Mundo!' ```

Você não precisa digitar aspas para referir a algum numero

``` 10 ```

Caso coloque "." no numero ele deixa de ser inteiro para ser real tipo 

EX: Nota 9,5 ``` 9.5 ```

Preste atenção em uma pegadinha ``` "9.5" ``` uma vez que coloca aspas em qualquer numero deixa de ser numero para ser uma palavra, para o computador palavra pode ter qualquer caractere, se vc pensar bem o espaço é um caractere invisivel sem forma que ocupa lugar de uma letra!

EX:  ``` "1ss0 um4 p4l4vr4 c0ns3gu1 3nt3nd3r" ```

Para o computador uma palavra é uma coleção de caracteres, uma frase para ser humano pode ser uma palavra para o computador.

EX:  ``` "Eu estou vivo, ainda bem" ``` , para ser humano essa frase contem 5 palavras para o computador só é uma. Claro para o Computador palavra inicia na aspa e termina nas aspas.

Observa esse exemplo: 
 ``` "Eu estou vivo, ainda bem" "10.4" "5" "Olá Mundo" 8 2.5``` 

Se você respondeu tem 4 palavras , 1 numero inteiro , 1 numero real , parabens esse é o caminho que o Python interpreta as coisas.

que tal parti para patrica! Antes disso para criar o codigo de python presta atenção que o comentario é a linha ou linhas que não serão compiladas estão ali para entendimento. toda linha que iniciar com "#" é um comentario, (''' ou """) possivel criar comentarios de varias linhas ''' varias linhas ... ''' ou """ varias linhas """ vamos ser mais tradicional usar "#"


Que tal imprimir "Olá, Mundo!"
>print("Olá , Mundo!")

>#saida será: Olá , Mundo!

Que tal imprimir um numero 10
>print(10)
>#saida será: 10

Que tal somar 5+6
>print(5+6)
>#saida será: 11

Que tal somar "5"+"6"
>print("5"+"6")
>#saida será: 56, aqui você tem 2 palavras, a soma de palavras cria uma maior, chamamos isso de concatenação!!! 

## Comando input

O comando input faz com que uma variavel possa receber o objeto escrito objserva os exemplos.

>nome = input("Digite seu nome: ")

>print("Olá, " + nome + "! Seja bem-vindo(a) ao curso de Python")

>print("Vamos começar nossa jornada na programação!")

## Desafios!
Tente fazer antes de olhar para a respostas dos desafios.

## Desafio 01 
Pergunte o nome da pessoa, depois e imprima "Olá [NOME_DA_PESSOA] ! Grande prazer está na jornada Python com você." 
## Desafio 02 
Leia dia , o mês e o ano de um nascimento de uma pessoa e mostra mensagem com data formatada
## Desafio 03
Leia dois numeros e tente mostra a soma entre eles, obs: o input tem por natureza da uma saida do tipo palavra ou seja a soma de entrada 4 e 3 pode sair 43 , por ele ter uma saida 4 transformando em palavra e 3 em palavra "4" + "3" para evitar isso voce pode converter a variavel em numero inteiro. DICA ... 

>num1 = int(input("Digite um numero: "))

DICA de Impressão! para colocar variaveis de formatos diferentes usamos um print dessa forma com f de format.
>print(f"Mensagem {numero}")

Dentro dos {} você coloca as variaveis assim que você vai vencer o Desafio 03, qualquer coisa veja a resposta que abrirá sua mente. 