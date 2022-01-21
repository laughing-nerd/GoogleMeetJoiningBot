import pyautogui as p
import time
l=[]
def joinMeeting():
    ret=0
    while(ret==0):
        if (p.locateCenterOnScreen('ask.png')!=None):
            coords=p.locateCenterOnScreen('ask.png')
            ret=1
        elif (p.locateCenterOnScreen('join.png')!=None):
            coords=p.locateCenterOnScreen('join.png')
            ret=1
        else:
            pass
    p.hotkey('ctrl','d')
    time.sleep(0.1)
    p.hotkey('ctrl','e')
    time.sleep(0.1)
    p.click(coords)

def rewriteSchedule():
    t=input("Enter the time when you want to join(Format = 15:00): ")
    l=input("Enter the link (or Copy Paste the link): ")
    f=open('read.txt','w')
    f.write('1 '+t+' '+l+' ')
    f.close()

def words():
    l.clear()
    f=open('read.txt','r')
    s=""
    for i in f.read():
        if (i!=' '):
            s=s+i
        else:
            l.append(s)
            s=""
    f.close()

words() #stores the words in a list
f=open('read.txt','r')
if (l[0]=='0'):
    f.close()
    rewriteSchedule()
else:
    f.close()
    pass

words()
timeCheck=0
while(timeCheck==0):
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    if (current_time==l[1]):
        timeCheck=1
p.press('win')
p.typewrite("Google Chrome")
p.press('enter')
time.sleep(1)
while(p.locateCenterOnScreen('search.png')==None):
    pass
p.typewrite(l[2])
p.press('enter')
joinMeeting()
p.alert("You have joined a meeting")
    
        
