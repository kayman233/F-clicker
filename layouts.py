from tkinter import *


def layout(App):

    """Layout of the buttons and labels"""

    App.background_label.place(x=-2, y=-2)

    App.current_clicks_text.place(x=100, y=50)
    App.current_clicks_value.place(x=100, y=125)

    App.auto_click_text.place(x=280, y=330, anchor=SE)
    App.auto_click_value.place(x=300, y=293)

    App.click_text.place(x=280, y=370, anchor=SE)
    App.click_value.place(x=300, y=333)

    column_num = 0
    for name in App.names:
        getattr(App,
                name+'_price_value'
                ).place(x=920, y=8 + 65*column_num)
        column_num += 1

    App.one_click_price_value.place(x=920, y=19 + 65*column_num)

    App.click_button.place(x=70, y=410)

    App.exit_button.place(x=1050, y=550)
