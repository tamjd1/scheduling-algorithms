import json


def run(tasks=None):
    if not tasks:
        num_tasks = int(input("\n[EDF] How many tasks? "))

        tasks = []

        for i in range(1, num_tasks+1):
            arrival = int(input("[EDF] What is the arrival time for task {}? ".format(i)))
            computation = int(input("[EDF] What is the worst case computation time for task {}? ".format(i)))
            deadline = int(input("[EDF] What is the deadline for task {}? ".format(i)))
            tasks.append({"task_num": i, "arrival": arrival, "computation": computation, "deadline": deadline})

    # # sort tasks by arrival time, then deadline
    # sorted_tasks = sorted(tasks, key=lambda x: (x["arrival"], x["deadline"]))

    completed_task_nums = []
    total_computation_time = 0
    existing_arrived_tasks = []
    sorted_tasks = []
    task_timeline = []
    task_completed_computation = {}

    while True:  # keep looping until all tasks have completed
        new_arrived_tasks = list(filter(lambda x: x["arrival"] == total_computation_time and x["task_num"] not in completed_task_nums, tasks))
        if new_arrived_tasks:
            arrived_tasks = existing_arrived_tasks + new_arrived_tasks
            sorted_tasks = sorted(arrived_tasks, key=lambda x: x["deadline"])

        current_task = sorted_tasks[0]
        task_num = current_task["task_num"]

        total_computation_time += 1
        task_timeline.append({"time": total_computation_time, "task": task_num})

        if task_num in task_completed_computation:
            task_completed_computation[task_num] += 1
        else:
            task_completed_computation[task_num] = 1

        if int(current_task["computation"]) == task_completed_computation[task_num]:
            del sorted_tasks[0]
            completed_task_nums.append(task_num)

        existing_arrived_tasks = sorted_tasks

        if len(completed_task_nums) == len(tasks):
            break

    # print(json.dumps(task_timeline, indent=4))

    task_lookup = {
        task["task_num"]: {"arrival": task["arrival"], "computation": task["computation"], "deadline": task["deadline"]}
        for task in tasks
    }

    temp_tasks_lateness = {}
    max_lateness = 0
    schedule_feasible = True

    for x in task_timeline:
        task_num = x["task"]
        lateness = x["time"] - task_lookup[task_num]["deadline"]
        temp_tasks_lateness[task_num] = lateness
        if lateness > 0:
            schedule_feasible = False
            if max_lateness < lateness:
                max_lateness = lateness

    tasks_lateness = [{"task_num": k, "lateness": v} for k, v in temp_tasks_lateness.items()]

    # print task lateness
    print("[EDF] Task lateness:")
    print(json.dumps(tasks_lateness, indent=4))
    print()

    if not schedule_feasible:  # schedule not feasible, print message and max lateness
        print("[EDF] Schedule is not feasible")
        late_tasks = list(filter(lambda x: x["lateness"] > 0, tasks_lateness))
        nums = []
        latenesses = []
        for t in late_tasks:
            nums.append(t["task_num"])
            latenesses.append(t["lateness"])
        if len(nums) > 1:
            print("[EDF] Tasks {} have lateness of {}, respectively".format(nums, latenesses))
        else:
            print("[EDF] Task {} has lateness of {}".format(nums[0], latenesses[0]))

        print("[EDF] Max lateness is {}".format(max_lateness))
        print()

    else:  # schedule feasible, print schedule
        print("[EDF] Schedule is feasible")
        schedule = []
        for task_num in task_lookup:
            temp_task_timeline = list(filter(lambda x: x["task"] == task_num, task_timeline))
            deadline = task_lookup[task_num]["deadline"]
            start = temp_task_timeline[0]["time"] - 1
            finish = temp_task_timeline[-1]["time"]
            schedule.append({"task_num": task_num, "start": start, "finish": finish, "deadline": deadline})

        print("[EDF] Task schedule based on Earliest Deadline First algorithm:")
        print(json.dumps(schedule, indent=4))
        print()

        _schedule = {}
        for x in schedule:
            for i in range(x["start"], x["finish"]):
                _schedule[i+1] = x["task_num"]

        _schedule = [{"time": k, "task": v} for k, v in _schedule.items()]

        print(json.dumps(_schedule, indent=4))

        # visualize schedule
        interval = 10 if len(_schedule) >= 10 else 5
        x_axis_tasks = " |" + ".".join(["0"+str(x["task"]) if x["task"] else "NA" for x in _schedule])
        x_axis_line = "-|--" + "--".join(["." for _ in _schedule])
        x_axis_labels = " 0  " + "  ".join([str(x["time"]) if x["time"] % interval == 0 else "" if x["time"] % 11 == 0 else " " for x in _schedule])
        print(" | TASK SCHEDULE BASED ON EARLIEST DEADLINE FIRST ALGORITHM")
        print(x_axis_tasks)
        print(x_axis_line)
        print(x_axis_labels)


if __name__ == '__main__':
    __tasks_fail = [
        {"task_num": 1, "arrival": 0, "computation": 1, "deadline": 2},
        {"task_num": 2, "arrival": 0, "computation": 2, "deadline": 5},
        {"task_num": 3, "arrival": 2, "computation": 2, "deadline": 4},
        {"task_num": 4, "arrival": 3, "computation": 2, "deadline": 8},
        {"task_num": 5, "arrival": 6, "computation": 2, "deadline": 6}
    ]
    __tasks_success = [
        {"task_num": 1, "arrival": 0, "computation": 1, "deadline": 2},
        {"task_num": 2, "arrival": 0, "computation": 2, "deadline": 5},
        {"task_num": 3, "arrival": 2, "computation": 2, "deadline": 4},
        {"task_num": 4, "arrival": 3, "computation": 2, "deadline": 10},
        {"task_num": 5, "arrival": 6, "computation": 2, "deadline": 9}
    ]
    # _tasks = __tasks_fail
    _tasks = __tasks_success
    run(_tasks)
