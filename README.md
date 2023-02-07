# Bot de whatsapp para consultas ao Chatgpt

# Overview

Este repositório tem como finalidade compartilhar os códigos utilizados na construção de um chatbot de whatsapp onde é possível realizar consultas ao ChatGPT da OpenAI através da API denominada GPT-3. A API GPT-3 é uma das mais avançadas APIs de modelos de linguagem disponíveis no mercado. Treinada com milhões de exemplos de textos  ela é capaz de produzir texto natural e convincente em uma ampla gama de tarefas, incluindo geração de texto, tradução, respostas a perguntas, e muito mais. Além disso, a API é fácil de usar e oferece suporte a várias linguagens de programação, incluindo Python, Java, e JavaScript.

Assim, a aplicação apresentada neste repositório tem como objetivo testar a integração do Python com a API GPT-3 da OpenAI. Basicamente, é um bot de whatsapp a partir do qual se pode interagir com o ChatGPT através de sua API. Para as respostas retornadas pelo o bot estão sendo utilizadas duas das engines (text-davinci-002 e text-curie-001) desenvolvidas pela OpenAI  especificamente para gerar textos em linguagem natural. Importante ressaltar que as respostas para a mesma pergunta podem ser diferentes quando feitas através da API e do navegador por vários motivos, incluindo:

- Diferentes fontes de dados: A API pode ter acesso a fontes de dados diferentes do que o navegador, o que pode resultar em respostas diferentes.

- Configurações de privacidade e personalização: As configurações de privacidade e personalização do navegador podem afetar os resultados da pesquisa.

- Algoritmos de classificação diferentes: A API e o navegador podem usar algoritmos de classificação diferentes para organizar e priorizar os resultados da pesquisa.

- Erros técnicos: Problemas técnicos, como a instabilidade da rede ou erros no servidor, podem afetar os resultados da pesquisa.

Em resumo, a combinação desses fatores pode resultar em respostas diferentes para a mesma pergunta feita através da API e do navegador.

O conceito da aplicação é simples, mas acredito que pode ajudar principalmente quem está iniciando na área.Ela ainda está na versão beta e para acessá-la basta adicionar [este número](https://wa.me/+14155238886) ao whatsapp, enviar o código **"join passage-grew"** e depois começar a interagir com o chatbot.

Todo o projeto foi desenvolvido em Python e atualmente o chatbot roda na plataforma [Deta](https://www.deta.sh/). Também estou utilizando o serviço da Twilio para realizar a entrega das mensagens.

[Este artigo](https://programdiary.com/post/create-a-whatsapp-bot) apresenta um exemplo de como criar um chatbot em Python e testá-lo utilizando o serviço da Twilio. [Este](https://www.gormanalysis.com/blog/building-and-deploying-rock-paper-scissors-with-python-fastapi-and-deta/) e [este](https://nolowiz.com/deta-free-heroku-alternative-step-by-step-guide-to-deploy-a-python-app/) artigos mostram como fazer o deploy do bot na plataforma Deta.

# Organização do repositório

**whatsbot_chatgpt:** Esta pasta contém o código do bot bem como outros recursos necessário para realizar o deploy da aplicação na Deta.

# Fluxo do chatbot

<p align="center"><img alt="fluxo_chatbot" width="90%" src="https://github.com/mvpalheta/bot_whatsapp_chatgpt/blob/main/fluxo1_chatbot_chatgpt.png"></p>

<br>

Espero que tanto a aplicação quanto os códigos disponibilizados aqui sejam úteis para alguém. Estou à disposição para esclarecer dúvidas, receber críticas construtivas e/ou sugestões através do e-mail mvpalheta@gmail.com. **Abraços**.

 
