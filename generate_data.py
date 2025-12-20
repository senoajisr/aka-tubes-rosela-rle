import csv
from enum import Enum
import rle_iterative
import rle_recursive
import logging
import timeit


class RleType(Enum):
    ITERATIVE = 0
    RECURSIVE = 0


def append_csv_row(file_path: str, row_data: list) -> None:
    try:
        open(file_path, "r")
    except IOError:
        logging.info(f"CSV file {file_path} does not exist, creating a new one.")
        with open(file_path, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["number", "text", "text_length", "character_variation", "encoded_length", "encoded_efficiency", "time_taken_encode", "time_taken_decode", "encoded_text", "decoded_text"])
    
    with open(file_path, "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row_data)


def character_times_n(character: str = "a", amount: int = 1000, rle_type: RleType = RleType.ITERATIVE, file_name: str = "example.csv") -> None:
    for i in range(1, amount+1):
        number: int = i
        text: str = character * i
        text_length: str = len(text)
        character_variation: int = len(set(text))
        time_taken_encode: float = 0
        time_taken_decode: float = 0
        decoded_text: str = ""
        
        if rle_type == RleType.ITERATIVE:
            time_taken_encode = timeit.timeit(lambda : rle_iterative.encode(text), number=1)
            encoded_text = rle_iterative.encode(text)
            
            time_taken_decode = timeit.timeit(lambda : rle_iterative.decode(encoded_text), number=1)
            decoded_text = rle_iterative.decode(encoded_text)
        
        if rle_type == RleType.RECURSIVE:
            time_taken_encode = timeit.timeit(lambda : rle_recursive.encode(text), number=1)
            encoded_text = rle_recursive.encode(text)
            
            time_taken_decode = timeit.timeit(lambda : rle_recursive.decode(encoded_text), number=1)
            decoded_text = rle_recursive.decode(encoded_text)
        
        encoded_length: int = len(encoded_text)
        encoded_efficiency: float = (1 - (encoded_length / text_length)) * 100
        
        row = [i, text, text_length, character_variation, encoded_length, encoded_efficiency, time_taken_encode, time_taken_decode , encoded_text, decoded_text]
        append_csv_row(f"datas/{file_name}", row)
        logging.debug(f"generated: {row}")


def single_run() -> None:
    text_encode: str = "abbcccddddeeeeeF"
    text_decode: str = "a1b2c3d4e5F1"
    logging.info(f"Input text to encode is \"{text_encode}\"")
    logging.info(f"Input text to decode is \"{text_decode}\"")
    
    runtime: float = timeit.timeit(lambda : rle_iterative.encode(text_encode), number=1)
    result: str = rle_iterative.encode(text_encode)
    logging.info(f"Run time for iterative RLE encode is {runtime} with result {result}")
    
    runtime: float = timeit.timeit(lambda : rle_iterative.decode(text_decode), number=1)
    result: str = rle_iterative.decode(text_decode)
    logging.info(f"Run time for iterative RLE decode is {runtime} with result {result}")
    
    runtime: float = timeit.timeit(lambda : rle_recursive.encode(text_encode), number=1)
    result: str = rle_recursive.encode(text_encode)
    logging.info(f"Run time for recursive RLE encode is {runtime} with result {result}")
    
    runtime: float = timeit.timeit(lambda : rle_recursive.decode(text_decode), number=1)
    result: str = rle_recursive.decode(text_decode)
    logging.info(f"Run time for recursive RLE decode is {runtime} with result {result}")