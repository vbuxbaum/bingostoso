from flask import Flask, render_template, request
from random import sample

app = Flask(__name__)


@app.route("/")
def home_page():
    player = request.args.get('player')
    if player:
        return hello_player(player)
    return render_template("home.html")


@app.route("/<player>")
def hello_player(player):
    card_values = gen_card()
    return render_template(
        "card.html",
        player=player,
        first_card_values=card_values[0],
        second_card_values=card_values[1],
    )


def gen_card():
    columns = [sample(range(1, 15), 5)]
    columns.append(sample(range(16, 30), 5))
    middle_cloumn = sample(range(31, 45), 4)
    middle_cloumn.insert(2, None)
    columns.append(middle_cloumn)
    columns.append(sample(range(46, 60), 5))
    columns.append(sample(range(61, 75), 5))
    print(columns)
    half_counter = 0
    ordered_values = [[], []]
    for index1 in range(5):
        for column_index, column in enumerate(columns):
            if column[index1]:
                ordered_values[half_counter].append(column[index1])
            else:
                half_counter += 1
    return ordered_values
