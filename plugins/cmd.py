import re

from util import hook

@hook.command(adminonly=True)
def cmd(inp, conn = None, nick =''):
    ".cmd <command> <arg>[; <arg2>...] Executes raw commands (requires authorization)."
    
    str = inp.split(' ', 1)
    cmd = str[0]
    args = re.split('; ?', str[1])
    conn.cmd(cmd, args)
