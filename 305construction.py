#!/usr/bin/env python3

from yard import Yard
from task import Task
from sys import argv

def parser():
    yard = Yard()
    taskList = []

    if (len(argv) != 2):
        quit(84)

    try:
        with open(argv[1], "r") as file:
            taskList = [line.strip() for line in file]
    except:
        quit(84)

    [yard.tasks.append(Task(x)) for x in taskList]

    return yard

def main():
    yard = parser()

    yard.fillPrerequitesTaskFromYard()
    yard.findFirstTasks()
    yard.algo()
    yard.printYard()

if __name__ == "__main__":
    main()