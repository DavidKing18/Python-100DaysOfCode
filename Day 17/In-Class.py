# # How to create your own class in Python
# class UserAlpha:
#     pass
#
#
# user_1 = UserAlpha()
# user_1.id = '001'
# user_1.username = "david"
#
# print(user_1.username)
#
#
# # Working with Attributes, Class Constructors and the __init__() Function
# class UserBeta:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#
#
# user_1 = UserBeta('001', 'David')
# user_2 = UserBeta('002', 'Jeroboam')
#

# Adding Methods to a class

class UserMega:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_x = UserMega('001', 'Michael')
user_y = UserMega('002', 'Fernando')

user_x.follow(user_y)
print(user_x.followers)
print(user_x.following)
print(user_y.followers)
print(user_y.following)
