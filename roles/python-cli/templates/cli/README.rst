{{ template_name }}-cli
========

*A command line client for JIRA.*


Purpose
-------

This is a command line client which allows to interact with the JIRA platform.

Usage
-----

You first need to open a session in JIRA, the command you'll want to run is::

    $ {{ template_name }} session login <url> <username> <api_token>

Before you leave, close your session::

    $ {{ template_name }} session logout

All commands::

    $ {{ template_name }}
    Usage:
    {{ template_name }} session (login <url> <username> <api_token>|logout)
    {{ template_name }} -h | --help
    {{ template_name }} --version

Examples::

    $ {{ template_name }} session login http://myhost:8080/{{ template_name }} myusername mypassword

Help
----

For help using this tool, please open an issue on the Github repository:
{{ scm_url }}

References
----------

 * `Building Simple Command Line Interfaces in Python <https://stormpath.com/blog/building-simple-cli-interfaces-in-python>`__
