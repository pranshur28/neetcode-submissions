class Solution:
    def isValid(self, s: str) -> bool:

        new_hash = {}

        new_hash['('] = ')'
        new_hash['{'] = '}'
        new_hash['['] = ']'

        my_stack = []

        for char in s:
            if char in new_hash.keys():
                my_stack.append(char)
            else:
                if not my_stack:
                    return False
                opener = my_stack.pop()
                if new_hash[opener] == char:
                    pass
                else:
                    return False
        return not my_stack
            



                

        
        

        
        