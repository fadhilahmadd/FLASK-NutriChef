from flask import jsonify, Blueprint

meals_blueprint = Blueprint('meals', __name__)


@meals_blueprint.route('/api/json/v1/meals/<category>', methods=['GET'])
def get_meals(category):
    if category == 'Daging':
        meals = [
            {
                "strMeal": "Daging Sapi Kecap",
                "strMealThumb": "http://192.168.100.34:5000/img/daging-kecap.png",
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
    elif category == 'Ayam':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "1201"
            },
            {
                "strMeal": "Brown Stew Chicken",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg",
                "idMeal": "1202"
            },
            {
                "strMeal": "Chick-Fil-A Sandwich",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/sbx7n71587673021.jpg",
                "idMeal": "1203"
            }
        ]
    elif category == 'Seafood':
        meals = [
            {
                "strMeal": "Baked salmon with fennel & tomatoes",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/1548772327.jpg",
                "idMeal": "1301"
            },
            {
                "strMeal": "Cajun spiced fish tacos",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/uvuyxu1503067369.jpg",
                "idMeal": "1302"
            },
            {
                "strMeal": "Escovitch Fish",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/1520084413.jpg",
                "idMeal": "1303"
            },
        ]
    elif category == 'Sayuran':
        meals = [
            {
                "strMeal": "Bubur Manado (Tinutuan)",
                "strMealThumb": "http://192.168.100.34:5000/img/bubur-manado.jpeg",
                "idMeal": "1401"
            },
            {
                "strMeal": "Cap Cay",
                "strMealThumb": "http://192.168.100.34:5000/img/capcay.jpeg",
                "idMeal": "1402"
            },
            {
                "strMeal": "Tumis Buncis",
                "strMealThumb": "http://192.168.100.34:5000/img/tumis-buncis.jpeg",
                "idMeal": "1403"
            },
            {
                "strMeal": "Tumis Brokoli Jamur Tiram",
                "strMealThumb": "http://192.168.100.34:5000/img/tumis-brokoli-jamur-tiram.jpeg",
                "idMeal": "1404"
            },
        ]
    elif category == 'Sarapan':
        meals = [
            {
                "strMeal": "Bread omelette",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/hqaejl1695738653.jpg",
                "idMeal": "1501"
            },
        ]
    elif category == 'Pembuka':
        meals = [
            {
                "strMeal": "Broccoli & Stilton soup",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/tvvxpv1511191952.jpg",
                "idMeal": "1601"
            },
        ]
    else:
        return jsonify({"message": "Category not found"})

    return jsonify({"meals": meals})
