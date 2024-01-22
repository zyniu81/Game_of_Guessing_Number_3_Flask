from flask import Flask, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def game(n=10):
    user_input = request.form.get("user_input", "")
    global computer

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
                        <button type="submit" name="start">Start</button>
                        <button type="submit" name="too_small">Too small</button>
                        <button type="submit" name="too_big">Too big</button>
                        <button type="submit" name="you_win">You win</button>
                        <button type="submit" name="stop">Stop</button>
                    </form>
                </body>
            </html>
        """

    try:
        min_number = 0
        max_number = 1000
        list_computer = []
        if request.form.get("start"):
            computer = random.randint(min_number, max_number)
            list_computer.append(computer)
        while len(list_computer) <= n:
            if user_input == "Too small":
                min_number = computer + 1
            elif user_input == "Too big":
                max_number = computer - 1
            elif user_input == "You win":
                return f"I'm win in {len(list_computer)} attempt"
            elif user_input == "Stop":
                return "Interrupted by user"

            if len(list_computer) == n:
                return f"{list_computer} I lost game"

            computer = random.randint(min_number, max_number)
            list_computer.append(computer)

            return f"""
                <html>
                    <body>
                        <p>{computer}</p>
                        <p>{list_computer}</p>
                        <form action="/" method="POST">
                            <label>
                                Think the number from 0 to 1000 and I will guess it as quickly as possible.
                                ENTER Start
                            </label>
                            <input type="hidden" name="user_input" value="{user_input}"/>
                            <input type="hidden" name="computer" value="{computer}" />
                            <button type="submit" name="start">Start</button>
                            <button type="submit" name="too_small">Too small</button>
                            <button type="submit" name="too_big">Too big</button>
                            <button type="submit" name="you_win">You win</button>
                            <button type="submit" name="stop">Stop</button>
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
