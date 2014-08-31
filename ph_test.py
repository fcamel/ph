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
        pass

    def tearDown(self):
        pass

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

if __name__ == '__main__':
    unittest.main()
