#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys


__author__ = 'fcamel'


_tags = set([
    'html', 'body', 'head', 'link', 'meta', 'div', 'p', 'form', 'legend',
    'input', 'select', 'span', 'strong', 'b', 'i', 'option',
    'img', 'script', 'style',
    'table', 'tr', 'td', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'fieldset', 'a', 'title', 'body', 'head', 'br',
    'ul', 'ol', 'li',
])

def escape_double_quote(string):
    return string.replace('"', '&quot;')


class Tag(object):
    tag_name = 'noname'

    def __init__(self, *args, **kwargs):
        self._children = []
        self._attributes = kwargs
        if len(args) >= 1:
            self << Text(args[0])

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
        output = []
        attributes = []
        attr_keys = self._attributes.keys()
        default_inline_style = self.__class__.default_inline_style
        if 'style' not in attr_keys and default_inline_style:
            attr_keys.append('style')
        for key in sorted(attr_keys):
            k = escape_double_quote(key)
            v = escape_double_quote(self._attributes.get(key, u''))
            if k == 'style' and default_inline_style:
                v = default_inline_style + v
            attributes.append(u'%s="%s"' % (k, v))

        if attributes:
            attr = u' ' + u' '.join(attributes)
        else:
            attr = u''
        output.append(u'<%s%s>' % (self.tag_name, attr))
        for tag in self._children:
            output.append(unicode(tag))
        output.append(u'</%s>' % self.tag_name)
        return u''.join(output)

    def __lshift__(self, child):
        if not isinstance(child, Tag):
            child = Text(child)
        self._children.append(child)
        return self

    def __xor__(self, replacement):
        self._children = [replacement]

    def last_child(self):
        if not self._children:
            return None
        return self._children[-1]

    @classmethod
    def set_default_inline_style(cls, style):
        cls.default_inline_style = style


class Text(Tag):
    tag_name = '__text__'

    def __init__(self, string):
        self._string = string

    def __unicode__(self):
        if not isinstance(self._string, unicode):
            self._string = unicode(self._string)
        return self._string


def create_new_tag(name):
    class NewTag(Tag):
        tag_name = name
        default_inline_style = u''
    NewTag.__name__ = name
    return NewTag


class HTML(object):
    doc_type = u'<!DOCTYPE html>'

    def __init__(self):
        self._html = html()
        self._title = title(u'No Title')
        self._head = head() << self._title
        self._body = body()
        self._html << self._head << self._body

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
        return HTML.doc_type + unicode(self._html)

    def head(self):
        return self._head

    def body(self):
        return self._body

    def title(self):
        return self._title


def setup():
    module = sys.modules[__name__]
    for t in _tags:
        setattr(module, t, create_new_tag(t))

setup()


if __name__ == '__main__':
    # This is useful to generate HTML in email.
    h2.set_default_inline_style('color: orange;')

    html = HTML()
    html.title() ^ 'My HTML Report'
    body = html.body()
    body << h1('The Headline')
    body << h2('Subtitle')
    body << div(id='main')
    new_div = body.last_child()
    new_div << p('This is the first paragraph.')
    new_div << (p() << 'This is an ' << strong('important') << ' sentence.')
    body << div('Another div.')

    output = unicode(html)
    try:
        import BeautifulSoup
        soup = BeautifulSoup.BeautifulSoup(output)
        output = soup.prettify()
    except ImportError, e:
        pass
    print output
