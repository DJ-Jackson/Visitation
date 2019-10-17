
import time
from datetime import datetime
from datetime import date
from selenium import webdriver



class Guest:
    def __init__(self, name, tele):
        self.name = name
        self.tele = tele

def person():
    people_count = int(input("How many guests do you have?: "))
    guest = []
    for i in range(people_count):
        name = input("What is Guest " + i + "'s name?: ")
        number = input("What is Guest " + i + "'s phone number?: ")
        guest[i] = Guest(name, number)
    return guest

#This will get the time in the appropriate format
def getTime():
    times = str(datetime.now())
    times = times.split(" ")
    times = times.replace(":","")
    strs = ''
    times = strs.join(i for i in times if i.isdigit())
    if int(times[:2]) > 12:
         hour = int(times[:2])-12
         min = int(times[2:4])
         case = "PM"
    else:
        hour = int(times[:2])
        min = int(times[2:4])
        case = "AM"
    time.sleep(1)

    # Time

    InputFieldHour = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
    InputFieldHour.send_keys(hour)

    InputFieldMin = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/input')
    InputFieldMin.send_keys(min)



#This will het the date in the appropriate format
def getDate():
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

    time.sleep(1)

    # Date
    InputFieldDate = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
    InputFieldDate.send_keys(date)



def personal_fill():
    #Student Name
    name = input("What is your name?: ")
    InputFieldStudent = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldStudent.send_keys(name)

    #Morehouse Number
    m_num = input("what is your M-Number?: ")
    InputFieldNumber = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldNumber.send_keys(m_num)

    #Room Number
    r_num = input('What is your room number?: ')
    InputFieldRoom = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldRoom.send_keys(r_num)

    #Phone Number Student
    p_num = input('What is your phone number?: ')
    InputFieldPhone = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldPhone.send_keys(p_num)


#Guest 1 Full Name Field
def guest_fill(guest):
    InputFieldGuestOneName = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldGuestOneName.send_keys(guest[0].name)


    #Guest 1 Phone Number Field
    InputFieldGuestOneTele = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[8]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldGuestOneTele.send_keys(guest[0].tele)


    #Guest 2 Full Name Field
    InputFieldGuestTwoName = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[9]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldGuestTwoName.send_keys(guest[1].name)


    #Guest 2 Phone Number Field
    InputFieldGuestTwoTele = driver.find_element_by_xpath(r'/html/body/div/div[2]/form/div/div[2]/div[2]/div[10]/div/div[2]/div/div[1]/div/div[1]/input')
    InputFieldGuestTwoTele.send_keys(guest[1].tele)


#Submits the form
def submit(a):
    submit = driver.find_element_by_xpath(r'/html/body/div[1]/div[2]/form/div/div[2]/div[3]/div[1]/div/div/span/span')
    submit.click()
    driver.quit()

def main():
    driver = webdriver.Chrome(r'path of chromedriver')
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdLDw__VdOaQheC1XUmgLr9yyTRG4ozd0KA1TQmesFIxRxX_g/viewform')
    list = person()
    guest_fill(list)
    getTime()
    getDate()
    personal_fill()
    #submit()

main()