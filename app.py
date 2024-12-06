from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route for rendering the calculator interface
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Parse the JSON data from the frontend
        data = request.get_json()
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation')

        # Perform the calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed.'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation.'}), 400

        # Return the result as JSON
        return jsonify({'result': result})

    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

