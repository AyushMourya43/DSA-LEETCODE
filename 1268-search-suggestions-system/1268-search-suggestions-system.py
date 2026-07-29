class Solution(object):
    def suggestedProducts(self, products, searchWord):
        
        products.sort()
        prefix = ""
        ans = []

        for ch in searchWord:
            prefix +=ch

            low = 0
            high = len(products)-1

            while low <= high:

                mid = low + (high - low) //2

                if products[mid] < prefix : # # Search right half
                    low = mid +1

                else:        # Search left half
                    high = mid -1

            temp = []
              # Check only 3 products
            for i in range(low,min(low + 3 , len(products))):
                 if products[i].startswith(prefix):
                    temp.append(products[i])

            ans.append(temp)

        return ans            

#brute force 

#  products.sort()

#         ans = []

#         prefix = ""

#         for ch in searchWord:

#             prefix += ch

#             temp = []

#             for product in products:

#                 if product.startswith(prefix):
#                     temp.append(product)

#                 if len(temp) == 3:
#                     break

#             ans.append(temp)

#         return ans