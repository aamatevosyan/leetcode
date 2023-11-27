class Node(
    var isWord: Boolean = false,
    val children: Array<Node?> = Array<Node?>(26) { null }
)

class Trie(
    val root: Node = Node(),
) {

    fun insert(word: String) {
        var current = root
        
        for (c in word) {
            val ind = getInd(c)
            if (current.children[ind] == null) {
                current.children[ind] = Node()
            }
            current = current.children[ind]!!
        }
        
        current.isWord = true
    }
    
    private fun getInd(c: Char) = c.code - 'a'.code
    
    private fun find(word: String): Node {
        var current = root
        
        for (c in word) {
            val ind = getInd(c)
            if (current.children[ind] == null) {
                return root
            }
            current = current.children[ind]!!
        }
        
        return current
    }

    fun search(word: String): Boolean {
        val node = find(word)
        
        return node != root && node.isWord
    }

    fun startsWith(prefix: String): Boolean {
        val node = find(prefix)
        
        return node != root
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */