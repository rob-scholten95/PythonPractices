import os
import datetime
import csv

projectList = "F:/1-Development/3-Python/ProjectOrganizer/projectlist.csv"

title = "Project 1"
path = f"F:/1-Development/4-Projects/{title}"
date = datetime.datetime.now()


def CreateProjectFolder():
    try:
        date = datetime.datetime.now()
        path = f"F:/1-Development/4-Projects/{title}"
        os.mkdir(path)
        print(f"Project folder Created by the name of {title}")
    except FileExistsError:
        print("Folder already Exists!")
        

try:
    os.path.isfile(projectList)
    print("projectlist found!")    
    with open('projectlist.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, path ,date]) 
        file.close()
    CreateProjectFolder()

except FileNotFoundError:
    print("projectlist file not found!")
    



   
    









