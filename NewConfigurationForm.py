import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkGrey11')

EXCEL_FILE = 'Database.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('All inapplicable fields can be skipped.')],
    [sg.Text('Make', size=(15,1)), sg.InputText(default_text="",key='make')],
    [sg.Text('Model', size=(15,1)), sg.InputText(default_text="",key='model')],
    [sg.Text('Machine Type', size=(15,1)), sg.InputText(default_text="",key='machType')],
    [sg.Text('CPU Model', size=(15,1)), sg.InputText(default_text="",key='cpuModel')],
    [sg.Text('CPU Speed', size=(15,1)), sg.InputText(default_text="",key='cpuSpeed')],
    [sg.Text('Memory', size=(15,1)), sg.InputText(default_text="",key='totalMemory')],
    [sg.Text('Drive Type', size=(15,1)), sg.InputText(default_text="",key='driveType')],
    [sg.Text('Drive Capacity', size=(15,1)), sg.InputText(default_text="",key='driveCapacity')],
    [sg.Text('Optical Drive', size=(15,1)), sg.InputText(default_text="No Optical",key='opticalDrive')],
    [sg.Text('Battery', size=(15,1)), sg.InputText(default_text="Yes",key='batteryYN')],
    [sg.Text('Adapter', size=(15,1)), sg.InputText(default_text="Yes",key='adapterIncluded')],
    [sg.Text('Screen', size=(15,1)), sg.InputText(default_text="Intact",key='screenCondition')],
    [sg.Text('Keyboard', size=(15,1)), sg.InputText(default_text="Intact",key='keyboardCondition')],
    [sg.Text('Operating System', size=(15,1)), sg.InputText(default_text="na",key='operatingSystem')],
    [sg.Text('Battery Condition', size=(15,1)), sg.InputText(default_text="normal",key='battCond')],
    [sg.Text('Battery Cycle Count', size=(15,1)), sg.InputText(default_text="",key='battCyc')],
    [sg.Text('GPU Brand', size=(15,1)), sg.InputText(default_text="",key='gpuMake')],
    [sg.Text('GPU Model', size=(15,1)), sg.InputText(default_text="",key='gpuModel')],
    [sg.Text('GPU Memory', size=(15,1)), sg.InputText(default_text="",key='gpuMem')],
    [sg.Text('Screen Resolution', size=(15,1)), sg.InputText(default_text="",key='scrRes')],
    [sg.Text('Screen Brightness', size=(15,1)), sg.InputText(default_text="",key='scrNits')],
    [sg.Text('Touch or Nontouch', size=(15,1)), sg.InputText(default_text="",key='touchEnabled')],
    [sg.Text('Apple Failcode', size=(15,1)), sg.InputText(default_text="",key='appleFailcode')],
    [sg.Text('Comment', size=(15,1)), sg.InputText(default_text="",key='comment')],
    [sg.Text('Tags', size=(15,1)), sg.InputText(default_text="",key='tags')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
        ]

window = sg.Window('Add Configuration', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Clear':
            clear_input()
        if event == 'Submit':
            new_record = pd.DataFrame(values, index=[0])
            df = pd.concat([df, new_record], ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)
            sg.popup('Written to file.')
window.close()
