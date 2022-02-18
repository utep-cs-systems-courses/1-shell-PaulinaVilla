import os, sys, re

def get_input(args):
    #makes a list of strings

    commands = []
    for word in args.split():
        commands.append(word)

    return commands 



def ch_dir(folder):
    #change directory 

    try:
        os.chdir(folder)
    except FileNotFoundError:
        os.write(1, (f'file {folder} not found\n').encode())



def perform_task(commands):

    for dir in re.split(':', os.environ['PATH']):
        process = f'{dir}/{commands[0]}'
        try:
            os.execve(process, commands, os.environ)
        except OSError:
            pass    #errorcode 

def execute_command(commands):
    #fork child 

    rc = os.fork()

    if rc < 0: 
        perform_task(commands)
    else:
        os.wait()

def redirect(commands):
    rc = os.fork()     #fork child 

    if rc < 0:
        os.write(2,("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        args = [commands[0], commands[1]]

        os.close(1)
        os.open(commands[3], os.O_CREAT | os.O_WRONLY);
        os.set_interitable(1, True)

        perform_task(args) 

    else:
        os.wait()


def main():
    #run until exit command used 

    if(str == 'exit'):
        sys.exit(0)
    elif((str[0:2] == 'cd') and (len(str) > 2)):
        ch_dir(str[3:])
    elif((len(str) == 2) and (str[0:2] == 'cd')):
        os.chdir(os.environ['HOME'])
    else:
        commands = get_input(str)
        #put redirection here

        execute command(commands)

main()

