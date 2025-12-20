import logging


def encode(text: str) -> str:
    result: str = ''
    count = 1  
    
    for i in range(1, len(text)):
        if text[i] == text[i - 1]: 
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1  
    
    result += text[-1] + str(count)
    
    return result


def decode(text: str) -> str:
    result: str = ''
    character: str = text[0]
    count: str = ''
    
    for i in range(1, len(text)):
        if not text[i].isdigit():
            result += character * int(count)
            character=text[i]
            count = ''
            continue
        
        count += text[i]
    
    result += character * int(count)
    
    return result