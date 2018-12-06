# -*- coding: utf-8 -*-
#Robin kütüphanesi
def list_functions(file):
    import csv    
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def setDialog(file):
    query    = []
    command  = []
    answers  = []
    
    with open(file, newline='') as File:  
        reader = csv.DictReader(File)
        for row in reader:
            query.append(row["query"])
            command.append(row["command"])
            answers.append(row["answer"].split("|"))
    mDialog = {"query"   : query,
               "command" : command,
               "answer"  : answers}
    return mDialog

def add_function(file):
    import csv
    newquery = input("Please input the query you want to add: ")
    newcom = input("Please input the Python command or command file you want to add\n(if command file doesn't exist, leave blank!)")
    newans = input("Please input the answer of this function: ")
    with open(file, 'a') as f:
        if(newcom=="" or newcom==" "): 
            newcom="0"
        thewriter=csv.writer(f)
        thewriter.writerow([newquery, newcom, newans])
        print("Your new function has been added!")
        f.close()