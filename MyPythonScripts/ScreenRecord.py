#! python3


#Import Modules
import os, webbrowser, pyautogui, time


# Specify code directory
os.chdir(r'C:\Users\ridel\Desktop\FedevelAcademy')

# Open Fedevel Academy Website in Chrome

# URL string formatting for each lesson
url=r'https://portal.fedevel.com/lessonDetail.html?dbid=1569757626596&lesnum={}&instrid=us-east-2_KpwYC7yK5:45f6c01d-ccc8-43e0-8f33-c5a70caf707f&boughtnum=2'

#Video Duration in Seconds
videolengths=[0, 0, 0, 0, 0, 0, 4823, 4107, 4444, 4230]



#Function to Navigate Website (Causing bugs, deactivating)
"""
def ScreenRecord():
    #Press Full Screen
    pyautogui.click(915,574)
    time.sleep(5)

    #Start Screen Record
    pyautogui.hotkey('win','alt','r')
    time.sleep(5)

    #Press "Start to Beginning" prompt
    pyautogui.click(714,655)

    #Wait for x sceonds to record whole lecture
    time.sleep(videolengths[i])

    #Stop Screen Record
    pyautogui.hotkey('win','alt','r')
"""

for i in range(6,10):
    
    #Open Lecutres
    urlLesson=url.format(i)
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(urlLesson)
    print(urlLesson)

    #Wait for page to load for 30 sec
    time.sleep(15)

    #Start Screen Recording
    
    #Press Full Screen
    pyautogui.click(915,574)
    time.sleep(5)

    #Start Screen Record
    pyautogui.hotkey('win','alt','r')
    time.sleep(5)

    #Press "Start to Beginning" prompt
    pyautogui.click(714,655)

    #Wait for x sceonds to record whole lecture
    time.sleep(videolengths[i])

    #Stop Screen Record
    pyautogui.hotkey('win','alt','r')
    
    #Close Tab
    pyautogui.hotkey('ctrl','w')
     
    


#Slam mouse to top left corner to cancel program anytime
