import subprocess, os, sys

#"F*ck it. Do your thing. Love yourself."

print('''
    this is a script for quick setup of this machine
    written by yours truly...

''')
print('setting up network...\n\n-- -- -- --\n')
def net_setup():

    try:
        proc = subprocess.run(["nmcli", 'dev', 'wifi'], capture_output=True)
        for i in proc[0].split(',')[4].split('\'',maxsplit=1)[1].split('\\n'):
            print(i)
    except:
        print('dependency \'nmcli\' is not installed. exitting.')
        exit(0)
    nw = input('which network would you like to choose?\ntype "R" for a rescan: ')
    if nw.lower() == 'r':
        net_setup()
    else:
        try:
            x = subprocess.run(["nmcli", 'dev', 'wifi', 'con', nw, 'password', input('password: ')], capture_output=True)
            print(x)
        except:
            print('password incorrect or dependency nmcli not installed (to test if installed try nmcli --help. error implies its not installed)')

#this function handles the commands and downloads
def get_packages(hacking, radio):
    cmd = 'sudo apt-get install'
    pkgs = []
    #uses the os.system function for all downloads in case mok key is added
    #install defaults
    with open('APT/defaults.txt') as f:
        #append all of the listed packages to the end of the command
        for i in f:
            #comment condition
            if '#' in i or i.startswith('#'):
                continue
            pkgs.append(' '+i.strip('\n'))
    if hacking == 1:
        # append all of the listed packages to the end of the command
        with open('APT/hacking.txt') as f:
            for i in f:
                # comment condition
                if '#' in i or i.startswith('#'):
                    continue
                pkgs.append(' '+i.strip('\n'))
    if radio == 1:
        with open('APT/radios.txt') as f:
            for i in f:
                # comment condition
                if '#' in i or i.startswith('#'):
                    continue
            pkgs.append(' '+i.strip('\n'))

    print('\npackages:\n')
    for i in pkgs:
        cmd += i

    print('running command: ', cmd)
    try:
        os.system(cmd)
    except:
        print('failed to download exitting...')


#this function is for user input
def install_packages():

    #ask for hacking packages

    c = input('do you wish to install hacking tools? (Y/n)')

    if c.lower() == 'yes' or c.lower() == 'y':
        x = 1
    else:
        x = 0
    #ask for radio packages
    c = input('do you wish to install radio tools? (Y/n)')
    if c.lower() == 'yes' or c.lower() == 'y':
        y = 1
    else:
        y = 0

    if x == 0 and x == y:
        print('only installing defaults')
    elif x==1 and x==y:
        print('installing all specified packages')
    elif x ==0 and y!=x:
        print('installing \'default\' and \'radio\' packages')
    elif x==1 and y!=x:
        print('installing \'default\' and \'hacking\' packages')


    get_packages(x, y)

net_setup()
install_packages()
