from flask import Blueprint, jsonify

categories_detect_blueprint = Blueprint('categories_detect', __name__)

@categories_detect_blueprint.route('/api/json/v1/categories_detect/<kategori>', methods=['GET'])
def get_categories_detect(kategori):
    requested_categories = kategori.split(',')

    response_data = {"categories": []}

    for category in requested_categories:
        if category == 'Kentang':
            data = {
                "idCategory": "1",
                "strCategory": "Kentang",
                "strCategoryThumb": "http://192.168.49.16:5000/img/kentang.png",
                "strCategoryDescription": "Beef is the culinary name for meat from cattle..."
            }
        elif category == 'Kembang Kol':
            data = {
                "idCategory": "2",
                "strCategory": "Kembang Kol",
                "strCategoryThumb": "http://192.168.49.16:5000/img/kembang-kol.png",
                "strCategoryDescription": "Chicken is a type of domesticated fowl..."
            }
        elif category == 'Kubis':
            data = {
                "idCategory": "3",
                "strCategory": "Kubis",
                "strCategoryThumb": "http://192.168.49.16:5000/img/kubis.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        elif category == 'Labu':
            data = {
                "idCategory": "4",
                "strCategory": "Labu",
                "strCategoryThumb": "http://192.168.49.16:5000/img/labu.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        elif category == 'Paprika':
            data = {
                "idCategory": "5",
                "strCategory": "Paprika",
                "strCategoryThumb": "http://192.168.49.16:5000/img/paprika.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        elif category == 'Timun':
            data = {
                "idCategory": "6",
                "strCategory": "Timun",
                "strCategoryThumb": "http://192.168.49.16:5000/img/timun.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        elif category == 'Tomat':
            data = {
                "idCategory": "7",
                "strCategory": "Tomat",
                "strCategoryThumb": "http://192.168.49.16:5000/img/tomat.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        elif category == 'Wortel':
            data = {
                "idCategory": "8",
                "strCategory": "Wortel",
                "strCategoryThumb": "http://192.168.49.16:5000/img/wortel.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        elif category == 'Brokoli':
            data = {
                "idCategory": "9",
                "strCategory": "Brokoli",
                "strCategoryThumb": "http://192.168.49.16:5000/img/brokoli.png",
                "strCategoryDescription": "Dessert is a course that concludes a meal..."
            }
        else:
            return jsonify({"message": f"Kategori '{category}' not found"}), 404

        response_data["categories"].append(data)

    return jsonify(response_data)
