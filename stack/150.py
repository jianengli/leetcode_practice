class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        para = ['+','-','*','/'] 
        for ele in tokens:
            if ele in para:
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                if ele == para[0]:
                    stack.append(t1+t2)
                elif ele == para[1]:
                    stack.append(t2-t1)
                elif ele == para[2]: 
                    t = t1*t2
                    stack.append(t)
                elif ele == para[3]:
                    stack.append(int(t2/t1))
                continue
            
            stack.append(int(ele))
        return stack.pop()
            