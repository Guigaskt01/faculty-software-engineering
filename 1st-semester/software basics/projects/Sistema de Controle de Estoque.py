"""
Sistema de Controle de Estoque

Funcionalidades:
- Cadastrar produtos
- Listar produtos
- Buscar produtos
- Excluir produtos

Menus:
- Menu Principal
- Menu Administrativo
"""

# ===========================
# Variáveis Globais
# ===========================

# Lista temporária para armazenar produtos cadastrados na sessão
estoque = []

# Opções do menu principal
opcoes_menu = [
    "1 - Administrador",
    "2 - Operador",
    "0 - Sair"
]

# Opções do menu administrativo
opcoes_adm = [
    "1 - Cadastrar novo Produto",
    "2 - Listar Produto",
    "3 - Buscar Produto",
    "4 - Excluir Produto",
    "0 - Voltar"
]

# ===========================
# Funções de Menu
# ===========================

def menu():
    """
    Exibe o menu principal com as opções disponíveis.
    """
    print("\nMenu Principal")
    for opcao in opcoes_menu:
        print(opcao)


def menu_adm():
    """
    Exibe o menu administrativo com as funcionalidades disponíveis para o administrador.
    """
    print("\nMenu Administrativo")
    for opcao in opcoes_adm:
        print(opcao)

# ===========================
# Funções do Sistema
# ===========================

def cadastrar():
    """
    Solicita ao usuário o nome do produto e adiciona na lista 'estoque'.
    Faz uma validação para não aceitar nome vazio ou apenas números.
    """
    produto = input('Digite o nome do produto:\n').strip()

    while produto == "" or produto.isdigit():
        print("Nome inválido. Tente novamente.")
        produto = input('Digite o nome do produto:\n').strip()

    estoque.append(produto)


def salvar_estoque():
    """
    Salva os produtos cadastrados na lista 'estoque' no arquivo de texto 'Lista_de_produto.txt'.
    """
    arquivo = open("Lista_de_produto.txt", "a", encoding="utf-8")
    for item in estoque:
        arquivo.write(f"{item}\n")
        print(f"Produto '{item}' salvo com sucesso.")
    arquivo.close()


def listar_estoque():
    """
    Lista todos os produtos que estão registrados no arquivo 'Lista_de_produto.txt'.
    Caso o arquivo esteja vazio, informa que o estoque está vazio.
    """
    arquivo = open("Lista_de_produto.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()

    print("\nProdutos no estoque:")
    if conteudo:
        print(conteudo)
    else:
        print("Estoque vazio.")

    arquivo.close()


def buscar_estoque():
    """
    Permite buscar um produto específico pelo nome.
    O sistema lê o arquivo 'Lista_de_produto.txt' e verifica se o produto existe.
    """

    encadeador=0

    while encadeador == 0:
        produto = input("Digite o nome do produto para buscar:\n").strip()

        arquivo = open("Lista_de_produto.txt", "r", encoding="utf-8")
        encontrado = False

        for linha in arquivo:
            if produto.lower() in linha.lower():
                print(f"Produto encontrado: {linha.strip()}")
                encontrado = True
                encadeador = 1

        if not encontrado:
            print("Produto não encontrado no estoque.")

        arquivo.close()


def excluir_estoque():
    """
    Permite excluir um produto do estoque.
    O sistema lê todos os produtos do arquivo, remove o produto especificado e sobrescreve o arquivo sem ele.
    """
    produto = input("Digite o nome do produto que deseja excluir:\n").strip()

    # Abrir o arquivo para leitura
    arquivo = open("Lista_de_produto.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    # Criar nova lista sem o produto a ser removido
    encontrado = False
    nova_lista = []

    for linha in linhas:
        if produto.lower() != linha.strip().lower():
            nova_lista.append(linha)
        else:
            encontrado = True

    # Se o produto foi encontrado, sobrescreve o arquivo
    if encontrado:
        arquivo = open("Lista_de_produto.txt", "w", encoding="utf-8")
        for item in nova_lista:
            arquivo.write(item)
        arquivo.close()
        print(f"Produto '{produto}' foi excluído com sucesso.")
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

# ===========================
# Código Principal (Main)
# ===========================

# Controle de execução do programa
encadeador = 0

# Loop principal do programa
while encadeador == 0:
    # Exibe o menu principal
    menu()

    # Solicita a opção do usuário
    opcao = int(input('\nEscolha a opção conforme seu cargo:\n'))

    # Validação da opção
    while opcao not in [0, 1, 2]:
        print("Opção inválida. Tente novamente.")
        opcao = int(input('Escolha a opção conforme seu cargo:\n'))

    # Menu Administrador
    if opcao == 1:
        menu_adm()

        opcao_adm = int(input('Escolha a opção desejada:\n'))

        if opcao_adm == 1:
            cadastrar()
            salvar_estoque()
            encadeador = 1

        elif opcao_adm == 2:
            listar_estoque()
            encadeador = 1

        elif opcao_adm == 3:
            buscar_estoque()

        elif opcao_adm == 4:
            excluir_estoque()

        elif opcao_adm == 0:
            continue  # Volta para o menu principal

        else:
            print('Opção inválida. Tente novamente.')
            
            opcao_adm = int(input('Escolha a opção desejada:\n'))

    # Menu Operador (não implementado)
    elif opcao == 2:
        print("Função Operador ainda não implementada.")
        encadeador = 1

    # Encerrar o programa
    elif opcao == 0:
        print("Encerrando o sistema.")
        encadeador = 1
