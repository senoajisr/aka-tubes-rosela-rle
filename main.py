import rle_iterative
import rle_recursive
import logging
import timeit


def main() -> None:
    initialization()
    
    text: str = "abbcccddddeeeeeF"
    logging.info(f"Input text \"{text}\"")
    
    iterative_runtime: float = timeit.timeit(lambda : rle_iterative.encode(text))
    iterative_result: str = rle_iterative.encode(text)
    logging.info(f"Run time for iterative {iterative_runtime} with result {iterative_result}")
    
    recursive_runtime: float = timeit.timeit(lambda : rle_recursive.encode(text))
    recursive_result: str = rle_recursive.encode(text)
    logging.info(f"Run time for recursive {recursive_runtime} with result {recursive_result}")


def initialization():
    initialize_logging()
    display_credits()


def display_credits() -> None:
    logging.info("Tugas besar Analisis Kompleksitas Algoritma menggunakan algoritma RLE secara iteratif dan rekursif.")
    logging.info("Dibuat oleh tim Rosela:")
    logging.info("> 103012500136 - Senoaji Sapta Ramadhana")


def initialize_logging() -> None:
    format = "%(asctime)s | %(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG)
    logging.debug("Logging initialized.")


if __name__ == "__main__":
    main()