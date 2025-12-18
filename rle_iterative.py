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
    
    for i in range(0, len(text), 2):
        result += text[i] * int(text[i+1])
    
    return result