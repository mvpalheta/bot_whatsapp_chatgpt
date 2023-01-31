from flask import Flask, request, Response
import requests
from twilio.twiml.messaging_response import MessagingResponse
import io
import boto3
# Definindo um mapeamento para substituir acentos
normalMap = {'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
             'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'ª': 'A',
             'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
             'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
             'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
             'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
             'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
             'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'º': 'O',
             'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U',
             'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
             'Ñ': 'N', 'ñ': 'n',
             'Ç': 'C', 'ç': 'c',
             '§': 'S',  '³': '3', '²': '2', '¹': '1'}
normalize = str.maketrans(normalMap)

#Definindo um client para conectar ao S3
s3_client = boto3.client(
        's3',
        aws_access_key_id='SUA_CHAVE_AQUI',
        aws_secret_access_key='SUA_CHAVE_AQUI'
        )

app = Flask(__name__)

@app.route("/", methods=["POST"])
# Definindo o bot
def bot():
    # Pega o termo, coloca em caixa baixa e retira os acentos
    incoming_msg = ' '.join(request.values.get('Body', '').lower().translate(normalize).split())
    termo = "'" + incoming_msg + "'"
    # Definindo a query SQL que irá realizar a busca do termo na tabela de dados
    expression = f"SELECT definicao FROM s3object s where s.termo_pt = {termo} or s.termo_ingles = {termo}"
    resp = MessagingResponse()
    msg = resp.message()
    # Definindo a msg de boas vinda que será apresentada caso o usuário envie um "alô"
    if incoming_msg in ['alo', 'ola', 'alow', 'oi', 'oii', 'ei', 'eii', 'bom dia', 'boa tarde', 'boa noite', 'hello','hi','hey','start','hii']:
        response = """
            *Olá!! Seja bem vindo(a) ao Bot Termos DS*

Minha finalidade é trazer para você os conceitos de termos referentes à área de ciência de dados. 
        
Para começar, basta enviar o termo que deseja consultar e eu trarei a definição do mesmo para você.

*Críticas e/ou sugestões: mvpalheta@gmail.com*
        
*Happy Learning!!!*"""
        msg.body(response)
    # Caso o usuário envie um termo para consulta, será realizada a busca do mesmo na tabela de dados, que está em formato parquet
    # de acordo com a query definida acima
    else:
        resp_s3 = s3_client.select_object_content(
            Bucket='botwhatsapp',
            Key='base_whatsbot.parquet',
            ExpressionType='SQL',
            Expression= expression,
            InputSerialization = {'Parquet': {}, 'CompressionType': 'NONE'},
            OutputSerialization = {'CSV': {}}
            )
        for event in resp_s3['Payload']:
            if 'Records' in event:
                response = event['Records']['Payload'].decode('utf-8')
                break
            # Caso o termo não seja encontrado na tabela de dados será retornada a msg abaixo
            else:
                response = """Que pena :-( Infelizmente não foi possível retornar uma definição para o termo procurado. Por favor, verifique se ele foi digitado corretamente.
                
Felizmente, se você quiser sugerir um termo para adicionar futuramente à minha base de dados, pode fazer isso acessando aqui: www.termosds.vagasds.com"""
                break
        msg.body(response)
    # Retornando a resposta para o serviço de mensagem (Twilio, neste caso)
    return Response(str(resp), mimetype="application/xml")

if __name__ == '__main__':
   app.run()