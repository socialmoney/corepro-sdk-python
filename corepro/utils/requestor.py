__author__ = 'socialmoneydev'
#from ..connection import Connection
import httplib

class Requestor:

    SDK_USER_AGENT = "CorePro Python SDK v {0}".format("0.0.1")

    @staticmethod
    def post(relativeUrl, toPost, classType, connection, loggingObject):
        pass

    @staticmethod
    def get(relativeUrl, classType, connection, loggingObject):
        #connection.proxyServer = None
        if connection.proxyPort is not None and connection.proxyServer is not None:
            httpConn = httplib.HTTPSConnection(connection.proxyServer, int(connection.proxyPort))
            httpConn.set_tunnel(connection.domainName, 443)
            relativeUrl = 'https://' + connection.domainName + relativeUrl
        else:
            httpConn = httplib.HTTPSConnection(connection.domainName, 443)

        headers = {'User-Agent': Requestor.SDK_USER_AGENT,
                  'Content-Type': 'application/json; charset=utf-8',
                  'Accept': 'application/json; charset=utf-8',
                  'Authorization': connection.headerValue,
                  'Host': connection.domainName}

        httpConn.request("GET", relativeUrl, None, headers)
        resp = httpConn.getresponse()
        status = resp.status
        body = resp.read()
        repr(body)
        return body









