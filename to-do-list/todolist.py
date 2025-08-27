class Pessoa:
    def __init__(self, nome, idade, tarefas):
        self.nome = nome
        self.idade = idade
        self.tarefas = tarefas

    def escolhas(self):
        print('[1] - Adicionar tarefa\n[2] - Ver tarefas\n[3] - Sair\n')
        escolha = int(input('Escolha uma opção: '))

        return escolha

    def cadastrar_pessoa(self):
        self.nome = input('Digite o seu nome: ')
        self.idade = int(input('Digite a sua idade: '))

        return self
    
    def cadastrar_tarefa(self):
        nova_tarefa = input('Cadastre a sua tarefa: ')
        self.tarefas.append(nova_tarefa)

        return self
        
pessoa = Pessoa('', 0, [])
infoPessoa = pessoa.cadastrar_pessoa()

while True:
    escolha = infoPessoa.escolhas()
    if escolha == 1:
        pessoa.cadastrar_tarefa()
    elif escolha == 2:
        print(pessoa.tarefas)
    elif escolha == 3:
        print('Sair')
        break

