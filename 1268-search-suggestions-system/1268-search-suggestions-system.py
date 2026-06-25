class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        result = []
        prefix = ""

        def lower_bound(arr, target):
            left, right = 0, len(arr)

            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        for char in searchWord:
            prefix += char
            start = lower_bound(products, prefix)

            suggestions = []

            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])

            result.append(suggestions)

        return result