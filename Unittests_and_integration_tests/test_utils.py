#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized
import unittest
import utils
from utils import get_json
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that
    inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """assertRaises context manager to test that a
        KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError):
            self.assertEqual(utils.access_nested_map(nested_map, path))


class TestGetJson(unittest.TestCase):
    """class and implement the TestGetJson.test_get_json
    method to test that utils.get_json
    returns the expected result"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_payload, test_url):
        mockresponse = Mock()
        mockresponse.json = Mock(return_value=test_payload)
        with patch('requests.get', return_value=mockresponse):
            json_data = get_json(test_url)
            self.assertEqual(json_data, test_payload)
