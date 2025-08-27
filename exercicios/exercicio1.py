class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def calcula_imc(self):
        imc = self.peso / (self.altura ** 2)

        return imc
    
n = input('Digite o seu nome: ')
i = int(input('Digite a sua idade: '))
p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))

pessoa = Pessoa(n, i, p, a);    
print(pessoa.calcula_imc())

print(pessoa.nome)