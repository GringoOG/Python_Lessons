is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male ! ")
elif is_male and not(is_tall):
    print("You are a male, but not tall")
elif not(is_male) and is_tall:
    print("You are not a male,but you are tall")
else:
    print("You are neither male and tall")


is_short = True
is_big = True

if is_short or is_big:
    print("You are short and big!")
else:
    print("You are neither short or big or both")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:    # != - not equal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(40, 5, 6))











