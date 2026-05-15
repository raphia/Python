# Tipos Primitivos

Voçê já tem a noção do que é uma palavra no Python, mas deve está atento que é um tipo, e sim esse tipo é 'String'. 

Vejamos alguns tipos impostantes.

 TIPO NO PYTHON | TIPO | EXEMPLO 
-----------------|------|---------
 str | Palavra [String] | "Cerveja" 
 int | Inteiro [Integer] | 42
 float | Decimais [float] | 31.5
 char | Letra [Charactere] | 'R'
 bool | Boolean [Booleano] | True

 ## Variantes do Inteiro

 int para declarar inteiro! Porem se numero for pequena de 8 Bits, pode usar 'byte' se numero for muito grande pode usar 'long' tem 32 bits, se tem curiosidade sim o int tem 16 bits o tamanho da variavel. 

 ## Variante do float

 Caso numero decimal seja muito grande use double no lugar de float! 

 A palavra que você buscou é **Booleano** (ou **Boolean** em inglês). Em programação, e fundamentalmente em **Python**, este é o tipo de dado mais básico da lógica de programação. Ele representa a ideia de que algo pode ser **verdadeiro** ou **falso**.



## O Que é um Booleano?

Um booleano é um tipo de dado que só pode ter um de dois valores possíveis:

1.  **`True`** (Verdadeiro)
2.  **`False`** (Falso)

Esses valores são usados para controlar o fluxo do código, permitindo que seu programa tome decisões. O tipo em Python é `bool`.

```python
esta_ligado = True
tem_erro = False

print(type(esta_ligado)) # Saída: <class 'bool'>

Com certeza! Aqui está o conteúdo sobre Booleanos em Python formatado em Markdown (MD).

Você pode copiar e colar este texto diretamente em um arquivo com a extensão .md (por exemplo, booleano.md).
Markdown
```

# O Tipo de Dado Booleano em Python

A palavra que você buscou é **Booleano** (ou **Boolean** em inglês). Em programação, e fundamentalmente em **Python**, este é o tipo de dado mais básico da lógica de programação. Ele representa a ideia de que algo pode ser **verdadeiro** ou **falso**.



## O Que é um Booleano?

Um booleano é um tipo de dado que só pode ter um de dois valores possíveis:

1.  **`True`** (Verdadeiro)
2.  **`False`** (Falso)

Esses valores são usados para controlar o fluxo do código, permitindo que seu programa tome decisões. O tipo em Python é `bool`.

```python
esta_ligado = True
tem_erro = False

print(type(esta_ligado)) # Saída: <class 'bool'>
```


## Operadores de Comparação em Python

Estes operadores são usados para comparar dois valores e sempre retornam um resultado **Booleano** (`True` ou `False`).

| Operador | Significado | Exemplo | Resultado |
| :---: | :---: | :---: | :---: |
| **`==`** | Igual a | `5 == 5` | `True` |
| **`!=`** | Diferente de | `10 != 5` | `True` |
| **`>`** | Maior que | `7 > 9` | `False` |
| **`<`** | Menor que | `7 < 9` | `True` |
| **`>=`** | Maior ou igual a | `3 >= 3` | `True` |
| **`<=`** | Menor ou igual a | `3 <= 3` | `True` |

## 2.2. Operadores Lógicos

Os operadores lógicos são usados para combinar ou manipular valores booleanos:

| Operador | Função | Exemplo |
| :---: | :---: | :---: |
| **`and`** | Retorna `True` se **AMBOS** os lados forem `True`. | `True and False` $\rightarrow$ `False` |
| **`or`** | Retorna `True` se **PELO MENOS UM** dos lados for `True`. | `True or False` $\rightarrow$ `True` |
| **`not`** | Inverte o valor booleano (negação). | `not True` $\rightarrow$ `False` |