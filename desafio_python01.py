# Agenda_APP -> (Salvar, Editar, Deletar e Marcar contato como favorito) 
# Regras da aplicação 
#   Inicia com lista de opções -> receber a opção escolhida pelo usuário -> executar opção escolhida
#   Adicionar um contato com os seguintes dados: Nome, Telefone, Email, Favorito[Marcar]
#   Visualizar lista de contatos cadastrados
#   Editar um contato
#   Marcar/Desmarcar favorito
#   lista de contatos favoritos
#   Apagar um contato


## FUNÇÕES PRINCIPAIS DA AGENDA ##
def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    """
    Adiciona um novo contato à agenda.
    Parâmetros:
        agenda (list): Lista que armazena todos os contatos
        nome_contato (str): Nome do contato a ser adicionado
        telefone_contato (str): Telefone do contato
        email_contato (str): Email do contato
    """
    contato = {
        "nome": nome_contato,
        "telefone": telefone_contato,
        "email": email_contato,
        "favorito": False  # Por padrão, novo contato não é favorito
    }
    agenda.append(contato)  # Adiciona o dicionário de contato à lista agenda
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(agenda):
    """
    Exibe todos os contatos da agenda formatados.
    Se a agenda estiver vazia, informa ao usuário.
    Parâmetros:
        agenda (list): Lista de contatos a ser exibida
    """
    print("\nContatos da sua agenda:")
    if not agenda:  # Verifica se a agenda está vazia
        print("Nenhum contato cadastrado.")
        return
    
    # Enumera os contatos começando do 1 (mais amigável para o usuário)
    for indice, contato in enumerate(agenda, start=1):
        # Usa ♥ para favoritos, espaço vazio para não favoritos
        status = "♥" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        # Formata a saída para exibição organizada
        print(f"{indice}. [{status}] {nome_contato} - Tel: {telefone} - Email: {email}")
    return

def editar_contato(agenda, indice_agenda, novo_nome, novo_telefone, novo_email):
    """
    Edita um contato existente na agenda.
    Parâmetros:
        agenda (list): Lista de contatos
        indice_agenda (str/int): Número do contato a editar (começa em 1)
        novo_nome (str): Novo nome para o contato
        novo_telefone (str): Novo telefone
        novo_email (str): Novo email
    """
    indice_agenda_ajustado = int(indice_agenda) - 1  # Converte para índice interno (começa em 0)
    
    # Verifica se o índice é válido
    if 0 <= indice_agenda_ajustado < len(agenda):
        # Atualiza cada campo do contato
        agenda[indice_agenda_ajustado]["nome"] = novo_nome
        agenda[indice_agenda_ajustado]["telefone"] = novo_telefone
        agenda[indice_agenda_ajustado]["email"] = novo_email
        print(f"Contato {indice_agenda} foi atualizado para: {novo_nome}, {novo_telefone}, {novo_email}")
    else:
        print("Índice de contato inválido")
    return

def alternar_favorito(agenda, indice_agenda):
    """
    Alterna o status de favorito de um contato (marca/desmarca).
    Parâmetros:
        agenda (list): Lista de contatos
        indice_agenda (str/int): Número do contato a modificar
    """
    indice_agenda_ajustado = int(indice_agenda) - 1  # Ajusta o índice
    
    if 0 <= indice_agenda_ajustado < len(agenda):
        # Inverte o status atual de favorito (True <-> False)
        agenda[indice_agenda_ajustado]["favorito"] = not agenda[indice_agenda_ajustado]["favorito"]
        
        # Determina a mensagem a ser exibida
        status = "marcado como favorito" if agenda[indice_agenda_ajustado]["favorito"] else "desmarcado como favorito"
        print(f"Contato {indice_agenda} ({agenda[indice_agenda_ajustado]['nome']}) foi {status}!")
    else:
        print("Índice de contato inválido")
    return

def ver_favoritos(agenda):
    """
    Exibe apenas os contatos marcados como favoritos.
    Parâmetros:
        agenda (list): Lista completa de contatos
    """
    print("\nContatos favoritos:")
    # Filtra apenas os contatos com favorito=True usando list comprehension
    favoritos = [contato for contato in agenda if contato["favorito"]]
    
    if not favoritos:  # Se a lista filtrada estiver vazia
        print("Nenhum contato favorito.")
        return
    
    # Exibe os favoritos formatados
    for indice, contato in enumerate(favoritos, start=1):
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. ♥ {nome_contato} - Tel: {telefone} - Email: {email}")
    return

def deletar_contato(agenda, indice_agenda):
    """
    Remove um contato da agenda.
    Parâmetros:
        agenda (list): Lista de contatos (será modificada)
        indice_agenda (str/int): Número do contato a remover
    """
    indice_agenda_ajustado = int(indice_agenda) - 1  # Ajusta o índice
    
    if 0 <= indice_agenda_ajustado < len(agenda):
        # Remove e retorna o contato deletado (para exibir feedback)
        contato_removido = agenda.pop(indice_agenda_ajustado)
        print(f"Contato {indice_agenda} ({contato_removido['nome']}) foi removido com sucesso!")
    else:
        print("Índice de contato inválido")
    return

## LOOP PRINCIPAL DA APLICAÇÃO ##

agenda = []  # Inicializa a lista vazia para armazenar os contatos

while True:  # Loop infinito até que o usuário escolha sair
    # Menu principal - exibe as opções disponíveis
    print("\nAgenda_APP")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Visualizar lista de contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Selecione a opção desejada: ")

    # Opção 1: Adicionar novo contato
    if escolha == "1":
        nome_contato = input("Informe o nome do seu contato: ")
        telefone_contato = input("Informe o telefone do seu contato: ")
        email_contato = input("Informe o email do seu contato: ")
        adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)
    
    # Opção 2: Visualizar todos os contatos
    elif escolha == "2":
        ver_contatos(agenda)
    
    # Opção 3: Editar contato existente
    elif escolha == "3":
        ver_contatos(agenda)  # Mostra lista para usuário escolher
        if agenda:  # Só permite editar se houver contatos
            indice_contato = input("Digite o número do contato que deseja editar: ")
            
            # Permite manter valores atuais deixando em branco
            novo_nome = input("Novo nome (deixe em branco para manter): ")
            novo_telefone = input("Novo telefone (deixe em branco para manter): ")
            novo_email = input("Novo email (deixe em branco para manter): ")
            
            # Obtém contato atual para valores padrão
            contato_atual = agenda[int(indice_contato)-1]
            
            # Mantém valor atual se usuário não informar novo
            novo_nome = novo_nome if novo_nome else contato_atual["nome"]
            novo_telefone = novo_telefone if novo_telefone else contato_atual["telefone"]
            novo_email = novo_email if novo_email else contato_atual["email"]
            
            editar_contato(agenda, indice_contato, novo_nome, novo_telefone, novo_email)
    
    # Opção 4: Alternar status de favorito
    elif escolha == "4":
        ver_contatos(agenda)
        if agenda:
            indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
            alternar_favorito(agenda, indice_contato)
    
    # Opção 5: Ver apenas favoritos
    elif escolha == "5":
        ver_favoritos(agenda)
    
    # Opção 6: Deletar contato
    elif escolha == "6":
        ver_contatos(agenda)
        if agenda:
            indice_contato = input("Digite o número do contato que deseja deletar: ")
            deletar_contato(agenda, indice_contato)
    
    # Opção 7: Sair do programa
    elif escolha == "7":
        print("Saindo da Agenda... Até logo!")
        break  # Encerra o loop while
    
    # Tratamento para opção inválida
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 7.")