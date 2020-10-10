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
        print(options.status)
        command = ['systemctl', 'is-active']
        for i in options.status:
            command.append(i)
        s = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = s.communicate()
        print(out)
        print(type(out))
        
    elif options.start:
        print('start')
    elif options.stop:
        print('stop')
    else:
        p.print_help()


if __name__ == '__main__':
    main()
