#  rankURL(query, page_rank, inverted_index)
#  All the inputs are supposed to be of dictionary

# three webpages. The first 2 has all the same data
# except the second one has high pageRank, while in the 3rd one
# no target ngrams exist.
# rankURL should put the second webpage "www.anotherexample.com" a higher rank

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
        'transformed_trigrams': ['our first search']
    }
}

page_rank = {
    'webpages': [
        {
            'webpage': "www.example.com",
            'pageRankValue': 10,
            'dateLastUpdated': "2017-11-22",
            'frequency': 'daily'
        },
        {
            'webpage': "www.anotherexample.com",
            'pageRankValue': 20,
            'dateLastUpdated': "2017-11-22",
            'frequency': 'daily'
        },
        {
            'webpage': "www.example-3.com",
            'pageRankValue': 20,
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
            'documentID': 'www.example.com',
            'wordCount': 13,
            'pageLastIndexed': '2017-11-22',
            'importantTokenRanges': [
                {
                    'fieldName': 'no idea what this is',
                    'rangeStart': 0,
                    'rangeEnd': 6
                }
            ]
        },
        {
            'documentID': 'www.anotherexample.com',
            'wordCount': 19,
            'pageLastIndexed': '2017-11-22',
            'importantTokenRanges': [
                {
                    'fieldName': 'no idea what this is',
                    'rangeStart': 0,
                    'rangeEnd': 6
                }
            ]
        },
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
    'tokens': [
        {
            'token': 'our',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'www.example.com',
                    'locations': [1]
                },
                {
                    'documentID': 'www.anotherexample.com',
                    'locations': [1, 2, 3]
                },
            ]
        },
        {
            'token': 'first',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'www.example.com',
                    'locations': [1]
                },
                {
                    'documentID': 'www.anotherexample.com',
                    'locations': [1, 2, 3]
                },
            ]
        },
        {
            'token': 'search',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'www.example.com',
                    'locations': [1]
                },
                {
                    'documentID': 'www.anotherexample.com',
                    'locations': [1, 2, 3]
                }
            ]
        },
        {
            'token': 'our first',
            'ngramSize': 2,
            'documentOccurences': [
                {
                    'documentID': 'www.example.com',
                    'locations': [1]
                },
                {
                    'documentID': 'www.anotherexample.com',
                    'locations': [1, 2, 3]
                }
            ]
        },
        {
            'token': 'first search',
            'ngramSize': 2,
            'documentOccurences': [
                {
                    'documentID': 'www.example.com',
                    'locations': [1]
                },
                {
                    'documentID': 'www.anotherexample.com',
                    'locations': [1, 2, 3]
                }
            ]
        },
        {
            'token': 'our first search',
            'ngramSize': 3,
            'documentOccurences': [
                {
                    'documentID': 'www.example.com',
                    'locations': [1]
                },
                {
                    'documentID': 'www.anotherexample.com',
                    'locations': [1, 2, 3]
                }
            ]
        },
    ]
}
