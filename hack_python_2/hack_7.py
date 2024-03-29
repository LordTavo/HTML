"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = []
    i = 0
    j = 0

    while i < (len(s)):
        if s[i] == 0:
            return [0]
        else:
            i += 1

    while j < (len(s)):
        if j % 2 == 0:
            result.append(chr(j + 49))
            j += 1
        else:
            result.append(j + 1)
            j += 1

    return result

lista = ["a","b","c","d","e"] 
lista_2 = [0]
print(fn_hack_7(lista_2))
print(fn_hack_7(lista))