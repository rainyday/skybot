import re

from util import hook

@hook.command(adminonly=True)
def say(inp, conn = None, nick='', bot=None):
    ".say <target> <message> -- Sends message to target channel."
    
    if not re.match(r'\#[^ ]+ .*', inp):
        return "Invalid input"
    
    text = inp.split(' ', 1)
    msg = text[1]
    
    conn.msg(text[0], msg)

