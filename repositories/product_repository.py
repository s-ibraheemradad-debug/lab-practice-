from models.product import Product
from core.file_singleton import FileManager


class ProductRepository:
    def __init__(self):
        # Get the singleton file manager
        self.file = FileManager()

    def get_all(self):
        rows = self.file.read_csv("data/products.csv")
        return [Product(int(r["id"]), r["name"], float(r["price"])) for r in rows]

    def get_by_id(self, id):
        all_products = self.get_all()
        for product in all_products:
            if product.id == id:
                return product
        return None
