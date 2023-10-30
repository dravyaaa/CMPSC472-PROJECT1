import os
import subprocess
import threading
import time
import multiprocessing
import logging
import signal
import sys
import tkinter as tk

# Configure the logger
logging.basicConfig(filename='process_manager.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Dictionary to store information about running processes
processes = {}

# Create a GUI window
root = tk.Tk()
root.title("Process Manager")

# Create a text widget to display logs
log_text = tk.Text(root)
log_text.pack()

def append_log(log_entry):
    log_text.insert(tk.END, log_entry + '\n')
    log_text.see(tk.END)

# Function to create a new process with improved security and priority management
def create_process():
    program_name = program_name_entry.get()
    args = args_entry.get().split()
    priority = int(priority_entry.get())

    try:
        # Validate user inputs
        if not is_safe_program_name(program_name) or not all(is_safe_argument(arg) for arg in args):
            logging.error("Invalid program name or argument.")
            append_log("Invalid program name or argument.")
            return

        # Ensure that the process is created with reduced privileges
        process = subprocess.Popen([program_name] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=drop_privileges)

        # Store information about the process using its PID as the key
        processes[process.pid] = {
            'process': process,
            'threads': [],
            'state': 'running',
            'output_pipe': process.stdout,
            'start_time': time.time(),
            'priority': priority  # Store process priority
        }

        logging.info(f"Process {process.pid} created with priority {priority}.")
        append_log(f"Process {process.pid} created with priority {priority}.")
    except Exception as e:
        logging.error(f"Error creating process: {e}")
        append_log(f"Error creating process: {e}")

# Function to check if a program name is safe
def is_safe_program_name(program_name):
    # Implement your program name validation logic here
    return True

# Function to check if an argument is safe
def is_safe_argument(argument):
    # Implement your argument validation logic here
    return True

# Function to drop privileges and run the process with reduced rights
def drop_privileges():
    # Ensure that the process is created with reduced privileges
    try:
        # Change group ID (GID)
        os.setgid(target_gid)

        # Change user ID (UID)
        os.setuid(target_uid)
    except OSError as e:
        logging.error(f"Failed to drop privileges: {e}")
        append_log(f"Failed to drop privileges: {e}")

# Function to list running processes
def list_processes():
    logging.info("Listing running processes.")
    append_log("Running Processes:")
    for pid, info in sorted(processes.items(), key=lambda x: x[1]['priority']):
        logging.info(f"PID: {pid}, State: {info['state']}, Priority: {info['priority']}")
        if info['threads']:
            thread_ids = [str(thread_id) for thread_id in range(len(info['threads']))]
            thread_info = ', '.join(thread_ids)
            logging.info(f"Threads in process {pid}: {thread_info}")
            append_log(f"  Threads: {thread_info}")
        append_log(f"  Start Time: {time.ctime(info['start_time'])}")

# Function to terminate a process
def terminate_process():
    try:
        pid = int(terminate_pid_entry.get())
        if pid in processes:
            process = processes[pid]['process']
            process.terminate()
            processes[pid]['state'] = 'terminated'
            logging.info(f"Process {pid} terminated.")
            append_log(f"Process {pid} terminated.")
        else:
            logging.error(f"Process with PID {pid} not found.")
            append_log(f"Process with PID {pid} not found.")
    except ValueError:
        logging.error("Invalid input for PID. Please enter a valid PID.")
        append_log("Invalid input for PID. Please enter a valid PID.")

# Function to create a new thread within a process
def create_thread():
    try:
        pid = int(thread_pid_entry.get())
        if pid in processes:
            thread = threading.Thread(target=worker, args=(len(processes[pid]['threads']), pid))
            processes[pid]['threads'].append(thread)
            thread.start()
            logging.info(f"Thread created in process {pid}.")
            append_log(f"Thread created in process {pid}.")
        else:
            logging.error(f"Process with PID {pid} not found.")
            append_log(f"Process with PID {pid} not found.")
    except ValueError:
        logging.error("Invalid input for PID. Please enter a valid PID.")
        append_log("Invalid input for PID. Please enter a valid PID.")

# Function to simulate work in threads
def worker(thread_id, pid):
    with shared_variable_lock:
        shared_variable = processes[pid]['shared_variable']
        shared_variable += 1
        logging.info(f"Thread {thread_id} in process {pid}: Shared variable incremented to {shared_variable}")

# Function for a multiprocessing process with improved security
def multiprocessing_process(pipe, shared_variable):
    while True:
        time.sleep(1)
        with shared_variable_lock:
            shared_variable.value += 1
            pipe.send(f"Process {os.getpid()}: Shared variable incremented to {shared_variable.value}")

def signal_handler(sig, frame):
    logging.info("Received a termination signal. Exiting gracefully.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
logging.info("Process Manager started.")

# Create labels and entry widgets for user input
program_name_label = tk.Label(root, text="Program Name:")
program_name_label.pack()
program_name_entry = tk.Entry(root)
program_name_entry.pack()

args_label = tk.Label(root, text="Program Arguments (space-separated):")
args_label.pack()
args_entry = tk.Entry(root)
args_entry.pack()

priority_label = tk.Label(root, text="Process Priority (1-10):")
priority_label.pack()
priority_entry = tk.Entry(root)
priority_entry.pack()

create_button = tk.Button(root, text="Create Process", command=create_process)
create_button.pack()

terminate_pid_label = tk.Label(root, text="PID to Terminate:")
terminate_pid_label.pack()
terminate_pid_entry = tk.Entry(root)
terminate_pid_entry.pack()
terminate_button = tk.Button(root, text="Terminate Process", command=terminate_process)
terminate_button.pack()

thread_pid_label = tk.Label(root, text="PID to Create Thread In:")
thread_pid_label.pack()
thread_pid_entry = tk.Entry(root)
thread_pid_entry.pack()
thread_button = tk.Button(root, text="Create Thread", command=create_thread)
thread_button.pack()

list_button = tk.Button(root, text="List Processes", command=list_processes)
list_button.pack()

# You can add additional buttons for other functionalities

root.mainloop()
