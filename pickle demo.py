from guizero import App, Text, TextBox, Window, PushButton, ListBox, Box, Window, Picture
import time
import datetime


#app opens the code
app = App(title= "Main window")
name_list = []
surname_list = []
tob_list = []
temp_list = []
float_num = 0
tempova = 0

#Window opens for user to input code
def open_window():
    global name, surname, tob
    window = Window(app, title ="Second Window")
    window.show(wait=True)
    app.hide()
    name_label = Text(window, text="Name", grid=[0,0])
    name = TextBox(window, grid=[1,0])
    surname_label = Text(window, text="Surname", grid=[0,1])
    surname = TextBox(window, grid=[1,1])
    tob_label = Text(window, text="Time of Birth(HH.MM)", grid=[0,2])
    tob = TextBox(window, grid=[1,2])
    save_button = PushButton(window, text="Save Data", command=save)
    open_button = PushButton(window, text="Menu", command=close_window, args=[app, window])
#Window opens with a scroll bar with list of babies
def profile():
    global name_list, surname_list, tob
    window = Window(app, title ="List of babies Window")
    window.show(wait=True)
    listbox = ListBox(window, items=name_list, scrollbar=True, command=individual_temp)
    close_button = PushButton(window, text="Close", command=close_window, args=[app, window])
    open_button = PushButton(window, text="Menu", command=close_window, args=[app, window])
    app.hide()

#The baby can input their temp
def individual_temp(value):
    global float_num, tempova
    window = Window(app, title ="Individual Window")
    window.show(wait=True)
    app.hide()
    pos = name_list.index(value)
    born = tob_list[pos]
    lastname = surname_list[pos]
    name_label = Text(window, text="Hi " + value + " " + lastname +" you were born at " + born)
    open_button = PushButton(window, text="Menu", command=close_window, args=[app, window])
    temp = app.question("Hello", "What's your temperature?")
    # If cancel is pressed, None is returned
    # so check a name was entered
    if temp is not None:
        temp2 = float(temp)
        temp3 = round(temp2, 1)
        print(temp3)
        temp_list.append(temp3)
        print(temp_list)
    if temp3 >= 37.5:
        tempover = Text(window, text=" Your temp is too high doctor coming soon ")
        tempova += 1
        print(tempova)
    elif temp3 <= 36.0:
        tempunder = Text(window, text=" Your temp is too low doctor coming soon ")
        tempova += 1
    else:
        tempok = Text(window, text=" Your temp is in a healthy range ")


    if tempova >= 2:
        tempova1 = Text(window, text=" Emergency service is comming you have been outside of range too much ")


    for item in temp_list:
      if isinstance(item, float):
        float_num += 1

    print(float_num)

    if float_num == 6:
        timeup = Text(window, text="Your time is up")
        min_value = min(temp_list)
        max_value = max(temp_list)
        range = max_value - min_value
        range = Text(window, text="Your range in temp is " + str(range) + " the high is " + str(max_value) + " the low was " + str(min_value))
    else:
        timegoing = Text(window, text="Your time is still going")



#Closes window when button is pressed
def close_window(open, close):
    close.hide()
    open.show()

#Using a button it saves the data
def save():
    global name_list, surname_list, tob_list
    name_value = name.value
    surname_value = surname.value
    tob_value = tob.value
    name_list.append(name.value)
    surname_list.append(surname.value)
    tob_list.append(tob.value)

#Closes the app
def quit():
    exit()

#Menu that opens new windows with a pushbutton
app.bg = "pink"
open_button = PushButton(app, text="Input Data", command=open_window)
window2 = PushButton(app, text="List of babies", command=profile)
quit_button = PushButton(app, text=" Quit", command=quit)


app.display()
