
"""
Calculator made my PurplelemonsDev
License GPLv3
Fun fact: this is my first project made fully with NVIM :D
"""

def transform(txt:str) -> str:
    """
    Transforms a given string into it's python-executable form
    """
    out = txt[:]
    for idx,char in enumerate(txt[1:]):
        # note: `txt[idx]` is the character before `char`
        if (txt[idx] != "*" and char == "("): 
            pt1 = txt[:idx+1]
            pt2 = txt[idx+1:]
            out = pt1 + "*" + pt2
        elif (txt[idx] == ")" and char != "*"):
            pt1 = txt[:idx+1]
            pt2 = txt[idx+1:]
            out = pt1 + "*" + pt2
    return out

if __name__ == "__main__":
    vars = dict()
    while True:
        user_in = input("> ")
        for key,val in vars.items():
            user_in.replace(key,val)
        # check if we need to exec code (setting variables, etc) or simply eval
        if user_in.count("=")==1 or ";" in user_in:
            exec(user_in)
        else:
            user_in = transform(user_in)
            out = eval(user_in)
            print(out)

