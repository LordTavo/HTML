"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    cont = 1

    for i in s:
        if isinstance(i, dict):
            result_elemento = {str(cont):str(cont + 1)}
            cont += 2
        else:
            result_elemento = [str(cont),str(cont + 1)]
            cont += 2
        result.append(result_elemento)
    
    return result


lista_original = [{"a":"b"},{"c","d"},{"e":"f"}]
print(fn_hack_10(lista_original))