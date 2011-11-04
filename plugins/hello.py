from util import hook

@hook.regex(r'(?i)^(hello|hi|hey|what\'?s? up) tardbot')
def say_hello(match, say=None, nick=''):
    say('Hi, ' + nick + '!')
