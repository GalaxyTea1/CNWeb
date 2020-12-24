class Customer:
    def __init__(self, CustomerID=None, CustomerName=None, ContactName=None, Address=None, City=None, PostalCode=None, Country=None):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country

    def fetch_data(self,data):
        self.CustomerID = data[0]
        self.CustomerName = data[1]
        self.ContactName = data[2]
        self.Address = data[3]
        self.City = data[4]
        self.PostalCode = data[5]
        self.Country = data[6]

    def to_json(self):
        return{
            'CustomerID': self.CustomerID,
            'CustomerName': self.CustomerName,
            'ContactName': self.ContactName,
            'Address': self.Address,
            'City': self.City,
            'PotalCode': self.PostalCode,
            'Country': self.Country
        }

class Product:
    def __init__(self, ProductID=None, ProductName=None, SupplierID=None, CategoryID=None, Unit=None, Price=None):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.Unit = Unit
        self.Price = Price

    def fetch_data(self, data):
        self.ProductID = data[0]
        self.ProductName = data[1]
        self.SupplierID = data[2]
        self.CategoryID = data[3]
        self.Unit =  data[4]
        self.Price = data[5]

    def to_json(self):
        return{
            'ProductID': self.ProductID,
            'ProductName': self.ProductName,
            'SupplierID': self.SupplierID,
            'CategoryID': self.CategoryID,
            'Unit': self.Unit,
            'Price': self.Price
        }


class Shipper:
     def __init__(self, ShipperID=None, ShipperName=None, Phone=None):
        self.ShipperID = ShipperID
        self.ShipperName = ShipperName
        self.Phone = Phone


    def fetch_data(self, data):
        self.ShipperID = data[0]
        self.ShipperName = data[1]
        self.Phone = data[2]


    def to_json(self):
        return{
            'ShipperID': self.ShipperID,
            'ShipperName': self.ShipperName,
            'Phone': self.Phone
        } 

if __name__ == "__main__":
    print('this is business object package')