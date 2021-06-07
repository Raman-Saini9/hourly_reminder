import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Cancel, theme_text_color
import schedule

Cancel = False
def popupstopped():
    global Cancel
    layout = [[sg.Text("Reminders have been switched off!\nRun the program again to recieve popups.",text_color= 'black')],
    [sg.Button('Ok')]]

    window = sg.Window('Popup switched off',layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Ok':
            Cancel = True        
            break
    window.close()

def popups():
    layout = [[sg.Text("Hey! It's been over an hour, take a break.",text_color='black')],
            [sg.Button("Ok"),sg.Button('Dont show again')]]

    window = sg.Window('Hourly reminder',layout)

    popups_stopped = False

    while True:
        
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Ok':
            break
        
        if event == 'Dont show again':
            popups_stopped = True
            break

    window.close()

    if popups_stopped is True:
        popupstopped()

schedule.every(1).hour.do(popups)


while True:
    if Cancel: 
        schedule.cancel_job(popups)
        break
    schedule.run_pending()