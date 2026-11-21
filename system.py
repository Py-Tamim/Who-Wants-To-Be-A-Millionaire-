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

def ask_question(row, number):
    """Show one question and return True if the player answers correctly."""
    options = list(row["options"])
    correct_text = options["ABCD".index(row["answer"])]
    random.shuffle(options)
    correct_letter = "ABCD"[options.index(correct_text)]

    print(f"\nQuestion {number} - ${PRIZES[number - 1]:,}   [{row['category']}]")
    if number in SAFE_HAVENS:
        print("(Safe Haven question!)")
    print(row["question"])
    for letter, option in zip("ABCD", options):
        print(f"  {letter}. {option}")
    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in ("A", "B", "C", "D"):
            return choice == correct_letter
        print("Please type A, B, C or D.")

def main():
    df = pd.read_json("MCQ.json")            # load the dataset
    questions = pick_questions(df)
    print("=== WHO WANTS TO BE A MILLIONAIRE? ===")

    for number, (_, row) in enumerate(questions.iterrows(), start=1):
        if ask_question(row, number):
            print(f"Correct! You now have ${PRIZES[number - 1]:,}")
            if number in SAFE_HAVENS:
                print(f"*** Safe Haven reached! ${SAFE_HAVENS[number]:,} is guaranteed. ***")
        else:
            earned = guaranteed_money(number)
            print("\nYou lose the game")
            print(f"Your total earned money: {earned:,} USD.")
            return

    print("\nCONGRATULATIONS! You are a MILLIONAIRE!")
    print("Your total earned money: 1,000,000 USD.")


if __name__ == "__main__":
    main()