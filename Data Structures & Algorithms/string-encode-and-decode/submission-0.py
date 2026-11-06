class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: # first we check if the list is empty 
            return ""
        sizes, res=[],[]# sizes stores the length of each word in the list
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:#if the input is ["Hello","World"] we want ["5",",","5",",","#","Hello","World"]
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        print(''.join(res))#join will compine the whole list
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:# check if the string is empty
            return []
        #we want retrive the numbers of each word until we reach our dividor #
        sizes , res, i = [],[],0
        while s[i] !='#':
            j = i
            while s[j] != ',':
                j+= 1
            sizes.append(int(s[i:j]))
            i=j+1
        i+=1
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        return res

        

