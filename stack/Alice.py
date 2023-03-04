s="/""u""/""love""\\""i""\\"
stack = [""]

for ch in s[1:-1]:

  if ch == "\\":

    last_str = stack.pop()

    stack[-1] += last_str[::-1]

    continue

  if ch == "/":

    stack.append("")

    continue

  stack[-1] += ch
  print(stack)
print(stack[-1][::-1])
        

