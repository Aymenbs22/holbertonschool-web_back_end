#!/usr/bin/env python3
"""Parameterize and patch as decorators
"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient(unittest.TestCase) class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """test_org method"""
        gitorg = GithubOrgClient(org)
        gitorg.org()
        mock.assert_called_once_with("https://api.github.com/orgs/" + org)
