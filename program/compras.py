import json
import time
import os

from menu.menu import print_menu_principal, print_gerenciar_compras

compras = {}


def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade


def remover_item(compras, item):
    if item in compras:
        del compras[item]
        print('Item removido com sucesso!')
    else:
        print('O item não se encontra nessa lista!')


def visualizar_compras(compras):
    print('_' * 50)
    for item, value in compras.items():
        print(f'{item.capitalize()}: {value}')
    print('_' * 50)
    print('Pressione Enter para continuar.')


def salvar_compras(compras, nome_arquivo):
    with open(f'listas_de_compras/{nome_arquivo}.json', 'w', encoding='utf-8') as arquivo:
        json.dump(compras, arquivo, ensure_ascii=False, indent=4)


def carregar_compras(nome_arquivo):
    try:
        with open(f'listas_de_compras/{nome_arquivo}.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f'{nome_arquivo} - Arquivo não encontrado!')

    return {}


def arquivo_existente(nome_arquivo) -> bool:
    """Checa se um arquivo é existente e retorna true se for e false caso não seja"""

    if os.path.exists(os.path.join('listas_de_compras', f'{nome_arquivo}.json')):
        return True

    return False


def listar_arquivos_existentes():
    """Lista todos os arquivos existentes na pasta listas_de_compras"""
    try:
        arquivos = [f for f in os.listdir('listas_de_compras') if os.path.isfile(os.path.join('listas_de_compras', f))]

        if arquivos:
            for arquivo in arquivos:
                print(arquivo.replace('.json', ''))
        else:
            print(f'Nenhuma lista de compras encontrada.')
    except:
        print('Não foi possível listar as listas de compras')

def criar_lista_de_compras(nome_arquivo):
    """Cria um novo arquivo na pasta listas_de_compras"""

    diretorio = 'listas_de_compras'

    os.makedirs(diretorio, exist_ok=True)

    try:
        with open(f'{diretorio}/{nome_arquivo}.json', 'x') as arquivo:
            json.dump({},arquivo)
        print("Arquivo criado com sucesso!")
    except FileExistsError:
        print("Erro: O arquivo já existe.")


def excluir_lista_de_compras(nome_arquivo):
    """Recebe o nome do arquivo como parãmetro e busca este arquivo no diretório lista de compras para excluí-lo"""
    try:
        caminho_arquivo = f'listas_de_compras/{nome_arquivo}.json'
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            print('Arquivo removido com sucesso!')
        else:
            print('Não foi possível excluir o arquivo.')

    except:
        print('Não foi possível excluir o arquivo.')


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu_principal()
        op = input('Digite a opção desejada: \n')

        match op:
            case '1':
                nome_arquivo = input('Digite o nome da lista de compras:')
                criar_lista_de_compras(nome_arquivo)

            case '2':
                nome_arquivo = input('Digite o nome da lista de compras:')

                if not arquivo_existente(nome_arquivo):
                    print(f'{nome_arquivo} - Lista inexistente')
                else:
                    compras = carregar_compras(nome_arquivo)

                    while True:
                        print_gerenciar_compras()
                        match input('Escolha uma opção: \n'):
                            case '1':
                                item = input('Digite o nome do item: \n')
                                quantidade = input('Digite a quantidade do item: \n')
                                adicionar_item(compras, item, quantidade)
                            case '2':
                                item = input('Digite o nome do item a ser removido: \n')
                                remover_item(compras, item)
                            case '3':
                                visualizar_compras(compras)
                            case '4':
                                salvar_compras(compras, nome_arquivo)
                                break
                            case '5':
                                break
                            case _:
                                print('Opção inválida.')
                                time.sleep(1)
            case '3':
                listar_arquivos_existentes()
            case '4':
                nome_arquivo = input('Digite o nome da lista de compras que deseja excluir:\n')
                excluir_lista_de_compras(nome_arquivo)
            case '5':
                print('Fechando o programa...')
                break
            case _:
                print('Opção inválida.')
                time.sleep(1)

