"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}

    for i, (key, value) in enumerate(s.items()):
        if i % 2 == 0 and ("k" in key.lower() or "k" in value.lower()):
            key = key.title().replace('k', '').replace('K', '')
            value = value.title().replace('k', '').replace('K', '')
            result[key] = value
    
    return result


lista = {"foo":"fookziman","bar":"barziman"}
print(fn_hack_9(lista))