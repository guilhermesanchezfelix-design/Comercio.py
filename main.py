
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
                "quantidade": int(quantidade)
            })
            linha = arquivo.readline()

    return produtos_csv


def salvar_produtos_csv(produtos_csv):
    with open("dados.csv", "w", encoding="utf8") as arquivo:
        arquivo.write("produtos, preço, quantidade\n")
        for produto in produtos_csv:
            arquivo.write(
                produto["nome"] + ", " +
                str(produto["preco"]) + ", " +
                str(produto["quantidade"]) + "\n"
            )


def listar_produtos_alteraveis(produtos_csv, apenas_com_estoque=False):
    produtos_alteraveis = [
        produto for produto in produtos_csv
        if not apenas_com_estoque or produto["quantidade"] > 0
    ]

    print("\n===== PRODUTOS DISPONIVEIS =====")
    for produto in produtos_alteraveis:
        print(produto["nome"], "- Quantidade:", produto["quantidade"])

    return produtos_alteraveis


def registrar_venda():
    produtos_csv = ler_produtos_csv()
    produtos_com_estoque = listar_produtos_alteraveis(
        produtos_csv, apenas_com_estoque=True
    )
    if not produtos_com_estoque:
        print("Nao ha produtos com estoque para registrar uma venda.")
        return

    for produto in produtos_com_estoque:
        if produto["quantidade"] < 5:
            print("Aviso: baixa quantidade em estoque para", produto["nome"])

    nome = input("Digite o nome do produto vendido: ").strip()

    produto_encontrado = None
    for produto in produtos_com_estoque:
        if produto["nome"].lower() == nome.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Erro: produto nao encontrado. Digite um nome de produto valido.")
        return

    try:
        quantidade_vendida = int(input("Digite a quantidade vendida: "))
        if quantidade_vendida <= 0:
            raise ValueError
    except ValueError:
        print("Erro: digite uma quantidade vendida valida.")
        return

    if quantidade_vendida > produto_encontrado["quantidade"]:
        print("Aviso: venda maior que o estoque. A quantidade ficara em zero.")

    quantidade_anterior = produto_encontrado["quantidade"]
    produto_encontrado["quantidade"] = max(
        0, produto_encontrado["quantidade"] - quantidade_vendida
    )
    salvar_produtos_csv(produtos_csv)
    print("Venda registrada. Estoque atualizado.")

    if quantidade_anterior >= 5 and produto_encontrado["quantidade"] < 5:
        print("Aviso: baixa quantidade em estoque para", produto_encontrado["nome"])


def adicionar_estoque():
    produtos_csv = ler_produtos_csv()
    produtos_alteraveis = listar_produtos_alteraveis(produtos_csv)
    if not produtos_alteraveis:
        print("Nao ha produtos cadastrados para adicionar estoque.")
        return

    nome = input("Digite o nome do produto: ").strip()

    produto_encontrado = None
    for produto in produtos_alteraveis:
        if produto["nome"].lower() == nome.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Erro: produto nao encontrado. Digite um nome de produto valido.")
        return

    try:
        quantidade_adicionada = int(input("Digite a quantidade adicionada: "))
        if quantidade_adicionada <= 0:
            raise ValueError
    except ValueError:
        print("Erro: digite uma quantidade adicionada valida.")
        return

    produto_encontrado["quantidade"] += quantidade_adicionada
    salvar_produtos_csv(produtos_csv)
    print("Quantidade adicionada. Estoque atualizado.")


def listar_produtos():
    print("\n===== PRODUTOS =====")

    for produto in ler_produtos_csv():
        print("Nome:", produto["nome"])
        print("Preco: R$", produto["preco"])
        print("Quantidade:", produto["quantidade"])
        if produto["quantidade"] <= 0:
            print("⚠️ Aviso: produto sem estoque.")
        elif produto["quantidade"] <= 5:
            print("⚠️ Aviso: produto com baixa quantidade no estoque.")
        print("-------------------")


def mostrar_painel_consolidado():
    produtos_csv = ler_produtos_csv()
    valor_total = 0

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
    print("2 - Painel consolidado")
    print("3 - Registrar venda")
    print("4 - Adicionar quantidade ao estoque")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "":
        print("Digite uma opcao!")

    elif opcao == "1":
        listar_produtos()

    elif opcao == "2":
        mostrar_painel_consolidado()

    elif opcao == "3":
        registrar_venda()

    elif opcao == "4":
        adicionar_estoque()

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opcao invalida!")
