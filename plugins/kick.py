from util import hook

@hook.command()
def kick(inp, chan, conn):
    ".kick <nick> -- kicks user"

    nicks = inp.split(' ')
    for nick in nicks:
       conn.cmd('KICK', [chan,  nick])
    return
