from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
from constants import (
    LOGIN_INTERVAL,
    _,
    TOTAL__MAX,
    LOOP,
    _MAX,
    WAITING_INTERVAL,
    RELEASING_INTERVAL,
    SLACK_CHANNEL_LOG,
    _URL,
    _ID,
    _PASSWORD,
    _SWITCH,
)
from helpers import (
    driver,
    _,
    _,
    slack_app,
    search_value,
)


def access_():
    driver.get(_URL)

    time.sleep(LOGIN_INTERVAL * 2)
    login_id = driver.find_element_by_name("")
    login_pass = driver.find_element_by_name("")
    login_id.send_keys(_ID)
    login_pass.send_keys(_PASSWORD)

    login_btn = driver.find_element_by_xpath("")
    login_btn.click()

    time.sleep(LOGIN_INTERVAL)
    access_btn = driver.find_element_by_xpath("")
    access_btn.click()

    time.sleep(LOGIN_INTERVAL)
    driver.switch_to.frame("")
    driver.find_element_by_xpath("").click()

    time.sleep(LOGIN_INTERVAL)
    _dropdown = driver.find_element_by_xpath("")
    _select = Select(_dropdown)
    _select.select_by_index(_ + 2)

    time.sleep(LOGIN_INTERVAL)
    subject_dropdown = driver.find_element_by_xpath("")
    subject_select = Select(subject_dropdown)
    subject_select.select_by_index(1)

    time.sleep(LOGIN_INTERVAL)
    driver.find_element_by_xpath("").click()


def switch_():
    _dropdown = driver.find_element_by_xpath("")
    _select = Select(_dropdown)
    _select.select_by_index(3)


# frameの切替
def switch_frame():
    driver.switch_to.default_content()
    frame = driver.find_element_by_xpath("")
    driver.switch_to.frame(frame)
    driver.find_element_by_xpath("").click()


def get__():
    for _ in range(5):
        try:
            access_()
        except NoSuchElementException as e:
            slack_app(f"\n\n>>>{e}", SLACK_CHANNEL_LOG)
            time.sleep(5)
        else:
            slack_app("", SLACK_CHANNEL_LOG)
            break
    else:
        slack_app(f"。", SLACK_CHANNEL_LOG)

    _number = 0
    absence_count = 0
    current_amount = 0
    has__change = False
    has__start = False
    has_end_ = False

    while True:
        try:
            switch_frame()
        except Exception:
            slack_app("", SLACK_CHANNEL_LOG)
            break

        try:
            data_exist = driver.find_element_by_id("").text
        except Exception as e:
            slack_app(f"\n\n>>>{e}", SLACK_CHANNEL_LOG)

            for _ in range(10):
                try:
                    access_()
                except:
                    slack_app(f"\n\n>>>{e}", SLACK_CHANNEL_LOG)
                    time.sleep(2)
                else:
                    slack_app("", SLACK_CHANNEL_LOG)
                    has__start = True
                    break
            else:
                slack_app("", SLACK_CHANNEL_LOG)

            switch_frame()
            data_exist = ""
        finally:
            absence_count = absence_count + 1 if data_exist == "" else 0

        if data_exist != "":
            if not has__start:
                if not has__change:
                    slack_app(
                        f"{'' if _ == 0 else ''}",
                        SLACK_CHANNEL_LOG,
                    )
                has__start = True

            for i in range(LOOP):
                try:
                    if "" in driver.find_element_by_xpath("").text:
                        has_end_ = True

                    can_get_ = search_high_value(i)
                    if can_get_[0]:  # bool
                        get_button = driver.find_element_by_xpath("")
                        name = driver.find_element_by_xpath("").text
                        get_button.click()
                        if driver.find_element_by_id("").text != "":
                            if has__change or _ == 1:
                                exam_s.append(name)
                                current_amount += can_get_[1]  # float
                            else:
                                exam_backnumbers.append(name)
                            slack_app(f"{name}", SLACK_CHANNEL_LOG)
                            _number += 1
                        else:
                            slack_app(f"", SLACK_CHANNEL_LOG)

                    if _number >= _MAX or current_amount >= TOTAL__MAX:
                        break
                except:
                    break

        if _number >= _MAX or current_amount >= TOTAL__MAX:
            break

        if has__start and ((absence_count == 15) or (has_end_ and absence_count == 5)):
            if has__change:
                break
            else:
                if _SWITCH and not _:
                    slack_app("", SLACK_CHANNEL_LOG)
                    has__change = True
                    has_end_ = False
                    has__start = False
                    absence_count = 0
                    switch_()
                else:
                    break

        # サーバ負担軽減
        time.sleep(RELEASING_INTERVAL if has__start else WAITING_INTERVAL)
