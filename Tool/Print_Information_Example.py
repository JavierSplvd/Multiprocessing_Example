import os
import time

import pandas


def print_process_information(title, output_path):
    start_time = time.time()
    # Print the process information
    print("Process number: " + title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    # sleep() function is called to simulate a heavy calculation
    time.sleep(3)
    csv = pandas.DataFrame()
    csv.to_csv(output_path + ".csv")
    # Print the elapsed time
    elapsed_time = time.time() - start_time
    print("Process: " + title + " elapsed time: " + str(elapsed_time))
    print("\n")
    print("\n")
