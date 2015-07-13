import re

REGEX = re.compile(r"(ng|.)")
ALPHABET = "a b k d e g h i l m n ng o p r s t u w y".split()
NUM_CHARS = len(ALPHABET)
CHAR_MAP = {c: i for i, c in enumerate(ALPHABET)}


class Node:
    def __init__(self, children, is_word=False):
        self.children = children
        self.is_word = is_word


def insert(word, trie):
    chars = REGEX.findall(word)
    for char in chars:
        index = CHAR_MAP[char]
        if not trie.children[index]:
            trie.children[index] = Node([None] * NUM_CHARS)
        trie = trie.children[index]
    trie.is_word = True


def traverse(trie, prefix):
    words = []
    if trie.is_word:
        words.append(prefix)
    for i in range(NUM_CHARS):
        if trie.children[i]:
            words.extend(traverse(trie.children[i], prefix + ALPHABET[i]))
    return words


def sort_words(words):
    trie = Node([None] * NUM_CHARS)
    for word in words:
        insert(word, trie)
    return traverse(trie, "")


def main():
    test_lists = [
        ["abakada", "alpabet", "tagalog", "ako"],
        ["ang", "ano", "anim", "alak", "alam", "alab"],
        ["siya", "niya", "kaniya", "ikaw", "ito", "iyon"],
        ["kaba", "baka", "naba", "ngipin", "nipin"],
        ["knilngiggnngginggn", "ingkigningg", "kingkong", "dingdong", "dindong",
         "dingdont", "ingkblot"],
        ["silangang", "baka", "bada", "silang"]
    ]
    for i, test_list in enumerate(test_lists):
        print("Test Case #{}:".format(i + 1))
        print("   BEFORE: {}".format(test_list))
        print("    AFTER: {}".format(sort_words(test_list)))

if __name__ == "__main__":
    main()