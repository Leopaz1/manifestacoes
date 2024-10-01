import mysql.connector
from mysql.connector import Error
import datetime

# Conectar ao banco de dados
def criar_conexao():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='manifestacoes_db',
            user='root',  # Substitua pelo seu usuário
            password='Leo1285Paz'  # Substitua pela sua senha
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Erro na conexão: {e}")
    return None

# Função para listar manifestações
def listar_manifestacoes(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM manifestacoes")
    resultados = cursor.fetchall()
    if not resultados:
        print("Nenhuma manifestação cadastrada.")
        return
    for manifestacao in resultados:
        print(manifestacao)
    cursor.close()

# Função para criar manifestação
def criar_manifestacao(conn):
    codigo = input("Informe o código da manifestação: ")
    nome = input("Informe o nome da manifestação: ")
    tipo = input("Informe o tipo da manifestação (reclamação, elogio, sugestão): ").strip().lower()
    descricao = input("Informe a descrição da manifestação: ")
    data = datetime.datetime.now()

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO manifestacoes (codigo, nome, tipo, descricao, data) VALUES (%s, %s, %s, %s, %s)",
                       (codigo, nome, tipo, descricao, data))
        conn.commit()
        print("Manifestação criada com sucesso.")
    except Error as e:
        print(f"Erro ao criar manifestação: {e}")
    finally:
        cursor.close()

# Função para pesquisar manifestações por nome
def pesquisar_por_nome(conn):
    nome = input("Informe o nome da manifestação a ser pesquisada: ")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM manifestacoes WHERE nome LIKE %s", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Nenhuma manifestação encontrada com o nome especificado.")
        return
    for manifestacao in resultados:
        print(manifestacao)
    cursor.close()

# Função para pesquisar manifestações por código
def pesquisar_por_codigo(conn):
    codigo = input("Informe o código da manifestação a ser pesquisado: ")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM manifestacoes WHERE codigo = %s", (codigo,))
    manifestacao = cursor.fetchone()
    
    if manifestacao:
        print(manifestacao)
    else:
        print("Manifestação com o código informado não encontrada.")
    cursor.close()

def menu():
    conn = criar_conexao()
    if conn is None:
        return

    while True:
        print("\nMenu do Sistema")
        print("1) Listagem das Manifestações")
        print("2) Criar uma nova Manifestação")
        print("3) Pesquisar manifestação por nome")
        print("4) Pesquisar manifestação por código")
        print("5) Sair do Sistema")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_manifestacoes(conn)
        elif opcao == '2':
            criar_manifestacao(conn)
        elif opcao == '3':
            pesquisar_por_nome(conn)
        elif opcao == '4':
            pesquisar_por_codigo(conn)
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

    conn.close()

# Execução do sistema
menu()