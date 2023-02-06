from flask import Flask, request, Response
#import requests
from twilio.twiml.messaging_response import MessagingResponse
#import io
import openai

# Configure sua chave de API
openai.api_key = "SUA_CHAVE_AQUI" #Você pode criar um chave em https://openai.com/api/


app = Flask(__name__)

@app.route("/", methods=["POST"])
# Definindo o bot
def bot():
    # Pega a consulta, coloca em caixa baixa
    incoming_msg = ' '.join(request.values.get('Body', '').lower().split())
    consulta = "'" + incoming_msg + "'"

    resp = MessagingResponse()
    msg = resp.message()
    # Definindo a msg de boas vindas que será apresentada caso o usuário envie um "alô"
    if incoming_msg in ['alo', 'ola', 'olá' 'alow', 'oi', 'oii', 'ei', 'eii', 'bom dia', 'boa tarde', 'boa noite', 'hello', 'hi', 'hey', 'start', 'hii']:
        response = """
            *Olá!! Seja bem vindo(a) ao Bot de consulta ao ChatGPT*

Minha finalidade é facilitar suas consultas ao ChatGPT. 
        
Para começar, basta enviar o que deseja consultar e eu trarei a resposta para você.

*Críticas e/ou sugestões: mvpalheta@gmail.com*
        
*Happy Learning!!!*"""

        msg.body(response)
    # Caso o usuário envie algo para consulta, o mesmo será enviada para a API do ChatGPT a fim de receber a resposta
    # Neste caso, serão utilizadas duas engines diferentes e seus resultados combinados a fim de se obter uma melhor resposta
    else:
        # Execute a primeira chamada à API usando a engine "text-davinci-002"
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
        # Combine as respostas das duas engines
        response = response1["choices"][0]["text"] + " " + response2["choices"][0]["text"]
        msg.body(response)
    # Retornando a resposta para o serviço de mensagem (Twilio, neste caso)
    return Response(str(resp), mimetype="application/xml")

if __name__ == '__main__':
   app.run()