from flask import Flask,request,render_template, send_from_directory, Response,jsonify
from core.Mundo import *

app = Flask(__name__)
app.config.from_object('config')
COLORESF =["green","blue","gray","yellow","pink"]
COLORESC = ["white","chocolate","orange"]

@app.route('/generarMundo', methods = ['GET', 'POST'])
def crearMundo():
    if request.method == 'POST':
        data = request.form
        print(data)
        test = Mundo(int(data["x"]),int(data["y"]),COLORESC,COLORESF,2,int(data["lados"]),int(data["porcentaje"]))
        test.generarEnunciados(int(data["enunciados"]),int(data["subenunciados"]))
        return Response(test.obtenerMundo(),mimetype='application/json')

    if request.method == 'GET':
        test = Mundo(2,2,["black","green"],["black","green"],2,8,70)
        test.generarEnunciados(4,5)
        return jsonify(test.obtenerMundo())

@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

@app.route('/static/js/<path:path>')
def sendjs(path):
    return send_from_directory('static/js', path)

@app.route('/static/imgs/<path:path>')
def sendimgs(path):
    return send_from_directory('static/imgs', path)

@app.route('/static/css/<path:path>')
def sendcss(path):
    return send_from_directory('static/css', path)

@app.route('/static/templates/<path:path>')
def sendtemplate(path):
    return send_from_directory('static/templates', path)

if __name__ == '__main__':
    app.run()
