#!/usr/bin/env python3

from task import Task

class Yard:
    def __init__(self, tasks = []):
        self.tasks = tasks
        self.firstTasks = []
        self.duration = 0

    def fillPrerequitesTaskFromYard(self):
        for task in self.tasks:
            task.fillPrerequites(self.tasks)

    def findFirstTasks(self):
        for task in self.tasks:
            if not task.prerequites:
                self.firstTasks.append(task)

    def algoPath(self, task, startTask, path=[]):
        path = path + [task]
        if startTask == task:
            return [path]
        if task not in self.tasks:
            return []
        paths = []
        for node in task.prerequites:
            if node not in path:
                newpaths = self.algoPath(node, startTask, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def newTask(self, task):
        length = 0
        paths = []
        tmp = []
        for startTask in self.firstTasks:
            tmp = self.algoPath(task, startTask)
            if tmp: paths += tmp
        for path in paths:
            duration = 0
            for loc in path[1:]:
                duration += loc.duration
            tmp = duration
            if tmp > length: length = tmp
        return length

    def putFloat(self, duration):
        for task in self.tasks:
            next_time = duration
            for current in self.tasks:
                if task in current.prerequites and next_time > current.earlyTime:
                    next_time = current.earlyTime
            task.flexibility = next_time - task.earlyEnd

    def findDuration(self):
        duration = 0
        for task in self.tasks:
            task.earlyTime = self.newTask(task)
            task.earlyEnd = task.earlyTime + task.duration
            if (task.earlyEnd > duration):
                duration = task.earlyEnd
        self.putFloat(duration)
        self.duration = duration

    def algo(self):
        self.findDuration()
        self.tasks = sorted(self.tasks, key=lambda elem: (elem.earlyTime, elem.duration, elem.flexibility))

    def printYard(self):
        print("Total duration of construction:", self.duration, "weeks")
        print()

        for task in self.tasks:
            task.printBeginDate()
        
        print()

        for task in self.tasks:
            task.printGanttChar()