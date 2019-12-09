import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def send_fsm(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    fsm = ImageSendMessage(
        original_content_url='https://i.imgur.com/8EU4lGi.png',
        preview_image_url='https://i.imgur.com/8EU4lGi.png'
    )
    line_bot_api.reply_message(reply_token, fsm)
    return "OK"

def send_button_message(reply_token,btn_action,indicate,textdic='選擇接近的餐點',imageurl='https://i.imgur.com/Fe3neuK.jpg'):
    line_bot_api = LineBotApi(channel_access_token)
    if textdic == "":
        textdic = "選擇接近的餐點"
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            thumbnail_image_url=imageurl,
            title=indicate,
            text=textdic,
            actions=btn_action
        )
    )

    line_bot_api.reply_message(reply_token, buttons_template )

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
