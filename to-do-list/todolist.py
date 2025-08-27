class Pessoa:
    def __init__(self, nome, idade, tarefas):
        self.nome = nome
        self.idade = idade
        self.tarefas = tarefas

    def escolhas(self):
        print('[1] - Adicionar tarefa\n[2] - Ver tarefas\n[3] - Deleter tarefas\n[4] - Sair\n')
        escolha = int(input('Escolha uma opção: '))

        return escolha

    def cadastrar_pessoa(self):
        self.nome = input('Digite o seu nome: ')
        self.idade = int(input('Digite a sua idade: '))

        return self
    
    def cadastrar_tarefa(self):
        while True:
            print('[1] - Cadastre suas tarefas: \n [2] - Sair')
            escolha = int(input('Escolha uma opção: '))
            if escolha == 2:
                return False
            else:
                nova_tarefa = input('Cadastre a sua tarefa: ')
                self.tarefas.append(nova_tarefa)
        
    
    def exibir_tarefas(self):
        i = 0
        for tarefa in self.tarefas:
            i = i + 1
            print('Tarefa', i, '', tarefa)

    def deletar_tarefa(self):
        self.exibir_tarefas()
        escolha = int(input('Escolha a tarefa que deseja deletar: '))
        self.tarefas.pop(escolha - 1)

pessoa = Pessoa('', 0, [])
infoPessoa = pessoa.cadastrar_pessoa()

while True:
    escolha = infoPessoa.escolhas()
    if escolha == 1:
        pessoa.cadastrar_tarefa()
    elif escolha == 2:
        pessoa.exibir_tarefas()
    elif escolha == 3:
        pessoa.deletar_tarefa()
    elif escolha == 4:
        print('Sair')
        break

