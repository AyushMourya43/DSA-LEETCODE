class Solution(object):
    def mostWordsFound(self, sentences):
        
        ans = 0

        for sentence in sentences :
            ans = max(ans,sentence.count(" ")+1) 

        return ans    


        #  by split function 
        #  ans = 0 
        #  for sentence in sentences:
        #     ans = max(ans,len(sentence.split()))

        #  return ans     
