from tkinter import *


def layout(My_class):
    """Layout of the buttons"""
    My_class.background_label.place(x=-2, y=-2)

    My_class.current_clicks_text.place(x=100, y=50)
    My_class.current_clicks_value.place(x=100, y=125)

    My_class.auto_click_text.place(x=280, y=330, anchor=SE)
    My_class.auto_click_value.place(x=300, y=293)

    My_class.click_text.place(x=280, y=370, anchor=SE)
    My_class.click_value.place(x=300, y=333)

    column_num = 0
    for name in My_class.names:
        getattr(My_class,
                name+'_price_value'
                ).place(x=920, y=8 + 65*column_num)
        column_num += 1

    My_class.one_click_price_value.place(x=920, y=19 + 65*column_num)

    My_class.click_button.place(x=70, y=410)
