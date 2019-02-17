#!/usr/bin/env python3
import requests
import argparse

import sys


def get_json():
    with requests.get('https://gist.githubusercontent.com/genzj/eaa8dfd1b26b3dea298785cf2db99e43/raw/dynamic-host.json') as res:
        return res.json()


def main():
    parser = argparse.ArgumentParser(description='pull inventory info for ansible.')
    parser.add_argument('--hostname', type=str, nargs=1, help='specific host for connection')
    parser.add_argument('--list', action='store_true', help='list host names')
    args = parser.parse_args()

    if args.list:
        hosts = get_json()
        ans = {
            # '_meta': {
            #     'hostvars': {}
            # },
            # 'all': {
            #     'children': list(hosts.keys())
            # },
            # 'ungrouped': {}
        }
        ans.update(hosts)
    elif args.hostname:
        ans = {
            '_meta': {
                'hostvars': {}
            },
        }
    else:
        raise ValueError('Unknown invocation args: ' + ' '.join(sys.argv))
        
    print(ans)



if __name__ == '__main__':
    main()
