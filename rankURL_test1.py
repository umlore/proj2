#  rankURL(query, page_rank, inverted_index)
#  All the inputs are supposed to be of dictionary

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
            'webpage': "www.example.com",
            'pageRankValue': 10,
            'dateLastUpdated': "2017-11-22",
            'frequency': 'daily'
        }
    ]
}

inverted_index = {
    returnCode: 1,
    error: NULL,
    documents: [
        {
            documentID: "doc A",
            wordCount: 13,
            pageLastIndexed: '2017-11-22',
            importantTokenRanges: [
                fieldName: 'no idea what this is',
                rangeStart: 0,
                rangeEnd: 6
            ]
        }
    ],
    tokens: [
        {
            'token': 'our',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'doc A',
                    'locations': [1]
                },
            ]
        },
        {
            'token': 'first',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'doc A',
                    'locations': [1]
                },
                {
                    'documentID': 'doc A',
                    'locations': [1]
                },
            ]
        },
        {
            'token': 'search',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'doc A',
                    'locations': [1]
                }
            ]
        },
        {
            'token': 'our first',
            'ngramSize': 2,
            'documentOccurences': [
                {
                    'documentID': 'doc A',
                    'locations': [1]
                }
            ]
        },
        {
            'token': 'first search',
            'ngramSize': 2,
            'documentOccurences': [
                {
                    'documentID': 'doc A',
                    'locations': [1]
                }
            ]
        },
        {
            'token': 'our first search',
            'ngramSize': 3,
            'documentOccurences': [
                {
                    'documentID': 'doc A',
                    'locations': [1]
                }
            ]
        },
    ]
}
