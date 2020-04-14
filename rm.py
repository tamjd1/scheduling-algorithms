import json


def run(tasks=None):
    if not tasks:
        num_tasks = int(input("\n[RM] How many tasks? "))

        tasks = []

        for i in range(1, num_tasks+1):
            computation = int(input("[RM] What is the worst case computation time for task {}? ".format(i)))
            period = int(input("[RM] What is the period for task {}? ".format(i)))
            tasks.append({"task_num": i, "computation": computation, "period": period})

    N = len(tasks)
    upper_bound = N*(2**(1/N) - 1)
    print("[RM] Upper bound for process utilization factor for {} tasks is {}".format(N, upper_bound))

    task_utilization_factor = sum([task["computation"]/task["period"] for task in tasks])

    schedule_feasible = True if task_utilization_factor <= upper_bound else False

    if not schedule_feasible:
        print("[RM] The bound is not met, therefore, this schedule is not feasible")
    else:
        print("[RM] The bound is met, therefore, this schedule is feasible")

        max_period = max([task["period"] for task in tasks])

        schedule = []

        task_lookup = {
            task["task_num"]: {"computation": task["computation"], "period": task["period"]}
            for task in tasks
        }

        task_computation = {k: 0 for k in task_lookup}
        completed_task_nums = []

        for i in range(1, (max_period*2)+1):
            current_tasks = list(filter(lambda x: x["task_num"] not in completed_task_nums, tasks))
            sorted_tasks = sorted(current_tasks, key=lambda x: x["period"])
            task_num = None
            for task in sorted_tasks:
                task_num = task["task_num"]
                break

            schedule.append({"time": i, "task": task_num})
            if task_num:
                task_computation[task_num] += 1
                if task_computation[task_num] == task_lookup[task_num]["computation"]:
                    completed_task_nums.append(task_num)

            for _task_num in task_lookup:
                if _task_num in completed_task_nums and i % task_lookup[_task_num]["period"] == 0:
                    completed_task_nums.remove(_task_num)
                    task_computation[_task_num] = 0

        sorted_schedule = sorted(schedule, key=lambda x: x["time"])

        print("[RM] Task schedule based on Rate Monotonic algorithm:")
        print(json.dumps(sorted_schedule, indent=4))
        print()

        # visualize schedule
        x_axis_tasks = " |" + ".".join(["0"+str(x["task"]) if x["task"] else "NA" for x in sorted_schedule])
        x_axis_line = "-|--" + "--".join(["." for _ in sorted_schedule])
        x_axis_labels = " 0  " + "  ".join([str(x["time"]) if x["time"] % 10 == 0 else "" if x["time"] % 11 == 0 else " " for x in sorted_schedule])
        print(" | TASK SCHEDULE BASED ON RATE MONOTONIC ALGORITHM")
        print(x_axis_tasks)
        print(x_axis_line)
        print(x_axis_labels)


if __name__ == '__main__':
    __tasks_fail = [
        {"task_num": 1, "computation": 20, "period": 100},
        {"task_num": 2, "computation": 40, "period": 150},
        {"task_num": 3, "computation": 100, "period": 350}
    ]
    __tasks_success = [
        {"task_num": 1, "computation": 1, "period": 4},
        {"task_num": 2, "computation": 2, "period": 6},
        {"task_num": 3, "computation": 1, "period": 10}
    ]
    # _tasks = __tasks_fail
    _tasks = __tasks_success
    run(_tasks)
