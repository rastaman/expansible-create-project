"""Tests for our `{{ template_name }} login` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestLogin(TestCase):
    def test_return_help_if_no_args(self):
        output = popen(['{{ template_name }}', 'login'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)
