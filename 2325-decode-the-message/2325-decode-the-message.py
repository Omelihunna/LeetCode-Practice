class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        checker = []
        [checker.append(x) for x in list(key) if x not in checker and x != " "]
      
        new_dict = {}
        for x in range(len(checker)):
            new_dict[checker[x]] = alpha[x]
        my_str = ''
        for x in message:
            if x == ' ':
                my_str += ' '
            else:
                my_str += new_dict[x]
        return my_str