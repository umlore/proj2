#  rankURL(query, page_rank, inverted_index)
#  All the inputs are supposed to be of dictionary

# three webpages. The first 2 has all the same data 
# except the second one has high pageRank, while in the 3rd one
# no target ngrams exist. 
# rankURL should put the second webpage "https://business.biz" a higher rank

queries = {
   'search_id': 17,
   'raw': {
       'raw_search': 'how to make huge profits',
       'raw_tokens': ['how', 'to', 'make', 'huge', 'profits']
   },
   'transformed': {
       'transformed_search': 'make huge profits',
       'transformed_tokens': ['make', 'huge', 'profits'],
       'transformed_bigrams': ['make huge', 'huge profits'],
       'transformed_trigrams': [ 'make huge profits' ]
   }
}

page_rank = {
    'webpages': [
        {
            'webpage': "https://www.money.com",
            'pageRankValue': 10,
            'dateLastUpdated': "2017-11-22",
            'frequency': 'monthly'
        },
        {
            'webpage': "https://www.business.biz",
            'pageRankValue': 20,
            'dateLastUpdated': "2017-12-11",
            'frequency': 'daily'
        },
        {
            'webpage': "https://www.sales.org",
            'pageRankValue': 5,
            'dateLastUpdated': "2017-11-27",
            'frequency': 'monthly'
        },
        {
            'webpage': "https://www.lucre.zone",
            'pageRankValue': 100,
            'dateLastUpdated': "2017-12-10",
            'frequency': 'daily'
        },
        {
            'webpage': "https://www.free.market",
            'pageRankValue': 1,
            'dateLastUpdated': "2017-01-30",
            'frequency': 'yearly'
        }
    ]
}

inverted_index = {
    'returnCode': 0,
    'error': '',
    'documents': [
        {
            'documentID': 'https://www.money.com',
            'wordCount': 566,
            'pageLastIndexed': '2017-12-11',
            'importantTokenRanges': [
                {
                    'fieldName': 'title',
                    'rangeStart': 0,
                    'rangeEnd': 6
                },
                {
                    'fieldName': 'subtitle',
                    'rangeStart': 200,
                    'rangeEnd': 214
                }
            ]
        },
        {
            'documentID': 'https://www.business.biz',
            'wordCount': 2983,
            'pageLastIndexed': '2017-12-11',
            'importantTokenRanges': [
                {
                    'fieldName': 'title',
                    'rangeStart': 0,
                    'rangeEnd': 9
                }
            ]
        },
        {
            'documentID': 'https://www.sales.org',
            'wordCount': 1313,
            'pageLastIndexed': '2017-11-22',
            'importantTokenRanges': [
                {
                    'fieldName': 'title',
                    'rangeStart': 0,
                    'rangeEnd': 15
                }
            ]
        },
        {
            'documentID': 'https://www.lucre.zone',
            'wordCount': 2993,
            'pageLastIndexed': '2017-11-22',
            'importantTokenRanges': [
                {
                    'fieldName': 'title',
                    'rangeStart': 0,
                    'rangeEnd': 19
                }
            ]
        },
        {
            'documentID': 'https://www.free.market',
            'wordCount': 344,
            'pageLastIndexed': '2017-11-22',
            'importantTokenRanges': [
                {
                    'fieldName': 'title',
                    'rangeStart': 4,
                    'rangeEnd': 20
                }
            ]
        }
    ],
    'tokens': [
        {
            'token': 'make',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'https://www.money.com',
                    'locations': [86, 731]
                },
                {
                    'documentID': 'https://www.business.biz',
                    'locations': [7, 453, 791, 880, 2338]
                },
                {
                    'documentID': 'https://www.lucre.zone',
                    'locations': [4, 133, 201, 367, 909, 1334]
                },
                {
                    'documentID': 'https://www.sales.org',
                    'locations': [89]
                },
                {
                    'documentID': 'https://www.free.market',
                    'locations': [55]
                }
            ]
        },
        {
            'token': 'huge',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'https://www.money.com',
                    'locations': [86, 731]
                },
                {
                    'documentID': 'https://www.business.biz',
                    'locations': [8, 454, 792, 881]
                },
                {
                    'documentID': 'https://www.lucre.zone',
                    'locations': [3, 200, 366, 562, 694, 749, 806, 933, 1123, 1316, 1794, 1909]
                },
                {
                    'documentID': 'https://www.sales.org',
                    'locations': [1, 2, 3]
                }
            ]
        },
        {
            'token': 'profits',
            'ngramSize': 1,
            'documentOccurences': [
                {
                    'documentID': 'https://www.money.com',
                    'locations': [1, 87, 323, 411]
                },
                {
                    'documentID': 'https://www.business.biz',
                    'locations': [9, 25, 150, 242, 333, 387, 455, 460, 1002, 1518, 2580]
                },
                {
                    'documentID': 'https://www.lucre.zone',
                    'locations': [5, 16, 154, 202, 235, 290, 351, 498, 499, 500, 666, 703, 880, 924, 1271, 1279]
                },
                {
                    'documentID': 'https://www.free.market',
                    'locations': [67, 112]
                }
            ]
        },
        {
            'token': 'make huge',
            'ngramSize': 2,
            'documentOccurences': [
                {
                    'documentID': 'https://www.lucre.zone',
                    'locations': [3, 200, 366]
                },
                {
                    'documentID': 'https://www.business.biz',
                    'locations': [7, 453, 791, 880]
                }
            ]
        },
        {
            'token': 'huge profits',
            'ngramSize': 2,
            'documentOccurences': [
                {
                    'documentID': 'https://www.lucre.zone',
                    'locations': [4, 15, 201, 289, 350, 879]
                },
                {
                    'documentID': 'https://www.business.biz',
                    'locations': [8, 454, 459]
                },
                {
                    'documentID': 'https://www.money.com',
                    'locations': [86]
                }
            ]
        },
        {
            'token': 'make huge profits',
            'ngramSize': 3,
            'documentOccurences': [
                {
                    'documentID': 'https://www.lucre.zone',
                    'locations': [3, 200]
                },
                {
                    'documentID': 'https://www.business.biz',
                    'locations': [7, 453]
                }
            ]
        },
    ]
}
