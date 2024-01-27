#!/usr/bin/env python3
"""unitests for utils.py file"""

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(TestCase):
    """Contains methods testing functions in utils.py

    Args:
        TestCase (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map function

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected (_type_): _description_
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """_summary_

        Args:
            nested_map (_type_): _description_
            path (_type_): _description_
            expected (_type_): _description_
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(error.exception))

class TestGetJson(TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """_summary_

        Args:
            test_url (_type_): _description_
            test_payload (_type_): _description_
        """
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()

class TestMemoize(TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_

    Returns:
        _type_: _description_
    """
    def test_memoize(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        class TestClass:
            """_summary_
            """
            def a_method(self):
                """_summary_

                Returns:
                    _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                    _type_: _description_
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mck:
            test_cls = TestClass()
            test_cls.a_property()
            test_cls.a_property()
            mck.assert_called_once()
