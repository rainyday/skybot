from util import hook

@hook.regex(r'(?i)runescape')
def kick_runescape(match, conn=None, nick='', chan=''):
    #print "\n\n---RuneScape---\n\n"
    if nick == 'fishmech': conn.cmd('KICK', [chan, nick, 'Fuck Runescape!!'])