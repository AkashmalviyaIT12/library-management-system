from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define routes and views

if __name__ == '__main__':
    app.run(debug=True)

books = []  # A list to store the books

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        book = {'title': title, 'author': author}
        books.append(book)
        return redirect('/display')
    return render_template('addbook.html')

@app.route('/search', methods=['GET', 'POST'])
def search_book():
    if request.method == 'POST':
        title = request.form['title']
        results = []
        for book in books:
            if book['title'].lower() == title.lower():
                results.append(book)
        return render_template('searchresults.html', results=results)
    return render_template('searchbook.html')

@app.route('/display')
def display_books():
    return render_template('displaybooks.html', books=books)
