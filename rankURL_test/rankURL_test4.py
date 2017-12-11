#  rankURL(query, page_rank, inverted_index)
#  All the inputs are supposed to be of dictionary

# a webpage with no target ngrams in it

queries = {
   'search_id': 2,
   'raw': {
       'raw_search': 'our first search',
       'raw_search': ['our', 'first', 'search']
   },
   'transformed': {
       'transformed_search': 'our first search',
       'transformed_tokens': ['our', 'first', 'search'],
       'transformed_bigrams': ['our first', 'first search'],
       'transformed_trigrams': [ 'our first search' ]
   }
}

page_rank = {
    'webpages': [
        {
            'webpage': "www.example-3.com",
            'pageRankValue': 10,
            'dateLastUpdated': "2017-11-22",
            'frequency': 'daily'
        }
    ]
}

inverted_index = {
    'returnCode': 1,
    'error': '',
    'documents': [
        {
            'documentID': 'www.example-3.com',
            'wordCount': 5,
            'pageLastIndexed': '2017-11-22',
            'importantTokenRanges': [
                {
                    'fieldName': 'no idea what this is',
                    'rangeStart': 0,
                    'rangeEnd': 0
                }
            ]
        }
    ],
    'tokens': []
}
