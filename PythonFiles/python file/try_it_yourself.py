usernames = ['mojjam', 'admin', 'suleman', 'badru', 'kaeru']

#user_login = input(f"\nLogin with just your username: ")
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"\nWelcome {username}, would you like to see your satatus report?")
        
        else:
            print(f"\nWelcome to your website {username}")

else:
    print("\nWe need to find some users")
    

    
# Ensure everyone has a unique u_name            
current_users = ['moses', 'jesus', 'abraham', 'noah', 'lut', 'david']
new_users = ['moses', 'jesus', 'job', 'solomon', 'adam', 'hud']


current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username")
    else:
        print(f"The username '{new_user}' is available.")


# Ordinal numbers

numbers = list(range(1, 30))

for number in numbers:
    if number == 1 or number == 21:
        ordinal = "st"
    elif number == 2 or number == 22:
        ordinal = "nd"
    elif number == 3 or number == 23:
        ordinal = "rd"
    else:
        ordinal = "th"
    print(f"{number}{ordinal}")