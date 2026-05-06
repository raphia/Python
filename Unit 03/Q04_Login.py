#Login Simples: Crie uma variável senha_mestra = "1234". 
#Peça para o usuário digitar uma senha. Se for igual, imprima "Acesso Liberado", senão imprima "Senha Incorreta".

senha_mestra = "1234"
user_pass = input("Digite a senha: ")

## Autenticação
if user_pass == senha_mestra :
    print("Autenticado com Sucesso!")
else :
    print("Senha digitada está incorreta")