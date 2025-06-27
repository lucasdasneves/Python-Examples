
def inverse_string(text_new: str) -> str:
    """
    This is a code based on an exercise made by a company
    The idea is to inverse the words from a text
    Input: text
    Return: inversed text
    """
    list_of_str = string_content.rsplit(" ")
    
    list_of_str.reverse()
    
    new_string = " ".join(str(i) for i in list_of_str)
    print(new_string)
    return new_string
    
string_content = "This is a test"

inverse_string(text_new=string_content)
