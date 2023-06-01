#!/usr/bin/env python
# pytemplate.py, rcampbel@purdue.edu, 2023-06-01 
 
import os
import sys
import subprocess
import datetime

import matplotlib.pyplot as plt

# Constants
TODAY_FILE = './today.txt'  # path to a file 
PLOT_FILE = 'plot.png'  # plot file name
LOG_FILE = 'pytemplate.log'
COMMAND = 'cat'

import logging

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)  # <-- Set log level here


def change_file(path):
    """Update the contents of a file."""
    logging.debug('Changing file: "'+path+'"!')

    # Get contents of file
    with open(path, 'r') as input_file:  # 'r' = read file 
        lines = input_file.readlines()

    input_file.close()

    # Modify 2nd line
    lines[1] = datetime.date.today().isoformat() + '\n'  

    # Put new contents back in file
    with open(path, 'w') as new_file:  # 'w' = write 
        
        for line in lines:
            new_file.write(line)

    new_file.close()

def run_app(file_path):
    """Run a binary (executable) program."""
    logging.info('Running: "'+COMMAND+'"')
    
    # Execute external program, wait for result
    result = subprocess.run([COMMAND, file_path]) 

    # Check for error
    if result.returncode != 0:
        logging.error("ERROR: Command exec. failed with return code:" + str(result.returncode))
        sys.exit(1)

def make_plot():
    """Create a plot using matplotlib."""
    _, ax = plt.subplots()
    ax.plot([1, 2, 3], [999, 1001, 1010])
    ax.set_xlabel("X Axis Label", fontsize=14)
    ax.set_ylabel("Y Axis Label", fontsize=14)
    ax.set_title("Small Numbers vs. Bigger Numbers", fontsize=15)
    plt.savefig(PLOT_FILE)
    logging.debug('Saved plot to: "'+PLOT_FILE+'"')
    plt.show()  # NOTE Will block execution until user closes plot window!
    plt.close()
    

if __name__ == "__main__":
    logging.info('Running pytemplate')

    try:
        change_file(TODAY_FILE)
        run_app(TODAY_FILE)
        make_plot()
        # TODO Add more code!
    except Exception as e:
        logging.exception("An error occurred: %s", str(e))

    logging.info('Done!')
