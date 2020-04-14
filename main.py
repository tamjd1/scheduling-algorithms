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
        message += "\nFor Earliest Due Date enter EDD"
        message += "\nFor Earliest Deadline First enter EDF"
        message += "\nFor Cyclic Executive enter CE"
        message += "\nFor Rate Monotonic enter RM"
        print(message)
        algorithm = input()

        try:
            eval(algorithm.lower()).run()
        except:
            print("{} is not a valid option".format(algorithm))
            print("Goodbye!")
            break
