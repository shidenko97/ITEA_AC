import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.DEBUG,
)
#
# logging.basicConfig(level=logging.INFO)


# logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
#
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')
#
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')
#
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')
#
# for n in range(1,5):
#     logging.warning(f"{n}")

# import logging
#
a = 5
b = 0

try:
    c = a / b
except Exception:
    logging.exception("Key Error")
print("program execute...")
#

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
