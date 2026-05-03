from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_password():
    data = request.get_json()
    
    length = int(data.get('length', 12))
    include_uppercase = data.get('uppercase', True)
    include_lowercase = data.get('lowercase', True)
    include_numbers = data.get('numbers', True)
    include_symbols = data.get('symbols', True)
    
    char_set = ""
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_lowercase:
        char_set += string.ascii_lowercase
    if include_numbers:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation
        
    if not char_set:
        return jsonify({"error": "At least one character type must be selected"}), 400
        
    password = ''.join(random.choice(char_set) for _ in range(length))
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
