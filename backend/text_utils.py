# def text_to_phonemes(text):
#     g2p = G2p()
#     phonemes = g2p(text)
#     phoneme_str = " ".join([p for p in phonemes if p != ' '])
#     return phoneme_str

def extract_letters(text):
    text = text.lower().strip()
    return ''.join(char for char in text if char.isalpha() or char.isspace() or char.isdigit())