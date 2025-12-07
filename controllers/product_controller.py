from flask import Blueprint, render_template
from repositories.repository_factory import RepositoryFactory

product_bp = Blueprint("product", __name__, url_prefix="/products")


@product_bp.route("/")
def list_products():
    repo = RepositoryFactory.get_repository("product")
    products = repo.get_all()
    return render_template("product/list.html", products=products)


@product_bp.route("/<int:id>")
def view_product(id):
    repo = RepositoryFactory.get_repository("product")
    product = repo.get_by_id(id)
    return render_template("product/detail.html", product=product)
