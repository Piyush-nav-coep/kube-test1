from flask import Flask
import time
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Python Application test |\"}"
def run1():
    return "{\"message\":\"Python Application test -\"}"
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("7044"), debug=True)
    time.sleep(2)
    helloworld.run1(host="0.0.0.0", port=int("7044"), debug=True)
    time.sleep(2)
