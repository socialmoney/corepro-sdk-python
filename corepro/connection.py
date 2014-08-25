__author__ = 'socuialmoneydev'
from ConfigParser import SafeConfigParser
import os.path
import base64

class Connection:

    defaultApiKey = None
    defaultApiSecret = None
    defaultDomainName = None
    defaultProxyServer = None
    defaultProxyPort = None
    defaultConfigFilePath = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

    @staticmethod
    def createFromConfig(configFilePath = None):
        c = Connection(configFilePath)
        c.apiKey = Connection.defaultApiKey
        c.apiSecret = Connection.defaultApiSecret
        c.domainName = Connection.defaultDomainName
        c.proxyServer = Connection.defaultProxyServer
        c.proxyPort = Connection.defaultProxyPort
        return c

    def __init__(self, configFilePath = None):
        configFile = configFilePath or Connection.defaultConfigFilePath

        if Connection.defaultApiKey == None and os.path.isfile(configFile):
            parser = SafeConfigParser()
            parser.read(configFile)
            Connection.defaultApiKey = parser.get('CorePro', 'CoreProApiKey')
            Connection.defaultApiSecret = parser.get('CorePro', 'CoreProApiSecret')
            Connection.defaultDomainName = parser.get('CorePro', 'CoreProDomainName')
            Connection.defaultProxyServer = parser.get('CorePro', 'CoreProProxyServer')
            Connection.defaultProxyPort = parser.get('CorePro', 'CoreProProxyPort')

        self.apiKey = Connection.defaultApiKey
        self.apiSecret = Connection.defaultApiSecret
        self.domainName = Connection.defaultDomainName
        self._headerValue = None
        self.proxyServer = Connection.defaultProxyServer
        self.proxyPort = Connection.defaultProxyPort

    @property
    def headerValue(self):
        if self._headerValue == None:
            b64 = base64.b64encode(unicode("{0}:{1}".format(self.apiKey, self.apiSecret)))
            self._headerValue = "Basic {0}".format(b64)

        return self._headerValue

