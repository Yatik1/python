import time

waitTime = 1
maxTries = 5
attempts = 0

while attempts < maxTries:
    print("Attemps" , attempts+1 , " : wait time" , waitTime)
    time.sleep(waitTime)
    waitTime*=2
    attempts+=1