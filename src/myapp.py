from flask import Flask
import toml


#load toml file
config = toml.load('./settings/settings.toml')
# Setting up the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    return project name

    :return: string
    """
    return str(config['project']['name'])


if __name__ == "__main__":
    app.run(port=500, debug=True)
