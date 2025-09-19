#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:05:25 2024

@author: widhi
"""

import requests
import argparse
import sys

BASE = 'http://rest-server:5151'

def call(endpoint, a, b):
    try:
        r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
        if r.status_code == 200:
            data = r.json()
            print(f"{endpoint}({a},{b}) = {data['result']}")
        else:
            print(f"{endpoint} error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"{endpoint} exception: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple REST client for add/mul/sub/div endpoints")
    parser.add_argument('--op', choices=['add','mul','sub','div','all'], default='all', help='Operation to invoke')
    parser.add_argument('-a', type=float, help='First number', required=True)
    parser.add_argument('-b', type=float, help='Second number', required=True)
    args = parser.parse_args()

    if args.op in ('add', 'all'):
        call('add', args.a, args.b)
    if args.op in ('mul', 'all'):
        call('mul', args.a, args.b)
    if args.op in ('sub', 'all'):
        call('sub', args.a, args.b)
    if args.op in ('div', 'all'):
        call('div', args.a, args.b)

if __name__ == '__main__':
    sys.exit(main())
