def extract_letters(text):
    text = text.lower().strip()
    return ''.join(char for char in text if char.isalpha() or char.isspace() or char.isdigit())