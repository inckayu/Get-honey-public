import datetime
import time
from constants import START_TIME, SLACK_CHANNEL_LOG
from get import get
from helpers import (
    driver,
    generate__list,
    confirm_variables,
    slack_app,
    result_output,
)


def main():
    flag = True
    confirm_variables()
    while flag:
        if datetime.datetime.now().hour >= START_TIME:
            generate__list()
            slack_app("", SLACK_CHANNEL_LOG)
            get()
            result_output()
            slack_app("", SLACK_CHANNEL_LOG)
            flag = False
            driver.quit()
        time.sleep(30)


main()
