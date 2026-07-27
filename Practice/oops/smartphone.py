class Caller:
    
    def make_call(self,number): 
        print(f"Calling: {number}")

    def end_call(self): 
        print("Call ended!")

class Camera:
    def take_photo(self): 
        print("📸 Photo taken!")

    def record_video(self): 
        print("🎥 Recording started")

class Browser:
    def open_url(self,url): 
        print(f"Opening: {url}")

class SmartPhone(Caller, Camera, Browser):
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def specs(self): 
        print(f"Brand: {self.brand} | Model: {self.model}")

phone = SmartPhone("Samsung", "S24")
phone.specs()
phone.make_call("9876543210")   # Caller se mila
phone.take_photo()              # Camera se mila
phone.open_url("google.com")    # Browser se mila
phone.end_call()

# MRO check karo:
print(SmartPhone.__mro__)