class Professor:

    def __init__(self, nome, hr_trabalhada):
        self.nome = nome
        self.hr_trabalhada = hr_trabalhada

    def calcular_salario_bruto(self):
        self.salario_bruto = self.hr_trabalhada * 50

        return self.salario_bruto

    def calcula_salario_liquido(self):
        salario_bruto = self.calcular_salario_bruto()
        self.__inss = salario_bruto * 0.12
        self.salario_liquido = self.salario_bruto - self.__inss
    
    def get_inss(self):
        return self.__inss


n = input('Digite o seu nome: ')
h = int(input('Digite a sua hora trabalhada: '))

professor = Professor(n, h)

professor.calcular_salario_bruto()
professor.calcula_salario_liquido()

print(professor.nome,'',professor.salario_liquido)

print('INSS: ', professor.get_inss())