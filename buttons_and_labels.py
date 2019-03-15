from tkinter import *


def create_text(App, key, fontsize, background_color, given_text):
    setattr(
        App,
        key + '_text',
        Label(App.master,
              bg=background_color,
              text=given_text,
              font=("Fixedsys", fontsize)
              )
    )


def create_variable(App, key, variable, fontsize, background_color):
    setattr(
        App,
        key + '_variable',
        IntVar()
    )
    getattr(App, key + '_variable').set(variable)

    setattr(
        App,
        key + '_value',
        Label(App.master,
              bg=background_color,
              textvariable=getattr(App, key + '_variable'),
              font=("Fixedsys", fontsize)
              )
    )


def create_button(App, key):
    path = 'pictures/{}.png'.format(key)
    setattr(
        App,
        key + '_image',
        PhotoImage(file=path)
    )
    setattr(
        App,
        key + '_button',
        Label(App.master, borderwidth=0, image=getattr(App, key + '_image'))
    )
    getattr(
        App,
        key + '_button'
    ).bind('<Button-1>', lambda event: App.update(key))


def create_buttons_and_labels(App):
    """Creation of the buttons"""

    # Background
    App.background_image = PhotoImage(file="pictures/background.png")
    App.background_label = Label(App.master, image=App.background_image)
    App.first_background_color = '#663399'

    # Main info
    create_text(App, 'current_clicks', 30, App.first_background_color, "YOUR RESPECT:")
    create_variable(App, 'current_clicks', App.current_clicks, 30, App.first_background_color)
    App.current_clicks_value.config(width=13)

    # CLICKS
    create_text(App, 'click', 20, App.first_background_color, "Power of F:")
    create_variable(App, 'click', App.one_click, 20, App.first_background_color)

    # AUTO_CLICKS

    create_text(App, 'auto_click', 20, App.first_background_color, "Respect per sec:")
    create_variable(App, 'auto_click', App.auto_click, 20, App.first_background_color)

    # CLICK BUTTON
    App.click_button = Button(App.master,
                              bg='#660066',
                              activebackground='#993399',
                              borderwidth=5,
                              text='F',
                              command=lambda: App.update("CLICK"),
                              font=("Fixedsys", 50)
                              )
    App.master.bind("<KeyRelease-F>", lambda event: App.update("CLICK"))

    # Auto-click buttons
    for name in App.names:
        create_button(App, name)
        create_variable(App, name + '_price', getattr(App, name + '_price'), 20, '#333399')

    create_button(App, 'one_click')
    create_variable(App, 'one_click_price', getattr(App, 'one_click_price'), 20, '#333399')
