import logging

count = 0


def user_log():
    logging.basicConfig(filename='user_actions.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info("Info message Occurred")
    logging.warning('Warning message occurred')
    logging.error('Error message occurred')
    logging.critical('Critical message occurred')
    if logging.info:
        count +=1
        if count == 20:
            raise SystemExit("To many attempts.")
    