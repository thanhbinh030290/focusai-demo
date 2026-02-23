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
<h1>FocusAI - AI Tutor</h1>

<form method="post">
Tên: <input name="username"><br><br>
Câu hỏi: <input name="question"><br><br>
<button type="submit">Hỏi AI</button>
</form>

<h3>Trả lời:</h3>
<p>{{answer}}</p>

<h3>Điểm của bạn: {{score}}</h3>
"""

@app.route("/", methods=["GET","POST"])
def home():
    answer = ""
    score = 0

    if request.method == "POST":
        user = request.form["username"]
        question = request.form["question"]

        answer = simple_ai(question)

        if user not in points:
            points[user] = 0

        points[user] += 10
        score = points[user]

    return render_template_string(HTML, answer=answer, score=score)

app.run(host="0.0.0.0", port=5000)
