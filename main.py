import rle_iterative
import rle_recursive
import logging

def main() -> None:
    initialization()


def initialization():
    initialize_logging()
    display_credits()


def display_credits() -> None:
    logging.info("Tugas besar Analisis Kompleksitas Algoritma menggunakan algoritma RLE secara iteratif dan rekursif.")
    logging.info("Dibuat oleh tim Rosela:")
    logging.info("> 103012500136 - Senoaji Sapta Ramadhana")


def initialize_logging() -> None:
    format = "%(asctime)s | %(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    logging.debug("Logging initialized.")


if __name__ == "__main__":
    main()