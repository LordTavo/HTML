"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []

    if not s:
        return ["0"]
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(chr(i + 49))
            else:
                result.append("-")

        return result

lista = ["a","b","c","d","e"] 
lista_2 = []
print(fn_hack_6(lista_2))
print(fn_hack_6(lista))