"""main
メイン
"""

from flask import Flask, jsonify

app = Flask(__name__)

# サンプルデータ
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]


# 全ての本を取得
@app.route("/", methods=["GET"])
def get_books():
    """
    本一覧を取得する関数
    """
    return jsonify({"books": books})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
