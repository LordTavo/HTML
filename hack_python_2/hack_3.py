"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    result = ''
    condiciones = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v'}
    txt = ''

    for i,char in enumerate(s):
        txt = condiciones.get(char.lower(),char)
        if i == 0 or i == len(s) - 1:
            txt = txt.upper()
        if s[i:i + 2].lower() == "u":
            txt = "v"
        result += txt

    return result

print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))