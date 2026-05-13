gastos = []
categorias_disponiveis = ['Alimentação', 'Transporte', 'Saúde', 'Lazer', 'Educação', 'Outros']


# ================= FUNÇÕES =================

def mostrar_menu():
    print('=' * 40)
    print('          Relatório de gastos        ')
    print('=' * 40)
    print('[1] Adicionar gastos')
    print('[2] Relatório Geral')
    print('[3] Listar por categoria')
    print('[4] Sair')
    print('[5] Excluir gastos')


def adicionar_gasto():
    produto = input('Digite o nome do produto: ').strip()

    while not produto:
        print('Nome não pode ser em branco')
        produto = input('Digite o nome do produto: ').strip()

    while True:
        try:
            valor_do_produto = float(input('Digite o preço do seu produto: '))
            if valor_do_produto <= 0:
                print('Valor inválido')
            else:
                break
        except ValueError:
            print('Digite apenas números')

    print('\nCategorias disponíveis:')
    for i, cat in enumerate(categorias_disponiveis, 1):
        print(f' [{i}] {cat}')

    escolha_a_categoria = input('Escolha a categoria (numero): ')

    if escolha_a_categoria.isdigit() and 1 <= int(escolha_a_categoria) <= len(categorias_disponiveis):
        categoria = categorias_disponiveis[int(escolha_a_categoria) - 1]
    else:
        categoria = 'Outros'
        print('Categoria inválida, definida como "Outros".')

    gastos.append({
        'produto': produto,
        'valor': valor_do_produto,
        'categoria': categoria
    })

    print('Gasto adicionado!')


def relatorio_geral():
    print('=' * 30)
    print('LISTA DE GASTOS')
    print('=' * 30)

    if not gastos:
        print('Nenhum gasto cadastrado.')
    else:
        for i, gasto in enumerate(gastos, 1):
            print(f'{i}. {gasto["produto"]} [{gasto["categoria"]}] - R$ {gasto["valor"]:.2f}')

        print(f'\nTotal de gastos cadastrados: {len(gastos)}')

        total = sum(gasto['valor'] for gasto in gastos)
        media = total / len(gastos)
        maior = max(gastos, key=lambda g: g['valor'])

        print(f'Total gasto: R$ {total:.2f}')
        print(f'Média dos gastos: R$ {media:.2f}')
        print(f'Maior gasto: {maior["produto"]} - R$ {maior["valor"]:.2f}')


def listar_por_categoria():
    if not gastos:
        print('Nenhum gasto cadastrado.')
    else:
        for categoria in categorias_disponiveis:
            gastos_da_categoria = [
                g for g in gastos if g['categoria'] == categoria
            ]

            if gastos_da_categoria:
                total_categoria = sum(g['valor'] for g in gastos_da_categoria)

                print(f'\n{categoria} — Total: R$ {total_categoria:.2f}')
                print('-' * 35)

                for g in gastos_da_categoria:
                    print(f'  {g["produto"]:<22} R$ {g["valor"]:.2f}')


def excluir_gasto():
    if not gastos:
        print('Nenhum gasto cadastrado.')
    else:
        print('=' * 30)
        print('EXCLUIR GASTO')
        print('=' * 30)

        for i, gasto in enumerate(gastos, 1):
            print(f'{i}. {gasto["produto"]} [{gasto["categoria"]}] - R$ {gasto["valor"]:.2f}')

        escolha = input('Escolha o que deseja excluir: ')

        if escolha.isdigit():
            indice = int(escolha) - 1

            if 0 <= indice < len(gastos):
                removido = gastos[indice]
                del gastos[indice]

                print(f'Gasto "{removido["produto"]}" removido com sucesso.')
            else:
                print('Número inválido.')
        else:
            print('Digite apenas números.')


def sair_do_sistema():
    while True:
        sair = input('Deseja sair? S/N: ').strip().upper()

        if sair == 'S':
            print('Encerrando o sistema')
            return False

        elif sair == 'N':
            print('Voltando ao menu')
            return True

        else:
            print('Valor não encontrado. Digite S ou N')


# ================= PROGRAMA PRINCIPAL =================

executando = True

while executando:
    mostrar_menu()

    servico = input('Escolha o serviço que voce quer: ')

    if servico == '1':
        adicionar_gasto()

    elif servico == '2':
        relatorio_geral()

    elif servico == '3':
        listar_por_categoria()

    elif servico == '4':
        executando = sair_do_sistema()

    elif servico == '5':
        excluir_gasto()

    else:
        print('Serviço não encontrado.')