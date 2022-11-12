import json
import re
import sys

def txt_to_dict(path):
    dictionary = {}
    regex = re.compile('^([0-9]) (.*)')
    qregex = re.compile('^.*[?]')
    file = open(path, encoding=sys.getdefaultencoding())
    current_q = ''
    for line in file:
        if not line: continue
        if res := qregex.match(line):
            current_q = res[0]
            dictionary[current_q] = {}
            continue
        if res := regex.match(line):
            dictionary[current_q][res[2]] = res[1]
    return dictionary


def txt_to_json(txt_path, out_path):
    questions = txt_to_dict(txt_path)
    json.dump(questions, open(out_path, 'w', encoding='UTF-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    txt_to_json('questions.txt', 'questions.json')