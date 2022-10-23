import json

JSON_PATH = r'./questions/questions.json'

class BeckTest:
    def __init__(self):
        self.questions = json.load(open(JSON_PATH, encoding='UTF-8'))
        self.question_generator = self.question_gen()
        self.points = 0

    def question_gen(self) -> tuple[str, list[str, int]]:
        for question in self.questions:
            self.current_question = question
            self.current_answers_dict = self.questions[question]
            self.current_answers_list = list(self.current_answers_dict.keys())
            yield question, self.questions[question]

    def add_answer(self, answer: str) -> None:
        self.points += int(self.current_answers_dict[answer])

