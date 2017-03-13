#!/usr/bin/env python

import unittest
from flaky import flaky

from source.services.info import Info

@flaky
class InfoTest(unittest.TestCase):

    def test_start(self):
        start = Info.start()
        assert start is not None

    def test_about(self):
        about = Info.about()
        assert about is not None

if __name__ == "__main__":
    unittest.main()
