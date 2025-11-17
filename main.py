import rle_iterative
import rle_recursive
import logging

def main() -> None:
    initialize_logging()


def initialize_logging() -> None:
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Logging initialized.")


if __name__ == "__main__":
    main()