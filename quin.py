from classes import User, Sound, Admin
from rich import pretty, print as rprint, console, style, panel, padding
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
console = Console() #DO NOT DELETE ME 
#yes that's reallynecessary 

# def soundboard_menu(user):
#     while True:
#         user_choice = get_response("    1. User Overview\n    2. Change Password\n    3. Logout\n    q to quit!")
#         if user_choice == "q":
#             return False # this just works ig 
#         elif user_choice ==  1:
#             user.overview()
#         elif user_choice ==  2:
#             password = input("please enter password: ")
#             if password == user.password:
#                 new_password = input("please enter new password: ")
#                 user.change_password(new_password)
#             else:
#                 print("Password was incorrect!")
#         elif user_choice == 3:
#             print(f"loging user: {user.name} out")
#             return True
def sounds_menu(user):
    while True:
        user_choice = get_response("    1. View Sound Board \n    2.  Delete Sound Board \n    3. Change Sound Board \n    4. Create Sound Board \n    5. \n    6. \n    q to quit!\n")
        if user_choice == "q":
            return True # this just works ig 
        elif user_choice ==  1:
            user.list_sounds()
        elif user_choice == 2:
            Sound.list_all_sounds()
        elif user_choice == 3:
            name = input("Enter the name for your sound: ")
            fname = input("Enter the file name for your sound: ")
            furl = input("Enter the url for your sound: ")
            new_sound = Sound(name, fname, furl)
            did_succeed = new_sound.play_sound()
            if did_succeed:
                user.sounds.append(new_sound.id)
                print("Sound Sucessfully Created")
            else:
                print("Sound failed to create! deleting sound!")
                new_sound.remove_sound()
                # user.sounds.remove(new_sound.id)
                # Sound.all_sounds.remove(new_sound)
                # del new_sound
                
        elif user_choice ==  4:
            if Sound.list_all_sounds(): 
                user_choice = input("What sound would you like to play from sounds above?")
                sound = Sound.get_sound_by_id(Sound.get_sound_id_by_name(user_choice))
                if sound.type == "Public":
                    sound.play_sound()
                else:
                    print("Sound must be public to be played!")
            else:
                print("No Public Sounds!")
        elif user_choice == 5:
            user.list_sounds()
            user_choice = input("What sound would you like to play from sounds above?")
            sound_id = Sound.get_sound_id_by_name(user_choice)
            sound = Sound.get_sound_by_id(sound_id)
            if sound_id in user.sounds:
                sound.play_sound()
            else:
                print("Sound not in users sounds!")
        elif user_choice == 6:
            if len(user.sounds) > 0:
                print(user.sounds) 
                user.list_sounds()
                user_choice = input("What sound would you like to publish from sounds above?")
                sound = Sound.get_sound_by_id(Sound.get_sound_id_by_name(user_choice)) 
                if sound.id in user.sounds:
                    if sound.type == "Private":
                        print(f"Sound: {sound.name} is now pending aproval")
                        sound.make_sound_public()
                    elif sound.type == "pending":
                        print("Sound is pending approval!")
                    elif sound.type == "public":
                        print("Sound already is Public!")
                else:
                    print("Sound not in users sounds!")      
            else:
                print("You must have sounds in order to make a sound public!")

# # def soundboard_menu(user):
# #     pass
# # def admin_menu(user):
# #     while True:
# #         user_choice = get_response("    1. Admin Overview\n    2. Change Admin Password\n    3. Check Sounds\n    4. Check Sound Boards\n    5. Remove Sounds\n    6. Remove Sound Boards\n    q to quit!")
# #         if user_choice == "q":
# #             return False # this just works ig 
# #         elif user_choice ==  1:
# #             user.overview()
# #         elif user_choice ==  2:
# #             password = input("please enter password: ")
# #             if password == user.password:
# #                 admin_password = input("please enter admin password: ")
# #                 if admin_password == user.apassword:
# #                     new_admin_password = input("please enter new admin password: ")
# #                     user.change_admin_password(new_admin_password)
# #                 else:
# #                     print("Admin Password was incorrect!")
# #             else:
# #                 print("Password was incorrect!")
# #         elif user_choice == 3:
# #             for sound_id in Sound.pending_sounds:
# #                 sound = Sound.get_sound_by_id(sound_id)
# #                 if sound.type == "pending":
# #                     print(f"ID: {sound.id} | name: {sound.file_name} | file url: {sound.file_url} | file name {sound.file_name}")
# #             sound_id = input("please enter a sound id from the ID's above to make public: ")
# #             if int(sound_id) in Sound.pending_sounds:
# #                 sound = Sound.get_sound_by_id(int(sound_id))
# #                 sound.confirm_sound()
# #             else:
# #                 print("Sound not in pending sounds!")
# #         elif user_choice == 4:
# #             print("Not implemented yet")
# #         elif user_choice == 5:
# #             for sound_id in Sound.pending_sounds:
# #                 sound = Sound.get_sound_by_id(sound_id)
# #                 if sound.type == "pending":
# #                     print(f"ID: {sound.id} | name: {sound.file_name} | file url: {sound.furl} | file name {sound.file_name}")
# #             sound_id = input("Please enter a sound ID from the ID's above: ")
# #             if sound_id in Sound.pending_sounds:
# #                 sound = Sound.get_sound_by_id(sound_id)
# #                 sound.remove_sound()
# #             else:
# #                 print("Sound not in pending sounds!")
# #         elif user_choice == 6:
