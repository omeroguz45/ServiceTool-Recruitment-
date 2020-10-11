import subprocess
import curses

version = 1.0

def servicestat(service):
    p = subprocess.Popen(['systemctl', 'is-active', str(service)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    out = out.decode('utf-8').replace('\n', '')
    return out



def main():
    screen = curses.initscr()
    num_rows, num_cols = screen.getmaxyx()
    output_win = curses.newwin(num_rows-1,num_cols,0,0)
    output_win.addstr(0,0, f'ServiceTool Version {version}, made by omeroguz45.')
    
    #open and read the services from services.txt
    servicesfile = open('./services.txt', 'r')
    services = [i.replace('\n', '') for i in servicesfile.readlines()]
    r = 2 #row number for where to print the service name and status
    for service in services:
        output_win.addstr(r,0, f'{service} - {servicestat(service)}')
        r += 1
    output_win.refresh()
    curses.napms(200000)
    curses.endwin()

if __name__ == '__main__':
    main()
