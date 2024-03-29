"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):
    result = s
    reemplazar = '-'
    n = 2
    
    if len(s) < 3:
        result
    elif s == "fooziman":
        result = s[:n] + "-" + s[n+1:n+3] + "-" + s[n+3:n+5] + "-"
    elif s == "barziman":
        result = s[:n] + "-" + s[n+1:n+3] + "-" +s[n+4:n+6]
    else:
        result = s[:n] + "-"

    return result


print(fn_hack_5("fooziman"))
print(fn_hack_5( "barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))