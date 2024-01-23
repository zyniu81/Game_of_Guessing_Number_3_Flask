"""
Flask Number Guessing Game

This is a simple Flask web application that plays a number guessing game. The user thinks of a number between 0 and 1000, and the computer tries to guess it with the user's feedback.

Usage:
- Access the root URL ("/") to start the game.
- The computer will generate a random number within the given range.
- Provide feedback to the computer's guesses using the "Too small" or "Too big" buttons.
- The game continues until the computer guesses the correct number or reaches the maximum number of attempts.
- You can stop the game at any time by clicking the "Stop" button.

Attributes:
- `app`: Flask application instance.
- `list_computer`: List to store the computer's guessed numbers.
- `user_input`: User input from the form.
- `computer`: The current computer-generated guess.
- `min_number`: The minimum possible number in the range.
- `max_number`: The maximum possible number in the range.

Routes:
- GET "/" : Renders the HTML form to start the game.
- POST "/" : Handles the form submission, updates the game state, and renders the appropriate response.

Functions:
- `game(n=10)`: Main game logic. Handles user inputs, updates the game state, and generates computer guesses.
"""

from flask import Flask, request
import random

app = Flask(__name__)

app.config['list_computer'] = []

@app.route("/", methods=["GET", "POST"])
def game(n=10):
    """
        Main game logic.

        Handles user inputs, updates the game state, and generates computer guesses.

        Parameters:
        - n (int): Maximum number of attempts allowed.

        Returns:
        - str: HTML response with the current game state.
        """
    user_input = request.form.get("user_input", "")
    global computer, min_number, max_number

    if request.method == "GET":
        return """
            <html>
                <body>
                    <form action="/" method="POST">
                        <label>
                            Think the number from 0 to 1000 and I will guess it as quickly as possible.
                            ENTER Start
                        </label>
                        <input type="hidden" name="user_input" value=""/>
                        <input type="hidden" name="computer" value="{computer}" />
                        <button type="submit" name="action" value="start">Start</button>
                        <button type="submit" name="action" value="too_small">Too small</button>
                        <button type="submit" name="action" value="too_big">Too big</button>
                        <button type="submit" name="action" value="you_win">You win</button>
                        <button type="submit" name="action" value="stop">Stop</button>
                    </form>
                </body>
            </html>
        """

    try:
        if request.form.get("action") == "start":
            app.config['list_computer'] = []
            min_number, max_number = 0, 1000
            computer = random.randint(min_number, max_number)
            while computer in app.config['list_computer']:
                computer = random.randint(min_number, max_number)
            app.config['list_computer'].append(computer)
            app.config['list_computer'].pop(0)

        if request.form.get("action") == "too_small" and app.config['list_computer']:
            min_number = max(min_number, app.config['list_computer'][-1] + 1)
        elif request.form.get("action") == "too_big" and app.config['list_computer']:
            max_number = min(max_number, app.config['list_computer'][-1] - 1)
        elif request.form.get("action") == "you_win":
            return f"I'm win in {len(app.config['list_computer'])} attempt"
        elif request.form.get("action") == "stop":
            return "Interrupted by user"

        if len(app.config['list_computer']) == n:
            return f"I lost game"

        computer = random.randint(min_number, max_number)
        while computer in app.config['list_computer']:
            computer = random.randint(min_number, max_number)
        app.config['list_computer'].append(computer)

        return f"""
            <html>
                <body>
                    <p>{computer}</p>
                    <form action="/" method="POST">
                        <label>
                            Think the number from 0 to 1000 and I will guess it as quickly as possible.
                            ENTER Start
                        </label>
                        <input type="hidden" name="user_input" value="{user_input}"/>
                        <input type="hidden" name="computer" value="{computer}" />
                        <button type="submit" name="action" value="start">Start</button>
                        <button type="submit" name="action" value="too_small">Too small</button>
                        <button type="submit" name="action" value="too_big">Too big</button>
                        <button type="submit" name="action" value="you_win">You win</button>
                        <button type="submit" name="action" value="stop">Stop</button>
                    </form>
                </body>
            </html>
        """
    except ValueError:
        return "You cheating."
    except KeyboardInterrupt:
        return "Interrupted by user"


if __name__ == "__main__":
    app.run(debug=True)
