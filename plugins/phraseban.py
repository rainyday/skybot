from util import hook

re = ['browngasm', 'brownginity']

@hook.regex(*re)
def phraseban(match, chan='', nick='', conn=None):
    conn.cmd('KICK', [chan, nick, 'fuck you'])
    return

