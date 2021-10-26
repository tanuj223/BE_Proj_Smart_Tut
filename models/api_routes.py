from flask import request
from flask import json
from flask.json import jsonify
from models.questiongenerator import QuestionGenerator
from flask_cors import CORS
from flask import Blueprint
from models.notes import extract_summary
from models.recommend import rec

api = Blueprint(
    'api', 'api', url_prefix='/')
CORS(api)

'''
{
    "chapter": string,
}


'''


@api.route("/qna")
def qna():
    #df = pd.read_csv('final_data.csv')
    #chapter = df.iloc[3]['0']
    request_data = request.get_json()
    chapter = request_data["chapter"]
    #file = open("book.txt", 'w')
    # file.write(str(chapter))
    qg = QuestionGenerator()
    qa_list = qg.generate(chapter)
    print(qa_list)
    return jsonify(qa_list)


'''qa_list = subprocess.check_output(
        ["python", "qna_model/run_qg.py", "--text_dir", "book.txt"])
    qa_list = qa_list.decode('utf8').replace("'", '"')
    qa_list = json.loads(qa_list)'''

''


@api.route("/notes")
def notes():
    #df = pd.read_csv('final_data.csv')
    request_data = request.get_json()
    chapter = request_data["chapter"]
    return jsonify(extract_summary(chapter, 3, True))


@api.route("/recommend")
def recommend():
    #df = pd.read_csv('final_data.csv')
    # print(str(df.iloc[0]['0']))
    request_data = request.get_json()
    chapter = request_data["chapter"]
    return jsonify(rec(chapter, max_ngram_size=1, deduplication_threshold=0.5, numOfKeywords=5))
