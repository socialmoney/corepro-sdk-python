__author__ = 'socialmoneydev'
from ..connection import Connection
from ..models.envelope import Envelope
from ..coreproapiexception import CoreProApiException
import httplib
import urllib

class Requestor(object):

    SDK_USER_AGENT = "CorePro Python SDK v {0}".format("0.0.1")

    @staticmethod
    def escape(val):
        if val is None:
            return ''
        else:
            return urllib.quote(val)

    def post(self, relativeUrl, classDef, toPost, connection, loggingObject):
        connection = connection or Connection.createFromConfig()
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

        requestBody = toPost.toJson()

        httpConn.request("POST", relativeUrl, requestBody, headers)
        resp = httpConn.getresponse()
        status = resp.status
        responseBody = resp.read()
        return self.parseResponse(status, requestBody, responseBody, classDef)

    def get(self, relativeUrl, classDef, connection, loggingObject):
        connection = connection or Connection.createFromConfig()
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
        return self.parseResponse(status, None, body, classDef)

    def parseResponse(self, status, requestBody, responseBody, classDef):
        e = Envelope()
        e.rawRequestBody = requestBody
        e.rawResponseBody = responseBody
        e.fromJson(responseBody, {'data': classDef})
        if len(e.errors) > 0 or (status != 200 and status != 201):
            raise CoreProApiException(e.errors, status)
        else:
            return e.data
