import re

pattern = re.compile("[abc]123")

result = pattern.findall("a123k3gggfasf43gggb123ggg2")

print(result)