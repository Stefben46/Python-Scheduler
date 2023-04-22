:warning: While this program is functional, it was designed for a specific use case and may encounter issues if used in other contexts. :warning:

This Python script provides a command line interface for scheduling and managing processes using the subprocess module. With this script, users can easily schedule programs to run at specific intervals or run them manually.

For any info just type help in the terminal when Main.py is open

To run the Example.py file every 5 minutes, you can use the command line interface provided by the scheduler.py script. Here are the steps to do it:

1. Make sure you have Example.py in the same Programs folder.

2. Open a terminal or command prompt and navigate to the directory where Main.py is present and type:
```python Main.py``` to run the program

3. To run  Example.py every 5 minutes (300 in seconds) type:
```runTime Example.py 300```

4. Press enter to run the command.

The script will now schedule Example.py to run every 5 minutes.

The Schedule.txt file is responsible for persisting the interval and time elapsed since the last run, which allows this information to be retained even when the program is shut down. When the program is restarted, it will retrieve these values from the file to resume its tasks.

To ensure uninterrupted execution, keep the terminal open while running your Python code or set it to run on startup. If you shut down your PC or terminal, any ongoing processes will be terminated. Alternatively, use a scheduler to automate the script without requiring manual input.
