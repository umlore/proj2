from flask import Flask, request, jsonify
import requests
import json
import operator

app = Flask(__name__)

class aDocument:
	document = ""
	total_tokens = 0

def parseTerms(query):
	#do something here
	return None

# query - dic from querying team
# result of what link analysis (check)
# dictionary
def rankUrls(query, page_ranks, index):
	# Check these
		# 1. does it have all the query terms?
		# 2. how many query terms does it match total?  including repeats?
		# 3. adjacency: are the query terms close together?
		# 4. multiply by some factor determined by page_rank for that url
		# 5. come up with some way of multiplying by recency

	## parse out the webpages from indexing and get list of webpages from link analysis
	documents = {}
	webpages = {'webpages':[]}

	for doc in index['documents']:
		webpages['webpages'].append(doc['documentID'])

		## dictionary with url as key. Value is a dictionary of {<token>:[<loc>]}
		documents[doc['documentID']] = {}


	for tk in index['tokens']:
		for occ in tk['documentOccurences']:
			documents[occ['documentID']][tk['token']] = occ['locations']

	all_adocs = []

	for key, value in documents:
		temp = aDocument()
		temp.document = key
		for val in value:
			temp.total_tokens += len(val)
		all_adocs.append(temp)

	sorted_adocs = sorted(doc, key=operator.attrgetter('total_tokens'))

	return sorted_adocs


@app.route('/ranking', methods=['POST'])
def search():
	#if post request is empty or incorrect, abort
	if not request.json or not 'raw' in request.json:
		return "Something Missing\n"

	print(request.url)

	#parse json query
	query = {
		"search_id": request.json["search_id"],
		"raw": request.json["raw"],
		"transformed": request.json["transformed"],
	}


	raw_tokens = query["raw"]["raw_tokens"]

	#todo: figure out the actual url of link analysis
	# url_link_analysis = 'todo: url goes here'
	# url_localHost = '/test'
	# urls_request = urls
	headers = {"Content-Type": "application/json"}

	#r = requests.post('https://localhost:5000/test', data=json.dumps(urlsRequest), headers=headers, timeout=1.000)
	#requests.get('https://localhost:5000/test', timeout=1.000)

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

	'''
	# Will need to convert json we recieve into actual structure
	if(inverted_index_json['returnCode'] != 0):
		print("An error occured (",inverted_index_json['error'],") with return code",inverted_index_json['returnCode'])
		return inverted_index_json['returnCode']
	'''

	#Dump received json to dictionary with the same format
	# json.dump(inverted_index,inverted_index_json)

	# error_code = requests.post("https://localhost:5000/test",data=json.dumps(inverted_index_json),headers=headers,timeout=1.000)
	# print(error_code)

	webpages = ["https://business.zone"] #TODO: generate this from the results of the 
		#post to indexing from inverted_index_json

	page_rank_request = jsonify({"webpages": webpages})

	'''
	page_rank_json = requests.post('https://teamqq.cs.rpi.edu/pageRank', data=page_rank_request, headers=headers, timeout=1.000)
	'''

	#page_rank_result = request.json["webpages"] 
	#TODO: page_rank_request should be parsed from page_rank_json not request.json
		#which is the querying request
	

	dummyReturn = {
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

	return jsonify(dummyReturn)


@app.route('/test', methods=['POST'])
def test():

	# prints out the entire json
	print(request.json)

	return "hello\n"

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0")
