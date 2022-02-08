import os, sys, re


def get_command(str):
    command_list = []
    for word in str.split():
        command_list.append(word)

    return command_list; 


def c_d(folder):

 #Change directory
    try:
        os.c_d(folder)
    except FileNotFoundError:
        os.write(1, (f'file {commands[1]} not found\n ').encode())
       

def fork_fail():
    #checks if fork failed 

    os.write(1,(f'fork failed {os.getpid()}\n').encode())
    sys.exit(1)


def perform_task(commands):

    for dir in re.split(':', os.environ['PATH'});
        program = f'{dir}/ {commands[0]}'
        try:
            os.execve(program, commands, os.environ)
        except OSError as error:
            os.write(1,(f'Error code: {error}\n').encode())

def execute_command(commands):
    #fork to make child 
    pid = os.getpid()

    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)
    elif rc ==0:
        os.write(1,("I am a child. My pid== %d\n" %( os.getpid())
        perform_task(commands)
    else:
        os.write(1,("I am parent. My pid ==%d\n" %(pid).encode())
        os.wait()
























