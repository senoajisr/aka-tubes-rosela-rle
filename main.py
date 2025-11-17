import rle_iterative
import rle_recursive
import logging

def main() -> None:
    initialize_logging()


def initialize_logging() -> None:
    format = "%(asctime)s | %(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    logging.debug("Logging initialized.")


if __name__ == "__main__":
    main()