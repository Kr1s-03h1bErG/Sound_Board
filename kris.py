from main import User

class Guest(User):
    def __init__(self):
        


    def confirm_board(self):
        raise NotImplementedError("Geusts cannot confirm a soundboard")
    def confirm_sound(self):
        raise NotImplementedError("Geusts cannot confirm a soundboard")