# from models.user import User
# from core.file_singleton import FileManager


# class UserRepository:
#     def __init__(self):
#         self.file = FileManager()

#     def get_all(self):
#         rows = self.file.read_csv("data/users.csv")
#         return [User(int(r["id"]), r["name"], r["email"]) for r in rows]

#     def get_by_id(self, id):
#         all_users = self.get_all()
#         for user in all_users:
#             if user.id == id:
#                 return user
#         return None


from models.user import User
from core.file_singleton import FileManager


class UserRepository:

    def get_all(self):
        fm = FileManager()
        rows = fm.read_csv()
        return [User(int(r["id"]), r["name"], r["email"]) for r in rows]

    def get_by_id(self, id):
        fm = FileManager()
        rows = fm.read_csv()
        for r in rows:
            if int(r["id"]) == id:
                return User(id, r["name"], r["email"])
        return None
