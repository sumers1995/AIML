def analyze_text(test):
    word_count = len(test.split())
    total = 0
    for word in test.split():
        total += len(word)
    vowel_count = len([a for a in test if a in ["a","e","i","o","u"]])
    return {"char_count":total,
            "word_count":word_count,
            "vowel_count":vowel_count}

if __name__ == "__main__":
    res = analyze_text("Sumer")
    print(res)