from abc import ABC, abstractmethod

# Target
class MessageService(ABC):
    @abstractmethod
    def new_send(self):
        pass

# Adaptee
class MailMessage:
    def __init__(self, msg):
        self.__msg = msg
    
    def send(self):
        return f'メッセージを送信(メール): {self.__msg}'

# Adapter
class MessageServiceAdapter(MessageService):
    def __init__(self, mail_msg: MailMessage):
        self.__mail_msg = mail_msg
        
    def new_send(self):
        message = self.__mail_msg.send()
        return message + ' **Adapter経由で送信'
    
adaptee = MailMessage('おはようございます。今から業務を始めます。')

adapter = MessageServiceAdapter(adaptee)
print(adapter.new_send())