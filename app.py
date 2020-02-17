from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes/add')
def add_note():
    return render_template('add.html')

@app.route('/notes/store', methods=['POST'])
def store_note():
    return render_template('index.html')

@app.route('/notes/show/<string:id>')
def show_note(id):
    return render_template('show.html', id=id)

@app.route('/notes/edit/<string:id>')
def edit_note(id):
    return render_template('edit.html', id=id)

@app.route('/notes/update', methods=['POST'])
def update_note():
    return render_template('index.html')

@app.route('/notes/destroy/<string:id>')
def destroy_note(id):
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()