#!/usr/bin/env python
# -*- encoding: utf8 -*-
import ph

# This is useful to generate HTML in email.
ph.h2.set_default_inline_style('color: orange;')

html = ph.HTML()
html.title() ^ 'My HTML Report'  # ^: replace "innerHTML"
body = html.body()
body << ph.h1('The Headline')  # <<: add child
body << ph.h2('Subtitle')
body << ph.div(id='main')
# Get the new div to add more contents.
new_div = body.last_child()
new_div << ph.p('This is the first paragraph.')
# Note that << is left-associative.
new_div << (ph.p() << 'This is an ' << ph.strong('important') << ' sentence.')
body << ph.h2('Another Subtitle')
body << ph.div('Another div.')
body << ph.div('Another div.')

output = unicode(html)
try:
    import BeautifulSoup
    soup = BeautifulSoup.BeautifulSoup(output)
    output = soup.prettify()
except ImportError, e:
    pass
print output
