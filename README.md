# Automatização de relatório de vendas

Este projeto foi feito durante o bootcamp **Intensivão de Python** da 
**Hashtag Treinamentos**.

# Objetivos

O objetivo do projeto é somente para aprendizado.

Durante a aula na qual este projeto foi desenvolvido foi proposto que fosse 
feito um sistema que ajudade com a automatização de relatórios de venda junto
com o envio de email com os calculos feitos durante a execução do código.

# Ferramentas

Foi usado PIP para a instalação das bibliotecas. A execução do código foi feita
por meio do interpretador do Python 2.7.18 - escolha feita por causa da versão
do PIP, que era ultilizado em conjunto com este interpretador.

# Set-up

Dentro do código possuem certas variáveis globais que são importantes para a sua
execução, sendo elas: `COMPANY_SERVER_URL`, `FILE_PATH`, `MAIL_SERVICE_URL`, 
`EMAIL_TO`.

Variável | Obrigatório | Descrição
-------- | ----------- | ----------
`COMPANY_SERVER_URL` | :heavy_check_mark: | Define o link do servidor (Google Drive recomendado)
`FILE_PATH` | :heavy_check_mark: | Caminho do arquivo que foi feito o download
`MAIL_SERVICE_URL` | :heavy_check_mark: | Link do provedor de email que será ultilizado (Gmail, Outlook, etc)
`EMAIL_TO` | :heavy_check_mark: | Endereço de email do destinatário do email
