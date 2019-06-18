import json
from squad.demo_prepro import prepro
from basic.demo_cli import Demo

shared = json.load(open("data/squad/shared_test.json", "r"))
contextss = [""]
context_questions = [""]
for i in range(len(shared['contextss'])):
    j = 1 if i==0 else 0
    contextss.append(shared["contextss"][i][j])
    context_questions.append(shared['context_questions'][i][j])
titles = ["Write own paragraph"]+shared["titles"]

demo = Demo()

def getTitle(ai):
    return titles[ai]

def getPara(rxi):
    return contextss[rxi[0]][rxi[1]]

def getAnswer(paragraph, question):
    pq_prepro = prepro(paragraph, question)
    if len(pq_prepro['x'])>1000:
        return "[Error] Sorry, the number of words in paragraph cannot be more than 1000." 
    if len(pq_prepro['q'])>100:
        return "[Error] Sorry, the number of words in question cannot be more than 100."
    return demo.run(pq_prepro)


if __name__ =='__main__':
    paragraph = input("Enter Context :")
    question = input("Enter Question :")
    print(getAnswer(paragraph,question))
