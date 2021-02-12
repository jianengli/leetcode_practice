class Solution:
    def simplifyPath(self, path: str) -> str:
        strs = list(path.split('/'))
        stack = []
        for ele in strs:
            if ele == '' or ele == '.':
                continue
            elif ele == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        print('/'.join(stack))
        return '/'+'/'.join(stack)