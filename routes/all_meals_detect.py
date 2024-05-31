from flask import jsonify, Blueprint

all_meals_detect_blueprint = Blueprint('all_meals_detect', __name__)

@all_meals_detect_blueprint.route('/api/json/v1/all_meals_detect/<kategori>', methods=['GET'])
def get_all_meals_detect(kategori):
    meals = []
    if 'Kentang' in kategori and 'Kembang Kol' in kategori:
        meals.extend([
            {
                "strMeal": "Tomat, Kentang & Kembang Kol Dish",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg",
                "idMeal": "a01"
            }
        ])
    
    if 'Tomat' in kategori and 'Kentang' in kategori and 'Kembang Kol' in kategori:
        meals.extend([
            {
                "strMeal": "Tomat, Kentang & Kembang Kol Dish",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg",
                "idMeal": "b01"
            }
        ])

    if not meals:
        return jsonify({"message": "No meals found for the specified categories"}), 404

    return jsonify({"meals": meals})