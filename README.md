# scheduling-algorithms
Scheduling algorithms for real time systems

### Prerequisites
* Python 3.7
* numpy==1.18.2

### Quick Start Guide
To run the application:
```bash
python main.py
```
You will be prompted to input one of the four algorithm options:
* `EDD` for Earliest Due Date
* `EDF` for Earliest Deadline First
* `CE` for Cyclic Executive
* `RM` for Rate Monotonic

Inputting anything else will exit the program.

Upon a valid input, you will be asked to enter the number of tasks to schedule along with their properties, such as computation time, arrival time, deadline, period, etc.
```bash
[RM] How many tasks? 3
[RM] What is the worst case computation time for task 1? 1
[RM] What is the period for task 1? 4
[RM] What is the worst case computation time for task 2? 2
[RM] What is the period for task 2? 6
[RM] What is the worst case computation time for task 3? 1
[RM] What is the period for task 3? 10
```

After entering all task details, the algorithm will determine whether your schedule is feasible or not. 

If it is feasible, it will print a visualization of the schedule in the form of a timeline.

```bash
 | TASK SCHEDULE BASED ON RATE MONOTONIC ALGORITHM
 |01.02.02.03.01.NA.02.02.01.NA.03.NA.01.02.02.NA.01.NA.02.02
-|--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.
 0                             10                            20
```
If the schedule is not feasible, it will output a message explaining why it is not feasible.
```bash
[RM] Upper bound for process utilization factor for 3 tasks is 0.7797631496846196
[RM] 7.523809523809524 <= 0.7797631496846196
[RM] The bound is not met, therefore, this schedule is not feasible
```

Alternatively, if you do not want to provide task details for algorithms, each algorithm script comes with a sample set of tasks for a feasible schedule case and a non-feasible schedule case. 

To use those sets of tasks, simply execute an algorithm script directly and enter `valid` or `invalid` as a command line argument to use the set of tasks which result in a valid schedule or invalid schedule (the default option is `valid`).

e.g.
```bash
$ python rm.py valid

 | TASK SCHEDULE BASED ON RATE MONOTONIC ALGORITHM
 |01.02.02.03.01.NA.02.02.01.NA.03.NA.01.02.02.NA.01.NA.02.02
-|--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.--.
 0                             10                            20

$ python rm.py invalid
[RM] Upper bound for process utilization factor for 3 tasks is 0.7797631496846196
[RM] 7.523809523809524 <= 0.7797631496846196
[RM] The bound is not met, therefore, this schedule is not feasible
```
