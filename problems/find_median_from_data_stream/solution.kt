import java.util.PriorityQueue

class MedianFinder {
    private val maxPriorityQueue = PriorityQueue<Int>({ a, b -> b - a })
    private val minPriorityQueue = PriorityQueue<Int>({ a, b -> a - b })

    fun addNum(num: Int) {
        if (maxPriorityQueue.size == minPriorityQueue.size) {
            minPriorityQueue.add(num)
            maxPriorityQueue.add(minPriorityQueue.poll())
        } else {
            maxPriorityQueue.add(num)
            minPriorityQueue.add(maxPriorityQueue.poll())
        }
    }

    fun findMedian(): Double {
        if (maxPriorityQueue.size == minPriorityQueue.size) {
            return (maxPriorityQueue.peek() + minPriorityQueue.peek()) * 0.5;
        } else {
            return maxPriorityQueue.peek() * 1.0;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */