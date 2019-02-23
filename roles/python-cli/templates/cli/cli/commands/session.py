# -*- coding: utf-8 -*-
"""The session command."""

import json
from .base import Base
from {{ template_name }}.api.{{ template_name }}_client import {{ template_name | capitalize }}Client


class Session(Base):
    """Manage sessions"""

    def run(self):
        #print('You supplied the following options:', json.dumps(self.options, indent=2, sort_keys=True))
        self.{{ template_name }}_client = {{ template_name | capitalize }}Client(self.loadConfiguration())
        if self.hasOption('login'):
            self.login()
        elif self.hasOption('logout'):
            self.logout()
        elif self.hasOption('dump'):
            self.dump()
        else:
            print("Nothing to do.")

    def login(self):
        url = self.options['<url>']
        username = self.options['<username>']
        password = self.options['<password>']

        rc = self.{{ template_name }}_client.login(url, username, password)

        if rc == 200:
            self.saveConfiguration(self.{{ template_name }}_client.getConfiguration())
        self.processResultCode(rc)

    def logout(self):
        rc = self.{{ template_name }}_client.logout()
        self.processResultCode(rc)

    def dump(self):
        configuration = self.{{ template_name }}_client.getConfiguration()
        print(json.dumps(configuration))

