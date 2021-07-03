from PIL import Image, ImageDraw, ImageFont
from playsound import playsound
import PySimpleGUI as sg

def watermark(organisation, case, exhibit, files):
    for file in files:
        try:
            im = Image.open(file)
            width, height = im.size
            draw = ImageDraw.Draw(im)
            text = ("{} {} {}".format(organisation, case, exhibit))
            font = ImageFont.truetype('arial.ttf', 150)
            textwidth, textheight = draw.textsize(text, font)
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin
            draw.text((x, y), text, font=font)
            im.save(file)
        except OSError:
            sg.Popup('File type not supported!', keep_on_top=True)

sg.theme('Dark Teal 4')

layout =    [[sg.Text('Organisation:'), sg.Input(pad=(1, 0), size=(30,0), key='_ORG_')],
            [sg.Text('Case Ref:'), sg.Input(pad=(20, 0), size=(30,0), key='_CASE_')],
            [sg.Text('Exhibit Ref:'), sg.Input(pad=(10, 0),size=(30,0), key='_EXHIBIT_')],
            [sg.Text('Select Photo(s)'), sg.FilesBrowse(key='_FILES_')],
            [sg.Button("Run"), sg.Button("Exit")]]

window = sg.Window('Hanko', layout, icon='saga-japan.ico')

while True:
    try:   
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event == 'Run':
            organisation = values['_ORG_']
            case = values['_CASE_']
            exhibit = values['_EXHIBIT_']
            files = values['_FILES_'].split(";")
            watermark(organisation, case, exhibit, files)
            playsound('dum dum.mp3')
            sg.Popup('Done!', keep_on_top=True) 
            
            
    except AttributeError:
        sg.Popup('No files selected!', keep_on_top=True)
