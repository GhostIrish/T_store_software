# Projeto T-Store

## Introdução

Este é o projeto T-Store, uma aplicação para gerenciamento de produtos utilizando uma interface gráfica construída com CustomTkinter e um banco de dados MySQL em contêineres Docker.

## Pré-requisitos

Antes de iniciar, certifique-se de que a máquina possui os seguintes softwares instalados:

- **Python**
- **Git**: [Instalar Git](https://git-scm.com/)
- **Docker**: [Instalar Docker](https://www.docker.com/products/docker-desktop)

Caso não possua, na pasta de downloads se encontram todos os instaladores necessários.

## Passos para Configuração e Execução

Siga os passos abaixo para configurar e executar a aplicação:

1. **Instalar as dependendências**:
   - Instale o Docker,o Git e o Python caso não possua em sua máquina.

2. **Executar o `setup.bat`**:

   - Execute o script clicando no `setup.bat`:
     ```cmd
     setup.bat
     ```

## O que o Script Faz

Quando o `setup.bat` é executado, ele realiza os seguintes passos:

1. **Constrói e inicia o conteiner da base de dados MySQL**:
   - O script faz todo o processo de preparar, configurar e iniciar a base de dados no seu docker desktop.

2. **Instala os requirements necessários para o projeto**:
   - O script executa o comando para instalar o requirements.txt.

3. **Cria e molda o banco para os padrões do software**:
   - O script executa o arquivo que configura o padrão da base de dados MySQL.


## Verificação

Após a execução do script, verifique o seguinte:

1. **Containers em Execução**:
   - Abra o Docker Desktop e verifique se os containers do MySQL e da aplicação estão em execução.

2. **Acesso ao Banco de Dados**:
   - Certifique-se de que o banco de dados MySQL foi iniciado corretamente e que a aplicação está conectada a ele.

3. **Execução da Aplicação**:
   - Inicie a API localizada na pasta *dist* clicando no executável.

4. **Inicie o Software**:
   - Após esses processos você pode finalmente executar o executável do software e testar o programa!

## Suporte

Se você encontrar problemas ou tiver dúvidas, sinta-se à vontade para abrir uma issue no repositório do GitHub ou entrar em contato com o suporte.



