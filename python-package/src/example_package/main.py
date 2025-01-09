#!/usr/bin/env python3

from icecream import ic

def main():
    data = {
        'hello': 'world',
        'foo': [
            'bar',
            'baz'
        ]
    }
    ic(data)

if __name__ == '__main__':
    main()
