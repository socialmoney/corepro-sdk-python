__author__ = 'socialmoneydev'
#from ..connection import Connection
from ..models.envelope import Envelope
from ..coreproapiexception import CoreProApiException
import httplib
import json

class Requestor(object):

    SDK_USER_AGENT = "CorePro Python SDK v {0}".format("0.0.1")

    def post(self, relativeUrl, toPost, classDef, connection, loggingObject):
        pass

    def get(self, relativeUrl, classDef, connection, loggingObject):
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
        return self.parseResponse(status, None, body, classDef)

    def parseResponse(self, status, requestBody, responseBody, classDef):
        if status == 501:
            raise 501
        elif status == 502:
            raise 502
        elif status == 503:
            raise 503
        elif status == 504:
            raise 504
        elif status == 505:
            raise 505
        else:
            parsedJson = json.loads(responseBody)
            e = Envelope()
            e.rawRequestBody = requestBody
            e.rawResponseBody = responseBody
            e.fromJson(parsedJson, { 'data': classDef })
            if len(e.errors) > 0:
                raise CoreProApiException(e.errors)
            else:
                return e.data
