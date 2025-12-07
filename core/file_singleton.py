# import csv


# class FileManager:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(FileManager, cls).__new__(cls)
#         return cls._instance

#     def read_csv(self, path):
#         with open(path, newline='') as f:
#             return list(csv.DictReader(f))


import csv


class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = "data/users.csv"
        return cls._instance

    def read_csv(self, path=None):
        path = path or self.file_path
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
