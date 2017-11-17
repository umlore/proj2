from flask import Flask, request, jsonify, request
import requests
import json

app = Flask(__name__)

received_queries = []

@app.route('/ranking/', methods=['POST'])
def search():
	#if post request is empty or incorrect, abort
	#(todo: probably don't want to abort)
	if not request.json or not 'query' in request.json:
		abort(400)

	#parse json query
	query = {
		"query": request.json["query"],
		"ngrams": request.json["ngrams"],
		"aliases": request.json["aliases"],
	}

	#keep track of sent queries to verify that our server works
	#todo: remove
	received_queries.append(query);

	#compile list of urls to get data from, based on comparison 
	urls = query["query"]

	#todo: figure out the actual url of link analysis
	urlLinkAnalysis = 'todo: url goes here'
	urlLocalHost = '/test'
	urlsRequest = urls
	headers = {"Content-Type": "application/json"}

	#todo: instead of returning dummy text, return what we get
	#from calling test
	#return jsonify(["www.com", "wallstreet.biz", "zombo.com"])

	#r = requests.post('https://localhost:5000/test', data=json.dumps(urlsRequest), headers=headers, timeout=1.000)
	#requests.get('https://localhost:5000/test', timeout=1.000)

	return query["query"]


if __name__ == '__main__':
	app.run(debug=True)