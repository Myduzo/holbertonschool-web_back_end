#!/usr/bin/env python3
"""
"""

from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock
from client import GitHubOrgClient
from parameterized import parameterized, parameterized_class


class TestGitHubOrgClient(TestCase):
    """ Class for testing org function
    """
    @parameterized.expand([
        ('google', {'google': True}),
        ('abc', {'abc': True})
    ])
    @patch('client.get_json')
    def test_org(self, org, patched, expected):
        """ Test org method
        """
        g = GitHubOrgClient(org)
        self.assertEqual(g.org, expected)
        patched.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """ test _public_repos_url method
        """
        mock_path = 'client.GitHubOrgClient.org'
        expected = 'www.google.com'
        payload = {'repos_url': expected}
        with patch(mock_path, PropertyMock(return_value=payload)):
            client = GitHubOrgClient('g')
            self.assertEqual(client._public_repos_url, expected)
