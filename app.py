from flask import Flask

from views.admin import admin_blu
from views.index import index_blu
from gevent import pywsgi
app = Flask(__name__)


app.register_blueprint(admin_blu)
app.register_blueprint(index_blu)

if __name__ == '__main__':
    server = pywsgi.WSGIServer((8080),app)
    server.serve_forever()


