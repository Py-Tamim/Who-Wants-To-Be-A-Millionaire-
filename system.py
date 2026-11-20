import random
import pandas as pd

PRIZES = [100, 200, 300, 500, 1_000,
          2_000, 4_000, 8_000, 16_000, 32_000,
          64_000, 125_000, 250_000, 500_000, 1_000_000]       # Prize for each question (index 0 = Question 1)

SAFE_HAVENS = {5: 1_000, 10: 32_000}                          # Safe havens: question number -> guaranteed money

def guaranteed_money(question_number):
    """Money the player keeps if they get `question_number` wrong."""
    if question_number > 10:
        return SAFE_HAVENS[10]
    if question_number > 5:
        return SAFE_HAVENS[5]
    return 0

def pick_questions(df):
    """Return 15 random rows: 5 easy, 5 medium, 5 hard (in that order)."""
    chosen = []
    for level in ("easy", "medium", "hard"):
        ids = df[df["difficulty"] == level].index.tolist()
        chosen += random.sample(ids, 5)
    return df.loc[chosen]