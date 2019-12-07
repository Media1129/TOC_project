from transitions.extensions import GraphMachine
from utils import send_text_message
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction
from utils import send_button_message



class TocMachine(GraphMachine):
    Ibreakfast = {'calorie':0,'dollar':0,'starch':0,'protein':0,'money':0}
    Ilunch     = {'calorie':0,'dollar':0,'starch':0,'protein':0,'money':0}   
    Idinner    = {'calorie':0,'dollar':0,'starch':0,'protein':0,'money':0}
    height = 175
    weight = 40
    Totalmoney = 1300
    Totalcalorie = 2000
    Totalstarch = 700
    Totalprotein = 120
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #start
    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"
    def on_enter_start(self, event):
        TocMachine.Ibreakfast['calorie'] = 0
        TocMachine.Ibreakfast['dollar'] = 0
        TocMachine.Ibreakfast['starch'] = 0
        TocMachine.Ibreakfast['protein'] = 0
        TocMachine.Ibreakfast['money'] = 0
        TocMachine.Ilunch['calorie'] = 0
        TocMachine.Ilunch['dollar'] = 0
        TocMachine.Ilunch['starch'] = 0
        TocMachine.Ilunch['protein'] = 0
        TocMachine.Ilunch['money'] = 0
        TocMachine.Idinner['calorie'] = 0
        TocMachine.Idinner['dollar'] = 0
        TocMachine.Idinner['starch'] = 0
        TocMachine.Idinner['protein'] = 0
        TocMachine.Idinner['money'] = 0
        
        btn_action=[
            MessageTemplateAction(
                label='輸入餐點',
                text='regfood'
            ),
            MessageTemplateAction(
                label='輸入個人資料',
                text='Information'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"請輸入")

    #input the food
    def is_going_to_regfood(self, event):
        text = event.message.text
        return text.lower() == "regfood"
    def on_enter_regfood(self, event):
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
    
    #input the information
    def is_going_to_information(self, event):
        text = event.message.text
        return text.lower() == "information"
    def on_enter_information(self, event):
        btn_action=[
            MessageTemplateAction(
                label='手動輸入身高',
                text='height'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"輸入資訊")
    #input the height
    def is_going_to_height(self, event):
        text = event.message.text
        return True
    def on_enter_height(self, event):
        print("in height")
        text = event.message.text
        TocMachine.height = int(text)
        btn_action=[
            MessageTemplateAction(
                label='手動輸入體重',
                text='weight'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"輸入資訊")
    #input the weight
    def is_going_to_weight(self, event):
        text = event.message.text
        return True
    def on_enter_weight(self, event):
        text = event.message.text
        TocMachine.weight = int(text)
        print("in weight")
        print(TocMachine.height,"=height")
        print(TocMachine.weight,"=weight")
        #     Totalmoney = 1300
        # Totalcalorie = 2000
        # Totalstarch = 700
        self.go_regfood(event)





    #check
    def on_enter_examine(self, event, strback):
        print("in examine")
        print(strback)
        self.go_money(event,strback)
    
    def on_enter_money_check(self, event, strback):
        print("in money check")
        sum = TocMachine.Idinner['money'] +TocMachine.Ibreakfast['money'] + TocMachine.Ilunch['money'] 
        print(TocMachine.Ibreakfast['money'],"breakfast")
        print(TocMachine.Ilunch['money'],"lunch")
        print(TocMachine.Idinner['money'],"dinner")
        print(sum,"sum = ")
        if sum < TocMachine.Totalmoney:
            self.go_calorie(event,strback)
        else:
            self.go_money_deny(event,strback)

    
    def on_enter_calorie_check(self, event,strback):
        print("in calorie check")
        sum = TocMachine.Idinner['calorie'] + TocMachine.Ibreakfast['calorie'] + TocMachine.Ilunch['calorie'] 
        print(TocMachine.Ibreakfast['calorie'],"breakfast")
        print(TocMachine.Ilunch['calorie'],"lunch")
        print(TocMachine.Idinner['calorie'],"dinner")
        print(sum,"sum = ")

        if sum < TocMachine.Totalcalorie:
            self.go_starch(event,strback)
        else:
            self.go_calorie_deny(event,strback)
        

    def on_enter_starch_check(self, event,strback):
        print("in starch check")
        sum = TocMachine.Idinner['starch'] +TocMachine.Ibreakfast['starch'] + TocMachine.Ilunch['starch'] 
        print(TocMachine.Ibreakfast['starch'],"breakfast")
        print(TocMachine.Ilunch['starch'],"lunch")
        print(TocMachine.Idinner['starch'],"dinner")
        print(sum,"sum = ")
        if sum < TocMachine.Totalstarch:
            self.go_regfood(event)
        else:
            self.go_starch_deny(event,strback)



        
    
    #deny
    def on_enter_money_deny(self, event, strback):
        print("in money deny")
        
        if strback == "breakfast":
            self.go_breakfast(event,'餘額不足')
        elif strback == "lunch":
            self.go_lunch(event,'餘額不足')
        else:
            self.go_dinner(event,'餘額不足')
        
    def on_enter_calorie_deny(self, event,strback):
        print("in calorie deny")
        if strback == "breakfast":
            self.go_breakfast(event,"熱量過多")
        elif strback == "lunch":
            self.go_lunch(event,"熱量過多")
        else:
            self.go_dinner(event,"熱量過多")
        
    def on_enter_starch_deny(self, event,strback):
        print("in starch deny")
        if strback == "breakfast":
            self.go_breakfast(event, "澱粉過多")
        elif strback == "lunch":
            self.go_lunch(event, "澱粉過多")
        else:
            self.go_dinner(event, "澱粉過多")
    
        

    #breakfast
    def is_going_to_breakfast(self, event,indic=""):
        text = event.message.text
        return text.lower() == "breakfast"
    def on_enter_breakfast(self, event ,indic=""):
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
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"早餐",indic)
    
    def is_going_to_nextbreakfast(self, event):
        text = event.message.text
        return True
    def on_enter_nextbreakfast(self, event):
        text = event.message.text
        print(text,"check the nextbreakfast")
        if text == 'hamegg':
            TocMachine.Ibreakfast['calorie'] = 500
            TocMachine.Ibreakfast['dollar']  = 500
            TocMachine.Ibreakfast['starch']  = 500
            TocMachine.Ibreakfast['protein'] = 500
            TocMachine.Ibreakfast['money'] = 500
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in hamegg")
        elif text == 'chiomelet':
            TocMachine.Ibreakfast['calorie'] = 500
            TocMachine.Ibreakfast['dollar']  = 500
            TocMachine.Ibreakfast['starch']  = 500
            TocMachine.Ibreakfast['protein'] = 500
            TocMachine.Ibreakfast['money'] = 500
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in chiomelet")
        elif text == 'riceroll':
            TocMachine.Ibreakfast['calorie'] = 500
            TocMachine.Ibreakfast['dollar']  = 500
            TocMachine.Ibreakfast['starch']  = 500
            TocMachine.Ibreakfast['protein'] = 500
            TocMachine.Ibreakfast['money'] = 500
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in riceroll")
        self.go_examine(event,"breakfast")

    
    #lunch
    def is_going_to_lunch(self, event):
        text = event.message.text
        return text.lower() == "lunch"
    def on_enter_lunch(self, event,indic=""):
        btn_action=[
            MessageTemplateAction(
                label='Subway',
                text='subway'
            ),
            MessageTemplateAction(
                label='炒飯',
                text='friedrice'
            ),
            MessageTemplateAction(
                label='乾麵',
                text='noodles'
            ),
            MessageTemplateAction(
                label='便當',
                text='boxedlunch'
            )
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"午餐",indic)
    #next lunch
    def is_going_to_nextlunch(self, event):
        text = event.message.text
        return True
    def on_enter_nextlunch(self, event):
        text = event.message.text
        print(text,"check the nextlunch")
        if text == 'subway':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['dollar']  = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money'] = 600
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in subway")
        elif text == 'friedrice':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['dollar']  = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money'] = 600
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in friedrice")

        elif text == 'noodles':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['dollar']  = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money'] = 600
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in noodles")
        elif text == 'boxedlunch':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['dollar']  = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money'] = 600
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in boxedlunch")
        self.go_examine(event,"lunch")
    
    #dinner
    def is_going_to_dinner(self, event):
        text = event.message.text        
        return text.lower() == "dinner"
    def on_enter_dinner(self, event,indic=""):
        btn_action=[
            MessageTemplateAction(
                label='海南雞飯',
                text= 'chickenrice'
            ),
            MessageTemplateAction(
                label='關東煮',
                text='oden'
            ),
            MessageTemplateAction(
                label='涼麵',
                text='coldnoodle'
            ),
            MessageTemplateAction(
                label='打拋豬飯',
                text='chilipork'
            )
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"晚餐",indic)
    #next dinner
    def is_going_to_nextdinner(self, event):
        text = event.message.text
        return True
    def on_enter_nextdinner(self, event):
        text = event.message.text
        print(text,"check the nextdinner")
        if text == 'chickenrice':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['dollar']  = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money'] = 700
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in chickenrice")
        elif text == 'oden':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['dollar']  = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money'] = 700
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in oden")

        elif text == 'coldnoodle':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['dollar']  = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money'] = 700
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in coldnoodle")
        elif text == 'chilipork':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['dollar']  = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money'] = 700
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in chilipork")
        self.go_examine(event,"dinner")

    # def on_exit_state2(self):
    #     print("Leaving state2")
