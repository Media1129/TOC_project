from transitions.extensions import GraphMachine
from utils import send_text_message
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction
from utils import send_button_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #start
    def is_going_to_start(self, event):
        btn_action=[
            MessageTemplateAction(
                label='輸入餐點',
                text='regfood'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"請輸入")
        text = event.message.text
        return text.lower() == "start"
    #input the food
    def is_going_to_regfood(self, event):
       
        btn_action=[
            MessageTemplateAction(
                label='早餐',
                text='breakfast'
            ),
            MessageTemplateAction(
                label='午餐',
                text='lunch'
            ),
            MessageTemplateAction(
                label='晚餐',
                text='dinner'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"選擇餐點")
        text = event.message.text
        return text.lower() == "regfood"
    #breakfast
    def is_going_to_breakfast(self, event):
        btn_action=[
            MessageTemplateAction(
                label='火腿蛋三明治',
                text='hamegg'
            ),

            MessageTemplateAction(
                label='蛋餅',
                text='chiomelet'
            ),
            MessageTemplateAction(
                label='飯糰',
                text='riceroll'
            ),
            MessageTemplateAction(
                label='下一頁',
                text='nextbreakfast'
            )
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"早餐")
        
        text = event.message.text
        return text.lower() == "breakfast"
    def is_going_to_nextbreakfast(self, event):
        btn_action=[
            MessageTemplateAction(
                label='豬肉漢堡',
                text='hamburger'
            ),
            MessageTemplateAction(
                label='皮蛋瘦肉粥',
                text='porridge'
            ),
            MessageTemplateAction(
                label='饅頭',
                text='steamedbun'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"早餐")
        
        text = event.message.text
        return text.lower() == "nextbreakfast"
    def is_going_to_hamegg(self, event):
        text = event.message.text
        return text.lower() == "hamegg"
    def is_going_to_chiomelet(self, event):
        text = event.message.text
        return text.lower() == "chiomelet"
    def is_going_to_riceroll(self, event):
        text = event.message.text
        return text.lower() == "riceroll"
    def is_going_to_hamburger(self, event):
        text = event.message.text
        return text.lower() == "hamburger"
    def is_going_to_porridge(self, event):
        text = event.message.text
        return text.lower() == "porridge"
    def is_going_to_steamedbun(self, event):
        text = event.message.text
        return text.lower() == "steamedbun"
    #lunch
    def is_going_to_lunch(self, event):
        btn_action=[
            MessageTemplateAction(
                label='Subway',
                text='subway'
            ),
            MessageTemplateAction(
                label='蛋餅',
                text='chiomelet'
            ),
            MessageTemplateAction(
                label='飯糰',
                text='riceroll'
            ),
            MessageTemplateAction(
                label='下一頁',
                text='nextbreakfast'
            )
        ]
      
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"午餐")

        text = event.message.text
        return text.lower() == "lunch"
    #dinner
    def is_going_to_dinner(self, event):
        btn_action=[
            MessageTemplateAction(
                label='ButtonsTemplate',
                text='ButtonsTemplate'
            ),
            MessageTemplateAction(
                label='ButtonsTemplate',
                text='ButtonsTemplate'
            )
        ]
           
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"晚餐")
        
        text = event.message.text
        return text.lower() == "dinner"


    # def on_enter_state1(self, event):
    #     print("I'm entering state1")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state1")
    #     self.go_back()

    # def on_exit_state1(self):
    #     print("Leaving state1")

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")
