# -*- coding: utf-8 -*-
"""The session command."""

import json
from .base import Base
from {{ python_template_name }}.api.{{ python_template_name }}_client import {{ template_name_capitalized }}Client


class Session(Base):
    """Manage sessions"""

    def run(self):
        #print('You supplied the following options:', json.dumps(self.options, indent=2, sort_keys=True))
        self.{{ python_template_name }}_client = {{ template_name_capitalized }}Client(self.loadConfiguration())
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

        rc = self.{{ python_template_name }}_client.login(url, username, password)

        if rc == 200:
            self.saveConfiguration(self.{{ python_template_name }}_client.getConfiguration())
        self.processResultCode(rc)

    def logout(self):
        rc = self.{{ python_template_name }}_client.logout()
        self.processResultCode(rc)

    def dump(self):
        configuration = self.{{ python_template_name }}_client.getConfiguration()
        print(json.dumps(configuration))

