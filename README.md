📝 Descrição
AgendaPy é uma aplicação de linha de comando (CLI) para gerenciamento de contatos pessoais, desenvolvida em Python. Permite organizar seus contatos de forma simples e eficiente, com funcionalidades completas de CRUD e marcação de favoritos.

✨ Funcionalidades
✅ Adicionar contatos com nome, telefone e e-mail

👀 Visualizar lista completa de contatos

✏️ Editar informações de contatos existentes

⭐ Marcar/desmarcar contatos como favoritos

💖 Listar apenas contatos favoritos

🗑️ Remover contatos da agenda

🚪 Sair do programa quando desejar

🛠️ Como Usar
Clone o repositório ou copie o código para um arquivo Python (.py)

Execute o programa com Python:

bash
python agenda_app.py
Siga o menu interativo:

Agenda_APP
1. Adicionar contato
2. Visualizar lista de contatos
3. Editar contato
4. Marcar/Desmarcar contato como favorito
5. Visualizar lista de contatos favoritos
6. Deletar contato
7. Sair
📊 Estrutura dos Contatos
Cada contato é armazenado como um dicionário com:

python
{
    "nome": "Nome do Contato",
    "telefone": "Telefone",
    "email": "email@exemplo.com",
    "favorito": False  # ou True para favoritos
}
🧩 Funções Principais
Função	Descrição
adicionar_contato()	Adiciona novo contato à agenda
ver_contatos()	Lista todos os contatos
editar_contato()	Modifica informações de um contato
alternar_favorito()	Marca/desmarca contato como favorito
ver_favoritos()	Exibe apenas contatos favoritos
deletar_contato()	Remove contato da agenda
💡 Dicas de Uso
Os contatos são armazenados apenas em memória (serão perdidos ao sair do programa)

Para editar, você pode deixar campos em branco para manter o valor atual

Contatos favoritos aparecem com um coração (♥) na listagem

📦 Próximas Melhorias
Salvar contatos em arquivo JSON

Busca de contatos por nome

Exportar contatos para CSV

Interface gráfica (GUI)
