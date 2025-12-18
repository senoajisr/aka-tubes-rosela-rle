def encode(text: str, count: int = 1, i: int = 0) -> str:
    text_length = len(text)
    i += 1
    
    if text_length == i:
        return text[-1] + str(count)
    
    if text[i] == text[i - 1]: 
        count+=1
        return encode(text, count, i)
    
    return text[i - 1] + str(count) + encode(text, 1, i)


def decode(text: str, i: int = 0) -> str:
    if i >= len(text):
        return ""
    
    result = text[i] * int(text[i+1])
    return result + decode(text, i+2)