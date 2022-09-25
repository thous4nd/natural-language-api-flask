from flask import Flask
import requests
app = Flask(__name__)


@app.route("/")
def hello():

    key = "AIzaSyBYefk15u2ogra1OuRqTgoD6WYqpyIFwII"
    text = "こんにちは、今日もいい天気ですね。"
    url = 'https://language.googleapis.com/v1beta2/documents:analyzeSyntax?key=' + key

    header = {'Content-Type': 'application/json'}
    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": text
        },
        "encodingType": "UTF8"
    }

    response = requests.post(url, headers=header, json=body).json()
    print("総合magnitude:",response["documentSentiment"]["magnitude"])
    print("総合score:",response["documentSentiment"]["score"])
    for i in response["sentences"]:
        print(i["text"]["content"],"magnitude:",i["sentiment"]["magnitude"],", score:",i["sentiment"]["score"])

    return "aaa"

@app.route("/hoge")
def hoge():
    return "出力テスト"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)