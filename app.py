from flask import Flask, request, render_template_string

app = Flask(__name__)

# Lưu điểm tạm thời (demo)
points = {}
streaks = {}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>FocusAI - Smart Learning AI</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            width: 450px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }

        h1 { margin-bottom: 10px; }

        input {
            width: 92%;
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
            margin-top: 8px;
        }

        button:hover { background: #5563c1; }

        .answer {
            margin-top: 15px;
            text-align: left;
            background: #f4f6ff;
            padding: 12px;
            border-radius: 8px;
            font-size: 14px;
            white-space: pre-line;
        }

        .score {
            margin-top: 10px;
            font-weight: bold;
        }

        .badge {
            margin-top: 8px;
            color: #ff9800;
            font-weight: bold;
        }

        .warning {
            background: #fff3cd;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
            font-size: 14px;
        }

        .footer {
            margin-top: 12px;
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
        <input name="question" placeholder="Nhập câu hỏi hoặc chia sẻ cảm xúc..." required><br>
        <button type="submit">Hỏi AI</button>
    </form>

    <form method="post">
        <input type="hidden" name="mock" value="screen">
        <input name="username" placeholder="Nhập lại tên để giả lập screen time"><br>
        <button type="submit">Giả lập đã dùng MXH 45 phút</button>
    </form>

    {% if warning %}
        <div class="warning">
            {{warning}}
        </div>
    {% endif %}

    {% if answer %}
        <div class="answer">
            <b>FocusAI:</b><br>
            {{answer}}
        </div>
    {% endif %}

    {% if score %}
        <div class="score">
            Điểm Focus: {{score}} | Level: {{level}}
        </div>
        {% if badge %}
            <div class="badge">
                🎖 Badge đạt được: {{badge}}
            </div>
        {% endif %}
    {% endif %}

    <div class="footer">
        Smart Learning • Mental Health Guard • Gamification 🚀
    </div>
</div>
</body>
</html>
"""

# ----------- LOGIC AI ------------

def detect_emotion(text):
    sad_keywords = ["mệt", "chán", "áp lực", "stress", "buồn", "không muốn học", "lo lắng"]
    for word in sad_keywords:
        if word in text.lower():
            return True
    return False


def tutor_logic(question):
    q = question.lower()

    if "pitago" in q:
        return "Định lý Pitago: Trong tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông."
    elif "đạo hàm" in q:
        return "Đạo hàm là giới hạn của tỉ số giữa sự thay đổi của hàm số và biến số khi biến số tiến đến 0."
    elif "tiếng anh" in q:
        return "Mẹo học tiếng Anh: Mỗi ngày 10 phút từ vựng + 5 phút nghe là đủ để tạo tiến bộ dài hạn."
    else:
        return "AI đang phân tích câu hỏi của bạn và đưa ra hướng học tập phù hợp theo chương trình Bộ Giáo dục."


@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    score = None
    level = None
    badge = None
    warning = None

    if request.method == "POST":

        # Giả lập screen time
        if "mock" in request.form:
            username = request.form.get("username")

            if username:
                warning = f"{username}, bạn đã dùng mạng xã hội 45 phút. Thử làm 1 quiz 10 phút để giữ streak nhé! 🔥"
            else:
                warning = "Vui lòng nhập tên để giả lập."

        else:
            username = request.form["username"]
            question = request.form["question"]

            # Health Guard
            if detect_emotion(question):
                answer = f"{username}, mình cảm nhận bạn đang hơi áp lực. Hãy thử bài thở 4-4-4: hít vào 4 giây, giữ 4 giây, thở ra 4 giây. Mình luôn ở đây để hỗ trợ bạn 💙"
            else:
                explanation = tutor_logic(question)
                answer = f"{username}, đây là phần giải thích cho bạn:\n\n{explanation}"

            # Tính điểm
            if username not in points:
                points[username] = 0
                streaks[username] = 0

            points[username] += 10
            streaks[username] += 1

            score = points[username]
            level = score // 50 + 1

            # Badge system
            if score >= 100:
                badge = "Chiến binh Focus"
            elif streaks[username] >= 5:
                badge = "5 ngày chăm chỉ"
            elif score >= 50:
                badge = "Người bắt đầu nghiêm túc"

    return render_template_string(
        HTML,
        answer=answer,
        score=score,
        level=level,
        badge=badge,
        warning=warning
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
