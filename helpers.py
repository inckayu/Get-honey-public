import requests
from selenium import webdriver
import pandas as pd
from constants import (
    _,
    Q_A,
    Q_B,
    Q_C,
    Q_D,
    Q_E,
    Q_F,
    Q_G,
    _MAX,
    SLACK_TOKEN,
    SLACK_CHANNEL_RESULT,
    SLACK_CHANNEL_LOG,
    LIMITATION,
    SLACK_URL,
    CHROMEDRIVER_PATH,
    _MIN,
    _MAX,
    BASIC_,
    _SWITCH,
)

exam_backnumbers = []
exam_genres = []
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

# slackアプリでメッセージ送信
def slack_app(text, channel):
    headers = {"Authorization": "Bearer " + SLACK_TOKEN}
    data = {"channel": channel, "text": text}
    requests.post(SLACK_URL, headers=headers, data=data)

def confirm_variables():
    if _SWITCH:
        if _ == 0:
            target_ = ""
        else:
            target_ = ""
    else:
        if _ == 0:
            target_genre = ""
        else:
            target_genre = ""

    body = f"\n\n>>>:  {target_}\n:  {_MIN}\n:  {_MAX}"

    slack_app(body, SLACK_CHANNEL_LOG)

def generate__list():
    input_book = pd.ExcelFile("")
    df = input_book.parse()
    df = df[df._ >= _MIN]
    df = df[df._ <= _MAX]
    selected_= []
    selected___index = []

    if Q_A:
        selected___index.append(2)
        selected___index.append(6)
    if Q_B:
        selected___index.append(3)
        selected___index.append(4)
    if Q_C:
        selected___index.append(7)
        selected___index.append(9)
    if Q_D:
        selected___index.append(0)
        selected___index.append(8)
    if Q_E:
        selected___index.append(5)
    if Q_F:
        selected___index.append(1)
    if Q_G:
        selected___index.append(10)

    for item in selected___index:
        selected__.append(_list[item])

    global df_selected_, target_
    df_selected_ = df[df[""].isin(selected__)]
    target_ = [
        list(e) for e in zip(df_selected_[""], df_selected_[""])
    ]


def search__value(num):
    is_over_ = False
    _name = driver.find_element_by_xpath(
        ''
    ).text

    for value in target_:
        if value[0] in _name:
            is_over_ = True
            _ = float(value[1])
            break
    if is_over_:
        return True, 
    else:
        return not LIMITATION, 0


def calc(item, kind):
    if kind == 0:
        item = item[:-4]
    try:
        target = df_selected_[df_selected_._ == item]
        output = (target._).to_string(index=False)
        return float(output)
    except:
        return 0


def _(item, kind):
    if kind == 0:
        item = item[:-4]
    try:
        target = df_selected_[df_selected_._ == item]
        output = (target._).to_string(index=False)
        return output
    except:
        return "-"


def result_output():
    result_ = ">"
    result_ = ">"
    _ = 0
    _ = 0

    if _ == []:
        result_ += ""
    if _ == []:
        result_ += ""
    for item in _:
        _ += calc(item, 0)
        result_ += f"{item},  {calc(item, 0)},  {_(item, 0)}\n>"
    for item in _:
        _ += calc(item, 1)
        result_ += f"{item},  {calc(item, 1)},  {_(item, 1)}\n>"

    _sum = len(_) + len(_)
    _sum = _ + _
    _ = f"**\n:{round(_, 3)},  :{len(_)},  : {round(_*BASIC_)}\n{result_}"
    _ = f"**\n:{round(_, 3)},  :{len(_)},  : {round(_*BASIC_)}\n{result_}"
    bar = "-" * 30
    slack_app(
        f"{_sum}\n: {round(_sum, 3)},  : {round(_sum*BASIC_)}\n{bar}\n\n{}\n\n{}",
        SLACK_CHANNEL_RESULT,
    )
