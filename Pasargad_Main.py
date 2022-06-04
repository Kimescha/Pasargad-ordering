import tkinter as tk
from tkinter import *
from tkinter import Tk, font
#
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import os
import sys
from selenium.webdriver.common.keys import Keys
#from selenium import org.openqa.selenium.support.ui.Select
#
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#
path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path, 'chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=address)
#initializing root
root = Tk()
root.geometry('+850+100')
root.configure(bg='goldenrod1')
root.defaultFont = font.nametofont("TkDefaultFont")
root.defaultFont.configure(family="B Nazanin", size = 11)
root.title("!به کارگزاری بانک پاسارگاد خوش آمدید")
root.geometry("375x500")
#
userField = '//*[@id="uid"]'
passField = '//*[@id="passwordInput"]'
capField = '//*[@id="cptch"]'
submit = '//*[@id="loginSmtBtn"]'
refreshcap = '//*[@id="captchaImage"]/a'

#LOGINS___________________________________________________________________________________________________________
def firstlogin():
    global second
    second = Toplevel()
    second.geometry('+750+100')
    second.configure(bg='goldenrod1')
    second.title("باز کردن صفحه ورود")
    refreshcap = '//*[@id="captchaImage"]/a'
    second.geometry("500x375") #500 * 250
    l4 = Label(second,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l4.pack(pady= 10)
    l1 = Label(second,  text = ":نام کاربری")
    l1.pack()
    text1 = Text(second , height = 2 , width = 20)
    text1.pack()
    l2 = Label(second, text = ":رمز عبور")
    l2.pack()
    text2 = Text(second , height = 2 , width = 20)
    text2.pack()
    l3 = Label(second ,text = ":کپچا")
    l3.pack()
    text3 = Text(second , height = 2 , width = 20)
    text3.pack()
    driver.switch_to.window("firsttab")
##############################################
    def ret1():
        inp1 = text1.get("1.0",'end-1c' )
        inp2 = text2.get("1.0",'end-1c' )
        inp3 = text3.get("1.0",'end-1c' )
        inp3 = int(inp3)
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_xpath(capField)
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        second.withdraw()
        time.sleep(3)
        it51 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'تنظیمات')]")))
        it51.click()
        time.sleep(0.25)
        it53 = driver.find_element_by_xpath("//input[starts-with(@id, 'checkbox-')]")
        check = it53.is_selected()
        if check == 1:
            it53.click()
        it66 = driver.find_element_by_xpath("//span[contains(text(), 'مدیریت سفارشات')]")
        it66.click()  
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    firstSave = Button(second , height = 1 , width = 15 , text = "اعمال تغییرات" , command=lambda: ret1())
    firstSave.pack(pady=10)
    l12 = Label(second,  text = ".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_dttsLogin_vecchio"]')))
    itt3.click()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#____________________________________________________________________________________________________
def secondlogin():
    global sixth
    sixth = Toplevel()
    sixth.geometry('+750+100')
    sixth.configure(bg='goldenrod1')
    sixth.title("باز کردن صفحه ورود")
    refreshcap = '//*[@id="captchaImage"]/a'
    sixth.geometry("500x375")
    l44 = Label(sixth,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l44.pack(pady= 10)
    l41 = Label(sixth,  text = ":نام کاربری")
    l41.pack()
    text21 = Text(sixth , height = 2 , width = 20)
    text21.pack()
    l29 = Label(sixth, text = ":رمز عبور")
    l29.pack()
    text22 = Text(sixth, height = 2 , width = 20)
    text22.pack()
    l33 = Label(sixth ,text = ":کپچا")
    l33.pack()
    text23 = Text(sixth, height = 2 , width = 20)
    text23.pack()
    driver.switch_to.window("secondtab")
##############################################
    def ret2(): 
        inp1 = text21.get("1.0",'end-1c' )
        inp2 = text22.get("1.0",'end-1c' )
        #inp1 = 'fa20030733'
        #inp2 = 'w7HbJHFW'
        inp3 = text23.get("1.0",'end-1c' )
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_xpath(capField)
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        sixth.withdraw()
        time.sleep(3)
        it51 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'تنظیمات')]")))
        it51.click()
        time.sleep(0.25)
        it53 = driver.find_element_by_xpath("//input[starts-with(@id, 'checkbox-')]")
        check = it53.is_selected()
        if check == 1:
            it53.click()
        it66 = driver.find_element_by_xpath("//span[contains(text(), 'مدیریت سفارشات')]")
        it66.click()
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    secondSave = Button(sixth , height = 1 , width = 15 , text = "اعمال تغییرات", command=lambda: ret2())
    secondSave.pack(pady=10)
    l12 = Label(sixth,  text = ".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_dttsLogin_vecchio"]')))
    itt3.click()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#_________________________________________________________________________________________________________________________
def thirdlogin():
    global seventh
    seventh = Toplevel()
    seventh.geometry('+750+100')
    seventh.configure(bg='goldenrod1')
    seventh.title("باز کردن صفحه ورود")
    refreshcap = '//*[@id="captchaImage"]/a'
    seventh.geometry("500x375")
    l44 = Label(seventh,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l44.pack(pady= 10)
    l41 = Label(seventh,  text = ":نام کاربری")
    l41.pack()
    text21 = Text(seventh , height = 2 , width = 20)
    text21.pack()
    l29 = Label(seventh, text = ":رمز عبور")
    l29.pack()
    text22 = Text(seventh, height = 2 , width = 20)
    text22.pack()
    l33 = Label(seventh ,text = ":کپچا")
    l33.pack()
    text23 = Text(seventh, height = 2 , width = 20)
    text23.pack()
    driver.switch_to.window("thirdtab")
##############################################
    def ret3(): 
        inp1 = text21.get("1.0",'end-1c' )
        inp2 = text22.get("1.0",'end-1c' )
        inp3 = text23.get("1.0",'end-1c' )
        inp3 = int(inp3)
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_xpath(capField)
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        seventh.withdraw()
        time.sleep(3)
        it51 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'تنظیمات')]")))
        it51.click()
        time.sleep(0.25)
        it53 = driver.find_element_by_xpath("//input[starts-with(@id, 'checkbox-')]")
        check = it53.is_selected()
        if check == 1:
            it53.click()
        it66 = driver.find_element_by_xpath("//span[contains(text(), 'مدیریت سفارشات')]")
        it66.click()
        #
        inp1 = 0
        inp2 = 0 
        inp3 = 0
    #login buttons
    thirdSave = Button(seventh , height = 1 , width = 15 , text = "اعمال تغییرات" , command=lambda: ret3())
    thirdSave.pack(pady=10)
    l12 = Label(seventh,  text = ".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_dttsLogin_vecchio"]')))
    itt3.click()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#_________________________________________________________________________________________________________________________
def fourthlogin():
    global eighth
    eighth = Toplevel()
    eighth.geometry('+750+100')
    eighth.configure(bg='goldenrod1')
    eighth.title("باز کردن صفحه ورود")
    refreshcap = '//*[@id="captchaImage"]/a'
    eighth.geometry("500x375")
    l44 = Label(eighth,  text =  ".لطفا بعد از وارد کردن موارد مورد نظر، دکمه اعمال تغییرات را بفشارید")
    l44.pack(pady= 10)
    l41 = Label(eighth,  text = ":نام کاربری")
    l41.pack()
    text21 = Text(eighth , height = 2 , width = 20)
    text21.pack()
    l29 = Label(eighth, text = ":رمز عبور")
    l29.pack()
    text22 = Text(eighth, height = 2 , width = 20)
    text22.pack()
    l33 = Label(eighth ,text = ":کپچا")
    l33.pack()
    text23 = Text(eighth, height = 2 , width = 20)
    text23.pack()
    driver.switch_to.window("fourthtab")
##############################################
    def ret4(): 
        inp1 = text21.get("1.0",'end-1c' )
        inp2 = text22.get("1.0",'end-1c' )
        #inp1 = 'fa20030733'
        #inp2 = 'w7HbJHFW'
        inp3 = text23.get("1.0",'end-1c' )
        #xpath(ONLINE PLUS SYSTEM)
        driver.find_element_by_xpath(userField).send_keys(inp1)
        driver.find_element_by_xpath(passField).send_keys(inp2)
        itt3 = driver.find_element_by_xpath(capField)
        itt3.send_keys(inp3)
        itt3.send_keys(Keys.ENTER)
        eighth.withdraw()
        time.sleep(3)
        it51 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'تنظیمات')]")))
        it51.click()
        time.sleep(0.25)
        it53 = driver.find_element_by_xpath("//input[starts-with(@id, 'checkbox-')]")
        check = it53.is_selected()
        if check == 1:
            it53.click()
        it66 = driver.find_element_by_xpath("//span[contains(text(), 'مدیریت سفارشات')]")
        it66.click()
        #
        inp1 = 0
        inp2 = 0 
        inp3 = 0
#login buttons
    fourthSave = Button(eighth , height = 1 , width = 15 , text = "اعمال تغییرات" , command=lambda: ret4())
    fourthSave.pack(pady=10)
    l12 = Label(eighth,  text =".لطفا صفحات نوتیفیکیشن را بعد از ورود به حساب کارگزاری ببندید")
    l12.pack()
    itt3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_dttsLogin_vecchio"]')))
    itt3.click()
    itt2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, refreshcap)))
    itt2.click()
#buy_________________________________________________________________________________________________________________________
def darsad():
    global third
    third = Toplevel()
    third.configure(bg='goldenrod1')
    third.title(":وارد کردن اطلاعات معامله با درصد")
    third.geometry("400x375")
    l40 = Label(third,  text = ":سهم مورد نظر را وارد کنید")
    l40.pack(pady= (15,0))
    text40 = Text(third , height = 2 , width = 20)
    text40.pack()
    l7 = Label(third,  text = ":درصد مورد نظر را وارد کنید")
    l7.pack()
    text7 = Text(third , height = 2 , width = 20)
    text7.pack()
    l8 = Label(third, text = ":قیمت مورد نظر را وارد کنید")
    l8.pack()
    text8 = Text(third , height = 2 , width = 20)
    text8.pack()
    l6 = Label(third,  text =  ":معامله مورد نظر را انتخاب کنید")
    l6.pack(pady= (15,0))
#####################################################
    def d_buy():
        inp7 = text7.get("1.0", 'end-1c' )
        inp8 = text8.get("1.0", 'end-1c' )
        inp1 = text40.get("1.0",'end-1c' )
        inpp = str(inp1) + '1'
        inp7 = int(inp7)
        dar = inp7 / 100
        ############################################
        driver.switch_to.window("firsttab")
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli = int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ###########################################
        driver.switch_to.window("secondtab")
        #
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli = int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("thirdtab")
        #
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli = int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("fourthtab")
        #
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli = int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ###############
        inp7 = 0
        inp8 = 0
        third.withdraw()

    def d_sell():
        inp7 = text7.get("1.0", 'end-1c' )
        inp8 = text8.get("1.0", 'end-1c' )
        inp1 = text40.get("1.0",'end-1c' )
        inpp = str(inp1) + '1'
        inp7 = int(inp7)
        dar = inp7 / 100
        ############################################
        driver.switch_to.window("firsttab")
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli = int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ###########################################
        driver.switch_to.window("secondtab")
        #
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli = int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("thirdtab")
        #
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli =int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("fourthtab")
        #
        #dar avardan mande hesab asli
        ele = driver.find_element_by_xpath('//*[@id="free2"]')
        azadHesab = int(ele.text)
        DarsadAsli =azadHesab * dar
        DarsadAsli =int(DarsadAsli)
        #safhe vared kardan
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(DarsadAsli)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp8)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        #
        inp7 = 0
        inp8 = 0
        third.withdraw()     

    da_buy = Button(third,height = 1 , width = 25 , text="خرید", command=d_buy)
    da_buy.pack()
    da_sell = Button(third,height = 1 , width = 25 , text="فروش", command=d_sell)
    da_sell.pack()
##################################################################################################################
def mablagh():
    #driver.switch_to.window("tab{}".format(m) )
    global fourth
    fourth = Toplevel()
    fourth.configure(bg='goldenrod1')
    fourth.title(":وارد کردن اطلاعات معامله با مبلغ")
    fourth.geometry("400x375")
    l41 = Label(fourth,  text = ":سهم مورد نظر را وارد کنید")
    l41.pack(pady= (15,0))
    text41 = Text(fourth , height = 2 , width = 20)
    text41.pack()
    l10 = Label(fourth,  text =  ":مبلغ مورد نظر را وارد کنید")
    l10.pack()
    text10 = Text(fourth , height = 2 , width = 20)
    text10.pack()
    l11 = Label(fourth, text = ":قیمت مورد نظر را وارد کنید")
    l11.pack()
    text11 = Text(fourth , height = 2 , width = 20)
    text11.pack()
    l9 = Label(fourth,  text = ":معامله مورد نظر را انتخاب کنید")
    l9.pack(pady= (15,0))
###################################################
    def m_sell():
        inp10 = text10.get("1.0", 'end-1c' )
        inp11 = text11.get("1.0", 'end-1c' )
        inp1 = text41.get("1.0",'end-1c' )
        inpp = str(inp1) + '1'
        #
        driver.switch_to.window("firsttab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it13 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it13.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ############################################################
        driver.switch_to.window("secondtab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("thirdtab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("fourthtab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20 = driver.find_element_by_xpath("//a[@class='x-btn d-sell-button x-unselectable x-box-item x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        #
        inp10 = 0 
        inp11 = 0
        fourth.withdraw()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def m_buy():
        inp10 = text10.get("1.0", 'end-1c' )
        inp11 = text11.get("1.0", 'end-1c' )
        inp1 = text41.get("1.0",'end-1c' )
        inpp = str(inp1) + '1'
        #
        driver.switch_to.window("firsttab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ############################################################
        driver.switch_to.window("secondtab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20=driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("thirdtab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 = driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        ##########################################
        driver.switch_to.window("fourthtab")
        #
        it15 = driver.find_element_by_xpath("//img[@class='x-tool-img x-tool-add x-rtl']")
        it15.click()
        time.sleep(0.5)
        it16 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]") #vared kardan sahm
        it16.send_keys(inpp)
        time.sleep(1) 
        it16.send_keys(Keys.ENTER) 
        #buy--------------------------------------------------------------------------------------------------------------
        it13 =driver.find_element_by_xpath("//input[starts-with(@id, 'numericfield-')]")
        it13.click() #avardan machine hesab
        time.sleep(0.5)
        it17 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='مبلغ']")
        it17.send_keys(inp10)
        #time.sleep(0.5)
        it18 = driver.find_element_by_xpath("//input[@type='text'][@placeholder='قیمت']") 
        it18.send_keys(inp11)
        it19=driver.find_element_by_xpath("//a[@class='x-btn x-unselectable x-rtl x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']") ########## PROBLEMATIC
        it19.click() #mohasebe hajm
        #driver.find_element_by_xpath(safhe).click()
        it20 = driver.find_element_by_xpath("//a[starts-with(@id, 'buybutton-')]")
        it20.click()
        time.sleep(0.25)
        test = driver.find_element_by_xpath("//div[starts-with(@id, 'messagebox-')]")
        test.send_keys(Keys.ESCAPE)
        test1 = driver.find_element_by_xpath("//input[starts-with(@id, 'instcombo-')]")
        test1.send_keys(Keys.ESCAPE)
        #########
        inp10 = 0 
        inp11 = 0
        fourth.withdraw()
    
    mabuy = Button(fourth,height = 1 , width = 25 , text="خرید", command=m_buy)
    mabuy.pack() 
    masell = Button(fourth,height = 1 , width = 25 , text="فروش", command=m_sell)
    masell.pack()       

def ex():
    driver.quit()
    root.quit()
    sys.exit()
#----------------------------------------------------------------------------------------------------------
#root widgets
l14 = Label(root,  text = ":انجام عملیات مد نظر شما")
l14.pack(pady = 15) 
l15 = Label(root,  text = ":ورود به حساب های مختلف")
l15.pack()
loginfirst = Button(root,height = 1 , width = 25 , text="ورود به اولین حساب", command=firstlogin)
loginfirst.pack()
loginsecond = Button(root,height = 1 , width = 25 , text="ورود به دومین حساب", command=secondlogin)
loginsecond.pack()
loginthird = Button(root,height = 1 , width = 25 , text="ورود به سومین حساب", command=thirdlogin)
loginthird.pack()
loginfourth = Button(root,height = 1 , width = 25 , text="ورود به چهارمین حساب", command=fourthlogin)
loginfourth.pack(pady= (0,15))
l18 = Label(root,  text = ":انجام عملیات با استفاده از درصد پورتفو یا مبلغ مورد نظر")
l18.pack()
buybutton = Button(root,height = 1 , width = 25 , text="معامله با استفاده از درصد", command=darsad)
buybutton.pack()
sellbutton = Button(root,height = 1 , width = 25 , text="معامله با استفاده از مبلغ", command=mablagh)
sellbutton.pack(pady= (0,15))
l24 = Label(root,  text = "خدانگهدار؟؟؟ :((")
l24.pack()
byebye = Button(root,height = 1 , width = 25 , text="!خدانگهدار", command=ex)
byebye.pack()
driver.execute_script("window.open('https://www.dttsonline.com/dtts/dtts/customer/login.jsp', 'firsttab');")
driver.execute_script("window.open('https://www.dttsonline.com/dtts/dtts/customer/login.jsp', 'secondtab');")
driver.execute_script("window.open('https://www.dttsonline.com/dtts/dtts/customer/login.jsp', 'thirdtab');")
driver.execute_script("window.open('https://www.dttsonline.com/dtts/dtts/customer/login.jsp', 'fourthtab');")
root.mainloop()


#it15 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//img[starts-with(@id, 'tool-')]")))
#driver.find_element_by_xpath("//img[starts-with(@id, 'tool-')]")
#it15 = driver.find_element_by_xpath("//div[@data-qtip='سفارش گذاری']")
#driver.find_element_by_xpath("//div[@data-qtip='سفارش گذاری']")
#it15 = driver.find_element_by_xpath("//input[starts-with(@class='x-tool') and contains('x-tool-pressed')]")