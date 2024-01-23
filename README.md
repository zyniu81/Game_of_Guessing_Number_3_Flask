# Game_of_Guessing_Number_3_Flask

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

## Requirements

- Python 3.x

## Usage

1. Clone the repository.
2. Open the file `guessing_game.py` in your Python IDE (such as PyCharm).
3. Run the file.
4. Follow the instructions on the screen to play the game.

## Author

zyniu81

## License

This project is licensed under the MIT License - see the LICENSE file for details.
