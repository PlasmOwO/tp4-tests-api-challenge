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


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user),200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)

