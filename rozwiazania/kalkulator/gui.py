import PySimpleGUI as sg
from core import exchange
# All the stuff inside your window.
layout = [  [sg.Text("Co chcesz wymienic?")],
            [sg.InputText()],
            [sg.Text("Ile?")],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    currency, amount = values[0], float(values[1])
    print(f"{amount} {currency} is {exchange(currency, amount):.2f} PLN")

window.close()