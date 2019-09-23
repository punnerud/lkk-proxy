from flask import Flask
from requests import get
from flask import request, Response

app = Flask(__name__)
SITE_NAME = 'https://studio.code.org/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  headers = request.headers
  print(headers)
  str(headers).replace('s-code-lkk.dynu.net','studio.code.org')
  print(headers)
  #headers = [(name, value) if (name.lower() != 'location') else (name, value.replace('10.0.0.128:8100', request.host_url)) for (name, value) in request.headers.items() if name.lower() not in excluded_headers]
  #print(headers["Referer"])
  #request.headers.update(headers["Referer"].replace('10.0.0.128:8100','code.org'))
  #print(headers["Referer"])
  a = ''
  prefix =  path.split('.')[-1]
  if prefix in ['html','js',''] or prefix.split('/')[-1] in ['courses','coursea-2019','coursea','elementary']:
   a = get(f'{SITE_NAME}{path}',headers=headers).text
   a = a.replace('code.org','code-lkk.dynu.net')
   a = a.replace('studio.code-lkk.dynu.net','s-code-lkk.dynu.net')
  else :
    a = get(f'{SITE_NAME}{path}',headers=headers).content
  #print(dir(a))
  return a

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8101)
