import os

#Criar uma lista fora de todas as funções, de um modo glopal para que todos tenham acesso
restaurantes = [{'nome':'Meimei','categoria':'Japonesa','ativo':False},
                {'nome': 'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome': 'Mc', 'categoria': 'Americana', 'ativo':False}]

def exibir_nome_programa():
    print("""
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulos('Finalizando o app')
    
def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao meu principal ')
    main()

def  opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    exibir_subtitulos('Cadastro novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso! \n')
   
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulos('Listando os restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:    #para cada restaurante na lista restaurantes:   mostre o nome do restaurante
        nome_resturantes = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'-{nome_resturantes.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:  #referindo ao restaurante como o Looping, não o todo da lista
            restaurante_encontrado = True
            #inverter o estado do restaurante:
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

     #caso o restaurante não seja encontrado:
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')



    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)
    
        if opcao_escolhida == 1:
            cadastrar_restaurante()    #print('Cadastrar restaurantes')

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
            
        
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

