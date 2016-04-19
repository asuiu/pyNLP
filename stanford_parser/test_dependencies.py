#!/usr/bin/env python
# coding:utf-8
# Author: ASU --<andrei.suiu@gmail.com>

import unittest


class TestCase(unittest.TestCase):
    def testChildren(self):
        import dependencies

        hierarchy = dependencies.StanfordDependencyHierarchy()
        self.assertEqual(hierarchy.isa("agent", "arg"), True)

        self.assertEqual(hierarchy.isa("ref", "dep"), True)
        self.assertEqual(hierarchy.isa("dep", "dep"), False)

        self.assertEqual(hierarchy.isa("predet", "mod"), True)


if __name__ == '__main__':
    unittest.main()
