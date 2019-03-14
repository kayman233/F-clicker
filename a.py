from tkinter import *
from buttons_and_labels import create_buttons_and_labels
from layouts import layout


class Press_F:

    def __init__(self, master):
        # Initialising variables
        self.total_clicks = 0
        self.current_clicks = 0

        self.one_click = 1
        self.auto_click = 0

        self.names = ('roommate', 'team', 'the_university', 'chinese',
                      'nine_year_olds', 'country', 'population')

        self.one_click_price = 5
        self.one_click_price_increment = 2

        self.roommate_clicks = 1
        self.roommate_price = 5
        self.roommate_price_increment = 2

        self.team_clicks = 10
        self.team_price = 10
        self.team_price_increment = 30

        self.the_university_clicks = 500
        self.the_university_price = 50
        self.the_university_price_increment = 100

        self.chinese_clicks = 1000
        self.chinese_price = 100
        self.chinese_price_increment = 1000

        self.nine_year_olds_clicks = 1000
        self.nine_year_olds_price = 100
        self.nine_year_olds_price_increment = 1000

        self.country_clicks = 1000
        self.country_price = 100
        self.country_price_increment = 1000

        self.population_clicks = 1000
        self.population_price = 100
        self.population_price_increment = 1000

        self.has_first_achievement = 0

        # Title
        self.master = master
        master.title("Press F to pay(get) respects")

        # Add buttons and labels
        create_buttons_and_labels(self)
        layout(self)

    def update(self, method):

        """Updates numbers after clicks"""
        if method == "one_click":
            if self.current_clicks > getattr(self, method + '_price'):
                self.one_click *= self.one_click_price_increment
                self.current_clicks -= getattr(self, method + '_price')
                setattr(self,
                        method + '_price',
                        getattr(self, method + '_price') + getattr(self, method + '_price_increment'),
                        )
        elif method == "CLICK":
            self.total_clicks += self.one_click
            self.current_clicks += self.one_click
        elif self.current_clicks > getattr(self, method + '_price'):
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


def autoclick():

    """Updates current_clicks every second"""

    my_gui.total_clicks += my_gui.auto_click
    my_gui.current_clicks += my_gui.auto_click
    my_gui.current_clicks_variable.set(my_gui.current_clicks)

    master.after(1000, autoclick)  # do this again 1 second later


def update_gui():

    """Updates gui every 0.05 sec"""
    column_num = 0
    for name in my_gui.names:
        if my_gui.current_clicks > getattr(my_gui, name + '_price'):
            getattr(my_gui, name + '_button').place(x=582, y=7+65*column_num)
        else:
            getattr(my_gui, name + '_button').place_forget()
        column_num += 1

    if my_gui.current_clicks > my_gui.one_click_price:
        my_gui.one_click_button.place(x=744, y=472)
    else:
        my_gui.one_click_button.place_forget()

    master.after(50, update_gui)  # do this again 1 second later


def check_achievements():

    """"Checks new achievements every 3 second """

    if my_gui.total_clicks > 0 and not my_gui.has_first_achievement:
        my_gui.first_achievement_label.place(x=500, y=200)
        my_gui.has_first_achievement = 1
    else:
        my_gui.first_achievement_label.place_forget()

    master.after(3000, check_achievements)


master = Tk()
master.minsize(1200, 625)
master.geometry("1200x625")
master.resizable(0, 0)
my_gui = Press_F(master)

autoclick()
update_gui()
check_achievements()

master.mainloop()
