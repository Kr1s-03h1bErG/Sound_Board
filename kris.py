from main import User

class Guest(User):
    next_guest = 0
    all_guest = [] # this will store instances so we can delete later 

    def __init__(self):
        self.id = next_guest
        Guest.next_guest += 1
        Guest.all_guest.append(self) 
        self.sounds = []
        self.board = []


    def confirm_board(self):
        raise NotImplementedError("Guests cannot confirm")
    def confirm_sound(self):
        raise NotImplementedError("Guests cannot confirm")

    # def convert_to_user(self)
    #     pass
        