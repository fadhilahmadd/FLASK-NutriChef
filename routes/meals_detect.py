from flask import jsonify, Blueprint

meals_detect_blueprint = Blueprint('meals_detect', __name__)

@meals_detect_blueprint.route('/api/json/v1/meals_detect/<kategori>', methods=['GET'])
def get_meals_detect(kategori):
    if kategori == 'Kentang':
        meals = [
            {
                "strMeal": "Beef and Mustard Pie",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/sytuqu1511553755.jpg",
                "idMeal": "1001"
            },
            {
                "strMeal": "Beef and Oyster pie",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/wrssvt1511556563.jpg",
                "idMeal": "1002"
            },
            {
                "strMeal": "Beef Asado",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/pkopc31683207947.jpg",
                "idMeal": "1003"
            }
        ]
    elif kategori == 'Kembang Kol':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "2001"
            }
        ]
    elif kategori == 'Kubis':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "3001"
            }
        ]
    elif kategori == 'Labu':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "4001"
            }
        ]
    elif kategori == 'Paprika':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "5001"
            }
        ]
    elif kategori == 'Timun':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "6001"
            }
        ]
    elif kategori == 'Tomat':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "7001"
            }
        ]
    elif kategori == 'Wortel':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "8001"
            }
        ]
    elif kategori == 'Brokoli':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "9001"
            }
        ]
    elif kategori == 'Daging':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "1101"
            }
        ]
    elif kategori == 'Ayam':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "1201"
            }
        ]
    elif kategori == 'Seafood':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "1301"
            }
        ]
    elif kategori == 'Sayuran':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "1401"
            }
        ]
    elif kategori == 'Sarapan':
        meals = [
            {
                "strMeal": "Ayam Percik",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
                "idMeal": "1501"
            }
        ]
    elif kategori == 'Pembuka':
        meals = [
            {
                "strMeal": "Tumis Brokoli Bawang Putih",
                "strMealThumb": "https://www.themealdb.com/images/media/meals/adxcbq1619787919.jpg",
                "idMeal": "1601"
            }
        ]
    else:
        return jsonify({"message": "Category not found"})

    return jsonify({"meals": meals})