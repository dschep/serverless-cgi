import json
import os
from shutil import copyfile
from subprocess import check_output
from urllib.parse import urlencode


def cgi(event, context):
    env = os.environ.copy()
    env.update(**{f'HTTP_{name.upper().replace("-", "_")}': value
                  for name, value in event.get('headers', {}).items()})

    script = event['pathParameters']['path']

    env.update(
        SERVER_SOFTWARE='serverless-cgi/0.1',
        SERVER_NAME=event['headers'].get('Host', ''),
        GATEWAY_INTERFACE='CGI/1.1',
        SERVER_PROTOCOL='HTTP/1.1',
        SERVER_PORT=event['headers'].get('X-Forwarded-Port', '' ),
        REQUEST_METHOD=event['httpMethod'],
        PATH_INFO='',  # TODO
        PATH_TRANSLATED='',  # TODO
        SCRIPT_NAME='',  # TODO
        QUERY_STRING=urlencode(event['queryStringParameters'] or {}),
        REMOTE_ADDR=event['requestContext']['identity']['sourceIp'],
        CONTENT_TYPE=event['headers'].get('Content-Type'),
        CONTENT_LENGTH=(len(event['body'])
                        if event.get('body') is not None
                        else 0),
    )

    copyfile(f'./cgi-bin/{script}', f'/tmp/{script}')
    os.chmod(f'/tmp/{script}', 0o755)
    headers, body = check_output([f'/tmp/{script}']).decode().split('\n\n', 1)

    response = {
        "statusCode": 200,
        "body": body,
    }

    return response
