# Tunisian Dialect Sentiment Chatbot

## Setup
```bash
pip install -r requirements.txt
```

## Train
```bash
python train.py
```
Detects GPU automatically. Model saved to `./sentiment_model`.

## Data
- `dataset/all_lines_labeled.json` — full dataset (2.8M entries, mostly unlabeled)
- `dataset/labeled_clean.json` — 2998 clean labeled samples used for training

## Notes
- Labels: `1` = positive, `-1` = negative
- Model: `bert-base-multilingual-cased` (handles Arabizi/Tunisian dialect)"# tunizi-sentiment" 
