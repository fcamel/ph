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


if __name__ == '__main__':
    unittest.main()
