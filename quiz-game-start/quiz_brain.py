class Quiz_Brain:

    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)
        #or
        # if self.question_no < len(self.question_list):
        #     return True
        # else:
        #     return False


    def next_qustion(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no} : {current_question.text}(True/False):")
        self.check_answer(user_answer, current_question.answer)
        # score_point = 0
        # if answer == current_question.answer:
        #     score_point += 1
        #     if self.question_no == len(self.question_list):
        #         answer = False
        #         print(f"your total score point {score_point}")
        #
        #
        #     else:
        #         print("Try again")

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got right")
            self.score += 1

        else:
            print("That'a worng.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_no}")

