import pyautogui as py
import random
import time
time.sleep(5)
mensagens=["Bom dia","como se ta","vai toma no cu","Quem?","Te perguntou","Olá","Que grande pauzao voce tem","viado","real real redpiill"]
for i in range (25):
    msg = random.choice(mensagens)
    py.write(msg)
    py.press('enter')
    time.sleep(1)