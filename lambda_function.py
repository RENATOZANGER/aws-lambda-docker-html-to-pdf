import boto3
import os
import pdfkit
from jinja2 import Environment, FileSystemLoader

access_key='xxx'
secret_key='xxx'

if 'LOCAL_EXECUTION' in os.environ:
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
else:
    s3 = boto3.client('s3')

def handler(event, context):
    dados = {
        'nome': event['nome'],
        'idade': event['idade']
    }
    template = Environment(loader=FileSystemLoader('.')).get_template('form.html').render(dados)
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdf = pdfkit.from_string(template, configuration=config)

    s3.put_object(Bucket='teste1122', Key='formulario.pdf', Body=pdf)
    
    return {
        'statusCode': 200,
        'body': 'PDF generated successfully'
    }
