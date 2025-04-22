from difflib import SequenceMatcher
from g2p_en import G2p

# Calculate the similarity ratio between two pronunciations
def compare_pronunciation(target, spoken):
    matcher = SequenceMatcher(None, target.lower(), spoken.lower())
    ratio = matcher.ratio()
    print(f"📊 Similarity score: {round(ratio * 100)}%")

    if ratio > 0.85:
        print("✅ Good job! That was pretty accurate.")
    elif ratio > 0.6:
        print("🟡 Almost there! Try to pronounce the tricky parts more clearly.")
    else:
        print("❌ Needs improvement. Try focusing on each word carefully.")

def text_to_phonemes(text):
    g2p = G2p()
    phonemes = g2p(text)
    phoneme_str = " ".join([p for p in phonemes if p != ' '])
    return phoneme_str