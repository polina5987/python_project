# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

user_phrase = input("Enter you hashtag: ").strip().title()
hashtag = "#" + user_phrase.replace(" ", "")

if len(hashtag) > 140:
    print(f"Error hashtag is too long! Shorten hashtag to {hashtag[:140]}")
else:
    result = ""
    for char in user_phrase:
        if char not in string.punctuation:
            result += char

    new_hashtag = "#" + result.replace(" ", "")

    print(f"Your final hashtag: {new_hashtag}")
