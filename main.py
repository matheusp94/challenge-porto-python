import pandas as pd
import json
import os
import csv
from tabulate import tabulate


# recebendo o banco de dados. O arquivo utilizado para teste foi bancodedados.csv, codificado em utf-8
# Lista de possíveis delimitadores
possiveis_delimitadores = [';', ',', '\t', '|', ':']

# Nome do arquivo CSV
nome_arquivo = 'bancodedados.csv'  # modifique aqui se necessário

# Inicializa o DataFrame como None
df = None

try:
    print('\nO programa está recebendo arquivos necessários para iniciar a área de trabalho.')

    for delimitador in possiveis_delimitadores:
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv, delimiter=delimitador)
                primeira_linha = next(leitor_csv)
                df = pd.DataFrame(list(leitor_csv), columns=primeira_linha)
            break  # Sair do loop quando um delimitador funcionar
        except (FileNotFoundError, UnicodeDecodeError):
            continue
        except Exception as e:
            print(
                f"Ocorreu um erro inesperado ao tentar o delimitador '{delimitador}': {e}")

    if df is not None:
        print("Arquivo CSV lido com sucesso.")

        # Verificar se a coluna 'id' não existe ou não é numérica
        if 'id' not in df.columns or not df['id'].str.replace(',', '', regex=True).str.isnumeric().all():
            # Adicionar uma coluna 'id' com valores incrementados automaticamente
            df.insert(0, 'id', range(1, len(df) + 1))

        data_dict = df.to_dict(orient='records')

        # Verificar se o arquivo JSON já existe
        if not os.path.exists('bancodedados.json'):
            # Salvando o JSON em um arquivo
            with open('bancodedados.json', 'w') as json_file:
                json.dump(data_dict, json_file, indent=4)

            print(
                f"O banco de dados editável inicial está pronto para uso. Foram encontrados {len(df)} registros.")
        else:
            print("O arquivo JSON já existe.")

    else:
        print(
            "Não foi possível ler o arquivo CSV com nenhum dos delimitadores disponíveis.")

except FileNotFoundError:
    print("O arquivo CSV não foi encontrado.")

except UnicodeDecodeError:
    print("O arquivo não pôde ser decodificado corretamente. Verifique a codificação.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

finally:
    print("Operação concluída.")
################################

try:
    with open('bancodedados.json', 'r') as json_file:
        print("O banco de dados já existe.")
except FileNotFoundError:
    print("O banco de dados editável inicial está sendo gerado...")

registros = []

for _, linha in df.iterrows():
    registro = linha.to_dict()

    registros.append(registro)


# criando lista de registros que alimentam um dicionário
numero_de_registros = df.shape[0]

# Substitua a seção onde você cria 'registros' pelo seguinte código
data_dict = df.to_dict(orient='records')

# Salvando o JSON em um arquivo
with open('bancodedados.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(
    f"O banco de dados editável está pronto para uso. Foram encontrados {numero_de_registros} registros.")

# Função para carregar o JSON a partir do arquivo


def carregar_json():
    try:
        with open('bancodedados.json', 'r') as json_file:
            data = json.load(json_file)

        # Atribuir IDs se não estiverem presentes nos registros carregados
        for i, registro in enumerate(data, start=1):
            if 'id' not in registro:
                registro['id'] = i

        return data
    except FileNotFoundError:
        print("O arquivo JSON não foi encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar o JSON: {e}")
        return []
    else:
        print("JSON carregado com sucesso.")
    finally:
        print("Operação de carregamento concluída.")


# Função para salvar o JSON de volta ao arquivo


def salvar_json(data):
    with open('bancodedados.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


# adicionando um novo registro com um "id" incrementado automaticamente


def adicionar_registro(data):
    novo_registro = {}
    print("\nAdicionar um novo registro:")

    # Verificando o próximo ID disponível
    proximo_id = max([registro.get("id", 0)
                     for registro in data], default=0) + 1

    for chave in data[0].keys():
        if chave == "id":
            novo_valor = proximo_id  # Configurar o novo ID automaticamente
        else:
            while True:
                novo_valor = input(f"{chave}: ")
                if novo_valor.lower() == "voltar":
                    return
                elif novo_valor:
                    break
                else:
                    print(f"{chave} não pode ser vazio.")
        novo_registro[chave] = novo_valor
    data.append(novo_registro)
    salvar_json(data)
    print("Registro adicionado com sucesso!")

# editando um registro existente


def editar_registro(data):
    print("\nEditar um registro existente:")

    # Exibir a lista de IDs disponíveis
    print("IDs disponíveis para edição:")
    for i, registro in enumerate(data):
        print(f"{i + 1}: ID {registro['id']}")

    while True:
        id_a_editar = input(
            "Digite o ID do registro a ser editado ou 'voltar' para retornar: ").strip()
        if id_a_editar.lower() == "voltar":
            return
        elif not id_a_editar.isdigit():
            print(
                "ID inválido. Digite um número inteiro válido ou 'voltar' para retornar.")
        else:
            id_a_editar = int(id_a_editar)
            if id_a_editar < 1 or id_a_editar > len(data):
                print("ID fora do intervalo válido.")
            else:
                break

    registro_a_editar = data[id_a_editar - 1]
    print(f"Editando Registro ID {registro_a_editar['id']}:")
    for chave in registro_a_editar.keys():
        if chave == "id":
            continue
        while True:
            novo_valor = input(f"{chave} ({registro_a_editar[chave]}): ")
            if novo_valor.lower() == "voltar":
                return
            elif novo_valor:
                break
            else:
                print(f"{chave} não pode ser vazio.")
        registro_a_editar[chave] = novo_valor
    salvar_json(data)
    print("Registro editado com sucesso!")

# Função para remover um registro pelo ID


def remover_registro(data):

    # Exibir a lista de IDs disponíveis
    print("IDs disponíveis para remoção:")
    for i, registro in enumerate(data):
        print(f"{i + 1}: ID {registro['id']}")

    while True:
        id_a_remover = input(
            "Digite o ID do registro a ser removido ou 'voltar' para retornar: ").strip()
        if id_a_remover.lower() == "voltar":
            return
        elif not id_a_remover.isdigit():
            print(
                "ID inválido. Digite um número inteiro válido ou 'voltar' para retornar.")
        else:
            id_a_remover = int(id_a_remover)
            if id_a_remover < 1 or id_a_remover > len(data):
                print("ID fora do intervalo válido.")
            else:
                break

    registro_removido = data.pop(id_a_remover - 1)
    # reatribuir IDs a todos os registros após a remoção
    for i, registro in enumerate(data):
        registro["id"] = i + 1
    salvar_json(data)
    print(f"Registro com ID {id_a_remover} removido com sucesso!")

# identifica largura do terminal


def get_terminal_width():
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except OSError:
        return 80  # Valor padrão

# visualizar todos os registros


def visualizar_registros(data):
    if not data:
        print("Nenhum registro disponível.")
        return

    registros_formatados = []
    for registro in data:
        registros_formatados.append(registro)

    print("\nVisualizar todos os registros (versão resumida, seu terminal pode não comportar toda a tabela):")

    terminal_width = get_terminal_width()  # Obtém a largura do terminal
    max_columns = terminal_width // 1  # Ajuste esse valor conforme necessário

    # Limita o número de colunas exibidas
    table = tabulate(registros_formatados, headers="keys",
                     tablefmt="pretty", showindex=False)
    lines = table.splitlines()

    for line in lines:
        print(line[:max_columns])


# Carregamento dos dados do JSON
data = carregar_json()


def exibir_menu_principal():
    menu = [
        ["Opção", "Descrição"],
        ["1", "Adicionar um novo registro"],
        ["2", "Editar um registro existente"],
        ["3", "Remover um registro por ID"],
        ["4", "Visualizar todos os registros"],
        ["5", "Sair"],
        ["voltar", "Retorna ao menu principal"]
    ]

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


# Menu principal
while True:
    exibir_menu_principal()
    escolha = input(
        "Escolha uma opção digitando o número correspondente: ").strip()
    escolha = escolha.lower()

    if escolha == '1':
        adicionar_registro(data)
    elif escolha == '2':
        editar_registro(data)
    elif escolha == '3':
        remover_registro(data)
    elif escolha == '4':
        visualizar_registros(data)
    elif escolha == '5':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma das opções listadas (1/2/3/4/5).")
