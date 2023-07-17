import base64
import datetime
import os
import time
from selenium.webdriver import ChromeOptions
import pyautogui as pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

session = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'ReturnUrl': 'https://dash-ngs.net/NextGear/Enterprise/Module/User/uPostLogin.aspx',
}

data = {
    '__LASTFOCUS': '',
    'ScriptManager1_TSM': '',
    'RadStyleSheetManager_TSSM': ';Telerik.Web.UI, Version=2022.3.913.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en-US:3607a1d0-e85e-4622-a893-12dcc72b870c:d7e35272:505983de:3e0dfe6c;Telerik.Web.UI.Skins, Version=2022.3.913.45, Culture=neutral, PublicKeyToken=121fae78165ba3d4:en-US:bb82e71f-c29d-4777-a8a7-96ea48208159:83614c22',
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATEFIELDCOUNT': '2',
    '__VIEWSTATE': 'rcXKix31eXvePOlIc7Gr9RatIpcuz+7/5hDtCAKQyXlh7FCAew4pexxOjgal2924Z4l1u7XZ1USDGD/VZhSfuGshtVl83ZlHIgXsZ4Lv0Ws8sWIA3VD6X5Bf9H3gVehhjOmH2tlDASBQA9Lr5kxp0EYpRbhWQBUzP72IY7FbmuLmpsYx5wqwkpJJ0/2//eA4Xs69lCI1jK5rraa1y9pLNaCSccN6kyiEbMsf+VXQurKT95NjbVKSl+Ky2j4jagB5O+9pFSntdq4kZfUc4lotN63IlpBldyuw/CgtxqudWlW6299DqvzpplMULPrfiY1qlmEjXO9tdiAJ4lZ9nmA558CczmZ/wM+8+bRvy1E11i8K3zV+nNkyGQy+/oD93CK6KX6L6Fivp/8eZ42UFYmnkK5tmhw03AI5vNN6VjH06CAYvx92SLvktzWreJgW0ga0GmAXVKCOKcTLtBfPCPzGdUTxiLQR9jiK5icpUXgWu/geiEIHph0LqnUYjGzOeNifSXWM3r6VUGs4J/uGvflC4rDidN0I2yZh+DV+BfhKk1zFxy3qbcS+KzZPfNM/sPHiL9/fePASO/TpJHzoBZIGaR2Tp0qTs6/Lnq1ERRoEASfn3VT3JEtzmcDxTswqAICBhwNjBEV2Gd5cy9GgbQe9jkZjLPL6qEVs8HxQ2WFRCIlvn1P0SIHv+ala9S/Z5yRpE0LQdyG2n2gbHt2e/Msl0Dcd5BXugbkRKMQoYeEhq3dD/QGxEL1zIp7UwZJPF2LSSxOajeFIspA5ngiUXdTy+ZBf8jGg2i78fDLPvNXeT8YtuJJmgzY+WB40IxLF/qvg8lBrivciC/1TcHewxchH/z6+Iaakgl+z2W2L4uy+cW89NHdTRwPPyf73CP8Zt9Acyg7S+pqWrcfSrSYn/BZMgM2d53q2a1z1DgOKUNm6Xmqx5en0QKnJ2/n45m3esY/3KjHdRy3nXRHDpV6PffT5y3nkK17mQJYlcRDtnNFL',
    '__VIEWSTATE1': 'z5GXbeuGMYZSk+F/6DpzVGxprE0z+3B5bnze24sB11QNdOUfEDGmI0gnWfchshnq9UMnohd+YGmueNj3BxDgVkh/+m4XyA==',
    '__VIEWSTATEGENERATOR': '48969150',
    '__EVENTVALIDATION': 'RkFOQPr/YX1kvlqXHH8x23XA8L7M9nU+Vi9+FyVY8senphF+TDebPUlc1aLE2FD/uFBypxczSV2uAu34/0GkpHT4WqhrHOEvc9wh7VR26ggQzdCTgdvtx47W6wNooa3Dh1nPOE4sv/OjYeXqSVtI9xntGv85AeOSBnC2OLWP3dCOCt8Hqx4V6akPLwWTTkXc/rf/hQfMbj0l4lzjP5tLYz9li3kkS8L3kOXEq5yNXzmnaCfACs1i0apzzfSgOVXC3F5Y6BEF/p0i1A8o4YAy+KT77GeRNqSc+a384FQS6f7mwUl7tIvAAkxf8gwmRu04glLhX4wov0kazDNhTuFQGqIxrctNPmvUEkxnQEhWTDC5wr6/QiiUR0gPGRsM1DmIwgmx0A==',
    'ddlLanguage': 'en-US',
    'txtDashId': '5878669',
    'txtUserName': 'nick.feitser',
    'txtPassword': 'Eappng.222',
    'btnLogIn': 'Login',
    'MessageWindow_ClientState': '',
}

response = session.post(
    'https://dash-ngs.net/NextGear/Enterprise/Module/User/Login.aspx',
    params=params,
    # cookies=cookies,
    headers=headers,
    data=data,
)

# print(response.text)
print(response.status_code)



def get_options():
    options = ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')

    return options

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=get_options())
#driver = webdriver.Chrome("C:\\Users\\Administrator\\.wdm\\drivers\\chromedriver\\win32\\114.0.5735.90\\chromedriver.exe")

driver.get("https://dash-ngs.net/NextGear/Enterprise/Module/User/Login.aspx")

for cookie in session.cookies:
    driver.add_cookie({'name': cookie.name, 'value': cookie.value, 'domain': 'dash-ngs.net'})

driver.get("https://dash-ngs.net/NextGear/Enterprise/Module/Job/jJobSlideBoard.aspx?JobNumber=23-04-81110&JobId=7818120")
time.sleep(5)
try:
    driver.find_element(By.XPATH, '//*[@id="border-8e12580b-ca77-dce7-da5f-b4c19acedbb9"]').click()
    time.sleep(1)
except:
    pass


panel = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ctl00_ContentPlaceHolder1_dockJobTabs_C_tabStripJobTabsPanel")
lis = panel.find_elements(By.TAG_NAME, "li")
for li in lis:
    if li.text == "Documents":
        li.click()
        break

time.sleep(5)

upload_btn = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$dockJobTabs$C$Documents_userControl$Button_UploadDocuments")
upload_btn.click()
time.sleep(10)

iframe = driver.find_element(By.CSS_SELECTOR, "iframe[name='RadWindow_Common']")
driver.switch_to.frame(iframe)

folder_btn = driver.find_element(By.ID, "ddlFolders_Arrow")
folder_btn.click()

time.sleep(1)

driver.find_element(By.ID, "ddlFolders_DropDown").find_element(By.XPATH, "//li[text()='Permits and Plans']").click()
time.sleep(2)
val = '{"logEntries":[],"value":"116473186","text":"Permits and Plans","enabled":true,"checkedIndices":[],"checkedItemsTextOverflows":false}'
script = f"document.getElementById('ddlFolders_ClientState').value = '{val}';"

# Execute the JavaScript code
driver.execute_script(script)

time.sleep(3)

driver.find_element(By.CLASS_NAME, "ruFileWrap").click()
time.sleep(2)


pyautogui.write("C:\\Users\\Administrator\\Desktop\\scraper\\AnnualTraining.pdf")
pyautogui.press('enter')

time.sleep(10)

driver.find_element(By.NAME, "ButtonSave").click()

time.sleep(10)
