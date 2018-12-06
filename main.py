import csv
import sys
from random import choice
from time import sleep

def q():
    """
    Shortcut and lower all letters from user-input
    """
    # get user-input
    req = input(">>> ")
    # lower letters
    req = req.lower()
    return req

def setDialog(file):
    category=[]
    command=[]
    query=[]
    answers=[]
    
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


if __name__ == "__main__":
    
    while True:
        # FONKSIYONLAR
        dialog  = setDialog("robin_answers.csv")
        request = q()
        for query in dialog["query"]: 
            qinq = query.split("|") 
            for cont in qinq:
                if(request == cont):
                    mAns = choice(dialog["answer"][dialog["query"].index(query)])
                    print(f"ANS : {mAns}")
                    if(dialog["command"][dialog["query"].index(query)]!="0"):
                        sleep(2)
                        exec(dialog["command"][dialog["query"].index(query)])

                     
