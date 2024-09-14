def data100Anos(nome, idade):
    ano = 100-idade
    ano100 = 2023+ano
    print("Fará 100 anos em ", ano100)
    
idade = 33
nome = "Lena"
data100Anos(nome, idade)

#definição dde valores padrão em funções
def data100Anos(nome, idade=30):
    ano = 100-idade
    ano100 = 2023+ano
    print("Fará 100 anos em ", ano100)

nome = "Lena"
data100Anos(nome)
