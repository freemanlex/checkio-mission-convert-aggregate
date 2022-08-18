"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[('a', 7), ('b', 8), ('a', 10)]],
            "answer": {'a': 17, 'b': 8}
        },
        {
            "input": [[]],
            "answer": {}
        },
        {
            "input": [[('a', 5), ('a', -5)]],
            "answer": {},
            "explanation": "zero-valued key"
        },
        {
            "input": [[('a', 5), ('a', 5), ('a', 0)]],
            "answer": {'a': 10}
        },
        {
            "input": [[('a', 5), ('', 15)]],
            "answer": {'a': 5},
            "explanation": "unknown key"
        }
    ],
    "Extra": [
        {
            "input": [[('a', 0), ('b', 0), ('', 35)]],
            "answer": {},
            "explanation": "zero-valued keys + unknown key"
        },
        {
            "input": [[('', 0)]],
            "answer": {}
        },
        {
            "input": [[('a', -5), ('', -20), ('a', -20)]],
            "answer": {'a': -25}
        },
        {
            "input": [[('a', -5), ('aa', -20), ('aaa', -20)]],
            "answer": {'a': -5, 'aa': -20, 'aaa': -20}
        }
    ]
}
