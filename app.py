from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

points = {}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>FocusAI - AI Tutor</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            width: 420px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            color: #333;
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 10px;
        }

        button:hover {
            background: #5563c1;
        }

        .answer {
            margin-top: 20px;
            text-align: left;
            background: #f4f6ff;
            padding: 12px;
            border-radius: 8px;
            font-size: 14px;
        }

        .score {
            margin-top: 10px;
            font-weight: bold;
            color: #444;
        }

        .footer {
            margin-top: 15px;
            font-size: 12px;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>FocusAI 🤖</h1>

        <form method="post">
            <input name="username" placeholder="Nhập tên của bạn" required><br>
            <input name="question" placeholder="Nhập câu hỏi..." required><br>
            <button type="submit">Hỏi AI</button>
        </form>

        {% if answer %}
        <div class="answer">
            <b>Trả lời:</b><br>
            {{answer}}
        </div>
        {% endif %}

        {% if score %}
        <div class="score">
            Điểm của bạn: {{score}}
        </div>
        {% endif %}

        <div class="footer">
            Powered by AI 🚀
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
  @app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    score = None

    if request.method == "POST":
        username = request.form["username"]
        question = request.form["question"]

       answer = f"AI đang giải thích câu hỏi: {question}\n\nĐịnh lý Pitago: Trong tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông."

        if username not in points:
            points[username] = 0

        points[username] += 10
        score = points[username]

    return render_template_string(HTML, answer=answer, score=score)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
