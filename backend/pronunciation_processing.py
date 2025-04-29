from difflib import SequenceMatcher
import sys
from flask import json
from g2p_en import G2p

# def text_to_phonemes(text):
#     g2p = G2p()
#     phonemes = g2p(text)
#     phoneme_str = " ".join([p for p in phonemes if p != ' '])
#     return phoneme_str


# Calculate the similarity ratio between two pronunciations overall
def compare_pronunciation(target, spoken):
    matcher = SequenceMatcher(None, target.lower(), spoken.lower())
    ratio = matcher.ratio()

    return ratio

def grade_pronunciation(target, spoken):
    overall_score = compare_pronunciation(target, spoken)

    word_scores = []  # List to hold the similarity scores for each word of the target phrase

    target_words = target.lower().split()  # Split target into words
    spoken_words = spoken.lower().split()  # Split spoken into words

    # Compare corresponding words from both target and spoken phrases
    for target_word, spoken_word in zip(target_words, spoken_words):
        matcher = SequenceMatcher(None, target_word, spoken_word)
        ratio = matcher.ratio()
        word_scores.append(round(ratio, 2)) 
    
    return word_scores, overall_score

if __name__ == "__main__":
    target = sys.argv[1]
    spoken = sys.argv[2]

    word_scores, overall_score = grade_pronunciation(target, spoken)

    result = {
        "word_scores": word_scores,
        "overall_score": round(overall_score, 2)
    }

    print(json.dumps(result))