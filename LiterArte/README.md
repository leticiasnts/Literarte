# LiterArte

O LiterArte é uma plataforma web de gestão de leitura desenvolvida com o framework Django. O objetivo da aplicação é permitir que usuários cataloguem livros, organizem suas listas de leitura pessoais e acompanhem o progresso de suas atividades literárias.

O projeto foca na aplicação de conceitos fundamentais de desenvolvimento web, incluindo arquitetura MTV (Model-Template-View), operações CRUD, autenticação de usuários e design responsivo.

## Funcionalidades Principais

* **Autenticação de Usuários:** Sistema de cadastro, login e logout seguros.
* **Catálogo de Livros:** Visualização de livros cadastrados com detalhes completos (sinopse, autor, capa, dados técnicos).
* **Gestão de Lista de Leitura:** Usuários podem adicionar livros à sua lista pessoal.
* **Status de Leitura:** Atualização dinâmica do status de cada livro (Quero Ler, Lendo, Lido).
* **Remoção de Itens:** Possibilidade de remover livros da lista pessoal.
* **Perfil do Usuário:** Edição de dados cadastrais e preferências literárias.
* **Interface Responsiva:** Layout adaptável para dispositivos móveis (smartphones e tablets) e desktops.

## Tecnologias Utilizadas

### Backend
* **Python 3.11+**: Linguagem principal.
* **Django 5**: Framework web de alto nível.

### Frontend
* **HTML5 & CSS3**: Estrutura semântica e estilização customizada.
* **JavaScript**: Interatividade no menu responsivo e formulários dinâmicos.
* **Django Template Language (DTL)**: Renderização dinâmica de páginas.

### Banco de Dados
* **SQLite**: Utilizado em ambiente de desenvolvimento.

### Infraestrutura e Deploy
* **Git**: Controle de versão.

## Pré-requisitos

Para executar este projeto localmente, você precisará ter instalado em sua máquina:
* Python (versão 3.10 ou superior)
* Git

## Como Executar o Projeto Localmente
  1. Baixe o código na sua máquina. Abra o terminal e faça:
            git clone https://github.com/LaysaCibele/LiterArte.git
            cd literarte

  2. Crie o Ambiente Virtual (VENV):
             python -m venv venv
     
      2.1 Ative o venv:
               venv\Scripts\activate
     2.1.1: Caso esteja no Linux/Mac
                 source venv/bin/activate

   4. Instale as dependências:
                  pip install -r requirements.txt
            
   5. Configure o Banco de Dados:
                    python manage.py runserver

   6. Crie um superusuário para acessar a área de administrador (adicionar livros, usuários, autores, gêneros):
                     python manage.py createsuperuser
      
      - ps.: ao criar um superusuário, quando você digitar a senha, por padrão do django, no terminal, não serão exibidos pontos (.....)  nem (******), o campo fica invisível.


   8. Rode o servidor:
                  python manage.py runserver
                        - clique no localhost que irá aparecer no seu terminal.

      6.1 Ao rodar o projeto, na barra de endereço, se você quiser acessar o painel de administrador, faça:
                 localhost:8000/admin
                   - você será direcionado para a página de admin do django e poderá acessá-la com o usuário e senha que você criou na 5º etapa (superusuário)




Para conseguir testar as funcionalidades do projeto, é necessário que você entre no menu de admin e adicione ao menos dois livros através do menu.
Essa versão atual é o MVP do LiterArte, mas pretendo trazer mais atualizações e  corrigir alguns erros identificados.


Laysa Cibele - Estudante do 3° período de Ciência da Computação [GitHub: https://github.com/LaysaCibele]

