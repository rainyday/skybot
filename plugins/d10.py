import random

from util import hook


@hook.command
def d10(inp):
    ".d10 <number> -- rolls <number> of 10 sided dice."

    if not inp.isdigit() or int(inp) > 40:
        return "Invalid dice roll."
    str = ""
    for i in range(0,int(inp)):
        num = random.randint(1,10)
        str = str + `num` + " "
        while num == 10:
            num = random.randint(1,10)
            str = str + `num` + " "
    return str

