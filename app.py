from flask import Flask, render_template, redirect, request, jsonify
from squad.demo_prepro import prepro
from basic.demo_cli import Demo
import json

app = Flask(__name__)
shared = json.load(open("data/squad/shared_test.json", "r"))
contextss = [""]
context_questions = [""]
for i in range(len(shared["contextss"])):
    j = 1 if i == 0 else 0
    contextss.append(shared["contextss"][i][j])
    context_questions.append(shared["context_questions"][i][j])
titles = ["Write own paragraph"] + shared["titles"]

demo = Demo()


def getTitle(ai):
    return titles[ai]


def getPara(rxi):
    return contextss[rxi[0]][rxi[1]]


def getAnswer(paragraph, question):
    pq_prepro = prepro(paragraph, question)
    if len(pq_prepro["x"]) > 1000:
        return (
            "[Error] Sorry, the number of words in paragraph cannot be more than 1000."
        )
    if len(pq_prepro["q"]) > 100:
        return "[Error] Sorry, the number of words in question cannot be more than 100."
    return demo.run(pq_prepro)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/select", methods=["GET", "POST"])
def select():
    # paragraph_id = request.args.get('paragraph_id', type=int)
    # rxi = [paragraph_id, 0]
    # paragraph = getPara(rxi)
    # return jsonify(result=paragraph)
    return jsonify(
        result={
            "titles": titles,
            "contextss": contextss,
            "context_questions": context_questions,
        }
    )


@app.route("/submit", methods=["GET", "POST"])
def submit():
    n = 1000
    # paragraph = request.args.get("paragraph").split()
    paragraph = "".join(
        [
            i
            for i in open("data.txt", "r", encoding="utf-8")
            .read()
            .replace("\n", " ")
            .replace("\t", " ")
            if not i.isdigit()
        ]
    )
    question = request.args.get("question")
    sub_paras = ["".join(paragraph[i : i + n]) for i in range(0, len(paragraph), n)]
    answer_dicts = list(
        filter(
            lambda dictn: True if dictn[0] != "" else False,
            map(lambda para: getAnswer(para, question), sub_paras),
        )
    )
    print(answer_dicts)
    answer_dict = max(answer_dicts, key=lambda dictn: dictn["scores"][0])
    print(answer_dict)
    answer = answer_dict[0]
    return jsonify(result=answer)


if __name__ == "__main__":
    app.run()
