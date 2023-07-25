
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
    try:
        assert len(out.split("..")) == 2
        first_part, second_part = map(list,out.split(".."))
        first_digits, second_digits = "", ""
        for char in first_part[::-1]:
            if not char.isdigit():
                first_digits = first_digits[::-1]
                break
            first_digits+=char
            del first_part[-1]
        for i in range(len(second_part)):
            if not second_part[0].isdigit():
                break
            # elif idx == len(second_part)-1:
            second_digits+=second_part[0]
            del second_part[0]
        insert = f"range({int(first_digits)},{1+int(second_digits)}) "
        # they put humpty dumpty back together
        out = " ".join([
            "".join(first_part),
            insert,
            "".join(second_part)
            ])

    except AssertionError as e:
        raise e
    except Exception as e:
        raise CalculatorException("Your range (`..`) failed")

    out = out.strip()
    
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

def main():
    _history = []
    while True:
        _user_in = input("> ")
        _history.append(_user_in)
        # check if we need to exec code (setting variables, etc) or simply eval
        if _user_in.count("=")==1 or ";" in _user_in:
            exec(_user_in)
        else:
            _user_in = transform(_user_in)
            _out = eval(_user_in)
            print(_out)

