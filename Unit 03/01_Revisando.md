# 1. O que é Python?

Imagine que você está dando ordens a um assistente muito eficiente, mas que precisa de instruções claras. Python é uma linguagem de alto nível, o que significa que ela é escrita de um jeito muito parecido com o inglês/português, facilitando a leitura.

### Por que aprender?

* __Simplicidade__: Menos regras chatas de sintaxe que outras linguagens (como C ou Java). 
* __Versatilidade__: Serve para inteligência artificial, automação de sistemas, criação de sites e ciência de dados.
* __Comunidade__: Se você tiver um erro, 99% de chance de alguém já ter resolvido na internet.

# 2. O Conceito de Variáveis

Uma variável é como uma caixa onde você guarda uma informação para usar depois. Em Python, você não precisa dizer "que tipo" de caixa ela é; o Python descobre sozinho.

```
# Guardando informações nas "caixas"
nome = "Raphia"         # Isso é um texto (String)
idade = 25              # Isso é um número inteiro (Int)
altura = 1.75           # Isso é um número decimal (Float)
estudando = True        # Isso é um valor verdadeiro/falso (Boolean)

# Usando as informações
print(nome)
```
# 3. Estruturas de Decisão (O "E se?")

A programação serve para tomar decisões. O comando principal aqui é o ``` if ``` (se) e o ``` else ``` (senão).
```
temperatura = 30

if temperatura > 25:
    print("Está calor, ligue o ventilador!")
else:
    print("A temperatura está agradável.")
```

# 4. Mão na Massa (Seu primeiro Script)
Como você já tem o Python configurado nas suas VMs (Mint ou Pop!_OS), abra o terminal ou seu editor de código (como o VS Code) e crie um arquivo chamado ```teste.py```.

Cole este código, que mistura o que vimos:
```
print("--- Sistema de Boas-Vindas ---")
usuario = input("Digite seu nome: ")

if usuario == "Raphia":
    print("Acesso concedido. Bem-vinda, Admin!")
else:
    print(f"Olá {usuario}, você tem acesso de visitante.")
```

Para rodar, basta digitar no terminal: ```python3 teste.py```

## Os desafios tentes fazer sozinhos depois olhe o Gabarito!

# DESAFIOS Q01 até Q05
Q01 - O Calculador de Idade: Crie um script que peça o ano de nascimento do usuário e calcule quantos anos ele terá em 2025.
Q02 - Par ou Ímpar: Peça um número ao usuário e use o operador % (resto da divisão) para dizer se o número é par ou ímpar. (Dica: se o resto da divisão por 2 for 0, é par).
Q03 - Conversor de Temperatura: Peça uma temperatura em Celsius e converta para Fahrenheit usando a fórmula: F = C * 1.8 + 32.
Q04 - Login Simples: Crie uma variável senha_mestra = "1234". Peça para o usuário digitar uma senha. Se for igual, imprima "Acesso Liberado", senão imprima "Senha Incorreta".
Q05 - Calculadora de Desconto: Peça o preço de um produto e aplique 10% de desconto. Exiba o novo preço na tela.

# DESAFIOS 2 
### Nível 1: Variáveis e Operações Matemáticas  N1_01 até N1_05
N1_01 Média de Notas: Peça 3 notas ao usuário e exiba a média aritmética.

N1_02 Dobro e Triplo: Peça um número e exiba o seu dobro e a sua terça parte.

N1_03 Conversor de Medidas: Peça um valor em metros e exiba convertido em centímetros e milímetros.

N1_04 Calculadora de Área: Peça a largura e a altura de uma parede em metros. Calcule a área e a quantidade de tinta necessária para pintá-la (considerando que cada litro de tinta pinta 2m²).

N1_05 Antecessor e Sucessor: Peça um número inteiro e mostre o seu antecessor e seu sucessor.

### Nível 1: Condições Básicas (if/else)  N1_06 até N1_10
N1_06 Radar Eletrônico: Peça a velocidade de um carro. Se ultrapassar 80km/h, exiba uma mensagem dizendo que ele foi multado. A multa custa R$ 7,00 por cada km acima do limite.

N1_07 Maior e Menor: Peça dois números e mostre qual deles é o maior ou se são iguais.

N1_08 Par ou Ímpar: Crie um programa que receba um número e diga se ele é par ou ímpar usando o operador %

N1_09 Aumento Salarial: Se o salário for superior a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

N1_10 Custo da Viagem: Pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

### Nível 1: Lógica e Condições Compostas (elif) N1_11 até N1_15