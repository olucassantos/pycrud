import os
import sqlite3

# Variaveis
opcaoSelecionada = ''
imprimeMenu = True

# Cria o banco de dados
conn = sqlite3.connect('PyCrud.db')
cursor = conn.cursor()

# Cria a tabela de usuários
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, senha TEXT, telefone TEXT)");

# Funções

# Imprime o logo PyCrud em ASCII
def imprimeLogo():
    print('         ____   __   __   ____    ____      _   _   ____    ')
    print('       U|  _"\ u\ \ / /U /"___|U |  _"\ uU |"|u| | |  _"\   ')
    print('       \| |_) |/ \ V / \| | u   \| |_) |/ \| |\| |/| | | |  ')
    print('        |  __/  U_|"|_u | |/__   |  _ <    | |_| |U| |_| |\ ')
    print('        |_|       |_|    \____|  |_| \_\  <<\___/  |____/ u ')
    print('        ||>>_ .-,//|(_  _// \\   //   \\_(__) )(    |||_    ')
    print('       (__)__) \_) (__)(__)(__) (__)  (__)   (__)  (__)_)   ')

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def selecionaOpcao():
    global opcaoSelecionada, imprimeMenu

    opcaoSelecionada = input()

    # Se apenas apertou enter, não faz nada
    if opcaoSelecionada == "":
        imprimeMenu = True
        limpaTela()
        return
    
    # Se digitou algo, verifica se é um número
    try:
        opcaoSelecionada = int(opcaoSelecionada)
    except ValueError:
        print("Opção inválida, tente novamente.")
        selecionaOpcao()

    opcoes = [1, 2, 0]

    if opcaoSelecionada not in opcoes:
        print("Opção inválida, tente novamente.")
        selecionaOpcao()
    else:
        imprimeMenu = False

    limpaTela()

def cadastrarUsuario(nome, email, senha, telefone):
    # Valida os valores
    if nome == "":
        print("Nome não pode ser vazio.")
        return False
    
    if email == "":
        print("Email não pode ser vazio.")
        return False
    
    if senha == "":
        print("Senha não pode ser vazia.")
        return False
    
    if telefone == "":
        print("Telefone não pode ser vazio.")
        return False

    # Salva no banco de dados
    cursor.execute("INSERT INTO usuarios (nome, email, senha, telefone) VALUES (?, ?, ?, ?)", (nome, email, senha, telefone))
    conn.commit()

    # Checa se salvou
    if cursor.lastrowid:
        print("Usuário cadastrado com sucesso.")
        return True
    else:
        print("Erro ao cadastrar usuário.")
        return False

def listaDeUsuarios():
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    return usuarios

def apagarUsuario():
    pass

def editarUsuario():
    pass

# Main loop
while opcaoSelecionada != 0:
    # Menu
    if imprimeMenu:
        imprimeLogo()
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        print(f"---[1]-Cadastrar Usuário----------------------------------------")
        print(f"---[2]-Lista de Usuários----------------------------------------")
        print(f"---[0]-Sair-----------------------------------------------------")
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        selecionaOpcao()

    # Cadastrar Usuário
    if opcaoSelecionada == 1:
        print("----------------------Cadastrar Usuário-------------------------")
        print("----------------------------------------------------------------")
        nome = input("Nome: ")
        print("----------------------------------------------------------------")
        email = input("Email: ")
        print("----------------------------------------------------------------")
        senha = input("Senha: ")
        print("----------------------------------------------------------------")
        telefone = input("Telefone: ")
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")

        # Salva os dados no sqlite
        usuario = cadastrarUsuario(nome, email, senha, telefone)

        # Volta para o menu
        limpaTela()
        imprimeMenu = True
        opcaoSelecionada = ''
        continue


    # Lista de Usuários
    if opcaoSelecionada == 2:
        usuarios = listaDeUsuarios()

        print("----------------------Lista de Usuários-------------------------")
        print("----------------------------------------------------------------")
        print("----------------------------------------------------------------")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}")
            print(f"Nome: {usuario[1]}")
            print(f"Email: {usuario[2]}")
            print(f"Senha: {usuario[3]}")
            print(f"Telefone: {usuario[4]}")
            print("----------------------------------------------------------------")
            print("----------------------------------------------------------------")
        
        input("Pressione enter para voltar ao menu...")
        # Volta para o menu
        limpaTela()
        imprimeMenu = True
        opcaoSelecionada = ''
        continue

    # Sair
    if opcaoSelecionada == 0:
        print("Saindo...")
        break