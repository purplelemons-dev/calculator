
"""
Calculator made my PurplelemonsDev
License GPLv3
Fun fact: this is my first project made fully with NVIM :D
"""

class CalculatorException(Exception):
    def __init__(self,*args,**kwargs):
        """
        yes i made my own error because im a pretentious prick
        """
        super().__init__(*args,**kwargs)

def transform(txt:str) -> str:
    """
    Transforms a given string into it's python-executable form
    """
    out = txt[:]
    # i never do xor operations in a calculator
    out.replace("^","**")
    # allows range functionality... (e.g. 1..100 == range(1,101))
    for count in out.count(".."):
        idx = out.index("..")
        try:
            ... 
        except Exception as e:
            raise CalculatorException("Your range (`..`) failed")

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
    _history = []
    while True:
        _user_in = input("> ")
        _history.append(_user_in)
        for key,val in vars.items():
            _user_in.replace(key,val)
        # check if we need to exec code (setting variables, etc) or simply eval
        if _user_in.count("=")==1 or ";" in user_in:
            exec(_user_in)
        else:
            _user_in = transform(user_in)
            _out = eval(_user_in)
            print(_out)

