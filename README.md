# Who Wants to Be a Millionaire? 💰

A Python-based quiz game inspired by the popular TV show **Who Wants to Be a Millionaire?**
The game challenges players to answer 15 multiple-choice questions correctly and win up to **$1,000,000**.
Questions are randomly selected from a JSON dataset and arranged into three difficulty levels: Easy, Medium, and Hard.

## 🎮 Game Features

- 15 randomly selected questions.
- Three difficulty levels: Easy, Medium, and Hard.
- Four answer options (A, B, C, D).
- Randomized answer positions.
- Increasing prize money after each correct answer.
- Two safe havens at Question 5 ($1,000) and Question 10 ($32,000).
- Final prize of $1,000,000.

## 💰 Prize Structure

| Question | Prize |
|---:|---:|
| 1 | $100 |
| 2 | $200 |
| 3 | $300 |
| 4 | $500 |
| 5 | $1,000 🔒 |
| 6 | $2,000 |
| 7 | $4,000 |
| 8 | $8,000 |
| 9 | $16,000 |
| 10 | $32,000 🔒 |
| 11 | $64,000 |
| 12 | $125,000 |
| 13 | $250,000 |
| 14 | $500,000 |
| 15 | $1,000,000 |

**Safe Haven Rules:**
- Answer Question 5 correctly to secure $1,000.
- Answer Question 10 correctly to secure $32,000.
- If you answer incorrectly, you keep the last safe haven amount reached.

## 🔄 How It Works

1. The game loads questions from `MCQ.json`.
2. It randomly selects 5 easy, 5 medium, and 5 hard questions.
3. The player answers each question by entering A, B, C, or D.
4. Correct answers increase the prize money.
5. An incorrect answer ends the game, and the player receives the guaranteed safe haven amount.
6. Answer all 15 questions correctly to win $1,000,000.

## 📁 Dataset Format

The game uses a JSON file named `MCQ.json`.

Each question contains the following information:

| Field | Description |
|---|---|
| question | The question text |
| options | Four possible answers |
| answer | Correct answer (A/B/C/D) |
| difficulty | Easy, Medium, or Hard |
| category | Question category |

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Loading and processing questions |
| Random | Random question and answer selection |
| JSON | Storing the question dataset |

## 📦 Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

**2. Install Pandas**

```bash
pip install pandas
```

**3. Run the game**

Make sure `MCQ.json` is in the same directory as the Python script.

```bash
python millionaire.py
```

## 📁 Project Structure

```text
Who-Wants-to-Be-a-Millionaire/
│
├── millionaire.py
├── MCQ.json
└── README.md
```

## 🤝 AI Assistance & Acknowledgement

I used AI tools as supporting resources during this project to:

- Explore and refine the initial game idea.
- Find suitable question datasets and understand CSV/JSON data formats.
- Compare possible approaches and choose suitable tools for the project.
- Understand how to organize questions by difficulty and implement the game logic.

- 
## 🚀 Future Improvements

- Add a graphical user interface.
- Include sound effects and a countdown timer.
- Add lifelines such as 50:50 and Ask the Audience.
- Add player scores and a leaderboard.
- Expand the question database.
AI was used as a learning and research assistant. I reviewed the suggestions and applied them during my own development process.

--

## *Developed for educational purposes as a part of my Python programming practice.
