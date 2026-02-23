from flask import Flask, request, render_template_string

app = Flask(__name__)

points = {}

def simple_ai(question):
    question = question.lower()

    if "pitago" in question:
        return "Định lý Pitago: Trong tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông."
    elif "đạo hàm" in question:
        return "Đạo hàm biểu thị tốc độ thay đổi của một hàm số tại một điểm."
    elif "cách mạng tháng 8" in question:
        return "Cách mạng tháng 8 năm 1945 đã giúp Việt Nam giành độc lập."
    else:
        return "Câu hỏi rất hay! Hãy thử diễn đạt rõ hơn để AI có thể hỗ trợ tốt hơn."

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
            width: 400px;
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
            padding: 10px;
            border-radius: 8px;
        }

        .score {
            margin-top: 10px;
            font-weight: bold;
            color: #444;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>FocusAI 🤖</h1>
        <form method="post">
            <input name="username" placeholder="Nhập tên của bạn"><br>
            <input name="question" placeholder="Nhập câu hỏi..."><br>
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
    </div>
</body>
</html>
"""
