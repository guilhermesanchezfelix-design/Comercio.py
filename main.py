
# ==========================================
# ELETROMAX - CONTROLE DE ESTOQUE
# SEMANA 2 - ALUNO 1: GUILHERME
# CADASTRO E ENTIDADES BASE
# ==========================================

# Dados da empresa
empresa = {
    "nome": "EletroMax",
    "ramo": "Comercio de eletronicos",
    "cidade": "Sao Paulo"
}

# Produtos da loja
produtos = [
    {"nome": "Teclado Logitech", "preco": 150.00, "quantidade": 10},
    {"nome": "Mouse Logitech", "preco": 100.00, "quantidade": 15},
    {"nome": "Monitor Samsung", "preco": 300.00, "quantidade": 8},
    {"nome": "Headset HyperX", "preco": 200.00, "quantidade": 12},
    {"nome": "Mousepad Logitech", "preco": 50.00, "quantidade": 20}
]

# Exibindo os dados da empresa
print("===== DADOS DA EMPRESA =====")
print("Nome:", empresa["nome"])
print("Ramo:", empresa["ramo"])
print("Cidade:", empresa["cidade"])

# Exibindo os produtos cadastrados
print("\n===== PRODUTOS CADASTRADOS =====")

for produto in produtos:
    print("Nome:", produto["nome"])
    print("Preco: R$", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("------------------------------")

# Etapa 2 - Matriz 2d (Willian Bryan)
matriz_estoque = [
    ["Perifericos", "Teclado", "Mouse"],
    ["Monitores", "Monitor Samsung", "Vazio"],
    ["Audio", "Headset HyperX", "Vazio"],
    ["Acessorios", "Mousepad", "Vazio"]
]

print("===== ORGANIZACAO DO ESTOQUE =====")

for setor in matriz_estoque:
    print(setor)

    def listar_produtos():
        print("\n===== PRODUTOS =====")

    for produto in produtos:
        print("Nome:", produto["nome"])
        print("Preco:", produto["preco"])
        print("Quantidade:", produto["quantidade"])
        print("-------------------")


def mostrar_matriz():
    print("\n===== MATRIZ DO ESTOQUE =====")

    for setor in matriz_estoque:
        print(setor)


while True:
    print("\n===== ELETROMAX =====")
    print("1 - Listar produtos")
    print("2 - Mostrar matriz")
    print("3 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "":
        print("Digite uma opcao!")

    elif opcao == "1":
        listar_produtos()

    elif opcao == "2":
        mostrar_matriz()

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opcao invalida!")