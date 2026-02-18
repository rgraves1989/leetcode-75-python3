"""

208. Implement Trie (Prefix Tree)

    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:
        - Trie() Initializes the trie object.
        - void insert(String word) Inserts the string word into the trie.
        - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

    Input:
        - ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        - [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output:
        - [null, null, true, false, true, null, true]
    Explanation:
        - Trie trie = new Trie();
        - trie.insert("apple");
        - trie.search("apple");   // return True
        - trie.search("app");     // return False
        - trie.startsWith("app"); // return True
        - trie.insert("app");
        - trie.search("app");     // return True

Constraints:

    - 1 <= word.length, prefix.length <= 2000
    - word and prefix consist only of lowercase English letters.
    - At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

"""


class TrieNode:
    def __init__(self, prefix=None):
        self.prefix = prefix
        self.nodes = [None] * 26
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node, word_len, prefix = self.root, len(word), ""
        for char_index in range(word_len):
            curr_char = word[char_index]
            prefix += curr_char
            curr_char_index = ord(curr_char) - 97

            if not curr_node.nodes[curr_char_index]:
                curr_node.nodes[curr_char_index] = TrieNode(prefix)
            curr_node = curr_node.nodes[curr_char_index]
        curr_node.is_word = True

    def search(self, word: str) -> bool:
        curr_node, word_len = self.root, len(word)
        for char_index in range(word_len):
            curr_char = word[char_index]
            curr_char_index = ord(curr_char) - 97

            if not curr_node.nodes[curr_char_index]:
                return False
            else:
                curr_node = curr_node.nodes[curr_char_index]

        return curr_node.is_word

    def startsWith(self, prefix: str) -> bool:
        curr_node, prefix_len = self.root, len(prefix)
        for char_index in range(prefix_len):
            curr_char = prefix[char_index]
            curr_char_index = ord(curr_char) - 97

            if not curr_node.nodes[curr_char_index]:
                return False
            else:
                curr_node = curr_node.nodes[curr_char_index]

        return True
