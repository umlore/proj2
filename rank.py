from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def parseQueryJson(query_json):
	#if post request is empty or incorrect, abort
	if not query_json or not 'raw' in query_json:
		return None;

	#parse json query
	query = {
		"search_id": query_json["search_id"],
		"raw": query_json["raw"],
		"transformed": query_json["transformed"],
	}

	return query

def parseIndexTermsFromQuery(query):
	index_query = list(set(query["transformed"]["transformed_tokens"] + 
		query["transformed"]["transformed_bigrams"] + 
		query["transformed"]["transformed_trigrams"]))
	return index_query

def parseJsonFromIndex(index_json):
	index = {
		"returnCode":index_json["returnCode"],
		"error":index_json["error"],
		"documents":index_json["documents"],
		"tokens":index_json["tokens"]
	}
	return index

def parseJsonFromLinkAnalysis(page_ranks_json):
	page_ranks = {
		"webpages": page_ranks_json["webpages"]
	}
	return page_ranks

def rankUrls(query, page_ranks, index):
	#do something here
	return None

@app.route('/ranking', methods=['POST'])
def search():
	query = parseQueryJson(request.json)
	if query == None:
		return "Error: query not parseable"

	print(request.url)

	raw_tokens = parseIndexTermsFromQuery(query)

	#todo: figure out the actual url of link analysis
	# url_link_analysis = 'todo: url goes here'
	# url_localHost = '/test'
	# urls_request = urls
	headers = {"Content-Type": "application/json"}

	#Turn all query content into one big set to send to indexing

	#TODO: figure out what to use other than just raw_tokens
	#query_set = set(query["query"] + query["ngrams"] + query["aliases"])
	#query_set_list = list(query_set)

	print(raw_tokens)

	#TODO: confirm tokens is the correct key for this data
	index_json_request = jsonify({"tokens": raw_tokens})
	
	#POST request to indexing to retreive inverted index for specified words
	#TODO: figure out what the actual teamy endpoint is OR fuckin interface with a diff team
	

	'''

	inverted_index_json = requests.post('https://teamy.cs.rpi.edu/index', data=index_json_request, headers=headers, timeout=1.000)

	'''

	webpages = ["https://business.zone"] 
	#TODO: generate this from the results of the post to indexing from inverted_index_json

	page_rank_request = jsonify({"webpages": webpages})

	'''
	page_rank_json = requests.post('https://teamqq.cs.rpi.edu/pageRank', data=page_rank_request, headers=headers, timeout=1.000)
	'''
	
	#TODO: page_rank_request should be parsed from page_rank_json not request.json
		#which is the querying request
	

	dummy_return = {
		"ID": 69,
	    "ranking": [
			{ 
				"url": "www.url.com",
				"rank": 1, 
				"positions": {"query": [1, 55, 3000], "test": [5], "example": [2, 90]}
			},
			{
				"url": "www.secondurl.com",
				"rank": 2,
				"positions": {"query": [34], "test": [34, 78, 989, 234325]}
			},
			{
				"url": "www.business.zone",
				"rank": 3,
				"positions": {"example": [70, 80, 903, 1122]}
			}
		]
	}

	return jsonify(dummy_return)


@app.route('/test', methods=['POST'])
def test():

	# prints out the entire json
	print(request.json)

	return "hello\n"

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0")
