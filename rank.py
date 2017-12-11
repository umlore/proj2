
from flask import Flask, request, jsonify
import requests
import json
import operator

app = Flask(__name__)

class aDocument:
    def __init__(self):
        self.document = ""
        self.total_tokens = 0
        self.rank = 0
        self.positions = []

def parseTerms(query):
    #do something here
    return None

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
    #if post request is empty or incorrect, abort
    if not query or not 'raw' in query:
        return None;

    index_query = list(set(query["transformed"]["transformed_tokens"] +
    query["transformed"]["transformed_bigrams"] + 
    query["transformed"]["transformed_trigrams"]))

    return index_query

def parseJsonFromIndex(index_json):
    #if post request is empty or incorrect, abort
    if not index_json or not 'documents' in index_json:
        return None;

    index = {
        "returnCode":index_json["returnCode"],
        "error":index_json["error"],
        "documents":index_json["documents"],
        "tokens":index_json["tokens"]
    }
    return index

def parseJsonFromLinkAnalysis(page_ranks_json):
    #if post request is empty or incorrect, abort
    if not page_ranks_json or not 'webpages' in page_ranks_json:
        return None;

    page_ranks = {
        "webpages": page_ranks_json["webpages"]
    }
    return page_ranks

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

    for key, value in documents.items():
        temp = aDocument()
        temp.document = key
        for k, val in value.items():
            temp.total_tokens += len(val)
                        #  temp.total_tokens += len(val)
        all_adocs.append(temp)

    #  sorted_adocs = sorted(doc, key=operator.attrgetter('total_tokens'))
    sorted_adocs = sorted(all_adocs, key=operator.attrgetter('total_tokens'), reverse=True)

    return sorted_adocs

#Given a list of documents, set rank attribute equal to total_tokens
#Helper function for frequency weight as to not disturb total_tokens count
def assignRank(docs):
    for d in docs:
        d.rank = d.total_tokens
    return docs

#Given a list of documents that have been run through rankURLs
#and a list of dictionaries containing {document,number of clicks}
#that would be received from querying,
#Add an appropriate score modifier
def frequencyWeight(weights, frequencies):
    for x in frequencies:
        for y in weights:
            #If the document is in weights, apply the modifier to it
            if x["document"] == y.document:
                y.rank += x["clicks"] * 1.1
    #sort the returned list of docs by rank instead of total_tokens
    weights = sorted(all_adocs, key=operator.attrgetter('rank'), reverse=True)
    return weights

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

    print("\nTHIS IS THE QUERY WOWW\n")
    print(query)

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

    return (dummy_return)


@app.route('/test', methods=['POST'])
def test():

    # prints out the entire json
    print(request.json)

    return "hello\n"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
