# http://lifemichael.com/moodle/mod/assign/view.php?id=13619

# Develop a new module. Its name should be MathUtils. It should include the following methods: sum, multiply,
# difference and divide. The new module should include the definition for the MathUtilsException class.
# MathUtilsException should extend Exception.
# When trying to call the divide function passing over 0 as the second argument a MathUtilsException should be raised.

import math_utils_from_statement as mathUtils


# mathUtils.devide(3, 0)
mathUtils.devide(3, 1)


try:
    print(int(mathUtils.devide(3, 0)))

except mathUtils.MyException:
    print("MyException was caught.")
