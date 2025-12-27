import generate_data
import logging
import csv
import sys

import rle_iterative
import rle_recursive


def main() -> None:
    initialization()
    #example()

    #generate_data.character_times_n(rle_type=generate_data.RleType.ITERATIVE, file_name="iterative_a_times_n.csv", amount=10000)
    #generate_data.process_kbbi_words(generate_data.RleType.ITERATIVE, "iterative_kbbi_words.csv")
    #generate_data.character_times_n(rle_type=generate_data.RleType.RECURSIVE, file_name="recursive_a_times_n.csv", amount=10000)
    #generate_data.process_kbbi_words(generate_data.RleType.RECURSIVE, "recursive_kbbi_words.csv")

    print(rle_iterative.encode('aaabbb'))
    print(rle_iterative.decode('a3b3'))
    print(rle_recursive.encode('aaabbb'))
    print(rle_recursive.decode('a3b3'))


def example() -> None:
    generate_data.single_run()
    generate_data.append_csv_row("data/example.csv", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])


def initialization() -> None:
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
    sys.setrecursionlimit(11000)
    logging.basicConfig(format=format, level=logging.DEBUG)
    logging.debug("Logging initialized.")


if __name__ == "__main__":
    main()