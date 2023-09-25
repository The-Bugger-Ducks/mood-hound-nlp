![mood hound header nlp](https://github.com/The-Bugger-Ducks/mood-hound-nlp/assets/79321198/dbc87ae2-7b71-4aa8-8a63-f4075d5e036d)

Este projeto permite a leitura, processamento e análise dos dados disponibilizados [aqui](https://github.com/americanas-tech/b2w-reviews01), aplicando classificação de temas e análise de sentimento em cima deles. Tem por objetivo auxiliar o desenvolvimento do projeto "MoodHound" (mais informações vide [este link](https://github.com/The-Bugger-Ducks/mood-hound-documentation)).

> Aplicação desenvolvida por alunos do 6º semestre do tecnólogo em Desenvolvimento de Software Multiplataforma, na FATEC Profº Jessen Vidal - São José dos Campos, SP :rocket:

### :hammer_and_wrench: Tecnologias

As seguintes tecnologias e ferramentas foram utilizadas neste projeto: `Python, NLTK, Spacy`

### :gear: Como utilizar

Para aplicar o processamento nos dados manualmente (rodando localmente) é preciso seguir o passo a passo abaixo com o Python3 já instalado em sua máquina:

- Tutorial para rodar o projeto

```bash
# Baixe este repositório ou clone pelo Git usando o comando:
$ git clone https://github.com/The-Bugger-Ducks/mood-hound-nlp.git

# Acesse a pasta do projeto
$ cd mood-hound-nlp

# Crie um ambiente virtual do Python
$ python -m venv nlp_api

# Ative o ambiente virtual
$ . nlp_api/Scripts/activate

# Instale as dependências necessárias
$ pip install -r requirements.txt

# Inicie o projeto
$ python main.py
```

O processamento inciará e logs aparecerão no terminal conforme cada etapa for concluída, permitindo seu acompanhamento.

![Exemplo de logs](https://github.com/The-Bugger-Ducks/mood-hound-nlp/assets/69374340/f7d3e645-2f2e-4f2d-9442-d7a01704af56)

### Estrutura das pastas

| Pasta                             | Definição                                                |
| --------------------------------- | -------------------------------------------------------- |
| :open_file_folder: pipeline/      | Arquivos com as funções de cada passo do processo de PLN |
| :open_file_folder: utils/         | Funções utilitárias compartilhadas                       |
| :page_facing_up: main.py          | Arquivo principal de inicialização do projeto            |
| :page_facing_up: requirements.txt | Arquivo usado para gerenciar as dependencias do projeto  |
