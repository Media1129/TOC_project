from transitions.extensions import GraphMachine
from utils import send_text_message
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction
from utils import send_button_message



class TocMachine(GraphMachine):
    Ibreakfast = {'calorie':0,'starch':0,'protein':0,'money':0}
    Ilunch     = {'calorie':0,'starch':0,'protein':0,'money':0}   
    Idinner    = {'calorie':0,'starch':0,'protein':0,'money':0}
    height = 175
    weight = 84
    Totalmoney = 300
    Totalcalorie = 2200
    Totalstarch = 134
    Totalprotein = 100
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #start
    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"
    def on_enter_start(self, event):
        TocMachine.Ibreakfast['calorie'] = 0
        TocMachine.Ibreakfast['starch'] = 0
        TocMachine.Ibreakfast['protein'] = 0
        TocMachine.Ibreakfast['money'] = 0
        TocMachine.Ilunch['calorie'] = 0
        TocMachine.Ilunch['starch'] = 0
        TocMachine.Ilunch['protein'] = 0
        TocMachine.Ilunch['money'] = 0
        TocMachine.Idinner['calorie'] = 0
        TocMachine.Idinner['starch'] = 0
        TocMachine.Idinner['protein'] = 0
        TocMachine.Idinner['money'] = 0
        
        btn_action=[
            MessageTemplateAction(
                label='輸入個人資料',
                text='information'
            ),
            MessageTemplateAction(
                label='輸入餐點',
                text='regfood'
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
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入身高(cm)")
    #input the height
    def is_going_to_height(self, event):
        text = event.message.text
        return True
    def on_enter_height(self, event):
        print("in height")
        text = event.message.text
        TocMachine.height = int(text)
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入體重(kg)")
    #input the weight
    def is_going_to_weight(self, event):
        text = event.message.text
        return True
    def on_enter_weight(self, event):
        text = event.message.text
        TocMachine.weight = int(text)
        print("in weight")
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入每日預算(dollar)")

    #input the money
    def is_going_to_money(self, event):
        text = event.message.text
        return True
    def on_enter_money(self, event):
        text = event.message.text
        TocMachine.Totalmoney = int(text)
        print("in money")
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入年齡")
    #input the age
    def is_going_to_age(self, event):
        text = event.message.text
        return True
    def on_enter_age(self, event):
        text = event.message.text
        TocMachine.age = int(text)
        # bmr = (13.7 x 體重) + (5.0 x 身高) – (6.8 x 年齡) + 66
        bmr = (13.7*TocMachine.weight) + (5*TocMachine.height) - (6.8*TocMachine.age) + 66
        tdee = bmr * 1.375 - 300
        TocMachine.Totalstarch = tdee * 0.3/4 #starch=tdee*0.3/4
        TocMachine.Totalcalorie = tdee
        # print("in age")
        # print(TocMachine.height,"=height")
        # print(TocMachine.weight,"=weight")
        # print(TocMachine.Totalmoney,"totalmoney")
        # print(TocMachine.age,"age")
        # print(bmr,"bmr")
        # print(tdee,'tdee')
        # print(TocMachine.Totalcalorie,"Totalcalorie")
        # print(TocMachine.Totalstarch,"Totalstarch")
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
                label='三明治 輸入(1+$)',
                text='hamegg'
            ),
            MessageTemplateAction(
                label='蛋餅 輸入(2+$)',
                text='chiomelet'
            ),
            MessageTemplateAction(
                label='飯糰 輸入(3+$)',
                text='riceroll'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"早餐",indic)
    #next breakfast
    def is_going_to_nextbreakfast(self, event):
        text = event.message.text
        return True
    def on_enter_nextbreakfast(self, event):
        text = event.message.text
        input = text.split()
        print(input)
        # print(text,"check the nextbreakfast")
        if input[0] == '1':
            TocMachine.Ibreakfast['calorie'] = 500
            TocMachine.Ibreakfast['starch']  = 500
            TocMachine.Ibreakfast['protein'] = 500
            TocMachine.Ibreakfast['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in hamegg")
        elif input[0] == '2':
            TocMachine.Ibreakfast['calorie'] = 500
            TocMachine.Ibreakfast['starch']  = 500
            TocMachine.Ibreakfast['protein'] = 500
            TocMachine.Ibreakfast['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in chiomelet")
        elif input[0] == '3':
            TocMachine.Ibreakfast['calorie'] = 500
            TocMachine.Ibreakfast['starch']  = 500
            TocMachine.Ibreakfast['protein'] = 500
            TocMachine.Ibreakfast['money']   = int(input[1])
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
                label='subway 輸入(1+$)',
                text='subway'
            ),
            MessageTemplateAction(
                label='炒飯 輸入(2+$)',
                text='friedrice'
            ),
            MessageTemplateAction(
                label='乾麵 輸入(3+$)',
                text='noodles'
            ),
            MessageTemplateAction(
                label='雞腿便當 輸入(4+$)',
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
        input = text.split()
        print(input)
        # print(text,"check the nextlunch")
        if input[0] == '1':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in subway")
        elif input[0] == '2':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money'] = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in friedrice")

        elif input[0] == '3':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in noodles")
        elif input[0] == '4':
            TocMachine.Ilunch['calorie'] = 600
            TocMachine.Ilunch['starch']  = 600
            TocMachine.Ilunch['protein'] = 600
            TocMachine.Ilunch['money']   = int(input[1])
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
                label='海南雞飯 輸入(1+$)',
                text= 'chickenrice'
            ),
            MessageTemplateAction(
                label='關東煮 輸入(2+$)',
                text='oden'
            ),
            MessageTemplateAction(
                label='涼麵 輸入(3+$)',
                text='coldnoodle'
            ),
            MessageTemplateAction(
                label='打拋豬飯 輸入(4+$)',
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
        input = text.split()
        print(input)
        # print(text,"check the nextdinner")
        if input[0] == '1':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in chickenrice")
        elif input[0] == '2':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in oden")

        elif input[0] == '3':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in coldnoodle")
        elif input[0] == '4':
            TocMachine.Idinner['calorie'] = 700
            TocMachine.Idinner['starch']  = 700
            TocMachine.Idinner['protein'] = 700
            TocMachine.Idinner['money']   = int(input[1])
            print(TocMachine.Ibreakfast['money'],"breakfast")
            print(TocMachine.Ilunch['money'],"lunch")
            print(TocMachine.Idinner['money'],"dinner")
            print("in chilipork")
        self.go_examine(event,"dinner")
