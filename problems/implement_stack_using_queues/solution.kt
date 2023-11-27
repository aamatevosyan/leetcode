import java.util.LinkedList
import java.util.Queue

class MyStack {
    private val input: Queue<Int> = LinkedList<Int>()
    private val output: Queue<Int> = LinkedList<Int>()

    fun push(x: Int) {
        while (input.isNotEmpty()) {
            output.add(input.poll())
        }

        input.add(x)

        while (output.isNotEmpty()) {
            input.add(output.poll())
        }
    }

    fun pop(): Int {
        return input.poll()
    }

    fun top(): Int {
        return input.peek() 
    }

    fun empty(): Boolean {
        return input.isEmpty() && output.isEmpty()
    }

}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */