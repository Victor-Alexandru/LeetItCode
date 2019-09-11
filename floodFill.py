import copy
class Solution:
    def infest(self,arr,sr,sc,value,newValue):
           if sr-1>=0 and arr[sr-1][sc] == value:
              old_value =copy.copy(arr[sr-1][sc])               
              arr[sr-1][sc] = newValue
              self.infest(arr,sr-1,sc,old_value,newValue)
           if sr+1<len(arr) and arr[sr+1][sc] == value:
              old_value =copy.copy(arr[sr+1][sc])               
              arr[sr+1][sc] = newValue
              self.infest(arr,sr+1,sc,old_value,newValue)
           if sc-1>=0 and arr[sr][sc-1] == value:
              old_value =copy.copy(arr[sr][sc-1])                             
              arr[sr][sc-1] = newValue
              self.infest(arr,sr,sc-1,old_value,newValue)

           if sc+1<len(arr) and arr[sr][sc+1] == value:
              old_value =copy.copy(arr[sr][sc+1])                                           
              arr[sr][sc+1] = newValue
              self.infest(arr,sr,sc+1,old_value,newValue)


    def floodFill(self, image, sr, sc, newColor):
           old_value =copy.copy(image[sr][sc]) 
           image[sr][sc]=newColor
           self.infest(image,sr,sc,old_value,newColor)
           return image


s=Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))