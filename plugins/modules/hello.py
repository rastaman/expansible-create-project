#!/usr/bin/python
# Inspired by ecs_cluster module
#
DOCUMENTATION = '''
---
module: mep
short_description: Module to drive IHM deploiement from Ansible
'''

EXAMPLES = '''
- name: Build configuration from delivery, packages and status
  mep:
    delivery: "{{ playbook_dir }}/delivery.json"
    executable: "/usr/local/appliMM/mep-py/bin/mep.py"
'''

import sys
import time
import json
import time
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec = dict(
            say    = dict(),
            action     = dict(default='status', choices=['create', 'status']),
            executable = dict(default='/usr/local/appliMM/mep-py/bin/mep.py'),
            delivery   = dict()
        )
    )

    module.exit_json(changed=True)

if __name__ == '__main__':
    main()