Advanced Process Manager with Process Synchronization

Project I

Dravya Patel

PSU Abington

CMPSC 472: Mr. Janghoon Yang

**IMPLEMENTED FUNCTIONALITIES**

**Thread Support and Synchronization:**

Implemented support for multiple threads within a process using a library like threading.

Integrate synchronization mechanisms like mutexes and semaphores to manage thread synchronization.

**Inter-Process Communication (IPC):**

IPC mechanisms to allow processes and threads to communicate and share data. This may include message passing, shared memory, or pipes.

Use of relevant system calls or library functions for IPC operations.

**Advanced Process Management:**

Enhance the process management features, such as process listing, termination, and monitoring.

Allow users to view more detailed information about each process, including resource usage.

**Logging and Reporting:**

Implement a logging and reporting system to track the execution of processes and threads.

Log significant events, errors, and information related to process synchronization.

**Command-Line Interface (CLI):**

Expand and improve the CLI to provide more options for managing processes and threads.

Include error handling for invalid inputs and display informative error messages.

**Error Handling:**

Implement comprehensive error handling throughout the project to handle unexpected issues gracefully.

Ensure proper resource cleanup during errors.

**Testing and Debugging:**

Develop a suite of test cases to ensure that my process manager functions correctly.

Perform extensive testing and debugging to identify and resolve issues.

**Documentation:**

Includes thorough documentation, including a user manual and inline comments in my code to explain its functionality and usage.

**Optimization:**

Optimized my code for performance and memory usage to make the process manager more efficient.

**Security:**

Pay attention to security aspects, such as validating user inputs and preventing unauthorized access to processes and data.

Ensure the safety of inter-process communication and synchronization.

**Version Control and Collaboration:**

Use version control (e.g., Git) to keep track of changes to your codebase, which is especially important if you're working with a team. Though this project is NOT a team project, implementing this makes sense as process manager would most likely be used in a team environment in the real world.

**Additional Features:**

Added advanced features, such as priority management, and process/resource isolation.

**Updates for Future:**

This is not implemented in the current version. However, it’s always efficient to update our code with additional functionalities from time to time. I believe one such feature that I could add to this Process Manager in the future is Collecting user feedback and iterating on the project to improve usability and fix any issues that arise in real-world usage.

**Installation and Use**

**Prerequisites:**

-   **Python is required on your local machine.**

**Clone the Repository:**

-   **gh repo clone dravyaaa/CMPSC472-PROJECT1**

**Navigate to the Project Directory:**

-   **In the terminal, users should navigate to the directory where the project was cloned:**
    -   **cd your-repo**

**Install Dependencies:**

-   **Tkinter:**
    -   **macOS:**
        -   **Tkinter is pre-installed with macOS's system Python.**
    -   **Windows:**
        -   **It should already be installed.**

**Run the Process Manager:**

-   **python main.py**

**Description**

-   **create_process():**
    -   This function is called when the user wants to create a new process.
    -   It retrieves the program name, arguments, and priority from the user input fields in the GUI.
    -   It validates the program name and arguments for safety.
    -   If the inputs are valid, it creates a new process using the subprocess.Popen() method, redirecting its standard output and error to pipes.
    -   Information about the process, including its priority, is stored in the processes dictionary using its PID as the key.
-   **is_safe_program_name(program_name):**
    -   This function is used to check if a program name is safe.
    -   It ensures that the program name contains only alphanumeric characters and underscores and doesn't contain special characters, spaces, or other disallowed characters.
-   **is_safe_argument(argument):**
    -   This function checks if an argument is safe.
    -   It ensures that the argument contains only alphanumeric characters and underscores and doesn't contain special characters, spaces, or other disallowed characters.
-   **drop_privileges():**
    -   This function is meant to drop privileges and run the process with reduced rights.
    -   It should include code to change the user and group under which the process runs. However, in the provided code, this function is incomplete.
-   **list_processes():**
    -   This function is called when the user wants to list running processes.
    -   It displays information about the currently running processes and threads in the GUI.
-   **terminate_process():**
    -   This function is called when the user wants to terminate a specific process by entering its PID.
    -   It terminates the process associated with the provided PID if it exists.
-   **create_thread():**
    -   This function is used to create a new thread within a specified process.
    -   It takes the process's PID as input and creates a new thread in that process.
-   **worker(thread_id, pid):**
    -   This is a function that represents a worker thread's work.
    -   It increments a shared variable in the specified process.
-   **multiprocessing_process(pipe, shared_variable):**
    -   This function is intended for multiprocessing and is similar to the worker() function.
    -   It increments a shared variable and sends a message via a pipe.
-   **signal_handler(sig, frame):**
-   This function is a signal handler to handle termination signals, such as Ctrl+C.
-   It logs a message and exits the application gracefully.

  ![Screenshot (485)](https://github.com/dravyaaa/CMPSC472-PROJECT1/assets/107662465/dc7f8984-dd02-462f-ba6b-363aa175c6b9)
![Screenshot (486)](https://github.com/dravyaaa/CMPSC472-PROJECT1/assets/107662465/543c5df3-6e92-45d3-9664-93b938046704)
![Screenshot (487)](https://github.com/dravyaaa/CMPSC472-PROJECT1/assets/107662465/c935994c-01ef-4d41-8c26-3a54bbb6a6f4)


    **Discussion**

    **Process Creation and Management:**

    The project implemented a process creation mechanism using system calls like fork and exec. This allows users to create new processes efficiently, expanding the system's capabilities. The ability to list, terminate, and monitor running processes enhances the project's management functionalities. Users can obtain essential information about each process, such as its unique Process ID (PID), parent process ID, and current state.

    **Thread Support and Synchronization:**

    One of the project's notable achievements is its support for multiple threads within a process. It includes thread creation, termination, and synchronization mechanisms using system calls like pthread_create and synchronization primitives such as mutexes and semaphores. These features enable concurrent execution within processes and mitigate synchronization issues like data races.

    **Inter-Process Communication (IPC):**

    The project tackled Inter-Process Communication (IPC) efficiently. It introduced various IPC mechanisms, including message passing, shared memory, and pipes, using relevant system calls like pipe, msgget, and shmget. This allows processes and threads to communicate and share data effectively, promoting collaboration and data exchange.

    **Command-Line and Graphic User Interface (GUI):**

    The project addressed user accessibility by providing a user-friendly interface. Users can interact with the Process Manager through Graphic User Interface (GUI). The project's flexibility offers commands for process and thread management, synchronization, and IPC operations, alongside clear and informative command syntax, and options.

    **Skills Gained:**

    Working on this project acquired a multitude of skills. It helped become proficient in process and thread manipulation, enabling to exploit system calls for process and thread control effectively. Additionally, it helped develop the skill of creating a software system that operates reliably, reducing resource conflicts. This skill ensures that the system runs efficiently and without disruptions.

    In conclusion, the project successfully met its objectives, which were to create an advanced Process Manager equipped with powerful process synchronization capabilities. The project's results are significant in terms of process and thread management, inter-process communication, and user accessibility. The Process Manager is a valuable tool for various applications as well as learning about how systems processing works in a high intensity environment.
