# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route('/commit',methods = ['GET'])
#@limit_content_length(500 * 1024 * 1024)
def commit():
    if request.method == 'GET':
        print('queeryd')
        fo = open("lastnum.txt", "w")
        fo.write(request.args.get('num'))
        fo.close()
        fo = open("dojobs.txt", "w")
        fo.write('0')
        fo.close()
        return jsonify( { 'msg': 'okay' } )

@app.route('/needpoints')
def needpoints():
    fo = open("needpoints.txt", "r")
    num = fo.read()
    fo.close()
    return num

@app.route('/dojobs')
def dojobs():
    fo = open("dojobs.txt", "r")
    num = fo.read()
    fo.close()
    return num

@app.route('/')
def index():
    fo = open("lastnum.txt", "r")
    num = fo.read()
    fo.close()
    return render_template("list.html", num=num)

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 8083)
