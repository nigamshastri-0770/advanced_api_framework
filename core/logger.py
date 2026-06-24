import logging
import os


os.makedirs(
    "logs",
    exist_ok=True
)


logger = logging.getLogger(
    "api"
)

logger.setLevel(
    logging.INFO
)


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)


file = logging.FileHandler(
    "logs/api.log"
)

file.setFormatter(
    formatter
)


console = logging.StreamHandler()

console.setFormatter(
    formatter
)


if not logger.handlers:
    logger.addHandler(file)
    logger.addHandler(console)