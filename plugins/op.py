from util import hook

@hook.command(adminonly=True)
def op(inp, chan='', conn=None):
    ".op <nick> -- gives nick operator status"

    nicks = inp.split(' ')
    for nick in nicks:
       conn.cmd('MODE', [chan, '+o', nick])
    return

@hook.command(adminonly=True)
def deop(inp, chan='', conn=None):
    ".deop <nick> -- takes operator status from nick"

    nicks = inp.split(' ')
    for nick in nicks:
        conn.cmd('MODE', [chan, '-o',  nick])
    return
