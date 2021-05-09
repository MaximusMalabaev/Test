class English:
    def thank_you(self):
        print("Tthank you")

class French(English):
    def thank_you(self):
        print("Merci")

class Italian(English):
    def thank_you(self):
        print("Grazie")

class German(Italian):
    def thank(self):
        print("Danke")


class NewLanguage(German, English):
    pass 

lang = NewLanguage() 
lang.thank_you()



