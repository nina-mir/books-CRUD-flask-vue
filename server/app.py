import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
# more info on config can be found here: https://github.com/mpdavis/319-project/blob/master/flask/config.py
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# list of books
BOOKS = [
    {
        "id": uuid.uuid4().hex,
        "title": "On the Road",
        "author": "Jack Kerouac",
        "read": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "People Immortal",
        "author": "Vasily Grossman",
        "read": True,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Green Eggs and Ham",
        "author": "Dr. Seuss",
        "read": False,
    },
]


# Books info route
@app.route("/books", methods=["GET", "POST"])
def all_books():
    """return the BOOKS list as a JSON object"""
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        BOOKS.append(
            {
                "id": uuid.uuid4().hex,
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "read": post_data.get("read"),
            }
        )
        response_object["message"] = "Book added!"
    else:
        response_object["books"] = BOOKS
    return jsonify(response_object)


@app.route("/books/<book_id>", methods=["PUT", "DELETE"])
def single_book(book_id):
    """update the information about a book entry or remove a book"""
    response_object = {"status": "success"}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append(
            {
                "id": uuid.uuid4().hex,
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "read": post_data.get("read"),
            }
        )
        response_object["message"] = "Book updated!"
    if request.method == "DELETE":
        remove_book(book_id)
        response_object["message"] = "Book removed!"
    return jsonify(response_object)


def remove_book(book_id):
    """helper function for single_book edit"""
    for book in BOOKS:
        if book["id"] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    """sanity check route"""
    return jsonify("pong from FLASK!!!")


if __name__ == "__main__":
    app.run()
