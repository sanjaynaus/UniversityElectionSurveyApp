# -----------------------------------------------------------
# University Election Survey App - Code Submission
# File: survey_app.py
#
# Description:
# This module defines the SurveyApp class, orchestrating the
# survey logic and visualization.
#
# Usage:
# - Imported by main.py or can be run standalone.
#
# Author: Sanjay Tamata
# Date: 25th May, 2025
# -----------------------------------------------------------

from survey_questions import questions
from candidate_data import candidate_manifestos
from data_logger import log_response
from visualizer import show_bar_chart, show_pie_chart


class SurveyApp:
    def __init__(self):
        self.questions = questions
        # Using the keys from candidate_manifestos to initialize scores.
        self.candidates = list(candidate_manifestos.keys())
        self.scores = {candidate: 0 for candidate in self.candidates}
        self.responses_log = []

    def conduct_survey(self):
        print("Welcome to the University of Sydney Election Candidate Selector Survey!\n")
        print("Please answer the following questions by typing the number corresponding to your chosen option.\n")

        for q in self.questions:
            print(q["question"])
            for option_text in q["options"]:
                print(option_text)

            user_input = input("Your answer (enter the corresponding number): ").strip()
            valid_option = None
            for option in q["options"]:
                if option.startswith(user_input + "."):
                    valid_option = option
                    break

            while not valid_option:
                print("Invalid input. Please try again.")
                user_input = input("Your answer (enter the corresponding number): ").strip()
                for option in q["options"]:
                    if option.startswith(user_input + "."):
                        valid_option = option
                        break

            candidate = q["options"][valid_option]
            self.scores[candidate] += 1
            self.responses_log.append({
                "question": q["question"],
                "answer": valid_option,
                "candidate": candidate
            })
            log_response(q["question"], valid_option, candidate)
            print()  # Blank line between questions

    def get_recommendation(self):
        top_candidate = max(self.scores, key=self.scores.get)
        manifesto = candidate_manifestos.get(top_candidate, [])
        return top_candidate, manifesto

    def show_visualizations(self):
        show_bar_chart(self.scores)
        show_pie_chart(self.scores)

    def run(self):
        self.conduct_survey()
        candidate, manifesto = self.get_recommendation()
        print("Survey Completed.\n")
        print("Based on your responses, we recommend Candidate {}.".format(candidate))
        print("\nCandidate Manifestos:")

        idx = 1
        for statement in manifesto:
            print("{}. {}".format(idx, statement))
            idx += 1
        print()
        self.show_visualizations()
