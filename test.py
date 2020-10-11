import curses

def get_input(window, row, col):
    curses.echo() 
    window.addstr(row, col, '>')
    inp = window.getstr(row, col+1)
    window.refresh()
    return inp

while True:
    screen = curses.initscr() #initialize screen
    num_rows, num_cols = screen.getmaxyx()
    half_col = int(round(num_cols/2))

    input_win = curses.newwin(num_rows,half_col,0,0)
    choice = get_input(input_win, 0,0)
    choice = choice.decode('utf-8')
    curses.flushinp()
    curses.setsyx(0,1)
    input_win.clrtobot()

    info_win = curses.newwin(num_rows, half_col, 0, half_col+1)
    info_win.addstr(0, 0, choice)
    info_win.refresh()
    input_win.refresh()

curses.endwin()
