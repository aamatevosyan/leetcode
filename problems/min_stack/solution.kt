import java.util.Stack

class MinStack {
    private val stack = Stack<Int>()
    private val minStack = Stack<Int>()

    fun push(`val`: Int) {
        if (minStack.isEmpty() || `val` <= getMin()) {
            minStack.push(`val`)
        }
        stack.push(`val`)
    }

    fun pop() {
        if (stack.pop() == getMin()) {
            minStack.pop()
        }
    }

    fun top(): Int {
        return stack.peek()
    }

    fun getMin(): Int {
        return minStack.peek()
    }

}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = MinStack()
 * obj.push(`val`)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */