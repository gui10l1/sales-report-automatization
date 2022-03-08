import pyautogui
import pyperclip
import time
import pandas as pd

COMPANY_SERVER_URL = ''
FILE_PATH = r"C:\File\Path\fileName.xlsx"
MAIL_SERVICE_URL = 'https://mail.google.com/mail/u/0/#inbox'
EMAIL_TO = 'pythonimpressionador+diretoria@gmail.com'

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy(COMPANY_SERVER_URL)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(4)

pyautogui.click(x=360, y=270, clicks=2)

time.sleep(2)

pyautogui.click(x=355, y=336)

time.sleep(1)

pyautogui.click(x=1158, y=157)
pyautogui.click(x=1006, y=531)

time.sleep(1)

pyautogui.press('enter')

time.sleep(5)

tableRead = pd.read_excel(FILE_PATH)

total = tableRead['Valor Final'].sum()
quantity = tableRead['Quantidade'].sum()

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy(MAIL_SERVICE_URL)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=84, y=171)

time.sleep(1)

pyautogui.write(EMAIL_TO)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Relatorio de vendas')
pyautogui.press('tab')

text = """Prezados, bom dia

O faturamento de ontem foi de: R$ {:,.2f}
A quantidade de vendas foi de: {}

Abs

GuiPython
""".format(total, quantity)

pyperclip.copy(text)
pyautogui.hotkey('ctrl', 'v')

pyautogui.hotkey('ctrl', 'enter')
