from main import User, Sound, Admin
from rich import pretty, print as rprint, console, style, panel, padding
from rich.pretty import pprint
from rich.style import Style
from rich.console import Console
from rich.padding import Padding
console = Console() #DO NOT DELETE ME 
#yes that's reallynecessary

def get_response(text):
    player_response = input(text)
    stripped_player_response = player_response.strip()
    nice_player_response = stripped_player_response.lower()
    # makes the response useable 

    # checks if y/n and sets it to false or True

    if nice_player_response == "y":
        return True
    elif nice_player_response == "n":
        return False
    try:
        old_player_response = nice_player_response
        nice_player_response = int(nice_player_response)
        nums = [1,2,3,4,5,6,7,8,9,0]
        if  nice_player_response in nums:
            return int(nice_player_response)
    except:
        nice_player_response = old_player_response
    return nice_player_response

#checks Returns if it succeeded or failed (bool)
def login():
    while True:
        need_login = get_response("Do you need to login? Y/N:")
        if need_login: # change here 
            username = get_response("What is your Username?: ")
            password = get_response("What is your Password?: ")
            return [User.is_password_users(username, password) , username, password] 
        else: # return that it failed to login so we can register later
            rprint("[bold black]Failed to find name in db/user didn't need to[/bold black]")
            return [[False, False] , "", ""]

def register():
    need_register = get_response("Do you need to register? Y/N: ")
    while True:
        if need_register:
            username = get_response("What will be your Username?: ")
            password = get_response("What is your Password?: ")
            if User.is_user_in_user(username): # change here 
                print("username already in db restarting register")
            else:
                User(username, password)
                return True
        else: # return that it failed to login so we can register later
            print("User Didn't need to register for new account! ")
            return False
# add this stuff
def overview_menu(user):
    while True:
        user_choice = get_response("    1. User Overview\n    2. Change Password\n    3. Logout\n    q to quit!\n")
        if user_choice == "q":
            return False # this just works ig 
        elif user_choice ==  1:
            user.overview()
        elif user_choice ==  2:
            password = input("please enter password: ")
            if password == user.password:
                new_password = input("please enter new password: ")
                user.change_password(new_password)
                print("Password was Changed exiting menu!")
                return "Password Was Changed!"    
            else:
                print("Password was incorrect!")
        elif user_choice == 3:
            print(f"loging user: {user.name} out")
            return True
def sound_menu(user):
    while True:
        user_choice = get_response("    1. Personal Sound Overview\n    2. Global Public Sound Overview\n    3. Make Sound\n    4. Play Public Sound\n    5. Play your Sounds\n    6. Publish a Sound\n    q to quit!\n")
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

def soundboard_menu(user):
    pass
def admin_menu(user):
    while True:
        user_choice = get_response("    1. Admin Overview\n    2. Change Admin Password\n    3. Check Sounds\n    4. Check Sound Boards\n    5. Remove Sounds\n    6. Remove Sound Boards\n    q to quit!")
        if user_choice == "q":
            return False # this just works ig 
        elif user_choice ==  1:
            user.overview()
        elif user_choice ==  2:
            password = input("please enter password: ")
            if password == user.password:
                admin_password = input("please enter admin password: ")
                if admin_password == user.apassword:
                    new_admin_password = input("please enter new admin password: ")
                    user.change_admin_password(new_admin_password)
                    print("Password was Changed exiting menu!")
                    return "Password Was Changed!"  
                else:
                    print("Admin Password was incorrect!")
            else:
                print("Password was incorrect!")
        elif user_choice == 3:
            for sound_id in Sound.pending_sounds:
                sound = Sound.get_sound_by_id(sound_id)
                if sound.type == "pending":
                    print(f"ID: {sound.id} | name: {sound.file_name} | file url: {sound.file_url} | file name {sound.file_name}")
            sound_id = input("please enter a sound id from the ID's above to make public: ")
            if int(sound_id) in Sound.pending_sounds:
                sound = Sound.get_sound_by_id(int(sound_id))
                sound.confirm_sound()
            else:
                print("Sound not in pending sounds!")
        elif user_choice == 4:
            print("Not implemented yet")
        elif user_choice == 5:
            for sound_id in Sound.pending_sounds:
                sound = Sound.get_sound_by_id(sound_id)
                if sound.type == "pending":
                    print(f"ID: {sound.id} | name: {sound.file_name} | file url: {sound.furl} | file name {sound.file_name}")
            sound_id = input("Please enter a sound ID from the ID's above: ")
            if sound_id in Sound.pending_sounds:
                sound = Sound.get_sound_by_id(sound_id)
                sound.remove_sound()
            else:
                print("Sound not in pending sounds!")
        elif user_choice == 6:
            print("Not implemented yet")

# seed a admin into the system
Admin("a", "a", "a")
def main():
    while True:
        # print(User.all_users)
        # login_stat[2] = password
        # login_stat[1] = username 
        # login_stat[0] = [user exists, is pass users] 
        login_stats = login()
        if login_stats[0][0] and login_stats[0][1]:
            break 
        else:
            register()
    while True:
        #changed from dict to object
        # user session is justg for debug now ig
        # user_session = User.get_users_login_session(User.get_user_id_by_login(login_stats[1], login_stats[2]))
        user = User.get_user_by_id(User.get_user_id_by_login(login_stats[1], login_stats[2]))
        # print(user_session)
        print("")
        menu = "1: User Overview Menu\n2. Sound Menu\n3. Soundboard Menu\n"
        if user.role == "Admin":
            menu += "4. Admin Menu\n"
        #Logic is down here 
        user_choice = get_response(menu)
        if user_choice == 1:
            is_logout = overview_menu(user)
            if is_logout == "Password Was Changed!":
                login_stats[2] = user.password
            elif is_logout:
                break
        elif user_choice == 2:
            sound_menu(user)
        elif user_choice == 3:
            soundboard_menu(user)
        elif user_choice == 4:
            if user.role == "Admin":
                password = input("Please enter admin password")
                if password == user.apassword:
                    is_logout = admin_menu(user)
                else: 
                    print("Admin Password Incorrect!")
            else:
                print("Must be Admin to acess this menu!")

while True:
    main()
