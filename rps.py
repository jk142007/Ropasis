from flask import Flask, render_template, request
import random

app = Flask(__name__)

options = ["rock", "paper", "scissors"]

@app.route("/", methods=["GET", "POST"])
def home():
    user = ""
    computer = ""
    result = ""

    if request.method == "POST":
        user = request.form["choice"]
        computer = random.choice(options)

        if user == computer:
            result = "😐 It's a draw!"
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            result = "🎉 You win!"
        else:
            result = "💻 Computer wins!"

    return render_template("ropasis.html", user=user, computer=computer, result=result)

if __name__ == "__main__":
    app.run(port=5005,debug=True)
