from flask import Flask, request, Response
import requests
from twilio.twiml.messaging_response import MessagingResponse
import io
import openai

# Configure sua chave de API
openai.api_key = "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"


app = Flask(__name__)

@app.route("/", methods=["POST"])
# Definindo o bot
def bot():
    # Pega a consulta, coloca em caixa baixa
    incoming_msg = ' '.join(request.values.get('Body', '').lower().split())
    consulta = "'" + incoming_msg + "'"

    resp = MessagingResponse()
    msg = resp.message()
    # Definindo a msg de boas vinda que será apresentada caso o usuário envie um "alô"
    if incoming_msg in ['alo', 'ola', 'olá' 'alow', 'oi', 'oii', 'ei', 'eii', 'bom dia', 'boa tarde', 'boa noite', 'hello', 'hi', 'hey', 'start', 'hii']:
        response = """
            *Olá!! Seja bem vindo(a) ao Bot de consulta ao ChatGPT*

Minha finalidade é facilitar suas consultas ao ChatGPT. 
        
Para começar, basta enviar o que deseja consultar e eu trarei a resposta para você.

*Críticas e/ou sugestões: mvpalheta@gmail.com*
        
*Happy Learning!!!*"""

        msg.body(response)
    # Caso o usuário envie algo para consulta, o mesmo será enviada para a API do ChatGPT a fim de receber a resposta
    else:
        # Execute a segunda chamada à API usando a engine
        response1 = openai.Completion.create(
            engine="text-davinci-002",
            prompt=consulta,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.2,
        )

        # Execute a segunda chamada à API usando a engine "text-curie-001"
        response2 = openai.Completion.create(
            engine="text-curie-001",
            prompt=consulta,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.2,
        )     
        #response = responseai["choices"][0]["text"]
        # Combine as respostas das duas engines
        response = response1["choices"][0]["text"] + " " + response2["choices"][0]["text"]
        msg.body(response)
    # Retornando a resposta para o serviço de mensagem (Twilio, neste caso)
    return Response(str(resp), mimetype="application/xml")

if __name__ == '__main__':
   app.run()