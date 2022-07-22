from logging import DEBUG, ERROR, INFO, Formatter, StreamHandler, getLogger


def get_loggers(logging_level):
    """config the logger format"""

    if logging_level.lower() == "info":
        log_lev = INFO
    elif logging_level.lower() == "debug":
        log_lev = DEBUG
    elif logging_level.lower() == "error":
        log_lev = ERROR

    formatter = Formatter(
        "%(asctime)s - %(name)s.%(lineno)d - %(levelname)s - %(message)s"
    )
    ch = StreamHandler()
    ch.setLevel(log_lev)
    ch.setFormatter(formatter)

    logger = getLogger()
    logger.setLevel(log_lev)
    logger.addHandler(ch)
    for ignore in (
        "boto",
        "boto3",
        "botocore",
        "requests",
        "urllib3",
        "simple",
        "s3transfer",
    ):
        getLogger(ignore).propagate = False

    return logger
