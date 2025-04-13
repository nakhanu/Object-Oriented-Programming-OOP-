# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

# Child Class
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"📸 Taking a {self.camera_megapixels}MP photo!")

# Create Objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
print(phone1.info())
phone1.call("0712345678")

camera_phone = CameraPhone("iPhone", "14 Pro", 256, 48)
print(camera_phone.info())
camera_phone.take_photo()
