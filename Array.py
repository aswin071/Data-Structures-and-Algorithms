#The array data structure is a fundamental concept in programming. 
#It represents a fixed-size collection of elements of the same type, stored in contiguous memory locations. 
#Each element in the array is identified by its index, which is an integer value starting from 0.

class Array:
    def __init__(self):
        self.data = []
        self.length = 0

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        item = self.data.pop()
        self.length -= 1
        return item

    def delete(self, index):
        if index < 0 or index >= self.length:
            return None
        item = self.data.pop(index)
        self.length -= 1
        return item

    def reverse_array(arr):
        reversed_arr = []
        for i in range(len(arr) - 1, -1, -1):
            reversed_arr.append(arr[i])
        return reversed_arr

    def find_max_min(arr):
        if len(arr) == 0:
            return None, None
        max_value = min_value = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
            if arr[i] < min_value:
                min_value = arr[i]
        return max_value, min_value


arr = Array()
arr.push(10)
arr.push(20)
arr.push(30)
print(arr.get(1))  
print(arr.pop())  
print(arr.delete(0))  


