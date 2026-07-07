class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for i in tokens:
            match i:
                case "*":
                    val = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                case "+":
                    val = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)

                case "-":
                    val = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                case "/":
                    val = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                case _:
                    stack.append(int(i))
            
        return int(stack[0])