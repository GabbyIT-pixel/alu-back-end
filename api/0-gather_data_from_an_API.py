#!/usr/bin/python3
"""
Using a REST API, and a given emp_ID, return info about their TODO list.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee data
    employee = requests.get(f"{base_url}/users/{emp_id}").json()
    employee_name = employee.get("name")

    # Get todos
    todos = requests.get(f"{base_url}/todos?userId={emp_id}").json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # First line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        len(done_tasks),
        total_tasks
    ))

    # Completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
