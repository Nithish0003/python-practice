def count_words(text):
    try:    
        tmp=text.count(" ")
        return tmp+1
    except Exception as e:
        return e
def count_char(text):
    try:
        tmp=text.count("")
        return tmp-1
    except Exception as e:
        return e
def reverse_char(text):
    try:
        return text[::-1]
    except Exception as e:
        return e
def capitalize_words(text):
    try:
        return text.capitalize()
    except Exception as e:
        return e