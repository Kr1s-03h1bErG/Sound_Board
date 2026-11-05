def get_response(text):
    player_response = console.input(text)
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
        need_login = get_response("Do you need to [dodger_blue2]login[/dodger_blue2]? [green]Y[/green]/[red3]N[/red3]: ")
        if need_login: # change here 
            username = get_response("What is your [dodger_blue2]Username[/dodger_blue2]?: ")
            return is_user_in_user(username) , username 
        else: # return that it failed to login so we can register later
            print("Failed to find name in db/user didn't need to")
            return False , ""

def register():
    need_register = get_response("Do you need to register? Y/N: ")
    while True:
        if need_register:
            username = get_response("What will be your Username?: ")
            if is_user_in_user(username): # change here 
                print("username already in db restarting register")
            else:
                return add_user(username) 
        else: # return that it failed to login so we can register later
            print("User Didn't need to register for new account! ")
            return False
def main():
    pass
