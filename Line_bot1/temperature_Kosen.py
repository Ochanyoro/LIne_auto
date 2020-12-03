import pyautogui
import time as t
from datetime import datetime,time
from password import *
def send_temp():

    now = datetime.now().time()
    time1 = time(hour=6, minute=00,second=00)
    time2 = time(hour=12, minute=00, second=00)
    if (now>time1 and now<time2):
        #クロームを開く
        pyautogui.moveTo(35,483)
        pyautogui.click()
        t.sleep(2)

        #ラインを開く
        pyautogui.moveTo(1801,95)
        pyautogui.click()
        t.sleep(3)

        #lineのpasswordを入力
        password = PASSWORD
        pyautogui.write(password,interval=0.25)
        pyautogui.moveTo(992,631)
        pyautogui.click()
        #pyautogui.keyDown("enter")
        t.sleep(3)

        #lineが開いたらbotページに移動
        pyautogui.moveTo(729,377)
        pyautogui.click()
        pyautogui.write("bot")
        t.sleep(1)
        pyautogui.moveTo(732,436)
        pyautogui.click()

        #urlの検索
        pyautogui.moveTo(1343,380)
        pyautogui.click()
        pyautogui.moveTo(1292,503)
        pyautogui.click()
        t.sleep(5)
        pyautogui.moveTo(799,413)
        pyautogui.click()
        t.sleep(2)

        #Teamsの検温
        pyautogui.moveTo(686,592)
        pyautogui.click()
        pyautogui.write("36.3")
        pyautogui.moveTo(714,927)
        pyautogui.click()
        t.sleep(3)

        #ウィンドウの削除
        pyautogui.moveTo(1897,57)
        pyautogui.click()
        return 1

    else:
        t.sleep(180)
        return 0




def main():
    """
    currentMouseX,currentMouseY = pyautogui.position()
    print("currentMouseX:{} currentMouseY:{}".format(currentMouseX,currentMouseY))
    """
    """
    now = datetime.now().time()
    time1 = time(hour=10, minute=35, second=00)
    time2 = time(hour=10, minute=35, second=59)
    if (now>time1 and now<time2):
        print("hello")
    """

    i=0
    while(i==0):
         i=send_temp()


if __name__=="__main__":
    main()
