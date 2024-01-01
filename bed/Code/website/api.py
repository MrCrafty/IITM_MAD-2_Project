from flask import Blueprint
from .models import Category
from . import db

api = Blueprint("api", __name__)


@api.route('/getCategories', methods=['GET'])
def getCategories():
    categories = []
    for category in Category.query.all():
        item = {
            "categoryId": category.categoryId,
            "categoryName": category.categoryName
        }
        categories.append(item)
    return categories


@api.route('/createCategory', methods=["POST"])
def createCategory():
    category = Category(categoryName="test")
    db.session.add(category)
    db.session.commit()
    return "Created"
