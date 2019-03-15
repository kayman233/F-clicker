from tkinter import *
from buttons_and_labels import create_buttons_and_labels
from layouts import layout
import json


class Press_F:

    def __init__(self, master):
        # Initialising variables

        with open('settings.json') as f:
            settings = json.load(f)

        for attr, value in settings.items():
            setattr(self, attr, value)

        # Title
        self.master = master
        master.title("Press F to pay(get) respects")

        # Adding buttons and labels
        create_buttons_and_labels(self)

        self.exit_button = Button(master,
                                  bg='#660066',
                                  activebackground='#993399',
                                  borderwidth=5,
                                  font=("Fixedsys", 20),
                                  text='EXIT',
                                  command=master.destroy
                                  )

        layout(self)

    def update(self, method):

        """Updates numbers after clicks"""
        if method == "one_click":
            if self.current_clicks > getattr(self, method + '_price'):
                self.one_click *= self.one_click_price_multiplier
                self.current_clicks -= getattr(self, method + '_price')
                setattr(self,
                        method + '_price',
                        getattr(self, method + '_price') * getattr(self, method + '_price_multiplier'),
                        )
        elif method == "CLICK":
            self.total_clicks += self.one_click
            self.current_clicks += self.one_click
        elif self.current_clicks >= getattr(self, method + '_price'):
            self.current_clicks -= getattr(self, method + '_price')
            setattr(self,
                    method + '_price',
                    getattr(self, method + '_price') + getattr(self, method + '_price_increment'),
                    )
            self.auto_click += getattr(self, method + '_clicks')

        self.current_clicks_variable.set(self.current_clicks)
        self.one_click_price_variable.set(self.one_click_price)
        self.click_variable.set(self.one_click)
        if method != "CLICK":
            self.auto_click_variable.set(self.auto_click)
            getattr(self,
                    method + '_price_variable'
                    ).set(getattr(self, method + '_price'))
