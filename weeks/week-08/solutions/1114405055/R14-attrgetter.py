# R14: attrgetter

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"User({self.user_id})"


users = [User(23), User(3), User(99)]
print("sorted users ->", sorted(users, key=attrgetter("user_id")))
