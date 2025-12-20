import csv
import rle_iterative
import rle_recursive
import logging
import timeit


def append_csv_row(file_path: str, row_data: list) -> None:
    try:
        open(file_path, "r")
    except IOError:
        logging.info(f"CSV file {file_path} does not exist, creating a new one.")
        with open(file_path, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["number", "text", "text_length", "character_variation", "encoded_length", "encoded_efficiency", "encoded_text", "decoded_text", "time_taken_encode", "time_taken_decode", "time_taken_both"])
    
    with open(file_path, "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row_data)


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