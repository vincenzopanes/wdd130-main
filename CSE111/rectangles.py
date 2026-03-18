def get_possitive_value(prompt_text):
    """
    Prompt the user for a value, and re-prompt them if the 
    original vaule is negative
    """
    # prompt for the value
    value = float(input(prompt_text))

    #ccheck if the value is positive and re-prompt if needed
    while value < 0:
        print("Sorry. The value cannot be negative")
        value = float(input(prompt_text))

    # return the value
    return value

length = get_possitive_value("What is the length of the rectangle? ")
width = get_possitive_value("What is the width of the rectangle? ")

area = length * width
print(f"The area is {area:.0f}")