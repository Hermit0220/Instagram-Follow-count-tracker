import re

def extract_usernames(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()  

    #extract usernames from profile links
    pattern = r'https://www.instagram.com/([a-zA-Z0-9_.]+)'
    
    #find all user & return as a set
    usernames = set(re.findall(pattern, content))
    
    return usernames

#extract users from followers & following
followers = extract_usernames("followers.html")
following = extract_usernames("following.html")

#find users that are not following back
not_following_back = following - followers

# output for "not following back"
print("\n-----ACCOUNTS NOT FOLLOWING ME BACK (USERNAME)------")
if not_following_back:
    for username in not_following_back:
        print(f"   https://instagram.com/{username}")
else:
    print("✔️ Everyone is following you back!")