from flask import Blueprint, jsonify

meals_by_diseases_blueprint = Blueprint('meals_by_diseases', __name__)

@meals_by_diseases_blueprint.route('/api/json/v1/meals_by_diseases', methods=['GET'])
def get_meals_by_diseases():
    meals = [
            {
                "strMeal": "Daging Sapi Kecap",
                "strMealThumb": "http://192.168.49.16:5000/img/daging-kecap.png",
                "idMeal": "1101"
            },
            {
                "strMeal": "Beef and Oyster pie",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg",
                "idMeal": "1102"
            },
            {
                "strMeal": "Beef Asado",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/pkopc31683207947.jpg",
                "idMeal": "1103"
            }
        ]
    return jsonify({"meals": meals})