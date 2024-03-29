"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    inicio = 1
    final = -1
    
    if s != 'qux':
        result = result[inicio:final]
    else:
        result

    return result


print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4('qux'))