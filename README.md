# ServiceTool by omeroguz45

Author: Omer Oguz Ozkahraman
Version: 1.0
Last Update: October 11th, 2020. UTC+3 22:22.
Python Compatibility: Only with Python 3.x
Requirements:
  - curses (comes with Unix)
  - subprocess (comes with Python)
Description:
  With ServiceTool you can start, stop, restart and monitor the status of the linux services.
  The interface is made for command line use and is split into three windows; top left for
  monitoring the real time status of services, if they are active (running) or inactive (stopped).
  Top right window for getting information about committed actions and on the bottom window you
  have a command input interface to interact with the software.
  
  The commands which you can use are:
  - start, to start services
  - stop, to stop services
  - restart, to restart services
  - help, to view the help screen.

  You must type your argument as "{command} {service name}".
  If you make a typo, you will be directed to the help screen.
  When you enter your argument correctly, on the top right window you will see the status of your
  action. It can be:
  - working on it,
  - successfully completed,
  - failed.

# ServiceTool-Recruitment-

ServiceTool is a command line tool meant to monitor the status of linux services
and start and stop them easily.

Service statuses can be:
- Running
- Stopped
- Starting
- Stopping
- Failed

## Hints

Services can be started, stopped and monitored by using linux commands like
```
systemctl start <service name>
systemctl stop <service name>
systemctl is-active <service name>
```

---

### Software requirements
- The software shall load services names from a file "services.txt"
- The user shall start and stop a service easily (usability)
- The user shall see the realtime status of a service
  - Refresh rate < 1 second
- The software shall be executed from a terminal over SSH over low-bandwidth connection

You can edit services.txt files according to your PC installed services
to test the tool during developement.

## Info for recruitement

You can write this tool in any programming language,
try to complete the software as much as you can.

### I don't use linux :(
If you don't have linux and you have no intention to install it just for this project
you can do the same for windows, no problem...