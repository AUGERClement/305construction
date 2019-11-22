#!/usr/bin/env python3

class Task:
    def __init__(self, lineTask = []):
        self.tag = []
        self.name = []
        self.duration = 0
        self.earlyTime = 0
        self.flexibility = 0
        self.earlyEnd = 0
        self.prerequitesTags = []
        self.prerequites = []
        self.lineParser(lineTask)

    def lineParser(self, lineTask):
        datas = lineTask.split(";")

        if len(datas) < 3:
            quit(84)
        self.tag = datas[0]
        self.name = datas[1]
        try:
            self.duration = int(datas[2])
        except:
            quit(84)
        self.prerequitesTags = datas[3:]

    def fillPrerequites(self, tasks):
        for prerequiteTag in self.prerequitesTags:
            for task in tasks:
                if prerequiteTag == task.tag:
                    self.prerequites.append(task)

    def printBeginDate(self):
        print(self.tag, end=' ')
        print("must begin ", end='')

        if (self.flexibility == 0):
            print("at t=", self.earlyTime, sep='')
        else:
            print("between t=", self.earlyTime, " and t=", self.earlyTime + self.flexibility, sep='')
            
    def printGanttChar(self):
        print(self.tag, end='\t')
        print("(", self.flexibility, ")", sep="", end='\t')
        
        print(" " * self.earlyTime, end='')
        print("=" * self.duration)