from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 여기에 사용할 이미지를 나열하세요
IMAGES = [
    '딸기.png',
    '망고.png',
    '오레오.png',
    '제철과일.png',
    # 추가 이미지
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tournament', methods=['GET', 'POST'])
def tournament():
    if request.method == 'POST':
        images = request.form.getlist('images')
        if len(images) == 1:
            winner = images[0]
            return redirect(url_for('result', winner=winner))
        next_round = []
        for i in range(0, len(images), 2):
            next_round.append(images[i])
        return render_template('tournament.html', images=next_round)
    return render_template('tournament.html', images=IMAGES)

@app.route('/result/<winner>')
def result(winner):
    return render_template('result.html', winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
