import subprocess

version = 1.0

def servicestat(service):
    p = subprocess.Popen(['systemctl', 'is-active', str(service)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out



def main():
    print(f'ServiceTool, Version{version} by omeroguz45')
    while True:
        service = 'ssh'
        stat = servicestat(service)
        print(f'{service} - {stat}', end='\r')

if __name__ == '__main__':
    main()
