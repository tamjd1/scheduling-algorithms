"""
@author: Taha Amjad
@date: April 2020
Usage: python main.py
"""

import edd
import edf
import rm
import ce

if __name__ == '__main__':
    while True:
        message = "\nPlease choose an algorithm below:"
        message += "\nFor Earliest Due Date type EDD"
        message += "\nFor Earliest Deadline First type EDF"
        message += "\nFor Cyclic Executive type CE"
        message += "\nFor Rate Monotonic type RM"
        message += "\nTo exit the application, hit Enter"
        print(message)
        algorithm = input()
        if len(algorithm) == 0:
            print("Goodbye!")
            break

        try:
            eval(algorithm.lower()).run()
        except:
            print("{} is not a valid option".format(algorithm))
            print("Goodbye!")
            break
