from flask import Blueprint, jsonify

categories_blueprint = Blueprint('categories', __name__)

@categories_blueprint.route('/api/json/v1/categories', methods=['GET'])
def get_categories():
    categories = [
        {
            "idCategory": "11",
            "strCategory": "Daging",
            "strCategoryThumb": "https://www.themealdb.com/images/category/beef.png",
        },
        {
            "idCategory": "12",
            "strCategory": "Ayam",
            "strCategoryThumb": "https://www.themealdb.com/images/category/chicken.png",
        },
        {
            "idCategory": "13",
            "strCategory": "Seafood",
            "strCategoryThumb": "https://www.themealdb.com/images/category/seafood.png",
        },
        {
            "idCategory": "14",
            "strCategory": "Sayuran",
            "strCategoryThumb": "https://www.themealdb.com/images/category/vegetarian.png",
        },
        {
            "idCategory": "15",
            "strCategory": "Sarapan",
            "strCategoryThumb": "https://www.themealdb.com/images/category/breakfast.png",
        },
        {
            "idCategory": "16",
            "strCategory": "Pembuka",
            "strCategoryThumb": "https://www.themealdb.com/images/category/starter.png",
        }
    ]
    return jsonify({"categories": categories})