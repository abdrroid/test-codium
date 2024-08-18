phone_list = []

class MobilePhone():
    def __init__ (self, model = "", color = "", battery = 0):
        self.model = model
        self.color = color
        self.battery = battery
    
    def charge(model, battery):
        global phone_list
        for phone in phone_list:
            if phone.model == model:
                if battery <= 0:
                    return
                if phone.battery + battery <= 100:
                    phone.battery += battery
                else:
                    phone.battery = 100
                return
        print("Такой модели не существует")
       
    
    def uncharge(model, battery):
        for phone in phone_list:
            if phone.model == model:
                if battery >= 0 and phone.battery  - battery >= 0:
                    phone.battery -= battery
                elif battery <= 0 and phone.battery + battery >= 0:
                    phone.battery += battery
                else:
                    phone.battery = 0
                return
        print("Такой модели не существует")
    

  def show_all():
    for i in range(0, len(phone_list)):
        print(phone_list[i].info())
    def info(self):
        print(f"Модель {self.model}, Цвет {self.color}, battery {self.battery}")

phones = [
    {
        "model" : "Samsung",
        "color" : "Black",
        "battery" : 15
    },
    {
        "model" : "Iphone",
        "color" : "White",
        "battery" : 19
    },
    {
        "model" : "Pixel",
        "color" : "Gray",
        "battery" : 8
    },
    {
        "model" : "Nokia",
        "color" : "Blue",
        "battery" : 99
    },
]


for i in phones:
    phone = MobilePhone(i["model"], i["color"], i["battery"])
    phone_list.append(phone)
