#!/usr/bin/env python3
"""
Unittest for utils.access_nested_map
"""
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import Mock, patch


class TestAccessNestedMap (unittest.TestCase):
    """
    TestAccessNestedMap class for
    testing access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, res):
        """
        Testcases for nested map function
        """
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("b",), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, res):
        """
        Testcases for error handling
        """
        self.assertRaises(res, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class for testing get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Method for testing the get_json function
        """
        response = Mock()
        response.json.return_value = test_payload
        mock_get.return_value = response
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class for testing
    memoize function
    """
    def test_memoize(self):
        """
        Method for testing the memoize function
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as m:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            m.assert_called_once()
