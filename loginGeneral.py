
import time
from datetime import datetime
from datetime import date
from selenium import webdriver



class Guest:
    def __init__(self, name, tele):
        self.name = name
        self.tele = tele


Guest1 = Guest("John Doe", 1231231234)
Guest2 = Guest("Jane Doe", 1231231234)

#This will get the time in the appropriate format

times = str(datetime.now())
_, times = times.split(" ")
times = times.replace(":","")


strs = ''
times = strs.join(i for i in times if i.isdigit())
if int(times[:2]) > 12:
     hour = int(times[:2])-12
     min = min = int(times[2:4])
     case = "PM"
else:
    hour = int(times[:2])
    min = int(times[2:4])
    case = "AM"
print(hour, min, case)

#This will het the date in the appropriate format
today = str(date.today())
today = list(today.replace("-",""))
newDay = []
newDay.append(today[6])
newDay.append(today[7])
newDay.append(today[4])
newDay.append(today[5])
newDay.append(today[0])
newDay.append(today[1])
newDay.append(today[2])
newDay.append(today[3])
strg = ""
date = int(strg.join(newDay))

driver = webdriver.Chrome(r'path of chromedriver')
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdLDw__VdOaQheC1XUmgLr9yyTRG4ozd0KA1TQmesFIxRxX_g/viewform')
time.sleep(1)

#Date
InputFieldDate = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
InputFieldDate.send_keys(date)

#Time

InputFieldHour = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
InputFieldHour.send_keys(hour)

InputFieldMin = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/input')
InputFieldMin.send_keys(min)


#Student Name
InputFieldStudent = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldStudent.send_keys("Samjuul Jackson ")
#Morehouse Number
InputFieldNumber = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldNumber.send_keys("M00000000")

#Room Number
InputFieldRoom = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldRoom.send_keys(000)

#Phone Number Student
InputFieldPhone = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldPhone.send_keys(1231231234)


#Guest 1 Full Name Field
InputFieldGuestOneName = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldGuestOneName.send_keys(Guest1.name)


#Guest 1 Phone Number Field
InputFieldGuestOneTele = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[8]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldGuestOneTele.send_keys(Guest1.tele)


#Guest 2 Full Name Field
InputFieldGuestTwoName = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[9]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldGuestTwoName.send_keys(Guest2.name)


#Guest 2 Phone Number Field
InputFieldGuestTwoTele = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[10]/div/div[2]/div/div[1]/div/div[1]/input')
InputFieldGuestTwoTele.send_keys(Guest2.tele)



submit = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/form/div/div[2]/div[3]/div[1]/div/div/span/span')
submit.click()


driver.quit()
