# Create a function that reverses a string

def reverse(string):
    reversed = ""

    if type(string) != str or len(string) < 2:
        return False

    for i in range(len(string)):
        i+=1
        reversed += string[-i]
    
    return reversed

print(reverse("This is a test string"))


