#!/usr/bin/env python
# -*- encoding: utf8 -*-

import unittest

import ph


__author__ = 'fcamel'


# TODO:
def split_tag_text(string):
    return string

class PhTest(unittest.TestCase):
    def setUp(self):
        ph.p.default_inline_style = u''

    def tearDown(self):
        ph.p.default_inline_style = u''

    def testEmpty(self):
        html = ph.HTML()
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>No Title</title>'
            u'</head>'
            u'<body>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))

    def testTwoParagraphsInSequence(self):
        html = ph.HTML()
        html.body() << ph.p('1st') << ph.p('2nd')
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>No Title</title>'
            u'</head>'
            u'<body>'
            u'<p>1st</p>'
            u'<p>2nd</p>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))

    def testNestedParagraphs(self):
        html = ph.HTML()
        html.body() << (ph.p('1st') << ph.p('2nd'))
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>No Title</title>'
            u'</head>'
            u'<body>'
            u'<p>1st'
            u'<p>2nd</p>'
            u'</p>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))

    def testInlineElements(self):
        html = ph.HTML()
        html.body() << ph.p()
        p = html.body().last_child()
        (p << 'This is an ' <<
            (ph.span() << 'very ' << ph.strong('important') << ' sentence.'))
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>No Title</title>'
            u'</head>'
            u'<body>'
            u'<p>This is an <span>very <strong>important</strong> sentence.</span></p>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))

    def testSetAttributes(self):
        html = ph.HTML()
        html.body() << ph.div('Hello', id='msg', style='width: 400px;')
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>No Title</title>'
            u'</head>'
            u'<body>'
            u'<div id="msg" style="width: 400px;">'
            u'Hello'
            u'</div>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))

    def testDefaultInlineStyle(self):
        html = ph.HTML()
        html.body() << ph.p('ohoh')
        ph.p.set_default_inline_style('color: red;')
        html.body() << ph.p('lala', style='line-height: 20px;')
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>No Title</title>'
            u'</head>'
            u'<body>'
            u'<p style="color: red;">'
            u'ohoh'
            u'</p>'
            u'<p style="color: red;line-height: 20px;">'
            u'lala'
            u'</p>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))

    def testReplaceContent(self):
        html = ph.HTML()
        html.title() ^ 'My New Title'
        actual = unicode(html)

        expected = (
            u'<!DOCTYPE html>'
            u'<html>'
            u'<head>'
            u'<title>My New Title</title>'
            u'</head>'
            u'<body>'
            u'</body>'
            u'</html>'
        )
        self.assertEquals(split_tag_text(expected), split_tag_text(actual))


if __name__ == '__main__':
    unittest.main()
