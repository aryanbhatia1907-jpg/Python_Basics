def word_count(sentence): 
    """ Counts how many times each word appears. Parameters:
    sentence (str): the sentence to analyze Returns: dict: word as key, count as value
    """ 
    words = sentence.split()
    counts = {}  
    for word in words: 
        if word in counts:
            counts[word] += 1 
        else: 
            counts[word] = 1 #
    return counts
sentence = "the cat sat on the mat the cat" 
result = word_count(sentence)
print(result)