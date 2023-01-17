strs = ["eat","tea","tan","ate","nat","bat", "tab"]
anagram_list = []
anagram_dict = {}
result = []

def find_anagrams(strs):
    for word in strs:
        srt_word = ""
        for letter in sorted(word):
            srt_word = srt_word+letter
        anagram_list.append(srt_word)
        if srt_word not in anagram_dict:
            anagram_dict[srt_word] = [word]
        else:
            new_val = anagram_dict.get(srt_word)
            new_val.append(word)
            anagram_dict.update({srt_word: new_val})
    for elem in anagram_dict:
        result.append(anagram_dict.get(elem))
    print(result)

find_anagrams(strs)

desired_result = [["bat"],["nat","tan"],["ate","eat","tea"]]
