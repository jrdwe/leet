
# runtime: O(n)
# space:   O(n)

class Solution(object):
    def isIsomorphic(self, s, t):
        
        # used to store what we switched
        keypairs = {}

        # iterate and transform 
        for index in range(len(s)):
            
            # case: key hasn't been given a value
            if s[index] not in keypairs:

                # case: value has been used for another key
                if t[index] in keypairs.values():
                    return False

                # switch with new value from 't'
                keypairs[s[index]] = t[index]
            else:
                # case: key has been used for another value
                if keypairs[s[index]] != t[index]:
                    return False
        
        return True

