#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys


__author__ = 'fcamel'


_tags = set([
    'html', 'body', 'head', 'link', 'meta', 'div', 'p', 'form', 'legend',
    'input', 'select', 'span', 'b', 'i', 'option', 'img', 'script', 'style',
    'table', 'tr', 'td', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'fieldset', 'a', 'title', 'body', 'head', 'br',
    'ul', 'ol', 'li',
])

class Tag(object):
    tag_name = 'noname'

    def __init__(self, *args, **kwargs):
        self._children = []
        if len(args) >= 1:
            self << Text(args[0])

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
        output = []
        output.append(u'<%s>' % self.tag_name)
        for tag in self._children:
            output.append(unicode(tag))
        output.append(u'</%s>' % self.tag_name)
        return u''.join(output)

    def __lshift__(self, child):
        self._children.append(child)
        return self

    def last_child(self):
        if not self._children:
            return None
        return self._children[-1]


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
    NewTag.__name__ = name
    return NewTag


class HTML(object):
    doc_type = u'<!DOCTYPE html>'

    def __init__(self):
        self._html = html() << (head() << title(u'No Title')) << body();

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
        return HTML.doc_type + unicode(self._html)


def setup():
    module = sys.modules[__name__]
    for t in _tags:
        setattr(module, t, create_new_tag(t))

setup()


if __name__ == '__main__':
    pass
