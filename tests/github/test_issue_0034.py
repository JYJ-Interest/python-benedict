# -*- coding: utf-8 -*-

from benedict import benedict

import json
import unittest


class github_issue_0034_test_case(unittest.TestCase):

    """
    https://github.com/fabiocaccamo/python-benedict/issues/34

    To run this specific test:
    - For each method comment @unittest.skip decorator
    - Run python -m unittest tests.github.test_issue_0034
    """

    def test_json_dumps(self):
        b = benedict({
            'a': 1,
            'b': {
                'c': {
                    'd': 2,
                },
            },
        })
        dumped = json.dumps(b)
        self.assertEqual(dumped, '{"a": 1, "b": {"c": {"d": 2}}}')