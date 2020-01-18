# This is an example from class.
# Date: 9.1.2020

import re


def lessonReTest():
    pattern = re.compile("[abc]123")
    result = pattern.findall("a123k3gggfasf43gggb123ggg2")
    print(result)


lessonReTest()
