"""
urllib3 is a simple python module that provides a class for URLs.
"""

import re
import subprocess

__version__ = "1.0"
__author__ = "Harold Cohen <kryptonb0y@harold-cohen.com>"

RGX_PROTOCOL = re.compile(u'^(?P<protocol>\w+):\/\/.*$')
RGX_URL = re.compile(u'^\w+:\/\/(?P<url>.*)$')


class Url(object):
    """
    A url.
    """
    url_ = None
    protocol_ = None
    fld_ = None
    domain_ = None
    tld_ = None

    def __init__(self, url, **kwargs):
        if url is None:
            raise AttributeError('No URL was provided.')
        else:
            self.url = url

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        if key is "url":
            match = re.match(RGX_URL, value)
            if match is not None:
                self.url_ = match.group('url')
            else:
                self.url_ = value
            self.protocol()

    def __str__(self):
        return self.protocol_ + "://" + self.url_

    def protocol(self):
        """
        Extract the protocol from a URL.
        :param url: A url as a string.
        :return: The protocol (a string).
        """
        if self.protocol_ is not None:
            return self.protocol_
        else:
            match = re.match(RGX_PROTOCOL, self.url)
            if match is not None:
                self.protocol_ = match.group('protocol')
                return match.group('protocol')
            else:
                self.protocol_ = None
                return None

    def tld(self):
        pass

    def domain(self):
        pass

    def host(self):
        """
        Returns the host for the provided url.
        :return: The host (mixed)
        """
        cmd = 'host ' + self.url_
        res = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        return res.stdout.read()
