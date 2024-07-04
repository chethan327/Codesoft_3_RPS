from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

choices = ['rock', 'paper', 'scissors']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    session['username'] = request.form['username']
    session['rounds'] = int(request.form['rounds'])
    session['current_round'] = 1
    session['results'] = []
    session['user_score'] = 0
    session['computer_score'] = 0
    return redirect(url_for('play_round'))

@app.route('/play_round', methods=['GET', 'POST'])
def play_round():
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            winner = 'Tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            winner = session['username']
            session['user_score'] += 1
        else:
            winner = 'Computer'
            session['computer_score'] += 1
        
        session['results'].append({
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'winner': winner
        })
        
        session['current_round'] += 1
        if session['current_round'] > session['rounds']:
            return redirect(url_for('result'))
    
    return render_template('game.html', round=session['current_round'], rounds=session['rounds'])

@app.route('/result')
def result():
    user_score = session.get('user_score', 0)
    computer_score = session.get('computer_score', 0)
    if user_score > computer_score:
        overall_winner = session['username']
    elif user_score < computer_score:
        overall_winner = 'Computer'
    else:
        overall_winner = 'It\'s a Tie'
    
    return render_template('result.html', results=session['results'], user_score=user_score, computer_score=computer_score, overall_winner=overall_winner)

if __name__ == '__main__':
    app.run(debug=True)
