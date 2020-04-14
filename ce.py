import json
import numpy as np


def run(tasks=None):
    if not tasks:
        num_tasks = int(input("\n[CE] How many tasks? "))

        tasks = []

        for i in range(1, num_tasks+1):
            computation = int(input("[CE] What is the worst case computation time for task {}? ".format(i)))
            period = int(input("[CE] What is the period for task {}? ".format(i)))
            tasks.append({"task_num": i, "computation": computation, "period": period})

    periods = [task["period"] for task in tasks]

    gcd = int(np.gcd.reduce(periods))
    lcm = int(np.lcm.reduce(periods))

    print("[CE] Minor Cycle (GCD): {}".format(gcd))
    print("[CE] Major Cycle (LCM): {}".format(lcm))

    total_computation = sum([task["computation"] for task in tasks])

    if total_computation > gcd:
        print("[CE] Schedule is not feasible")
        print("[CE] Total task computation ({}) will not fit into minor cycle ({})".format(total_computation, gcd))
    else:
        print("[CE] Schedule is feasible")
        print("[CE] Total task computation ({}) will fit into minor cycle ({})".format(total_computation, gcd))

        schedule = []

        task_lookup = {
            task["task_num"]: {"computation": task["computation"], "period": task["period"]}
            for task in tasks
        }

        task_computation = {k: 0 for k in task_lookup}
        completed_task_nums = []
        for i in range(1, lcm+1):
            current_tasks = list(filter(lambda x: x["task_num"] not in completed_task_nums and (x["computation"]-task_computation[x["task_num"]]) <= gcd-(i%gcd), tasks))
            sorted_tasks = sorted(current_tasks, key=lambda x: x["period"])
            task_num = None
            for task in sorted_tasks:
                task_num = task["task_num"]
                break

            schedule.append({"time": i, "task": task_num})
            schedule.append({"time": i+lcm, "task": task_num})
            if task_num:
                task_computation[task_num] += 1
                if task_computation[task_num] == task_lookup[task_num]["computation"]:
                    completed_task_nums.append(task_num)

            if i % gcd == 0:
                for _task_num in task_lookup:
                    if i >= task_lookup[_task_num]["period"]:
                        completed_task_nums.remove(_task_num)
                        task_computation[_task_num] = 0

        sorted_schedule = sorted(schedule, key=lambda x: x["time"])

        print("[CE] Task schedule based on Cyclic Executive algorithm:")
        print(json.dumps(sorted_schedule, indent=4))
        print()

        # visualize schedule
        x_axis_tasks = " |" + ".".join(["0"+str(x["task"]) if x["task"] else "NA" for x in sorted_schedule])
        x_axis_line = "-|--" + "--".join(["." for _ in sorted_schedule])
        x_axis_labels = " 0  " + "  ".join([str(x["time"]) if x["time"] % 10 == 0 else "" if x["time"] % 11 == 0 else " " for x in sorted_schedule])
        print(" | TASK SCHEDULE BASED ON CYCLIC EXECUTIVE ALGORITHM")
        print(x_axis_tasks)
        print(x_axis_line)
        print(x_axis_labels)


if __name__ == '__main__':
    __tasks_fail = [
        {"task_num": 1, "computation": 20, "period": 10},
        {"task_num": 2, "computation": 20, "period": 20},
        {"task_num": 3, "computation": 50, "period": 30}
    ]
    __tasks_success = [
        {"task_num": 1, "computation": 5, "period": 10},
        {"task_num": 2, "computation": 2, "period": 10},
        {"task_num": 3, "computation": 2, "period": 20}
    ]
    # _tasks = __tasks_fail
    _tasks = __tasks_success
    run(_tasks)
