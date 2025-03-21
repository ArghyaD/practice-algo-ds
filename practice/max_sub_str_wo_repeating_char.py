
class MaxSubStrWithoutRepeatingCharacters:
    def solution(self, input_str: str):
        n = len(input_str)

        input_str = input_str.lower()
        result = 0

        for i in range(n):
            buffer = {}
            for j in range(i, n):
                if buffer.get(input_str[j]):
                    break

                buffer[input_str[j]] = True
                result = max(result, j - i + 1)

        return result

    def better_solution(self, input_str: str):
        n = len(input_str)
        result = 0
        input_str = input_str.lower()
        buffer = [False] * 26
        i = 0
        j = 0

        while j < n:
            if buffer[ord(input_str[j]) - ord('a')]:
                buffer[ord(input_str[j]) - ord('a')] = False
                i += 1
            else:
                buffer[ord(input_str[j]) - ord('a')] = True
                result = max(result, j - i + 1)
                j += 1
        return result


if __name__ == '__main__':
    obj = MaxSubStrWithoutRepeatingCharacters()
    input_str = "abcdabcdqp"
    print(f"Max sub-string length without repeating characters {obj.solution(input_str)}. ")
    print(f"Max sub-string length without repeating characters {obj.better_solution(input_str)}. ")
