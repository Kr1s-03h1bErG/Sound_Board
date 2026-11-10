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
    def __init__(self, name, sound_obj):
        self.name = 

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
        