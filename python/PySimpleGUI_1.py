#!/usr/bin/env python

import PySimpleGUI as sg

def main_win(theme = None):
    #sel_theme = theme or "Default1"
    sel_theme = theme or "DefaultNoMoreNagging"
    #sel_theme = theme or "GrayGrayGray"
    layout = [
        [sg.Menu([["File",["New","Open","Save","SaveAs","Close","---","Exit"]],["Help",["About"]]])],
        [
            sg.Frame("Login", [
                [sg.Text("Username", size=(8,0)), sg.InputText(key="username")],
                [sg.Text("Pass", size=(8,0)), sg.InputText(key="pass")],
                [sg.Text("Role", size=(8,0)), sg.Combo(['admin','user','guest'], default_value='user', readonly=True, key="role")],
            ]),
            sg.VSep(),
            sg.Column([
                [sg.Text("Register", size=(8,0)), sg.Checkbox("", default=True, key="register")],
                [
                    sg.Text("Align", size=(8,0)),
                    sg.Column([
                        [sg.Radio("Left", "ALIGN", default=True, key="align_left")],
                        [sg.Radio("Center", "ALIGN", default=False, key="align_center")],
                        [sg.Radio("Right", "ALIGN", default=False, key="align_right")],
                    ]),
                    sg.Frame("Canvas", [[canvas]]),
                ],
            ]),
        ],
        [
            sg.Text("Theme", size=(8,0)),
            sg.Combo(sg.list_of_look_and_feel_values(), default_value=sel_theme, readonly=True, key="theme", enable_events=True),
#            sg.Button("Change"),
        ],
        [sg.HSep()],
        [sg.Submit(), sg.Cancel(), sg.Push(), sg.Exit()],
        [sg.StatusBar("Status Bar.")],
    ]
    context_menu = ["X", ["About","---","Exit"]]

    #sg.theme("DarkAmber")
    sg.theme(sel_theme)
    #win = sg.Window("Win #1", layout, size=(640,480))
    #win = sg.Window("Win #1", layout)
    win = sg.Window("Win #1", layout, finalize=True, right_click_menu=context_menu, resizable=True)
    #win = sg.Window("Win #1", layout, use_custom_titlebar=True)
    #win = sg.Window("Win #1", layout, element_justification="c")
    return win
    
def draw(canvas):
    tkc = canvas.TKCanvas
    sz = canvas.get_size()
    tkc.create_line(0,0,sz[0]-1,sz[1]-1)
    tkc.create_line(0,sz[1]-1,sz[0]-1,0)
    k = 10
    tkc.create_line(k,k,k,sz[1]-k,sz[0]-k,sz[1]-k,sz[0]-k,k,k,k,width=2,fill="red")
    k = 20
    # spline
    tkc.create_line(k,k,sz[0]-k,sz[1]-k,k,sz[1]-k,sz[0]-k,k,k,k,width=2,fill="blue",smooth=True)
    k = 50
    tkc.create_oval(k,k,sz[0]-k,sz[1]-k)

canvas = sg.Canvas(background_color='#cfc', size=(200,120))
win = main_win()

while True:
    event, values = win.read()
    print("event: ", event, "    values: ", values)
 
    if event in { sg.WIN_CLOSED, "Exit" }:
        break
    if event in ["Submit"]:
        draw(canvas)
        win.refresh()
    if event in ["Cancel"]:
        canvas.TKCanvas.delete("all")
        win.refresh()
    if event in ["Change", "theme"]:
        sel_theme = values["theme"]
        print(sel_theme)
        win.close()
        win = main_win(sel_theme)

win.close()
