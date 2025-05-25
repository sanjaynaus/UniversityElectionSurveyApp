# -----------------------------------------------------------
# University Election Survey App - Code Submission
# File: visualizer.py
#
# Description:
# Handles generation of bar and pie charts for survey results.
#
# Usage:
# - Called by the SurveyApp after survey completion.
#
# Author: Sanjay Tamata
# Date: 25th May, 2025
# -----------------------------------------------------------

import matplotlib.pyplot as plt

def show_bar_chart(scores):
    """
    Displays a bar chart for candidate scores.
    :param scores: Dictionary of candidate votes (e.g., {"Sanjay": 3, "Vivek": 1, ...})
    """
    candidates = list(scores.keys())
    votes = list(scores.values())

    plt.figure(figsize=(12, 5))
    bars = plt.bar(candidates, votes, color=["#4CAF60", "#2196F3", "#FFC107", "#9C27B0", "#E91E63"])
    plt.xlabel("Candidates")
    plt.ylabel("Total Number of Votes")
    plt.title("Candidate Score ")
    plt.ylim(0, max(votes) + 1)

    for bar in bars:
        y_value = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y_value + 0.1, int(y_value), ha='center', va='bottom')
    plt.show()

def show_pie_chart(scores):
    """
    Displays a pie chart for candidate vote share.
    :param scores: Dictionary of candidate votes.
    """
    # Filter out candidates with 0 votes
    filtered_scores = {candidate: votes for candidate, votes in scores.items() if votes > 0}

    if not filtered_scores:
        print("No votes recorded. Pie chart cannot be displayed.")
        return

    candidates = list(filtered_scores.keys())
    votes = list(filtered_scores.values())

    plt.figure(figsize=(9, 9))
    plt.pie(votes, labels=candidates, autopct='%1.1f%%', startangle=140)
    plt.title("Candidate Vote Share")
    plt.axis('equal')
    plt.show()
