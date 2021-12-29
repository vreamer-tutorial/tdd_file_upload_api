from flask import Flask, request
app = Flask(__name__)

@app.route('/file/upload', methods=['POST'])
def upload_file():
    file_name = request.form.get('file_name')
    file = request.files.get('file')

    return {
        'file_name': file_name,
        'file_content': file.read().decode("utf-8")
    }, 201


    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')