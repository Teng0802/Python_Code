# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:31:07 2022

@author: user1
"""

from flask import Flask,request,url_for, render_template
import pickle
import gzip
import numpy as np


app = Flask(__name__, template_folder='temp')
@app.route('/predict', methods = ["GET","POST"])
def index_view():
	bacno = int(request.args.get("bacno"))
	locdt = int(request.args.get("locdt"))
	loctm = int(request.args.get("loctm"))
	cano = int(request.args.get("cano"))
	contp = int(request.args.get("contp"))
	etymd = int(request.args.get("etymd"))
	mchno = int(request.args.get("mchno"))
	acqic = int(request.args.get("acqic"))
	mcc = int(request.args.get("mcc"))
	conam = int(request.args.get("conam"))
	ecfg = int(request.args.get("ecfg"))
	insfg = int(request.args.get("insfg"))
	iterm = int(request.args.get("iterm"))
	stocn = int(request.args.get("stocn"))
	scity = int(request.args.get("scity"))
	stscd = int(request.args.get("stscd"))
	ovrlt = int(request.args.get("ovrlt"))
	flbmk = int(request.args.get("flbmk"))
	hcefg = int(request.args.get("hcefg"))
	csmcu = int(request.args.get("csmcu"))
	flg_3dsmk = int(request.args.get("flg_3dsmk"))
	input1 = np.array([acqic,bacno,cano,conam,
		               contp,csmcu,ecfg,etymd,
		               flbmk,flg_3dsmk,hcefg,insfg,
		               iterm,locdt,loctm,mcc,
		               mchno,ovrlt,scity,stocn,
		               stscd]).reshape(1,-1)
	with gzip.open('./test_model.pgz', 'rb') as f:
		rf = pickle.load(f)
		pred = rf.predict(input1) 
		title = pred[0]
    # 網頁
	return render_template('index.html',title=title)
if __name__ == "__main__":
	app.run(debug=True)
    
    
