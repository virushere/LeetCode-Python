class Solution:
    def isValid(self, s: str) -> bool:
        # array = []
        # for item in s:
        #     if item == "(" or item == "[" or item == "{":
        #         array.append(item)
        #     elif item == ")" or item == "]" or item == "}":
        #         if not array:
        #             return false
        #         # Identify the element to pop
        #         # as it is stack  FILO the last element will be poped
        #         # array = ["[", "{", "(" , ")", "}", "]"]
        #         # array = ["[", "{", "(" , ")" , "}"]
        #         # array = ["[", "{", "(" , ")"]
        #         # array = ["[", "{", "(" ]
        #         # array = ["[", "{" ]
        #         # array = ["["]
        #         # array = []
        #         top_element = array.pop()
        #         if item == ")" and top_element != "(":
        #             return False
        #         if item == "]" and top_element != "[":
        #             return False
        #         if item == "}" and top_element != "{":
        #             return False
        #     else:
        #         continue
        # return len(array) == 0

        ## We can also solve this using a dictonary

        # first define a stack
        stack = []

        # now define a dictionary with key and value pairs
        map = {"]":"[", "}":"{", ")":"(" }

        for char in s:
            if char in map:
                top_element = stack.pop() if stack else "#"

                if map[char] != top_element:
                    return False
            
            else:
                stack.append(char)

        return not stack