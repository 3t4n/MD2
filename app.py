from flask import Flask,request
from core.Mundo import *

app = Flask(__name__)
app.config.from_object('config')

@app.route('/generarMundo', methods = ['GET', 'POST'])
def crearMundo():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        test = Mundo(2,2,["black","green"],["black","green"],2,8,70)
        test.generarEnunciados(4,5)
        return test.obtenerMundo()

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

@app.route('/static/js/<path:path>')
def sendjs(path):
    return send_from_directory('js', path)

@app.route('/static/imgs/<path:path>')
def sendimgs(path):
    return send_from_directory('imgs', path)

@app.route('/static/css/<path:path>')
def sendcss(path):
    return send_from_directory('css', path)

if __name__ == '__main__':
    app.run()
