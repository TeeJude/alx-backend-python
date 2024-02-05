#!/usr/bin/env python3
"""A Module for testing utils"""
import unittest
import requests
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
                               self, 
                               nested_map: Mapping,
                               path: Sequence,
                               expected: int
                               ) -> None:
        """
        Testing the access_nested_map method output.
        Args:
            nested_map (Dict): dictionary with nested dictionaries
            path(List, tuple, set): keys to needed value in nested dictionary
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
                               self, 
                               nested_map: Mapping,
                               path: Sequence
                               ) -> None:
        """
        Testing the access_nested_map method output
        Args:
            nested_map (Dict): dictionary with nested dictionaries
            path (List, tuple, set): keys to needed value in nested dictionary
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Testing the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(
                    self, 
                    test_url, 
                    test_payload, 
                    mock_requests_get
                    ):
        """
        Testing the get_json method output.
        Args:
            url: url to send http request
            payload: expected json response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Testing the memoize function"""
    def test_memoize(self):
        """Testing if utils.memoize decorator works as intended"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
