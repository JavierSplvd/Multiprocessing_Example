import os
import time
from multiprocessing import Process

from Tool.Print_Information_Example import print_process_information

if __name__ == '__main__':
    # Preparing the paths for the .py and the output
    cwd = os.getcwd().replace("\\", "/")
    path = "\Multiprocessing_Example\Tool\Print_Information_Example.py"
    path = path.replace("\\", "/")
    # Create all the processes with the function to run
    jobs = []
    start_time = time.time()
    for i in range(20):
        p = Process(target=print_process_information,
                    args=[str(i), cwd + "\Multiprocessing_Example\Tool\\" + "Result_" + str(i)])
        p.start()
        jobs.append(p)
    print("\n")
    print("\n")

    # Wait until all the process have terminated
    for j in jobs:
        j.join()

    elapsed_time = time.time() - start_time
    print("Final elapsed time: " + str(elapsed_time))
