import sqlite3

class Pessoa:
    def __init__(self, nome, idade, db_file='todolist.db'):
        self.nome = nome
        self.idade = idade
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL
            )
        ''')
        self.conn.commit()

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
                self.conn.execute('INSERT INTO tarefas (descricao) VALUES (?)', (nova_tarefa,))
                self.conn.commit()
        
    def exibir_tarefas(self):
        self.cursor.execute('SELECT id, descricao FROM tarefas ORDER BY id')
        tarefas = self.cursor.fetchall()
        if not tarefas:
            print('n tem tarefas')
        else:
            for tarefa in tarefas:
                print(f"Tarefa {tarefa[0]}: {tarefa[1]}")

    def deletar_tarefa(self):
        self.exibir_tarefas()
        escolha = int(input('Escolha a tarefa que deseja deletar: '))
        self.conn.execute('DELETE FROM tarefas WHERE id = ?', (escolha,))
        self.conn.commit()
        print('Tarefa deletada com sucesso!')
    
    def __del__(self):
        self.conn.close()

pessoa = Pessoa('', 0, 'todolist.db')
infoPessoa = pessoa.cadastrar_pessoa()

while True:
    escolha = pessoa.escolhas()
    if escolha == 1:
        pessoa.cadastrar_tarefa()
    elif escolha == 2:
        pessoa.exibir_tarefas()
    elif escolha == 3:
        pessoa.deletar_tarefa()
    elif escolha == 4:
        print('Sair')
        break

