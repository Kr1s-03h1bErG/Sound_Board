class User:
    next_id = 0
    all_users = []
    def __init__(self, id):
        self.id = User.next_id
        allusers.append(id)

class Guest:
    def __init__(self):
        pass

class Admin(User):
    def __init__(self, id):
        self.id = Admin.next_id
#functions and shit that admin can do
    def confirm_sound():
        pass
    def remove_sound():
        pass
    def confirm_board():
        pass
    def remove_board():
        pass