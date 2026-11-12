from main import User, Sound
# soundboard has buttons 
# a button has a sound
# soundboard has the button logic 

# all buttons public  
# we will just make and dupe button instances on demand 
# each button will have a list of soundboards its in 
# if it gets removed from a sound board after a while we will kill it 

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
    def list_all_buttons(cls):
        for button in Button.all_buttons:
            button.list_button()
    def list_button(self)
        print(f"sound: {self.button_name} | sound name: {}")
        
        

# needs toi add button logic
class Soundboard:
    next_id = 0
    all_sound_boards = []
    pending_soundboards = []
    public_soundboards = []
    def __init__(self, name, file_name, file_url):
        self.id = Soundboard.next_id
        Soundboard.next_id += 1
        self.name = name
        self.file_name = file_name
        self.file_url = file_url
        self.type = "private"
        Soundboard.all_sound_boards.append(self)

    # returns id (int)
    @classmethod
    def list_all_sound_boards(cls):
        if len(Soundboard.public_sounds) > 0:
            for soundboard_id in Soundboard.public_sounds:
                soundboard = Soundboard.get_sound_by_id(sound_id)
                print(f"    name: {soundboard.name} | fname: {soundboard.file_name} | furl: {soundboard.file_name}")
                return True
        else:
            print("No Public Sounds!")
            return False
    @classmethod
    def get_soundboard_id_by_name(cls, name):
        for soundboard in Soundboard.all_sound_boardss:
            if soundboard.name == name:
                return soundboard.id
            else: 
                print("couldn't find sound")
    # returns obj
    @classmethod
    def get_soundboard_by_id(cls, id):
        for soundboard in Soundboard.all_sound_boardss:
            if soundboard.id == id:
                return soundboard 
    def make_soundboard_public(self):
        self.type = "pending"
        Soundboard.pending_sounds.append(self.id)

#  killed playsound
    def remove_soundboard(self):
        print(f"deleting: {self.name}")
        if self.id in Soundboard.pending_sounds:
            Soundboard.pending_sounds.remove(self.id)
        for user in User.all_users:
            for soundboard_id in user.boards:
                if soundboard_id == self.id:
                    user.sounds.remove(self.id)
        if self.id in Soundboard.public_sounds:
            Soundboard.public_sounds.remove(self.id)
        del self
    def confirm_soundboard(self):
        self.type = "public"
        Soundboard.public_sounds.append(self.id)
        print(f"confirming soundboard: {self.name}")


# class Guest(User):
#     next_guest = 0
#     all_guest = [] # this will store instances so we can delete later 

#     def __init__(self):
#         self.id = next_guest
#         Guest.next_guest += 1
#         Guest.all_guest.append(self) 
#         self.sounds = []
#         self.boards = []


#     def confirm_board(self):
#         raise NotImplementedError("Guests cannot confirm")
#     def confirm_sound(self):
#         raise NotImplementedError("Guests cannot confirm")

#     def convert_to_user(self):
#         name = input("what is your name: ")
#         password = input("what is your password: ")
#         new_user = User(name, password, self.sounds, self.board)
        