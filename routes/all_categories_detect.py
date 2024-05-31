from flask import Blueprint, jsonify

all_categories_detect_blueprint = Blueprint('all_categories_detect', __name__)

@all_categories_detect_blueprint.route('/api/json/v1/all_categories_detect/<kategori>', methods=['GET'])
def get_all_categories_detect(kategori):
    
    requested_categories = kategori.split(',')

    response_data = {"categories": []}

    # Membuat irisan setiap kategori yang akan menampilkan data baru
    if set(requested_categories) == {'Kentang', 'Kembang Kol'}:
        data_kentang_kembangkol = {
            "idCategory": "21",
            "strCategory": "Kentang & Kembang Kol",
            "strCategoryThumb": "http://192.168.49.16:5000/img/kentang.png",
            "strCategoryDescription": "Description for Kentang & Kembang Kol..."
        }
        response_data["categories"].append(data_kentang_kembangkol)
    elif set(requested_categories) == {'Tomat', 'Kentang', 'Kembang Kol'}:
        data_tomat_kentang_kembangkol = {
            "idCategory": "22",
            "strCategory": "Tomat, Kentang & Kembang Kol",
            "strCategoryThumb": "http://192.168.49.16:5000/img/kentang.png",
            "strCategoryDescription": "Description for Tomat, Kentang & Kembang Kol..."
        }
        response_data["categories"].append(data_tomat_kentang_kembangkol)

    return jsonify(response_data)
