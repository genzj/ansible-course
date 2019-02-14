#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: python_expr

short_description: evaluate python expression

version_added: "2.4"

description:
    - "This is a module to evaluate python expressions"

options:
    expr:
        description:
            - This is the expression to evaluate
        required: true
    vars:
        description:
            - local variables to be used in evaluation
            - pass as dict
        required: false
    imports:
        description:
            - modules to be imported before evaluation
        required: false

author:
    - ZHU Jie (zj0512@gmail.com)
'''

EXAMPLES = '''
# Evaluate a expression
- name: Test with a expression
  python_expr:
    expr: "2 ** 4"

# pass in a expression and variables
- name: Test with a expression and variables
  python_expr:
    expr: "x ** y"
    vars:
      x: 2
      y: 4

# import modules to be used in expression
- name: Test expression with imports
  python_expr:
    expr: "''.join(random.choices(candidates, k=8))"
    vars:
      candidates: "abcdefg123456,.-=_+"
    imports:
    - random
'''

RETURN = '''
result:
    description: result of the expression
'''

from importlib import import_module

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        expr=dict(type='str', required=True),
        vars=dict(type='dict', required=False, default=dict()),
        imports=dict(type='list', required=False, default=[])
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        result=None,
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    global_vars = globals()
    del global_vars['ANSIBLE_METADATA']
    del global_vars['DOCUMENTATION']
    del global_vars['EXAMPLES']
    del global_vars['RETURN']

    local_vars = locals()
    del local_vars['result']
    del local_vars['module']
    del local_vars['module_args']
    del local_vars['global_vars']

    try:
        for lib in module.params['imports']:
            module.log('import lib %s' % (lib, ))
            if '.' in lib:
                base = lib.split('.', 1)[0]
                local_vars[base] = import_module(base)
                import_module(lib)
            else:
                local_vars[lib] = import_module(lib)

        local_vars.update(module.params['vars'])
        expr = module.params['expr']
        module.log('global variables: %r' % (global_vars, ))
        module.log('local variables: %r' % (local_vars, ))

        # manipulate or modify the state as needed (this is going to be the
        # part where your module will do what it needs to do)
        result['result'] = eval(expr, global_vars, local_vars)

        # use whatever logic you need to determine whether or not this module
        # made any modifications to your target
        result['changed'] = True
    except Exception as ex:
        # during the execution of the module, if there is an exception or a
        # conditional state that effectively causes a failure, run
        # AnsibleModule.fail_json() to pass in the message and the result
        module.fail_json(msg=str(ex), **result)
    else:
        # in the event of a successful module execution, you will want to
        # simple AnsibleModule.exit_json(), passing the key/value results
        module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

