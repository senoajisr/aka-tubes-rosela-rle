import rle_iterative
import rle_recursive
import logging
import timeit
import csv


csv_file_path: str = "datas/a_times_n.csv"


def main() -> None:
    initialization()
    single_run()
    append_csv_row(["a", "b", "c", "d", "e", "f", "g", "h", "i"])


def append_csv_row(row: list):
    try:
        open(csv_file_path, "r")
    except IOError:
        logging.info(f"CSV file {csv_file_path} does not exist, creating a new one.")
        with open(csv_file_path, "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["number", "text", "text_length", "character_variation", "encoded_length", "encoded_efficiency", "encoded", "decoded", "time_taken"])
    
    with open(csv_file_path, "a") as file:
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


def initialization():
    initialize_logging()
    display_credits()


def display_credits() -> None:
    logging.info("Tugas besar Analisis Kompleksitas Algoritma menggunakan algoritma RLE secara iteratif dan rekursif.")
    logging.info("Dibuat oleh tim Rosela:")
    logging.info("> 103012500136 - Senoaji Sapta Ramadhana")
    logging.info("> 103012580031 - Togi Samuel Simarmata")
    logging.info("> 103012500355 - Tiara Br Siahaan")


def initialize_logging() -> None:
    format = "%(asctime)s | %(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG)
    logging.debug("Logging initialized.")


if __name__ == "__main__":
    main()