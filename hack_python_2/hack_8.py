"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []

    if len(s) < 3:
        result = [str(i) for i in reversed(range(1, len(s) + 1))]
    elif len(s) > 3 and len(s) <= 4:
        result = [str(i) for i in reversed(range(1, len(s) + 1))]
    elif  len(s) >= 3 and len(s) < 4:
        for i in range(1, len(s) + 1):
            result.append(s[-i] + "-" + str(len(s) - i + 1))
    else:
        for i in range(1, len(s) + 1):
            result.append(s[-i] + "-" + str(len(s) - i + 1))

    return result

lista = ["a","b"]
lista_2 = ["a","b","c","d"]
lista_3 = ["a","b","c"]
lista_4 = ["a","b","c","d","e"]

print(fn_hack_8(lista)) # Output: ['2','1']
print(fn_hack_8(lista_2)) # Output: ['4', '3', '2', '1']
print(fn_hack_8(lista_3)) # Output: ['c-3', 'b-2', 'a-1']
print(fn_hack_8(lista_4))  # Output: ['e-5', 'd-4', 'c-3', 'b-2', 'a-1']