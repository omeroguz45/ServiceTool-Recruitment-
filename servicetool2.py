import subprocess
import sys

version = 1.0

def servicestat(service):
    p = subprocess.Popen(['systemctl', 'is-active', str(service)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    out = out.decode('utf-8')
    sys.stdout.write(out + '\r')
    sys.stdout.flush()



def main():
    print(f'ServiceTool, Version{version} by omeroguz45')
    while True:
        servicestat('ssh')
        servicestat('firewall')

if __name__ == '__main__':
    main()
