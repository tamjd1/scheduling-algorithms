import json


def run(tasks=None):
    if not tasks:
        num_tasks = int(input("\n[EDD] How many tasks? "))

        tasks = []

        for i in range(1, num_tasks+1):
            computation = int(input("[EDD] What is the worst case computation time for task {}? ".format(i)))
            deadline = int(input("[EDD] What is the deadline for task {}? ".format(i)))
            tasks.append({"task_num": i, "computation": computation, "deadline": deadline})

    # sort tasks by deadline
    sorted_tasks = sorted(tasks, key=lambda x: x["deadline"])

    # determine total computation time and lateness
    total_computation_time = 0
    tasks_lateness = []
    max_lateness = 0
    schedule_feasible = True
    for task in sorted_tasks:
        total_computation_time += task["computation"]
        lateness = total_computation_time-task["deadline"]
        tasks_lateness.append({"task_num": task["task_num"], "lateness": lateness})
        if lateness > 0:
            schedule_feasible = False
            if max_lateness < lateness:
                max_lateness = lateness

    # print task lateness
    print("[EDD] Task lateness:")
    print(json.dumps(tasks_lateness, indent=4))
    print()

    if not schedule_feasible:  # schedule not feasible, print message and max lateness
        print("[EDD] Schedule is not feasible")
        late_tasks = list(filter(lambda x: x["lateness"] > 0, tasks_lateness))
        nums = []
        latenesses = []
        for t in late_tasks:
            nums.append(t["task_num"])
            latenesses.append(t["lateness"])
        if len(nums) > 1:
            print("[EDD] Tasks {} have lateness of {}, respectively".format(nums, latenesses))
        else:
            print("[EDD] Task {} has lateness of {}".format(nums[0], latenesses[0]))

        print("[EDD] Max lateness is {}".format(max_lateness))
        print()

    else:  # schedule feasible, print schedule
        print("[EDD] Schedule is feasible")
        start = 0
        finish = 0
        schedule = []
        for task in sorted_tasks:
            task_num = task["task_num"]
            deadline = task["deadline"]
            finish += task["computation"]
            schedule.append({"task_num": task_num, "start": start, "finish": finish, "deadline": deadline})
            start = finish

        print("[EDD] Task schedule based on Earliest Due Date algorithm:")
        print(json.dumps(schedule, indent=4))
        print()

        _schedule = []
        for x in schedule:
            for i in range(x["start"], x["finish"]):
                _schedule.append({"time": i+1, "task": x["task_num"]})

        # print(json.dumps(_schedule, indent=4))

        # visualize schedule
        interval = 10 if len(_schedule) >= 10 else 5
        x_axis_tasks = " |" + ".".join(["0"+str(x["task"]) if x["task"] else "NA" for x in _schedule])
        x_axis_line = "-|--" + "--".join(["." for _ in _schedule])
        x_axis_labels = " 0  " + "  ".join([str(x["time"]) if x["time"] % interval == 0 else "" if x["time"] % 11 == 0 else " " for x in _schedule])
        print(" | TASK SCHEDULE BASED ON EARLIEST DUE DATE ALGORITHM")
        print(x_axis_tasks)
        print(x_axis_line)
        print(x_axis_labels)


if __name__ == '__main__':
    __tasks_fail = [
        {"task_num": 1, "computation": 1, "deadline": 2},
        {"task_num": 2, "computation": 2, "deadline": 5},
        {"task_num": 3, "computation": 1, "deadline": 4},
        {"task_num": 4, "computation": 4, "deadline": 8},
        {"task_num": 5, "computation": 2, "deadline": 6},
        {"task_num": 6, "computation": 3, "deadline": 9},
    ]
    __tasks_success = [
        {"task_num": 1, "computation": 1, "deadline": 2},
        {"task_num": 2, "computation": 2, "deadline": 5},
        {"task_num": 3, "computation": 1, "deadline": 4},
        {"task_num": 4, "computation": 1, "deadline": 8},
        {"task_num": 5, "computation": 2, "deadline": 6}
    ]
    _tasks = __tasks_success
    import sys
    args = sys.argv
    if len(args) >= 2:
        schedule_type = args[1]
        if schedule_type == "valid":
            _tasks = __tasks_success
        elif schedule_type == "invalid":
            _tasks = __tasks_fail

    run(_tasks)

