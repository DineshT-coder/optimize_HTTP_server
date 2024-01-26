from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name:
        file_path = f'/tmp/data/{file_name}.txt'

        if line_number:
            return get_line_from_file(file_path, int(line_number))
        else:
            return get_whole_file(file_path)

    return jsonify({'error': 'Invalid request'})

def get_line_from_file(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if 0 < line_number <= len(lines):
            return jsonify({'line_content': lines[line_number - 1]})
        else:
            return jsonify({'error': 'Invalid line number'})

def get_whole_file(file_path):
    with open(file_path, 'r') as file:
        return jsonify({'file_content': file.read()})

