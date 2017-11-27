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
	url_link_analysis = 'todo: url goes here'
	url_localHost = '/test'
	urls_request = urls
	headers = {"Content-Type": "application/json"}

	#todo: instead of returning dummy text, return what we get
	#from calling test
	#return jsonify(["www.com", "wallstreet.biz", "zombo.com"])

	#r = requests.post('https://localhost:5000/test', data=json.dumps(urlsRequest), headers=headers, timeout=1.000)
	#requests.get('https://localhost:5000/test', timeout=1.000)

	#Turn all query content into one big set to send to indexing
	index_request = list(set(query["query"] + query["ngrams"] + query["aliases"]))
	print ("Index request: " + str(index_request))

	#POST request to indexing to retreive inverted index for specified words
	# inverted_index_json = requests.post('https://placeholderindexteamurl.rpi.edu', data=json.dumps(index_request), headers=headers, timeout=1.000)

	#Dump received json to dictionary with the same format
	inverted_index = {}
	# json.dump(inverted_index,inverted_index_json)

	# error_code = requests.post("https://localhost:5000/test",data=json.dumps(inverted_index_json),headers=headers,timeout=1.000)
	# print(error_code)

	print(query)
	print(query["query"])
	print("got here")

	#throws a list cannot be indexed error???????? HUHH//?
	#test = query["query"]
	return "Finished ranking\n"

@app.route('/test/', methods=['POST'])
def test():

	# prints out the entire json
	print(request.json)

	return "hello\n"

if __name__ == '__main__':
	app.run(debug=True)