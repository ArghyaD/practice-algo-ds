

class MaximumSubArrayProduct:
    def solution(self, arr):
        smallest_negative_product = arr[0]
        largest_positive_product = arr[0]
        max_product = arr[0]
        for val in arr[1:]:
            smallest_negative_product, largest_positive_product = (
                min(val, val*smallest_negative_product, val*largest_positive_product),
                max(val, val*smallest_negative_product, val*largest_positive_product)
            )
            max_product = max(largest_positive_product, max_product)
        return max_product

if __name__ == "__main__":
    m = MaximumSubArrayProduct()
    print(m.solution([2, -1, 7, 3, -2, 1, -7]))

