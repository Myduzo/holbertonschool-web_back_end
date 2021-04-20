#!/usr/bin/env python3
""" Unit test file
"""
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Class for testing Nested Map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map method
        """
        test = access_nested_map(nested_map, path)
        self.assertEqual(test, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1},("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test method raises keyError
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """ Class for testing Get Json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json method
        """
        with patch('requests.get') as mock_res:
            mock_res.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            # Assert that the mock was called exactly once.
            mock_res.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """ Class for testing Memoize function
    """
    def test_memoize(self):
        """ Test memoize method
        """
        class TestClass:
            """ Class TestClass used to define methods
            """
            def a_method(self):
                """ Returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Returns the a_method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test = TestClass()
            self.assertEqual(test.a_property, patched.return_value)
            self.assertEqual(test.a_property, patched.return_value)
            patched.assert_called_once()
