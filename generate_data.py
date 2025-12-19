import rle_iterative
import rle_recursive
import logging
import timeit


def append_csv_row(file_path: str, row: list):
    try:
        open(file_path, "r")
    except IOError:
        logging.info(f"CSV file {file_path} does not exist, creating a new one.")
        with open(file_path, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["number", "text", "text_length", "character_variation", "encoded_length", "encoded_efficiency", "encoded", "decoded", "time_taken"])
    
    with open(file_path, "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow()


def single_run():
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