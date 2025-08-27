class Pessoa:
    def _init_(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def calcula_imc(self, nome, idade, peso, altura):
        imc = peso / (altura * altura)

        return imc
    
n = input('Digite o seu nome: ')
i = int(input('Digite a sua idade: '))
p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))

pessoa = Pessoa();
print(pessoa.calcula_imc(n, i, p, a))