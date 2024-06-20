import mysql.connector# Importa a função mysql.connector para conectar ao banco de dados MySQL

# Define a classe Aluno
class Aluno:# Define a classe aluno
    def __init__(self, nome, idade):#O método __init__ inicializa os atributos da classe aluno (Nome,idade)
        self.nome = nome# Atributo nome da instancia atribui o valor do parametro nome
        self.idade = idade# Atributo idade da instancia atribui o valor do parametro idade


class Professor:# Define a classe professor
    def __init__(self, nome, materia):#O método __init__ inicializa os atributos da classe professor (Nome,materia)
        self.nome = nome# Atributo nome da instancia atribui o valor do parametro nome
        self.materia = materia# Atributo materia da instancia atribui o valor do parametro materia

# Define a classe Curso
class Curso:# Define a classe curso
    def __init__(self, nome, carga_horaria):#O método __init__ inicializa os atributos da classe Usuario  (Nome,carga horaria)
        self.nome = nome# Atributo nome da instancia atribui o valor do parametro nome
        self.carga_horaria = carga_horaria# Atributo carga_horaria da instancia atribui o valor do parametro carga_horaria

# Define a classe SistemaEscola, que gerencia a conexão com o banco de dados e operações
class SistemaEscola:
    def __init__(self):#inicializa 
        # Estabelece a conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect( # conecta ao banco de dados 
            host="localhost",#endereco do servidor do banco de dados
            user="root",# Nome do usuário do banco de dados
            password="he182555@",# senha do usuário do banco de dados
            database="escola_db"# meu banco de dados
        )
        self.cursor = self.conexao.cursor()  # Cria um cursor para executar comandos SQL

    
    def adicionar_aluno(self): # Método para adicionar um aluno ao banco de dados
        nome = input("Digite o nome do aluno: ")  # Recebe o nome do aluno
        idade = input("Digite a idade do aluno: ")  # Recebe a idade do aluno
        aluno = Aluno(nome, idade)  # Cria uma instância da classe Aluno
        sql = "INSERT INTO aluno (nome_aluno, idade_aluno) VALUES (%s, %s)"  # Comando SQL para inserção
        valores = (aluno.nome, aluno.idade)  # definir  Valores a serem inseridos
        self.cursor.execute(sql, valores)  # Executa o comando SQL e valores
        self.conexao.commit()  # Confirma a transação
        print('Aluno adicionado com sucesso.')  # Mensagem de sucesso

    
    def adicionar_professor(self):# Método para adicionar um professor ao banco de dados
        nome = input("Digite o nome do professor: ")  # Recebe o nome do professor
        materia = input("Digite a matéria do professor: ")  # Recebe a matéria do professor
        professor = Professor(nome, materia)  # Cria uma instância da classe Professor
        sql = "INSERT INTO professor (nome_professor, materia_professor) VALUES (%s, %s)"  # Comando SQL para inserção
        valores = (professor.nome, professor.materia)  # Valores a serem inseridos
        self.cursor.execute(sql, valores)  # Executa o comando SQL
        self.conexao.commit()  # Confirma a transação
        print('Professor adicionado com sucesso.')  # Mensagem de sucesso

    
    def adicionar_curso(self): # Método para adicionar um curso ao banco de dados
        nome = input("Digite o nome do curso: ")  # Recebe o nome do curso
        carga_horaria = int(input("Digite a carga horária do curso: "))  # Recebe a carga horária do curso
        curso = Curso(nome, carga_horaria)  # Cria uma instância da classe Curso
        sql = "INSERT INTO curso (nome_curso, carga_horaria) VALUES (%s, %s)"  # executa o comando sql para inserir na tabela curso o nome do curso e sua carga horaria
        valores = (curso.nome, curso.carga_horaria)  # Valores a serem inseridos
        self.cursor.execute(sql, valores)  # Executa o comando SQL
        self.conexao.commit()  # Confirma a transação
        print('Curso adicionado com sucesso.')  # Mensagem de sucesso

    def listar_alunos(self): # Método para listar todos os alunos do banco de dados
        self.cursor.execute("SELECT nome_aluno, idade_aluno FROM aluno")  # Executa comando SQL para selecionar todos os alunos
        alunos = self.cursor.fetchall()  # Recupera todos os registros
        for aluno in alunos:  # para cada aluno em alunos  imprimir o resultado da f string abaixo
            print(f"Nome: {aluno[0]}, Idade: {aluno[1]}")  # Imprime os detalhes de cada aluno

    
    def listar_professores(self):# Método para listar todos os professores do banco de dados
        self.cursor.execute("SELECT nome_professor, materia_professor FROM professor")  # Executa comando SQL para selecionar todos os professores
        professores = self.cursor.fetchall()  # Recupera todos os registros
        for professor in professores:#para cada professor em professor imprimir  o resultado da f string abaixo
            print(f"Nome: {professor[0]}, Matéria: {professor[1]}")  # Imprime os detalhes de cada professor

    
    def listar_cursos(self):# Método para listar todos os cursos do banco de dados
        self.cursor.execute("SELECT nome_curso, carga_horaria FROM curso")  # Executa comando SQL para selecionar todos os cursos
        cursos = self.cursor.fetchall()  # Recupera todos os registros
        for curso in cursos:  # Itera sobre os registros
            print(f"Nome: {curso[0]}, Carga Horária: {curso[1]}")  # Imprime os detalhes de cada curso

    
    def fechar_conexao(self):# Método para fechar a conexão com o banco de dados
        self.cursor.close()  # Fecha o cursor
        self.conexao.close()  # Fecha a conexão

    
    def menu(self):# Método que exibe o menu de opções e chama os métodos correspondentes
        while True:  # enquanto for vverdadeiro Loop infinito para exibir o menu até que o usuário escolha sair
            print("Menu:")
            print("1. Adicionar aluno")
            print("2. Adicionar professor")
            print("3. Adicionar curso")
            print("4. Listar alunos")
            print("5. Listar professores")
            print("6. Listar cursos")
            print("7. Sair")
            escolha = input("Escolha uma opção: ")  # Recebe a escolha do usuário

            if escolha == '1':# se a opçao for 1
                self.adicionar_aluno()  # Chama o método para adicionar aluno
            elif escolha == '2':
                self.adicionar_professor()  # Chama o método para adicionar professor
            elif escolha == '3':
                self.adicionar_curso()  # Chama o método para adicionar curso
            elif escolha == '4':
                self.listar_alunos()  # Chama o método para listar alunos
            elif escolha == '5':
                self.listar_professores()  # Chama o método para listar professores
            elif escolha == '6':
                self.listar_cursos()  # Chama o método para listar cursos
            elif escolha == '7':
                self.fechar_conexao()  # Chama o método para fechar a conexão
                print("Conexão fechada. Saindo...")  # Mensagem de saída
                break  # Sai do loop
            else:
                print("Opção inválida. Tente novamente.")  # Mensagem para opção inválida

# Instancia o sistema de escola e exibe o menu
sistema = SistemaEscola()
sistema.menu()
