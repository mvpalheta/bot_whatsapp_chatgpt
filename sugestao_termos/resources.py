import io
import boto3

# Esta função vai salvar os dados do formulário em um bucket do AWS S3
def save2s3(df, bucket, filename):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id='SUA_CHAVE_AQUI',
        aws_secret_access_key='SUA_CHAVE_AQUI'
    )
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    response = s3_client.put_object(Bucket=bucket, Key=filename, Body=csv_buffer.getvalue())#, ACL ='aws-exec-read'
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
    return status