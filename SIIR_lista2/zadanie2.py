from flask import Flask, request

app = Flask(__name__)


@app.route('/file/get/<name>', methods=['GET'])
def get_file(name):
    no_of_line = int(request.args.get('linia') or 0)
    file_content = get_file_content(name)
    if no_of_line > len(file_content):
        return f"Nie ma takiej linii"
    if no_of_line == 0:
        return "\n".join(file_content)
    else:
        return file_content[no_of_line - 1]


@app.route('/file/post', methods=['POST'])
def post_file():
    file_content = request.files['file']
    filename = file_content.filename
    file_content.save(filename)
    return "Plik zapisany z powodzeniem"


def get_file_content(name):
    lines = []
    try:
        with open(f"{name}.txt") as file:
            lines = file.readlines()
    except:
        return "Taki plik nie istnieje"
    return lines
 

if __name__ == "__main__":
    app.run(debug = True)