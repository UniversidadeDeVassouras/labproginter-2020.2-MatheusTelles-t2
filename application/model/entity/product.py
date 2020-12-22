class Produto:
    def __init__(self, id, name, image, price, atual_price, description, parcel, parcel_value):
        self._id = id
        self._name = name
        self._image = image
        self._price = price
        self._atual_price = atual_price
        self._description = description
        self._parcel = parcel
        self._parcel_value = parcel_value


    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getImage(self):
        return self._image

    def getPrice(self):
        return self._price

    def getAtualPrice(self):
        return self._atual_price

    def getDescription(self):
        return self._description

    def getParcel(self):
        return self._parcel

    def getParcelValue(self):
        return self._parcel_value
