class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        left_products=[]
        right_products=[]


        for i in range (length):
            if i == 0:
                product = 1
            elif i > 0:
                product *= nums[i-1]
            left_products.append(product)

        for i in range (length - 1,-1,-1):
            if i == length - 1:
                product = 1
            elif i < length - 1 :
                product *= nums[i+1]
            right_products.append(product)
        right_products = right_products[::-1]

        result = [left_products[i]*right_products[i] for i in range(length)]
        return result


        


            


        