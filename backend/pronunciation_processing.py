from difflib import SequenceMatcher
import sys
from flask import json
from g2p_en import G2p
from text_utils import extract_letters

# def text_to_phonemes(text):
#     g2p = G2p()
#     phonemes = g2p(text)
#     phoneme_str = " ".join([p for p in phonemes if p != ' '])
#     return phoneme_str


# Calculate the similarity ratio between two pronunciations overall
def compare_pronunciation(target, spoken):
    matcher = SequenceMatcher(None, target, spoken) 
    ratio = matcher.ratio()

    return ratio

def grade_pronunciation(target, spoken):
    target_processed = extract_letters(target)
    spoken_processed = extract_letters(spoken)

    overall_score = compare_pronunciation(target_processed, spoken_processed)

    word_scores = []  # List to hold the similarity scores for each word of the target phrase

    target_words = target_processed.split()  # Split target into words
    spoken_words = spoken_processed.split()  # Split spoken into words

    # Compare corresponding words from both target and spoken phrases
    for target_word, spoken_word in zip(target_words, spoken_words):
        matcher = SequenceMatcher(None, target_word, spoken_word)
        ratio = matcher.ratio()
        word_scores.append(round(ratio, 2)) 

    # Fill missing scores with 0.0 if spoken_words was longer than the target
    while len(word_scores) < len(spoken_words):
        word_scores.append(0.0)
    
    return word_scores, overall_score, spoken.split()

if __name__ == "__main__":
    target = sys.argv[1]
    spoken = sys.argv[2]

    word_scores, overall_score, spoken_words = grade_pronunciation(target, spoken)

    result = {
        "word_scores": word_scores,
        "overall_score": round(overall_score, 2),
        "spoken_words": spoken_words
    }

    print(json.dumps(result))