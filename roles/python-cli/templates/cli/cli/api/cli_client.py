import json

import requests
from requests.auth import HTTPBasicAuth


class {{ template_name_capitalized }}Client:

    def __init__(self, configuration):
        self.configuration = configuration
        self.url = None
        if configuration is not None and 'url' in configuration:
            self.url = configuration['url']
        self.session = None
        # self.enableLogging()

    def enableLogging(self):
        import logging
        import time

        try:
            import http.client as http_client
        except ImportError:
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('--- %s ---', time.strftime("%H:%M:%S"))

    def getConfiguration(self):
        return self.configuration

    def formatResponse(self, response):
        if response.text is not None and response.text != '':
            try:
                return [response.status_code, json.dumps(json.loads(response.text), indent=True)]
            except:
                return [response.status_code, response.text]
        return [response.status_code, None]

    # Session API

    def login(self, url, username, password):
        self.configuration['url'] = url
        self.configuration['username'] = username
        self.configuration['password'] = password
        return 200

    def logout(self):
        # basicAuth = HTTPBasicAuth(self.configuration['username'],self.configuration['password'])
        # r = requests.delete(self.url + '/rest/auth/1/session', auth=basicAuth)
        # return 500
        return None

    def dump(self):
        return self.configuration

    def getSomething(self, something_key):
        basicAuth = HTTPBasicAuth(self.configuration['username'], self.configuration['password'])
        params = {
            'somethingKey': something_key
        }
        r = requests.get(self.url + '/rest/api/something', params=params, auth=basicAuth)
        return r.status_code, r.content
