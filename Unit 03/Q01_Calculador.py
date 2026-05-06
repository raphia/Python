#O Calculador de Idade: Crie um script que peça o ano de nascimento do usuário e calcule quantos anos ele terá em 2025.

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento
print(f"Em 2025, você terá {idade} anos.")