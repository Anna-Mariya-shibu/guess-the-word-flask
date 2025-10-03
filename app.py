from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "replace_this_with_a_random_secret"

# Game settings
WORD_BANK = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
MAX_ATTEMPTS = 6

def init_game():
    word = random.choice(WORD_BANK)
    session['word'] = word
    session['guessed'] = ['_'] * len(word)
    session['attempts'] = MAX_ATTEMPTS
    session['guessed_letters'] = []
    session['game_over'] = False
    session['message'] = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    # Start game if not already started
    if 'word' not in session:
        init_game()

    message = session.get('message', '')

    if request.method == 'POST' and not session.get('game_over', False):
        letter = request.form.get('letter', '').strip().lower()

        if not letter or len(letter) != 1 or not letter.isalpha():
            message = "Please enter a single letter (a-z)."
        elif letter in session['guessed_letters']:
            message = f'You already guessed "{letter}".'
        else:
            session['guessed_letters'].append(letter)
            if letter in session['word']:
                for i, ch in enumerate(session['word']):
                    if ch == letter:
                        session['guessed'][i] = letter
                message = f'Good! "{letter}" is in the word.'
            else:
                session['attempts'] -= 1
                message = f'Sorry, "{letter}" is not in the word.'

        session['message'] = message

    # Game status checks
    if '_' not in session.get('guessed', []):
        session['game_over'] = True
        message = f'🎉 You win! The word was "{session["word"]}".'
    elif session.get('attempts', 0) <= 0:
        session['game_over'] = True
        message = f'💀 Game over! The word was "{session["word"]}".'

    session['message'] = message

    return render_template(
        'index.html',
        word_display=session.get('guessed', []),
        attempts=session.get('attempts', 0),
        guessed_letters=', '.join(session.get('guessed_letters', [])),
        message=message,
        game_over=session.get('game_over', False)
    )

@app.route('/reset', endpoint='new_game')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
