def guarded_encode(text: str, count: int = 1, i: int = 0) -> str|None:
    if text == "":
        return None
    
    return encode(text, count, i)

def encode(text: str, count: int = 1, i: int = 1) -> str:
    text_length = len(text)
    
    if text_length == i:
        return text[-1] + str(count)
    
    if text[i] == text[i - 1]: 
        count+=1
        return encode(text, count, i+1)
    
    return text[i - 1] + str(count) + encode(text, 1, i+1)


def decode(text: str, character: str = "", count: str = "", i: int = 1) -> str:
    if i >= len(text):
        result = character * int(count)
        return result
    
    if not text[i].isdigit():
        result = character * int(count)
        character=text[i]
        count = ''
        return result + decode(text, character, count, i+1)

    count += text[i]
    return decode(text, character, count, i+1)