import subprocess
import sys

version = 1.0

def servicestat(service):
    p = subprocess.Popen(['systemctl', 'is-active', str(service)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    out = out.decode('utf-8')
    return (service, out)



def main():
    print(f'ServiceTool, Version{version} by omeroguz45')
    while True:
        service, stat = servicestat('ssh')
        print(f'{service} - {stat}', end='\r')

if __name__ == '__main__':
    main()
