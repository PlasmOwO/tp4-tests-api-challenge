from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}
next_id = 1

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Name required'}), 400
    user = {'id': next_id, 'name': data['name']}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

# TODO: Implémenter GET /users/<id>
# TODO: Implémenter DELETE /users/<id>

if __name__ == '__main__':
    app.run(debug=True)

