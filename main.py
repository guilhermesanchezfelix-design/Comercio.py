
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
#Nota: as informações dos produtos cadastrados se encontram no arquivo "dados.csv"

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

# ==========================================
# ETAPA 2 - MATRIZ DO ESTOQUE
# RESPONSAVEL: WILLIAN BRYAN
# Organizacao dos produtos por setores
# ==========================================

matriz_estoque = [
    ["Perifericos", "Teclado", "Mouse"],
    ["Monitores", "Monitor Samsung", "Vazio"],
    ["Audio", "Headset HyperX", "Vazio"],
    ["Acessorios", "Mousepad", "Vazio"]
]

print("===== ORGANIZACAO DO ESTOQUE =====")

for setor in matriz_estoque:
    print(setor)

def ler_produtos_csv():
    produtos_csv = []
    with open("dados.csv", "r", encoding="utf8") as arquivo:
        arquivo.readline()  # Ignora o cabecalho do CSV.
        linha = arquivo.readline()
        while linha:
            nome, preco, quantidade = linha.strip().split(",")
            # Converte os valores do arquivo para numeros antes dos calculos.
            produtos_csv.append({
                "nome": nome.strip(),
                "preco": float(preco),
                "quantidade": float(quantidade)
            })
            linha = arquivo.readline()

    return produtos_csv


def listar_produtos():
    print("\n===== PRODUTOS =====")

    for produto in ler_produtos_csv():
        print("Nome:", produto["nome"])
        print("Preco: R$", produto["preco"])
        print("Quantidade:", produto["quantidade"])
        print("-------------------")


def mostrar_painel_consolidado():
    produtos_csv = ler_produtos_csv()
    valor_total = 0

    # Usa os dados da empresa definidos anteriormente no projeto.
    print("\n===== PAINEL CONSOLIDADO -", empresa["nome"], "=====")
    print("Ramo:", empresa["ramo"])
    print("Cidade:", empresa["cidade"])
    print("\nPRODUTOS EM ESTOQUE")
    print("Produto | Quantidade | Preco unitario | Valor em estoque")

    for produto in produtos_csv:
        # Soma o valor de cada produto (preco unitario x quantidade).
        valor_produto = produto["quantidade"] * produto["preco"]
        valor_total += valor_produto
        print(
            produto["nome"], "|",
            produto["quantidade"], "| R$",
            produto["preco"], "| R$",
            valor_produto
        )

    print("\nValor total do estoque: R$", valor_total)
    print("\nORGANIZACAO DO ESTOQUE")
    # Exibe a matriz de organizacao cadastrada anteriormente.
    for setor in matriz_estoque:
        print(setor)


def mostrar_matriz():
    print("\n===== MATRIZ DO ESTOQUE =====")

    for setor in matriz_estoque:
        print(setor)
        
# ==========================================
# ETAPA 3 - MENU PRINCIPAL
# RESPONSAVEL: LUCAS EDUARDO
# Navegacao e opcoes do sistema
# ==========================================

while True:
    print("\n===== ELETROMAX =====")
    print("1 - Listar produtos")
    print("2 - Mostrar matriz")
    print("3 - Painel consolidado")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "":
        print("Digite uma opcao!")

    elif opcao == "1":
        listar_produtos()

    elif opcao == "2":
        mostrar_matriz()

    elif opcao == "3":
        mostrar_painel_consolidado()

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opcao invalida!")
