import os, jwt, json, pymysql
from flask import Flask, render_template, request, jsonify, send_from_directory
from features.image_classifier import classify_image
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity

from routes.categories import categories_blueprint
from routes.meals import meals_blueprint
from routes.recipe import recipe_blueprint
from routes.categories_detect import categories_detect_blueprint
from routes.meals_detect import meals_detect_blueprint
from routes.all_categories_detect import all_categories_detect_blueprint
from routes.all_meals_detect import all_meals_detect_blueprint

app = Flask(__name__, static_folder='img')
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

app.config['SECRET_KEY'] = 'fdlahmd'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lalaland88'
app.config['MYSQL_DB'] = 'nutrichef'

db = pymysql.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'], 
                     password=app.config['MYSQL_PASSWORD'], db=app.config['MYSQL_DB'])
cursor = db.cursor()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = get_user(data['email'])
        except:
            return jsonify({'error': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img/<path:filename>') 
def send_file(filename): 
    return send_from_directory(app.static_folder, filename)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part'})

    files = request.files.getlist('files[]')
    results = []

    for file in files:
        if file.filename == '':
            continue

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        predicted_class = classify_image(file_path)

        predicted_class = predicted_class.replace('_', ' ')

        results.append({'class': predicted_class})

    return jsonify({'results': results})

#----Auth----

def insert_user(username, email, password):
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, (username, email, password))
    db.commit()

def get_user(email):
    sql = "SELECT * FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    return cursor.fetchone()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if get_user(email):
        return jsonify({'error': 'Email sudah ada'}), 400

    password_hash = generate_password_hash(password)
    insert_user(username, email, password_hash)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user(email)
    if not user or not check_password_hash(user[3], password):
        return jsonify({'error': 'Invalid email or password'}), 401

    token = jwt.encode({'email': email}, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token}), 200

@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logout successful'}), 200

def get_username(email):
    sql = "SELECT username FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    return cursor.fetchone()

@app.route('/username/<string:email>', methods=['GET'])
def get_username_by_email(email):
    try:
        username = get_username(email)
        if username:
            return jsonify({'username': username[0]}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#----Diseases-----

def insert_disease(name):
    sql = "INSERT INTO diseases (name) VALUES (%s)"
    cursor.execute(sql, (name,))
    db.commit()

def get_disease(name):
    sql = "SELECT * FROM diseases WHERE name = %s"
    cursor.execute(sql, (name,))
    return cursor.fetchone()

@app.route('/diseases', methods=['POST'])
def disease():
    data = request.get_json()
    name = data.get('name')

    if get_disease(name):
        return jsonify({'error': 'Disease already exists'}), 400

    insert_disease(name)
    return jsonify({'message': 'Disease registered successfully'}), 201

@app.route('/diseases', methods=['GET'])
def get_all_diseases():
    try:
        # Execute SQL query to fetch all diseases
        cursor.execute("SELECT * FROM diseases")
        diseases = cursor.fetchall()

        # Prepare response data
        disease_list = []
        for disease in diseases:
            disease_data = {
                'id': disease[0],
                'name': disease[1]
            }
            disease_list.append(disease_data)

        return jsonify({'diseases': disease_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#----diseases detail-----

def insert_disease_detail(disease_id, data):
    # Convert data dictionary to JSON string
    data_json = json.dumps(data)
    
    sql = "INSERT INTO diseases_detail (disease_id, data) VALUES (%s, %s)"
    cursor.execute(sql, (disease_id, data_json))
    db.commit()

def get_disease_detail(disease_id):
    sql = "SELECT * FROM diseases_detail WHERE disease_id = %s"
    cursor.execute(sql, (disease_id,))
    return cursor.fetchone()

@app.route('/diseases_detail', methods=['POST'])
def add_disease_detail():
    data = request.get_json()
    disease_id = data.get('disease_id')

    if get_disease_detail(disease_id):
        return jsonify({'error': 'Disease already exists'}), 400

    # Insert disease details into diseases_detail table
    if 'data' in data:
        data_json = data.get('data')
        insert_disease_detail(disease_id, data_json)

    return jsonify({'message': 'Disease and details registered successfully'}), 201

@app.route('/diseases_detail/<int:id>', methods=['GET'])
def get_disease_detail_info(id):
    try:
        # Retrieve disease details from the database based on disease_id
        cursor.execute("SELECT d.name, dd.data FROM diseases_detail dd INNER JOIN diseases d ON dd.disease_id = d.id WHERE dd.disease_id = %s", (id,))
        disease_detail = cursor.fetchone()

        if not disease_detail:
            return jsonify({'error': 'Disease details not found'}), 404

        # Parse the JSON data field
        data_json = json.loads(disease_detail[1])

        # Prepare response data
        response_data = {
            'id': id,
            'name': disease_detail[0],
            'data': data_json
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/diseases_detail', methods=['GET'])
def get_all_diseases_detail():
    try:
        # Execute SQL query to fetch all diseases
        cursor.execute("SELECT * FROM diseases_detail")
        diseases = cursor.fetchall()

        # Prepare response data
        disease_list = []
        for disease in diseases:
            disease_data = {
                'id': disease[0],
                'name': disease[1]
            }
            disease_list.append(disease_data)

        return jsonify({'diseases': disease_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#----penyakit user----#

def get_user_penyakit(id):
    sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql, (id,))
    return cursor.fetchone()

def get_disease_detail_id(disease_id):
    sql = "SELECT * FROM diseases_detail WHERE id = %s"
    cursor.execute(sql, (disease_id,))
    return cursor.fetchone()

@app.route('/penyakit_user', methods=['POST'])
@token_required
def add_penyakit_user(current_user):
    try:
        # Parse request JSON
        data = request.get_json()
        user_id = current_user[0]  # Assuming user ID is the first element of current_user
        diseases_detail_id = data.get('diseases_detail_id')

        # Check if the user and disease detail exist
        if not get_user_penyakit(user_id):
            return jsonify({'error': 'User not found'}), 404

        if not get_disease_detail_id(diseases_detail_id):
            return jsonify({'error': 'Disease detail not found'}), 404

        # Insert into penyakit_user table
        sql = "INSERT INTO penyakit_user (user_id, diseases_detail_id) VALUES (%s, %s)"
        cursor.execute(sql, (user_id, diseases_detail_id))
        db.commit()

        return jsonify({'message': 'Penyakit user association added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_penyakit_user(user_id):
    try:
        sql = "SELECT p.id, p.user_id, p.diseases_detail_id, d.data, dd.name as disease_name \
               FROM penyakit_user p \
               INNER JOIN diseases_detail d ON p.diseases_detail_id = d.id \
               INNER JOIN diseases dd ON d.disease_id = dd.id \
               WHERE p.user_id = %s"
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()
    except Exception as e:
        return None, str(e)

@app.route('/penyakit_user/<int:user_id>', methods=['GET'])
@token_required
def get_user_penyakit(current_user, user_id):
    try:
        # Check if the current user matches the requested user_id
        if current_user[0] != user_id:
            return jsonify({'error': 'Unauthorized user'}), 401

        # Retrieve penyakit_user associations for the specified user
        penyakit_user_associations = get_penyakit_user(user_id)

        # If associations found, prepare response data
        if penyakit_user_associations:
            response_data = []
            for association in penyakit_user_associations:
                penyakit_user_id, user_id, diseases_detail_id, diseases_detail_data, disease_name = association
                response_data.append({
                    'penyakit_user_id': penyakit_user_id,
                    'user_id': user_id,
                    'diseases_detail_id': diseases_detail_id,
                    'diseases_detail_data': json.loads(diseases_detail_data),
                    'disease_name': disease_name
                })
            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'No penyakit_user associations found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.route('/penyakit', methods=['GET'])
# @token_required
# def get_penyakit():
#     try:
#         token = request.headers.get('Authorization')
#         data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#         current_user = get_user(data['email'])

#         if not current_user:
#             return jsonify({'error': 'User not found'}), 404

#         # Fetch diseases associated with the authenticated user
#         cursor.execute("SELECT * FROM penyakit WHERE user_id = %s", (current_user[0],))
#         penyakitt = cursor.fetchall()

#         # Prepare response data
#         list_penyakit = []
#         for penyakit in penyakitt:
#             data_penyakit = {
#                 'id': penyakit[0],
#                 'name': penyakit[1],
#             }
#             list_penyakit.append(data_penyakit)

#         return jsonify({'penyakitt': list_penyakit}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

app.register_blueprint(categories_blueprint)
app.register_blueprint(meals_blueprint)
app.register_blueprint(recipe_blueprint)
app.register_blueprint(categories_detect_blueprint)
app.register_blueprint(meals_detect_blueprint)
app.register_blueprint(all_categories_detect_blueprint)
app.register_blueprint(all_meals_detect_blueprint)

if __name__ == '__main__':
    app.run(host='192.168.96.16', port=5000,debug=True)
    # app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)



#----penyakit user----#

def get_user_penyakit(id):
    sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql, (id,))
    return cursor.fetchone()

def get_disease_detail_id(disease_id):
    sql = "SELECT * FROM diseases_detail WHERE disease_id = %s"
    cursor.execute(sql, (disease_id,))
    return cursor.fetchone()

@app.route('/penyakit_user', methods=['POST'])
@jwt_required()
def add_penyakit_user():
    try:
        current_user = get_jwt_identity()
        user_id = get_user(current_user)[0]  # Assuming user ID is the first element

        data = request.get_json()
        disease_id = data.get('disease_id')

        if not get_user_penyakit(user_id):
            return jsonify({'error': 'User not found'}), 404

        # Fetch diseases_detail_id from diseases_detail table based on disease_id
        disease_detail = get_disease_detail_id(disease_id)
        if not disease_detail:
            return jsonify({'error': 'Disease detail not found'}), 404

        diseases_detail_id = disease_detail[0]  # Assuming id is the first column

        # Insert into penyakit_user table with user_id and diseases_detail_id
        sql = "INSERT INTO penyakit_user (user_id, diseases_detail_id) VALUES (%s, %s)"
        cursor.execute(sql, (user_id, diseases_detail_id))
        db.commit()

        return jsonify({'message': 'Penyakit user association added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_penyakit_user(user_id):
    try:
        sql = "SELECT p.id, p.user_id, p.diseases_detail_id, d.data, dd.name as disease_name \
               FROM penyakit_user p \
               INNER JOIN diseases_detail d ON p.diseases_detail_id = d.id \
               INNER JOIN diseases dd ON d.disease_id = dd.id \
               WHERE p.user_id = %s"
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()
    except Exception as e:
        return None, str(e)

@app.route('/penyakit_user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_penyakit(user_id):
    try:
        current_user = get_jwt_identity()
        if current_user != user_id:
            return jsonify({'error': 'Unauthorized user'}), 401

        penyakit_user_associations = get_penyakit_user(user_id)
        if penyakit_user_associations:
            response_data = []
            for association in penyakit_user_associations:
                penyakit_user_id, user_id, diseases_detail_id, diseases_detail_data, disease_name = association
                response_data.append({
                    'penyakit_user_id': penyakit_user_id,
                    'user_id': user_id,
                    'diseases_detail_id': diseases_detail_id,
                    'diseases_detail_data': json.loads(diseases_detail_data),
                    'disease_name': disease_name
                })
            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'No penyakit_user associations found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500