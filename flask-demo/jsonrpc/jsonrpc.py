#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
from flask_jsonrpc import JSONRPC
import json

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@jsonrpc.method('App.index')         #响应无参数传入的method
def index():                             
	return "hello baby!"

@jsonrpc.method('App.name')         #响应有指定参数传入的method
def name(name):
	return 'hello %s' %  name 

@jsonrpc.method('App.user')        #响应有不定参数传入的method，最常用
def user(**kwargs):
	data = {}
	data['name'] = kwargs.get('name',None)
	data['age'] = kwargs.get('age',None)
	return 'I am  %s,age is %s' % (data['name'],data['age'])

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)
