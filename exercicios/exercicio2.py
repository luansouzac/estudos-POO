class Professor:

    def __init__(self, nome, hr_trabalhada):
        self.nome = nome
        self.hr_trabalhada = hr_trabalhada

    def calcular_salario_bruto(self):
        self.salario_bruto = self.hr_trabalhada * 50

    def calcula_salario_liquido(self):
        self.inss = self.salario_bruto * 0.12
        self.salario_liquido = self.salario_bruto - self.inss


n = input('Digite o seu nome: ')
h = int(input('Digite a sua hora trabalhada: '))

professor = Professor(n, h)

professor.calcular_salario_bruto()
professor.calcula_salario_liquido()

print(professor.nome,'',professor.salario_liquido)