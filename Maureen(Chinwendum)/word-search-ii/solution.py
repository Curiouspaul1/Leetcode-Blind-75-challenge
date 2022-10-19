class TrieNode:

	def __init__(self, char='', parent=None):

		self.char = char
		self.children = dict()
		self.is_end = False
		self.num_of_words_downward = 0
		self.parent = parent


	def prune(self, node):

		while node:
			node.num_of_words_downward -= 1
			node = node.parent


class Trie:

	def __init__(self):

		self.root = TrieNode()


	def insert(self, word: str):

		node = self.root

		for char in word:

			if char not in node.children:
				new_node = TrieNode(char)
				new_node.parent = node
				node.children[char] = new_node

			node = node.children[char]
			node.num_of_words_downward += 1

		node.is_end = True


class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

		trie = Trie()
		ans = []

		for word in words:
			trie.insert(word)

		for i in range(len(board)):
			for j in range(len(board[0])):
				self.dfs(board, trie.root, i, j, '', ans)

		return ans


	def dfs(self, board, node, i, j, path, ans):

		if node.is_end:
			ans.append(path)
			node.is_end = False
			node.prune(node)

		if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1:
			return

		tmp = board[i][j]
		if tmp not in node.children or node.children[tmp].num_of_words_downward == 0:
			return

		board[i][j] = '#'
		for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
			self.dfs(board, node.children[tmp], i + x, j + y, path + tmp, ans)
		board[i][j] = tmp