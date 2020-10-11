import subprocess
import curses

version = 1.0

def get_input(window, row, col):
    curses.echo() 
    window.addstr(row, col, '>')
    inp = window.getstr(row, col+1)
    window.refresh()
    return inp

def servicestat(service):
    p = subprocess.Popen(['systemctl', 'is-active', str(service)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    out = out.decode('utf-8').replace('\n', '')
    return out

def servicecommand(command):
    p = subprocess.Popen(['systemctl', str(command)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read()
    out = out.decode('utf-8').replace('\n', '')
    return out

def main():
    while True:
        #creating the main command line interface
        screen = curses.initscr() #initialize screen
        num_rows, num_cols = screen.getmaxyx() #get the size of the terminal that the program runs on
        half_col = int(round(num_cols/2))

        #creating an output window where services and their statuses are shown
        output_win = curses.newwin(num_rows-1, half_col+5, 0, 0)
        output_win.addstr(0,0, f'ServiceTool Version {version}, made by omeroguz45.')
        info_win = curses.newwin(num_rows-1, half_col-5, 0, half_col+6)
        info_win.addstr(0,0, "Hi!\nThis is ServiceTool, a tool where you can start, stop, restart and monitor the status of the linux services.\nThis is the info window.\nOn the left is the window where the system services and their status are shown.\nOn the bottom is the input window, type 'help' then press enter to start!")
        info_win.refresh()

        #opening and reading the services from services.txt
        servicesfile = open('./services.txt', 'r')
        services = [i.replace('\n', '') for i in servicesfile.readlines()]
        r = 2 #row number for where to print the service name and status
        #printing every service and their status on the output window
        for service in services:
            output_win.addstr(r,0, f'{service} - {servicestat(service)}')
            r += 1
        for line in range(0, num_rows-2):
            output_win.addstr(line, half_col+4, '|')
        #showing the output window
        output_win.refresh()
        while True:
            input_win = curses.newwin(2,num_cols,num_rows-2,0)
            for column in range(0, num_cols):
                input_win.addstr(0, column, '-')
            command = get_input(input_win, 1, 0)
            command = command.decode('utf-8')
            curses.flushinp()
            curses.setsyx(1,1)
            input_win.clrtoeol()
            command_split = command.split(' ')
            commands = ['start', 'stop', 'restart']

            if command_split[0] in commands:
                out = servicecommand(command_split)
                info_win.addstr(0,0, out)
                info_win.refresh()

            else:
                #help info
                info_win.addstr(0,0, f"Did someone call for help?\nIf you've come to here, you probably typed something wrong or just searched help.\nYou typed:{command}\nTo start, stop or restart a service, just type the action (f.e. 'start') then the service you wanna start with a blank in between.\nIt's just that simple!")
                info_win.refresh()
                
            info_win.refresh()
            input_win.refresh()


if __name__ == '__main__':
    main()
