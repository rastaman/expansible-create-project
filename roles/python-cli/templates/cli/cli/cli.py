"""
{{ template_name }}

Usage:
  {{ template_name }} session (login <url> <username> <password>|logout|dump)
  {{ template_name }} -h | --help
  {{ template_name }} --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  {{ template_name }} session login https://host.example.com myusername mypassword

Help:
  For help using this tool, please open an issue on the Github repository:
  {{ scm_url }}
"""

from inspect import getmembers, isclass
import inspect
import json

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import {{ template_name }}.commands
    options = docopt(__doc__, version=VERSION)

    # print("In entry point: %s" % json.dumps(options,indent=2))
    # print("Commands: %s" % json.dumps(dir({{ template_name }}.commands),indent=2))

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        # print("Look for %s (and %s)" % (k, v))
        if hasattr({{ template_name }}.commands, k) and v:
            module = getattr({{ template_name }}.commands, k)
            {{ template_name }}.commands = getmembers(module, isclass)
            command = [command[1] for command in {{ template_name }}.commands if command[0] != 'Base' and inspect.getmodule(
                command[1]).__name__.startswith('{{ template_name }}.commands')][0]
            # print("Command is %s" % command.__name__)
            command = command(options)
            command.run()
