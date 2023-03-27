from flask import Flask
from settings.config import config



#Test toml file
print(config['title'])

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
    app.run(host=config['environments']['environments.dev']['ip'],
            port=config['environments']['environments.dev']['port'], debug=True)
