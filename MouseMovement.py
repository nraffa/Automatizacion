#https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679
#chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=4%20Basic%20Python%20Tips%20to%20Automate%20Your%20Workflow%20-%20Better%20Programming%20-%20Medium&pos=4513&uri=https://medium.com/better-programming/4-basic-python-tips-to-automate-your-workflow-befabe140b83

import pyautogui
import time 

print pyautogui.size()
def foo():
    print time.ctime()
while True: 
    foo()
    pyautogui.moveTo(150,100, duration = 2)
    time.sleep(25)
    pyautogui.moveTo(100,150, duration = 2)