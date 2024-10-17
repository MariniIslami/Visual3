import PySimpleGUI as sg
susunan=[[sg.Push(),
        sg.Text("UNISKA MAB",font=("helvetica",24)),
        sg.VPush()],
        [sg.Push(),
        sg.Text("BANJARMASIN",font=("courier",18)),
        sg.VPush()] 
        ]
window = sg.Window(title="Elemen Text",
                layout=susunan,
                size=(430,200))

window.read()
window.close()