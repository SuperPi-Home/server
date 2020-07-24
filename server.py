# -*- coding: utf-8 -*-
from functools import wraps
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

@app.route('/makejob',methods = ['GET'])
#@limit_content_length(500 * 1024 * 1024)
def makejob():
    if request.method == 'GET':
        print('queeryd')
        if str(request.args.get('pwd')) == "PASSWORDHERE":
            fo = open("needpoints.txt", "w")
            fo.write(request.args.get('num'))
            fo.close()
            fo = open("dojobs.txt", "w")
            fo.write('1')
            fo.close()
    
    fo = open("lastnum.txt", "r")
    num = fo.read()
    fo.close()
    fo = open("needpoints.txt", "r")
    num1 = fo.read()
    fo.close()
    fo = open("dojobs.txt", "r")
    num2 = int(fo.read())
    fo.close()
    if(num2):
        num2 = "是"
    else:
        num2 = "否"
    return render_template("makejobok.html", num=num, num1=num1, num2=num2)

@app.route('/admin')
def admin():
    fo = open("lastnum.txt", "r")
    num = fo.read()
    fo.close()
    fo = open("needpoints.txt", "r")
    num1 = fo.read()
    fo.close()
    fo = open("dojobs.txt", "r")
    num2 = int(fo.read())
    fo.close()
    if(num2):
        num2 = "是"
    else:
        num2 = "否"
    return render_template("admin.html", num=num, num1=num1, num2=num2)

@app.route('/')
def index():
    fo = open("lastnum.txt", "r")
    num = fo.read()
    fo.close()
    fo = open("needpoints.txt", "r")
    num1 = fo.read()
    fo.close()
    fo = open("dojobs.txt", "r")
    num2 = int(fo.read())
    fo.close()
    if(num2):
        num2 = "是"
    else:
        num2 = "否"
    return render_template("list.html", num=num, num1=num1, num2=num2)

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 8083)
