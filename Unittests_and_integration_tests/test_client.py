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

    def test_public_repos_url(self):
        with patch("client.GithubOrgClient.org") as mock:
            playload = {"repos_url": "a"}
            mock.return_value = playload

    @patch('client.get_json')
    def test_public_repos(self, mock):
        with patch("client.GithubOrgClient._public_repos_url") as mock:
            playload = {"repos_url": "a"}
            mock.return_value = playload
