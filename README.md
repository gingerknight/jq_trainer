# jq_trainer 🧠📊

A terminal-powered GUI app built with Python and `jq` to train your JSON query skills on real-world Olympic data. Whether you're a beginner or brushing up, this interactive trainer helps you master `jq` one filter at a time.

## Features ✨

- 🌍 Real Olympic dataset (athletes, events, medals)
- 🧪 Progressive difficulty questions
- 💡 Instant feedback on your queries
- 🔍 Real-time `jq` execution
- 🎉 End-game celebration on completion

## Demo

> Coming soon

## Requirements 📦

- Python 3.8+
- `jq` installed and available in your system path

To install `jq`:

```bash
# macOS
brew install jq

# Ubuntu/Debian
sudo apt install jq

# Windows (via Chocolatey)
choco install jq
```

## Setup ⚙️

Clone the repo and run the app:

```bash
git clone https://github.com/gingerknight/jq_trainer.git
cd jq_trainer
tar -xvf archive_olympics.tar.gz # this file is quite large ~102MB
python3 main.py
```
### File Structure 📁
```
.
├── olympics.json         # Olympic athlete dataset (after extraction, Source: Kaggle)
├── prompts.json          # List of questions, answers, and datasets
├── main.py               # Entry point for the GUI trainer
├── gui.py                # JQWindowManager class (Tkinter logic)
└── README.md
```

### Example Question 🏅

    Question: How many women competed in the 1924 Olympics?

Write a valid jq query using the dataset to get the expected output. The app compares your result to the expected answer.

`[.[] | select(.sex == "F" and .year == 1924)] | length`

### Customization 🛠️

Want to add your own questions?

Update questions.json with this format:
```json
{
  "question": "Your question here?",
  "expected_output": "Expected string result",
  "hint": "what command to run or thinkg about"
}
```

## Future Work 💡
- Question difficulty tiers
- Add hint functionality
- Multi-dataset support?

## License 📄

MIT — use it, modify it, and sharpen your jq skills freely.

🚀 Master your filters. Conquer your data.