# colorchoices = [medium_orchid3, grey63, deep_pink4, dark_violet, red3, dark_red, hot_pink3, dark_orange3, light_pink3, sandy_brown, orange3, gold3, tan, yellow3, light_salmon1, green_yellow, dark_khaki, dark_sea_green3, rosy_brown, medium_purple, sea_green2, dark_sea_green4, cadet_blue, pale_turquoise4, navy_blue, dodger_blue3, turquoise4, green4, dark_cyan, cyan3, spring_green1, purple3, purple4, grey37, dark_magenta, pink1, thistle1, grey35, grey3, grey82, grey93, orchid2]
from rich import pretty, print as rprint, console, style, panel, padding
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
console = Console() #DO NOT DELETE ME 
#yes that's reallynecessary


class Button:
    next_id = 0
    all_buttons = []
    all_colors = [
    "medium_orchid3", "grey63", "deep_pink4", "dark_violet", "red3",
    "dark_red", "hot_pink3", "dark_orange3", "light_pink3", "sandy_brown",
    "orange3", "gold3", "tan", "yellow3", "light_salmon1",
    "green_yellow", "dark_khaki", "dark_sea_green3", "rosy_brown", "medium_purple",
    "sea_green2", "dark_sea_green4", "cadet_blue", "pale_turquoise4", "navy_blue",
    "dodger_blue3", "turquoise4", "green4", "dark_cyan", "cyan3",
    "spring_green1", "purple3", "purple4", "grey37", "dark_magenta",
    "pink1", "thistle1", "grey35", "grey3", "grey82",  "grey93", "orchid2"
    ]

    def __init__(self, button_name, button_sound_id, trigger_string):
        self.button_name = button_name
        self.button_sound_id = button_sound_id
        self.list_of_soundboards_used_in = button_sound_id
        self.color = "white"
        self.backround = "black"
        self.trigger_string = trigger_string
        self.innertext = trigger_string

    @classmethod
    def list_colors(cls):
        for color in Button.all_colors:
            console.print(color, style=color)

    # @classmethod
    # def list_all_buttons(cls):
    #     for button in Button.all_buttons:
    #         button.list_button()
    # def list_button(self):
    #     print(f"sound: {self.button_name} | sound name: {}")
Button.list_colors()