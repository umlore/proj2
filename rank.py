from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

received_queries = []

# curl -H 'Content-Type: application/json' -X POST -d '{"query":"this query","ngrams":"this gram","aliases":"this alias"}' http://localhost:5000/ranking/


@app.route('/ranking', methods=['POST'])
def search():
	#if post request is empty or incorrect, abort
	if not request.json or not 'query' in request.json:
		return "Somthing Missing\n"

	print(request.url)

	#parse json query
	query = {
		"query": request.json["query"],
		"ngrams": request.json["ngrams"],
		"aliases": request.json["aliases"],
	}

	#keep track of sent queries to verify that our server works
	#todo: remove
	# received_queries.append(query);

	urls = query["query"]

	#todo: figure out the actual url of link analysis
	# url_link_analysis = 'todo: url goes here'
	# url_localHost = '/test'
	# urls_request = urls
	# headers = {"Content-Type": "application/json"}

	#r = requests.post('https://localhost:5000/test', data=json.dumps(urlsRequest), headers=headers, timeout=1.000)
	#requests.get('https://localhost:5000/test', timeout=1.000)

	#Turn all query content into one big set to send to indexing

	theSet = set(query["query"] + query["ngrams"] + query["aliases"])
	newList = list(theSet)

	# index_request = json.dumps(newList)
	# print(index_request)

	json_index_request = jsonify(newList)
	print(json_index_request)


	#POST request to indexing to retreive inverted index for specified words
	# inverted_index_json = requests.post('https://placeholderindexteamurl.rpi.edu', data=json.dumps(index_request), headers=headers, timeout=1.000)

	#Dump received json to dictionary with the same format
	# json.dump(inverted_index,inverted_index_json)

	# error_code = requests.post("https://localhost:5000/test",data=json.dumps(inverted_index_json),headers=headers,timeout=1.000)
	# print(error_code)

	return json_index_request


@app.route('/test', methods=['POST'])
def test():

	# prints out the entire json
	print(request.json)

	return "hello\n"

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0")
