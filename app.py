from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# ====== Memory Storage (demo only) ======
points = {}
streaks = {}
user_profiles = {}

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>FocusAI 2.0</title>
<style>
body {
    margin:0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#667eea,#764ba2);
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
}
.card {
    background:white;
    padding:25px;
    border-radius:15px;
    width:480px;
    box-shadow:0 10px 25px rgba(0,0,0,0.2);
    text-align:center;
}
h1 { margin-bottom:10px; }
input {
    width:92%;
    padding:10px;
    margin:8px 0;
    border-radius:8px;
    border:1px solid #ccc;
}
button {
    background:#667eea;
    color:white;
    border:none;
    padding:10px 20px;
    border-radius:8px;
    cursor:pointer;
    font-weight:bold;
    margin-top:8px;
}
button:hover { background:#5563c1; }
.answer {
    margin-top:15px;
    text-align:left;
    background:#f4f6ff;
    padding:12px;
    border-radius:8px;
    font-size:14px;
    white-space:pre-line;
}
.mode {
    font-size:12px;
    color:#666;
    margin-top:6px;
}
.progress {
    background:#eee;
    border-radius:10px;
    height:10px;
    margin-top:8px;
}
.progress-bar {
    height:10px;
    border-radius:10px;
    background:#667eea;
}
.stats {
    margin-top:15px;
    font-size:13px;
    color:#444;
}
.footer {
    margin-top:12px;
    font-size:12px;
    color:#888;
}
.warning {
    background:#fff3cd;
    padding:10px;
    border-radius:8px;
    margin-top:10px;
}
.badge {
    color:#ff9800;
    font-weight:bold;
    margin-top:6px;
}
</style>
</head>
<body>
<div class="card">

<h1>FocusAI {{avatar}}</h1>

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
<div class="warning">{{warning}}</div>
{% endif %}

{% if answer %}
<div class="answer">
<b>FocusAI:</b><br>
{{answer}}
</div>
<div class="mode">AI Mode: {{mode}}</div>
{% endif %}

{% if score %}
<div style="margin-top:10px;font-weight:bold;">
Điểm: {{score}} | Level: {{level}}
</div>

<div class="progress">
<div class="progress-bar" style="width:{{progress}}%;"></div>
</div>

{% if badge %}
<div class="badge">🎖 {{badge}}</div>
{% endif %}

<div class="stats">
Tuần này:<br>
✔ {{streak}} ngày streak<br>
✔ Giảm 32% thời gian lướt mạng<br>
✔ 3 lần AI can thiệp kịp thời
</div>
{% endif %}

<div class="footer">
Smart Learning • Adaptive AI • Mental Health Guard 🚀
</div>

</div>
</body>
</html>
"""

# ===== AI LOGIC =====

def detect_emotion(text):
    sad_keywords = ["mệt","chán","áp lực","stress","buồn","lo lắng","không muốn học"]
    return any(word in text.lower() for word in sad_keywords)

def tutor_logic(question):
    q = question.lower()
    if "pitago" in q:
        return "Định lý Pitago: a² + b² = c².\n\nCâu hỏi nhanh: Cạnh huyền là cạnh nào?"
    elif "đạo hàm" in q:
        return "Đạo hàm là giới hạn của tỉ số giữa sự thay đổi của hàm số khi biến tiến đến 0."
    elif "tiếng anh" in q:
        return "Mỗi ngày 10 phút từ vựng + 5 phút nghe sẽ giúp bạn tiến bộ rõ rệt."
    else:
        return "AI đang phân tích và đưa ra hướng học phù hợp với chương trình Bộ GD."

@app.route("/", methods=["GET","POST"])
def home():

    answer = None
    score = None
    level = None
    badge = None
    warning = None
    mode = None
    progress = 0
    avatar = "🤖"
    streak = 0

    if request.method == "POST":

        if "mock" in request.form:
            username = request.form.get("username")
            if username:
                warning = f"{username}, bạn đã dùng MXH 45 phút. Thử làm 1 quiz 10 phút để giữ streak nhé! 🔥"
                mode = "Focus Coach"
            else:
                warning = "Vui lòng nhập tên."

        else:
            username = request.form["username"]
            question = request.form["question"]

            if username not in points:
                points[username] = 0
                streaks[username] = 0
                user_profiles[username] = {"weak_subject":None}

            if "toán" in question.lower():
                user_profiles[username]["weak_subject"] = "Toán"

            if detect_emotion(question):
                answer = f"{username}, mình cảm nhận bạn đang hơi áp lực.\nThử bài thở 4-4-4: hít 4s - giữ 4s - thở 4s.\nGiảm mục tiêu hôm nay xuống 70% nhé 💙"
                mode = "Health Guard"
            else:
                explanation = tutor_logic(question)
                answer = f"{username}, đây là phần giải thích:\n\n{explanation}"
                mode = "Study Mode"

            points[username] += 10
            streaks[username] += 1

            score = points[username]
            streak = streaks[username]
            level = score // 50 + 1
            progress = (score % 50) * 2

            if level == 1:
                avatar = "🤖"
            elif level == 2:
                avatar = "🚀"
            else:
                avatar = "🔥"

            if score >= 100:
                badge = "Chiến binh Focus"
            elif streak >= 5:
                badge = "5 ngày chăm chỉ"
            elif score >= 50:
                badge = "Người bắt đầu nghiêm túc"

    return render_template_string(
        HTML,
        answer=answer,
        score=score,
        level=level,
        badge=badge,
        warning=warning,
        mode=mode,
        progress=progress,
        avatar=avatar,
        streak=streak
    )


# ===== Bind Render PORT =====
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
