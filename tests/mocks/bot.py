class Bot:
    
    def __init__(self):
        self.text = None
        self.chat_id = None

    def sendMessage(self, chat_id, text):
        self.chat_id = chat_id
        self.text = text