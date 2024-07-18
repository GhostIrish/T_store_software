# Projeto T-Store

## Introdução

Este é o projeto T-Store, uma aplicação para gerenciamento de produtos utilizando uma interface gráfica construída com CustomTkinter e um banco de dados MySQL em contêineres Docker.

## Pré-requisitos

Antes de iniciar, certifique-se de que a máquina possui os seguintes softwares instalados:

- **Git**: [Instalar Git](https://git-scm.com/)
- **Docker**: [Instalar Docker](https://www.docker.com/products/docker-desktop)

## Passos para Configuração e Execução

Siga os passos abaixo para configurar e executar a aplicação:

1. **Baixar o `setup.bat`**:

   Baixe o arquivo `setup.bat` e salve-o em um diretório de sua escolha, por exemplo, `C:\project_setup`.

2. **Executar o `setup.bat`**:

   - Abra um prompt de comando (CMD) no Windows.
   - Navegue até o diretório onde o arquivo `setup.bat` está localizado:
     ```cmd
     cd C:\project_setup
     ```
   - Execute o script digitando `setup.bat` e pressionando Enter:
     ```cmd
     setup.bat
     ```

## O que o Script Faz

Quando o `setup.bat` é executado, ele realiza os seguintes passos:

1. **Clona o Repositório**:
   - O script clona o repositório do GitHub para o diretório atual.

2. **Navega para o Diretório do Projeto**:
   - O script muda o diretório para a pasta do projeto clonado.

3. **Inicia Docker Compose**:
   - O script inicia os serviços definidos no arquivo `docker-compose.yml`.


## Verificação

Após a execução do script, verifique o seguinte:

1. **Containers em Execução**:
   - Abra o Docker Desktop e verifique se os containers do MySQL e da aplicação estão em execução.

2. **Acesso ao Banco de Dados**:
   - Certifique-se de que o banco de dados MySQL foi iniciado corretamente e que a aplicação está conectada a ele.

3. **Execução da Aplicação**:
   - Navegue até o diretório do projeto clonado e execute o comando para iniciar a aplicação. Dependendo de como a aplicação é iniciada, execute:
     ```cmd
     python main.py
     ```

## Suporte

Se você encontrar problemas ou tiver dúvidas, sinta-se à vontade para abrir uma issue no repositório do GitHub ou entrar em contato com o suporte.

---

Com esse guia, os usuários poderão configurar e executar a aplicação com facilidade. Certifique-se de incluir esse arquivo README.md no diretório raiz do seu projeto.


