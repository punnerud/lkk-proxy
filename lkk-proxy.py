from flask import Flask, Response
from requests import get
import json

app = Flask(__name__)
SITE_NAME = 'https://code.org/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  a = get(f'{SITE_NAME}{path}')
  b = a.text.replace('code.org','10.0.0.128:8101')
  j = json.loads(json.dumps(a.headers.__dict__['_store']))
  #print(j)
  return Response(a.content, a.status_code, j)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8101)
