# soccer_sorter
#:rocket: Projeto Soccer Sorter 

##Objetivo
Levantar uma aplicação para Sorteador de Times de Futebol, aplicação web simples com back/front/integrados via api. 

___

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
Docker, Docker Compose, Git e uma IDE.

Checando a instalação do docker
```bash
docker-compose --version 
```

```bash
docker --version 
```
Caso não retorne uma versão é necessário instalar essas dependências, antes continuar e rodar o projeto.



___

###Executando o projeto com o Makefile

As etapas de build, execução, e alguns atalhos foram incorparados num script Makefile.
Basta que tenha os pré-requisitos instalados.

Pra executar os comando, na raiz do projeto em linha de comando:

- Cria containers e o arquivo .env.dev 
```bash
make build
```
___
- Cria migrations
```bash
make makemigrations  
``````
___

- Executa migrations
```bash
make migrate
```
___
- Criar um usuario
```bash
make createsuperuser
```
___
- Inicializa container, e executa serviço Django
```bash
make start
```
___
- Encerra execução dos containers BD e Django
```bash
make stop
```
___
- Executa todos os linters e flake8.
```bash
make lint
```
___
- Executa apenas um teste de coverage e pytest.
```bash
make test
```
___
- Pre commit. Executa os linters e executa um teste de coverage e pytest.
```bash
make pre
```
___

### Breve comentário sobre as variáveis de ambiente
Geralmente utilizamos o arquivo **.env em produção** e o arquivo **.env.dev para ambiente de desenvolvimento local**, isso para isolar senhas e constantes utilizadas em desenvolvimento e em produção.

Uma das variáveis utilizadas neste projeto é a **SECRET_KEY** do Django. Por padrão ela vem criada automaticamente no arquivo settings.py.
A chave secreta (secret key) do Django é uma parte fundamental da segurança da sua aplicação. Para se acostumar com boas práticas redefina a SECRET_KEY por algo mais seguro, editando o arquivo .env.dev do passo anterior. Em desenvolvimento esse passo pode ser descartado, mas é bom se familiarizar com esse conceito.

[Link parar Post explicando como criar uma SECRET_KEY](https://ohmycode.com.br/como-gerar-uma-secret_key-do-django/)

Também é uma boa prática utilizar uma boa senha para o Postgres, que está na variável DB_PASSWD do arquivo .env.dev example.

## Build do container
O build é o processo de criar os contêiners Docker conforme definido no arquivo docker-compose.yaml.
É preciso fazê-lo **somente na primeira execução do projeto, quando modificamos alguma variável de ambiente ou para recriar os contêiners.**

Nesse projeto você não precisa instalar Postgres em seu computador, nem mesmo ter um ambiente virtual local.
Tudo estará "conteinerizado" e com um grau de isolamento do seu computador host.
Uma das principais vantages de ter contêineres é, evitar o "mas funciona aqui no meu computador", permitindo que desenvolvedores de diferentes times e até em produção tenhamos um ambiente homogêneo.


