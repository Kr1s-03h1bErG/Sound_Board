class User:
    next_id = 0
    all_users = []
    def __init__(self, id):
        self.id = User.next_id
        allusers.append(id)
