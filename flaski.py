from flask import Flask
from flask import request
from flask import jsonify
#from quark.cli import entry_point
# from rq import Queue
# from worker import conn
# from utils import count_words_at_url
import apk_download   #apkdownload script
import andro #(androguard)
import ml_algo
import ann_result
app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
	if request.method == 'POST':
		packagename = request.form['packageName']
		apk_download.download_apk(packagename)
		x=1
		return jsonify(bool(x))
		#return packagename

@app.route('/posteval', methods = ['POST'])
def eval():
	if request.method == 'POST':
		andro.mainn()
		x=1
		return jsonify(bool(x))		

@app.route('/postrf', methods = ['POST'])
def eval2():
	if request.method == 'POST':
		output = ml_algo.tree()
		return jsonify(output)
		
@app.route('/postann', methods=['POST'])
def index():
	if request.method == 'POST':
		output = ann_result.tree()
		return jsonify(output)
    
 
  
		
if __name__ == '__main__':
    app.run(debug=True)
