# Import subprocess module to spawn new processes
import subprocess 

# Import StringListFile class from "string_list_file" module located in the current directory
from .string_list_file import StringListFile 

# Import atexit, sys and os modules
import atexit 
import sys 
import os

# Create an empty list to store subprocess objects
p_array=[] 

# Instantiate a StringListFile object with 'Schedule.txt' as its argument
fileList = StringListFile('Schedule.txt')

# Define cleanup function to terminate all subprocesses and unregister it using atexit
def cleanup():
    for proc in p_array:
        if proc[1].poll() is None:  # Check if the subprocess is still running
            proc[1].terminate()
atexit.register(cleanup)

# Define terminate function to stop a specific subprocess given a filename
def terminate(filename):
    for tup in p_array:
        if filename in tup[0]:
            try:
                tup[1].terminate()
                p_array.remove(tup)
            except Exception:
                print("Can't terminate")

# Define write function to add filename, input and 0 (to indicate that the process has not yet run) to the StringListFile object
def write(filename, input):
    list = fileList.read()
    for sublist in list:
        if sublist[0] == filename:
            return
    fileList.add([filename, str(input), str(0)])

# Define runTime function to run a program (specified by filename) every <input> seconds using the subprocess module
def runTime(filename,input):
    global p_array
    if os.path.isfile(filename):
        process = subprocess.Popen(['python', 'TimeController.py', filename, str(input)])
        # Add a tuple consisting of the filename and the corresponding process object to p_array
        p_array.append((filename, process))

    else:
        print("TimeController.py not found")

# Define runScheduler function to read the StringListFile object for scheduled programs and run them using the runTime function
def runScheduler():
    list = fileList.read()
    for sublist in list:
        if sublist[0] != "":
            runTime(sublist[0],sublist[1])
        
# Define run function to run a specified program (given by filename) using subprocess module
def run(filename):
    global p_array
    if os.path.isfile(filename):
        process = subprocess.Popen(['python', filename])
        # Add a tuple consisting of the filename and the corresponding process object to p_array
        p_array.append((filename,process))
    else:
        print(f"File {filename} not found in current directory")
        print("> ", end="")
        sys.exit()

# Define list_processes function to display all running processes
def list_processes():
    global p_array
    if len(p_array) == 0:
        print("No Processes Running")
    for i in p_array:
        print(i[0])

# Define alreadyRunning function to check if a program is already running and prompt the user whether to re-run it or not
def alreadyRunning(filename):
    for tup in p_array:
        if filename in tup[0]:
            print(filename+" is already Running, do you want to Re-Run it? [y/n]")
            response = str(input('>'))
            if response in ['y','Y']:
                run(filename)
            elif response not in['n','N']:
                print("Invalid Response")
            return
    run(filename)

# Main block of code
if __name__ == '__main__':
    # Start running all scheduled programs
    runScheduler()
    
    # Ask for user input until the program is stopped
    while True:
        # Split the input string and store it in the command list
        command = str(input('> ')).split()

        # Check the first element in the command list and execute corresponding code block
        if command[0] == 'list':
            list_processes()
            
        elif command[0] == 'run':
            if len(command) > 1:
                alreadyRunning(command[1])
            else:
                print("Specify which Program")
        elif command[0] == 'stop':
            break
        elif command[0] == 'runScheduler':
            runScheduler()
        elif command[0] == 'runTime':
            if len(command) > 2 and command[2].isdigit():
                runTime(command[1],command[2])
                write(command[1],command[2])
            elif len(command) > 1:
                print("Specify how often the program runs")
            else:
                print("Specify which Program you wish to run and how often the program runs")
        elif command[0] == 'terminate':
            if len(command) > 1:
                terminate(command[1])
            else:
                print("Specify which Program")
        
        elif command[0] == 'help':
            # Display a list of available commands and their descriptions
            print("List of commands:")
            print("list: List all currently running programs.")
            print("run <program_name>: Start running a program.")
            print("runScheduler: Start running all scheduled programs.")
            print("runTime <program_name> <time_in_seconds>: Run a program at a specified interval.")
            print("terminate <program_name>: Stop running a program.")
            print("stop: Stop the program.")
        
        else:
            print('Invalid command')
