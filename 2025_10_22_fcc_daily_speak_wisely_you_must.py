# Speak Wisely, You Must
# Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

    # Words are separated by a single space.
    # Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".

    # Move all words before and including that word to the end of the sentence and:
        # Preserve the order of the words when you move them.
        # Make them all lowercase.
        # And add a comma and space before them.

    # Capitalize the first letter of the new first word of the sentence.
    # All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
    # Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
    # For example, given "You must speak wisely." return "Speak wisely, you must."

# def wise_speak(sentence: str) -> str:
#     delimiter_words = ["have", "must", "are", "will", "can"]
#     earliest_index = -1
#     earliest_word = None
    
#     for word in delimiter_words:
#         current_index = sentence.lower().find(f"{word} ")

#         if current_index != -1:
#             if earliest_index == -1 or current_index < earliest_index:
#                 earliest_index = current_index
#                 earliest_word = word
    
#     if earliest_word:
#         punctuation_mark = sentence[-1]
#         split_index = earliest_index + len(earliest_word)
#         new_end_sentence = sentence[:split_index].lower() 
#         new_start_sentence = sentence[split_index + 1: -1].capitalize()
#         return f"{new_start_sentence}, {new_end_sentence}{punctuation_mark}"
#     else:
#         return "Error: no matching word found"






def wise_speak(sentence: str) -> str:
    delimiter_words = {"have", "must", "are", "will", "can"}
    punctuation_mark = sentence[-1]
    core_sentence = sentence[:-1]
    words = core_sentence.split()
    split_index = -1

    for index, word in enumerate(words):
        if word.lower() in delimiter_words:
            split_index = index
            break
    
    if split_index == -1:
        return "Error: no matching word found."

    original_first_part = words[:split_index + 1]
    original_second_part = words[split_index + 1:]
    new_start_sentence = ' '.join(original_second_part).capitalize()
    new_end_sentence = ' '.join(original_first_part).lower()

    return f"{new_start_sentence}, {new_end_sentence}{punctuation_mark}"

if __name__ == "__main__":
    # should return "Speak wisely, you must."
    print(wise_speak("You    must speak Wisely.")) 
    # should return "Do it, you can!"
    print(wise_speak("You Can do it!") )
    # should return "Complete this, do you think you will?"
    print(wise_speak("Do you think you will complete this?")) 
    # # should return "Belong to us, all your base are."
    print(wise_speak("All your base are belong to us.")) 
    # # should return "Much to learn, you have."
    print(wise_speak("You have much to learn."))