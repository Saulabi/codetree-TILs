class DynamicArray:
    def __init__(self):
        self.array = []


    def push_back(self, value):
        self.array.append(value)


    def pop_back(self):
        if self.array:
            self.array.pop()


    def size(self):
        return len(self.array)


    def get(self, k):
        if 1 <= k <= self.size():
            return self.array[k - 1]
        else:
            return None


N = int(input())
dynamic_array = DynamicArray()

for _ in range(N):
    command = input().split()

    if command[0] == "push_back":
        value = int(command[1])
        dynamic_array.push_back(value)

    elif command[0] == "pop_back":
        dynamic_array.pop_back()

    elif command[0] == "size":
        print(dynamic_array.size())

    elif command[0] == "get":
        k = int(command[1])
        result = dynamic_array.get(k)
        if result is not None:
            print(result)