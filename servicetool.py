#!/bin/bash/env python
import optparse
import subprocess

def main():
    p = optparse.OptionParser()
    p.add_option('-s','--status')
    p.add_option('-r','--start')
    p.add_option('-k','--stop')
    options, arguments = p.parse_args()


    if options.status:
        """
        print(type(arguments))
        print(options.status)
        print(options)
        """
        out = subprocess.call(f'systemctl is-active {options.status}') #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(type(out))
        print(out)
        #out = s.stdout.read()
        #print(f'{options.status} is {s}')
    elif options.start:
        print('start')
    elif options.stop:
        print('stop')
    else:
        p.print_help()


if __name__ == '__main__':
    main()
