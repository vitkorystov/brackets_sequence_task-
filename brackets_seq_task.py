

def is_correct_brackets_sequence(br_sequence):
    stack = []
    for s in br_sequence:
        if not stack:
            stack.append(s)
        else:
            if (stack[-1] == '(' and s == ')') \
                    or (stack[-1] == '{' and s == '}') \
                    or (stack[-1] == '[' and s == ']'):
                stack.pop()
            else:
                stack.append(s)
    res = True if not stack else False
    return res


bracket_seq_incorrect = "[(({)}){}]"
bracket_seq_correct = "{}([])[[]()]"

print(is_correct_brackets_sequence(bracket_seq_incorrect))
print(is_correct_brackets_sequence(bracket_seq_correct))
