class User:
    # constructor function(parameters): data is present for every instance
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        # followers attribute isn't necessary
        # initialize a value, rather than inputting a parameter when initializing


user_1 = User("001", "angela")
# we initialized the user_1 object with two starting values
# first value: user's id (self.id)
# second value: user's username (self.username)

print(user_1.username)
print(user_1.id)