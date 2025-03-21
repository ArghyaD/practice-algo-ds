

class ThreeSum:
    @classmethod
    def naive_approach(cls, arr, target):
        result = []

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if target == arr[i] + arr[j] + arr[k]:
                        result.append([i, j, k])
        return result

    @classmethod
    def better_approach(cls, arr, target):
        """
            Approach:
                Here we eliminate the 3 loop to reduce the time complexity
                from O(n^3) to O(n^2).

                To do that we use a Dictionary where we store the values
                as key and their keys as value.

                And whenever we compute arr[i] + arr[j], inside the inner loop,
                we also check if target - (arr[i] + arr[j]) is there in the dictionary

                If yes, we fetch it's key and append the i, j, k in the result.

                NOTE: To ensure that duplicate lists are not inserted in the result,
                we use a set data structure.
        :param arr:
        :param target:
        :return:
        """
        result = set()
        length = len(arr)

        for i in range(length - 1):
            buffer = {}
            for j in range(length):
                value = target - (arr[i] + arr[j])
                if buffer.get(value) and (i != j) and (j != buffer[value]) and (i != buffer[value]):
                    result.add(tuple(sorted([i, j, buffer[value]])))
                buffer[arr[i]] = i
                buffer[arr[j]] = j
        return list(result)

    @classmethod
    def optimal_approach(cls, arr, target):
        pass

if __name__ == '__main__':
    print(ThreeSum.naive_approach(arr=[0, -1, 2, -3, 1], target=0))
    print(ThreeSum.naive_approach(arr=[1, -2, 1, 0, 5], target=0))
    print(ThreeSum.naive_approach(arr=[2, 3, 1, 0, 5], target=0))

    print(ThreeSum.better_approach(arr=[0, -1, 2, -3, 1], target=0))
    print(ThreeSum.better_approach(arr=[1, -2, 1, 0, 5], target=0))
    print(ThreeSum.better_approach(arr=[2, 3, 1, 0, 5], target=0))
