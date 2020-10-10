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
        s = subprocess.Popen(['systemctl', 'is-active', f'{options.status}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = s.stdout.read()
        print(out)
        
    elif options.start:
        print('start')
    elif options.stop:
        print('stop')
    else:
        p.print_help()


if __name__ == '__main__':
    main()
