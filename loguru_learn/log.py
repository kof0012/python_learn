from pathlib import Path

import notifiers
from loguru import logger
from notifiers.logging import NotificationHandler

project_path = Path.cwd().parent
log_path = Path(project_path, "log")

# 是否开启回溯
backtrace = True

rotation = "7 days"


def info_only(record):
    return record["level"].name == "INFO"


logger.add(
    log_path / "info_log.log",
    backtrace=backtrace,
    filter=info_only,
    rotation=rotation,
    encoding="utf-8",
    enqueue=True,
    retention="14 days",
)


def warning_only(record):
    return record["level"].name == "WARNING"


logger.add(
    log_path / "warning_log.log",
    backtrace=backtrace,
    filter=warning_only,
    rotation=rotation,
    encoding="utf-8",
    enqueue=True,
    retention="14 days",
)


def debug_only(record):
    return record["level"].name == "DEBUG"


logger.add(
    log_path / "debug_log.log",
    backtrace=backtrace,
    filter=debug_only,
    rotation=rotation,
    encoding="utf-8",
    enqueue=True,
    retention="14 days",
)


def error_only(record):
    print(record)
    print(record["time"])
    return record["level"].name == "ERROR"


logger.add(
    log_path / "error_log.log",
    backtrace=backtrace,
    filter=error_only,
    rotation=rotation,
    encoding="utf-8",
    enqueue=True,
    retention="14 days",
)

params = {
    "host": "smtp.qq.com",
    "port": 465,
    "username": "1358244533@qq.com",
    "from": "1358244533@qq.com",
    "password": "wettvkqaipkdfgdi",
    "to": ["1358244533@qq.com"],
    "subject": "邮件标题",
    "ssl": True,
}

# # 测试用
# notifier = notifiers.get_notifier("email")
# notifier.notify(message="The application is running!", **params)

handler = NotificationHandler("email", defaults=params)
logger.add(handler, filter=error_only)

if __name__ == "__main__":
    # for i in range(10):
    #     Process(target=wlog, args=(i,)).start()

    # logger.info("中文test")
    # logger.debug("中文test")
    # logger.warning("中文test")
    # logger.error("中文test")
    logger.exception(Exception(""))
    # logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    # n1 = "cool"
    # n2 = [1, 2, 3]
    # logger.info(f'If you are using Python {n1}, prefer {n2} of course!')
    # hash("[TREASURE : T-TALK \ud83d\udde3'YOSHI x PARK JEONG WOO']\n#TRE")
    # import re
    #
    # string: str = "[TREASURE : T-TALK \ud83d\udde3'YOSHI x PARK JEONG WOO']\n#TRE"
    # # print(type("\ud83d\udde3"))
    # l = re.findall(r"([\ud000-\udfff])", string)
    # print(l)

    # print(string)
