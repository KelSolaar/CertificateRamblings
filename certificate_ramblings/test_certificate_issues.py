import os
import unittest
import tempfile
from six.moves import urllib


class TestCertificateIssues(unittest.TestCase):
    def test_certificate_issues(self):
        urllib.request.urlretrieve(
            'https://zenodo.org/api/files/a1f87ae9-bf9b-4451-becd-b4b3d7e35cc5/SRS-99-020.txt',
            filename=tempfile.mktemp(),
            data=None)
