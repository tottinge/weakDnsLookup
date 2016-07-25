import string
import socket

class DnsLookup(object):
    def dnslookup(self, str):
        """ Perform DNS lookup on str.  If first character of digit is numeric,
            assume that str contains an IP address.  Otherwise, assume that str
            contains a hostname."""
        if str == '': str = ' '
        if str[0] in string.digits:
            try:
                value = socket.gethostbyaddr(str)[0]
            except:
                value = 'Lookup failed'
        else:
            try:
                value = socket.gethostbyname(str)
            except:
                value = 'Lookup failed'
        return value
