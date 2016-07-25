import unittest

from dns_lookup import DnsLookup

class testDnsLookup(unittest.TestCase):
    def test_localhost(self):
        s = DnsLookup()
        r = s.dnslookup("localhost")
        self.assertEqual("127.0.0.1", r)

    def test_badlyAnother(self):
        s = DnsLookup()
        r = s.dnslookup("google.com")
        self.assertEqual("74.125.201.102", r)

    def test_reverse(self):
        s = DnsLookup()
        r = s.dnslookup("127.0.0.1")
        self.assertEqual("localhost", r)


