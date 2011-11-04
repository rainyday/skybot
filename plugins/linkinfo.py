import re, sys

from util import hook, http, urlnorm

@hook.command
@hook.command("li")
def linkinfo(inp):
    "Shows information for a link."

    if not re.compile(r'^http://').match(inp):
        inp = "http://" + inp

    try:
        page = http.get_html(inp)
    except:
        return "Can't open URL."

    title = page.xpath('//title/text()')[0].replace("\n", "")

    return smart_truncate(title)

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0]+suffix

excluded = [r'youtube\.com', r'forums.somethingawful.com']
