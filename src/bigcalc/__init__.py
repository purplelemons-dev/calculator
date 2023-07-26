
"""
Calculator made my PurplelemonsDev
License GPLv3
Fun fact: this is my first project made fully with NVIM :D
"""

class CalculatorError(Exception):
    def __init__(self,*args,**kwargs):
        """
        yes i made my own error because im a pretentious prick
        """
        super().__init__(*args,**kwargs)

def transform(txt:str, debug:bool = False) -> str:
    """
    Transforms a given string into it's python-executable form
    """
    out = txt[:]
    # i never do xor operations in a calculator
    out.replace("^","**")
    # allows range functionality... (e.g. 1..100 == range(1,101))
    if ".." in out:
        try:
            assert len(out.split("..")) == 2
            first_part, second_part = map(list,out.split(".."))
            first_is_neg, second_is_neg = False, False
            first_digits, second_digits = "", ""
            for char in first_part[::-1]:
                if not char.isdigit():
                    if char == "-":
                        first_digits = '-' + first_digits[::-1]
                        del first_part[0]
                    break
                first_digits+=char
                del first_part[-1]
            for i in range(len(second_part)):
                if not second_part[0].isdigit():
                    if char == "-":
                        second_digits = ['-'] + second_digits
                        del second_part[0]
                    break
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
            raise CalculatorError("Your range (`x..y`) failed")

    out = out.strip()
    
    for idx,char in enumerate(txt[1:]):
        # note: `txt[idx]` is the character before `char`
        if (txt[idx] != "*" and char == "("): 
            pt1 = txt[:idx+1]
            pt2 = txt[idx+1:]
            out = f"{pt1}*{pt2}"
        elif (txt[idx] == ")" and char != "*"):
            pt1 = txt[:idx+1]
            pt2 = txt[idx+1:]
            out = f"{pt1}*{pt2}"
    return out

def main(debug:bool=False):
    CLEAR = "\n"*128
    print(CLEAR)
    _history = []
    while True:
        try:
            _user_in = input("> ")
            _history.append(_user_in)
            if _user_in in ("exit","stop"):
                exit()
            elif _user_in == "clear":
                print(CLEAR)
                continue
            # check if we need to exec code (setting variables, etc) or simply eval
            if _user_in.count("=")==1 or ";" in _user_in:
                if debug: print(f"[DEBUG] Interpreted user input ({_user_in!r}) as executable") 
                exec(_user_in)
            else:
                _transformed = transform(_user_in, debug)
                if debug:
                    print(f"[DEBUG] Interpreted user input ({_user_in!r}) as evaluatable") 
                    print(f"[DEBUG] running transformed command ({_transformed})")
                _out = eval(_transformed)
                print(_out)
        # silence all non calc errors
        except CalculatorError as e:
            raise e
        except Exception as e:
            pass

