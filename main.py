from rich import pretty, print as rprint, console, style, panel, padding
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
console = Console() #DO NOT DELETE ME 
#yes that's reallynecessary

import os
import requests
from playsound3 import playsound  # pip install playsound

class User:
    next_id = 0
    all_users = [] # fills up with users 
    def __init__(self, name, password):
        self.id = User.next_id
        User.next_id += 1
        User.all_users.append(self)
        self.name = name
        self.password = password
        self.sounds = []
        self.boards = []
        self.role = "User"
    # @classmethod
    # def login()

# Returns Bool if suceeds (bool)
    @classmethod
    def is_user_in_user(cls, username):
        for user in User.all_users:
            if user.name == username:
                return True
        return False

#   returns [Bool, Bool] (list)
#   if user is in user as Bool and if password is users 
    @classmethod
    def is_password_users(cls, username, password):
        user_exists = False
        password_confirmed = False
        for user in User.all_users:
            if user.name == username:
                user_exists = True
                if user.password == password:
                   password_confirmed = True 
        return [user_exists, password_confirmed]  
    @classmethod
    def get_user_by_id(cls, id):
        for user in User.all_users:
            if user.id == id:
                return user

    #returns user instance (obj)
    @classmethod
    def get_user_id_by_login(cls, username, password):
        for user in User.all_users:
            if user.name == username and user.password == password:
                return user.id
    

    #returns dict #this might be redundant now
    @classmethod
    def get_users_login_session(cls , id):
        user = User.get_user_by_id(id)
        return {
        "name": user.name,
        "id": user.id,
        "password": user.password, 
        "sounds": user.sounds,
        "boards": user.boards,
        "role": user.role}

    def change_password(self, new_password):
        self.password = new_password
        print(f"password changed to '{new_password}'!")

    def overview(self):
        print(f"username: {self.name}\npassword: {self.password}\nsounds owned: {len(self.sounds)}\nboards owned: {len(self.boards)}\n")
    def list_sounds(self):
        for sound_id in self.sounds:
            sound = Sound.get_sound_by_id(sound_id)
            print(f"    name: {sound.name} | type: {sound.type} | fname: {sound.file_name} | furl: {sound.file_name}")


class Guest:
    def __init__(self):
        pass

class Admin(User):
    def __init__(self, name, password, admin_password):
        super().__init__(name, password)
        self.role = "Admin"
        self.apassword = admin_password
    def overview(self):
        super().overview()
        print(f"Admin Password: {self.apassword}")
    def change_admin_password(self, new_password):
        self.admin_password = new_password
        print(f"admin password changed to '{new_password}'!")
#functions and shit that admin can do
    # def confirm_sound():
    #     pass
    # def remove_sound():
    #     pass
    # def confirm_board():
    #     pass
    # def remove_board():
    #     pass

class Sound:
    next_id = 0
    all_sounds = []
    pending_sounds = []
    public_sounds = []
    def __init__(self, name, file_name, file_url):
        self.id = Sound.next_id
        Sound.next_id += 1
        self.name = name
        self.file_name = file_name
        self.file_url = file_url
        self.type = "private"
        Sound.all_sounds.append(self)
    # returns id (int)
    @classmethod
    def list_all_sounds(cls):
        if len(Sound.public_sounds) > 0:
            for sound_id in Sound.public_sounds:
                sound = Sound.get_sound_by_id(sound_id)
                print(f"    name: {sound.name} | fname: {sound.file_name} | furl: {sound.file_name}")
                return True
        else:
            print("No Public Sounds!")
            return False
    @classmethod
    def get_sound_id_by_name(cls, name):
        for sound in Sound.all_sounds:
            if sound.name == name:
                return sound.id
            else: 
                print("couldn't find sound")
    # returns obj
    @classmethod
    def get_sound_by_id(cls, id):
        for sound in Sound.all_sounds:
            if sound.id == id:
                return sound 
    def make_sound_public(self):
        self.type = "pending"
        Sound.pending_sounds.append(self.id)
    def play_sound(self):
        #i have a feeling it will error out if the url or name is wrong 
        #apparently this dosnt work in codespaces so i need another library 
        try:
            # AI Code!
            if not os.path.exists(self.file_name): # checks if file in files
                response = requests.get(self.file_url) #asks for the file from url
                with open(self.file_name, "wb") as file: #makes audio file
                    file.write(response.content)
            # plays sound 
            # playsound(self.file_name)
            print("fix playsound")
            print(f"Playing Sound {self.name}")
            return True
        except:
            print("error experienced while playing sound.")
            return False
    def remove_sound(self):
        print(f"deleting: {self.name}")
        if self.id in Sound.pending_sounds:
            Sound.pending_sounds.remove(self.id)
        for user in User.all_users:
            for sound_id in user.sounds:
                if sound_id == self.id:
                    user.sounds.remove(self.id)
        if self.id in Sound.public_sounds:
            Sound.public_sounds.remove(self.id)
        del self
    def confirm_sound(self):
        self.type = "public"
        Sound.public_sounds.append(self.id)
        print(f"confirming sound: {self.name}")
