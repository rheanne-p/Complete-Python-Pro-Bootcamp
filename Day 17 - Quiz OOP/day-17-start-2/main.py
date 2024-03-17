# Create Class
class User:
    # Attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Methods
    # self: a keyword, refers to which object called the follow method
    # user: argument must be an object of type User
    def follow(self, user):
        user.followers += 1
        self.following += 1
        # person who you follow gains a follower
        # you gain a following on your account


# Create Objects
user_1 = User("001", "angela")
user_2 = User("002", "jack")

# Print Attributes
print(user_1.followers)

# Call Methods
user_1.follow(user_2)
# user_1 will follow user_2
# they are both objects

print(f"User_1's followers: {user_1.followers}")
print(f"User_1's following: {user_1.following}")

print(f"User_2's followers: {user_2.followers}")
print(f"User_2's following: {user_2.following}")

