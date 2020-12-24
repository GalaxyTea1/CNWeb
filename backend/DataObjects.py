import psycopg2
from BusinessObjects import Customer as CustomerEntity
from BusinessObjects import Product as ProductEntity
from BusinessObjects import Shipper as ShipperEntity

class Customer:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, customer):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO TblCustomers(CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s)"
            record_to_insert = (customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblcustomers"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CustomerEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblcustomers WHERE customerid=%s"
            cur.execute(sql, (customer.CustomerID,))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = CustomerEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Customer ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblcustomers SET customername=%s, contactname=%s, address=%s, city=%s, postalcode=%s, country=%s WHERE customerid=%s "
            cur.execute(sql,(customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country, customer.CustomerID))
            con.commit()           
            row = cur.rowcount
            if row > 0:
                return 'Updated customer', 200
            con.close()
            return 'Customer ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblcustomers WHERE customerid=%s"
            cur.execute(sql,(customer.CustomerID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

# class Product:
#     def __init__(self, ConnectionData):
#         self.ConnectionData = ConnectionData
#     def insert(self, product):
#         con = None
#         try:
#             con = psycopg2.connect(user=self.ConnectionData['user'],
#                                   password=self.ConnectionData['password'],
#                                   host=self.ConnectionData['host'],
#                                   port=self.ConnectionData['port'],
#                                   database=self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "INSERT INTO tblproducts(ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%s, %s, %s, %s, %s)"
#             record_to_insert = (product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price)
#             cur.execute(sql, record_to_insert)
#             con.commit()
#             con.close()
#             return 'Insert TblProducts successfully'
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def get_all(self):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "SELECT * FROM tblproducts"
#             cur.execute(sql)
#             con.commit()           
#             rows = cur.fetchall()
#             result = []
#             for row in rows:
#                 c = ProductEntity()
#                 c.fetch_data(row)
#                 result.append(c.to_json())
#             con.close()
#             return result
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def get_by_id(self, product: ProductEntity):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "SELECT * FROM tblproducts WHERE productid=%s"
#             cur.execute(sql, (product.ProductID,))
#             con.commit()           
#             row = cur.fetchone()
#             if row:
#                 c = ProductEntity()
#                 c.fetch_data(row)
#                 return c, 200
#             con.close()
#             return 'Product ID not found', 404
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def update(self, product: ProductEntity):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "UPDATE tblproducts SET productname=%s, supplierid=%s, categoryid=%s, unit=%s, price=%s WHERE productid=%s "
#             cur.execute(sql,(product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price, product.ProductID))
#             con.commit()           
#             row = cur.rowcount
#             if row > 0:
#                 return 'Updated product', 200
#             con.close()
#             return 'Product ID not found', 404
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def delete(self, product: ProductEntity):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "DELETE FROM tblproducts WHERE productid=%s"
#             cur.execute(sql,(product.ProductID,))
#             con.commit()           
#             row = cur.rowcount
#             if row>0:
#                 return "Delete Product", 200
#             con.close()
#             return "Product ID not found", 404
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

# class Shipper:
#     def __init__(self, ConnectionData):
#         self.ConnectionData = ConnectionData
#     def insert(self, shipper):
#         con = None
#         try:
#             con = psycopg2.connect(user=self.ConnectionData['user'],
#                                   password=self.ConnectionData['password'],
#                                   host=self.ConnectionData['host'],
#                                   port=self.ConnectionData['port'],
#                                   database=self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "INSERT INTO tblshippers(ShipperID, ShipperName, Phone) VALUES (%s, %s, %s)"
#             record_to_insert = (shipper.ShipperID, shipper.ShipperName, shipper.Phone)
#             cur.execute(sql, record_to_insert)
#             con.commit()
#             con.close()
#             return 'Insert TblShippers successfully'
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def get_all(self):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "SELECT * FROM tblshippers"
#             cur.execute(sql)
#             con.commit()           
#             rows = cur.fetchall()
#             result = []
#             for row in rows:
#                 c = ShipperEntity()
#                 c.fetch_data(row)
#                 result.append(c.to_json())
#             con.close()
#             return result
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def get_by_id(self, shipper: ShipperEntity):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "SELECT * FROM tblshippers WHERE shipperid=%s"
#             cur.execute(sql, (shipper.ShipperID,))
#             con.commit()           
#             row = cur.fetchone()
#             if row:
#                 c = ShipperEntity()
#                 c.fetch_data(row)
#                 return c, 200
#             con.close()
#             return 'Shipper ID not found', 404
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def update(self, shipper: ShipperEntity):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "UPDATE tblshippers SET shippername=%s, phone=%s WHERE shipperid=%s "
#             cur.execute(sql,(shipper.ShipperName, shipper.Phone, shipper.ShipperID))
#             con.commit()           
#             row = cur.rowcount
#             if row > 0:
#                 return 'Updated shipper', 200
#             con.close()
#             return 'Shipper ID not found', 404
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

#     def delete(self, shipper: ShipperEntity):
#         con = None
#         try:
#             con = psycopg2.connect(user = self.ConnectionData['user'],
#                                 password = self.ConnectionData['password'],
#                                 host = self.ConnectionData['host'],
#                                 port = self.ConnectionData['port'],
#                                 database = self.ConnectionData['database'])
#             cur = con.cursor()
#             sql = "DELETE FROM tblshippers WHERE shipperid=%s"
#             cur.execute(sql,(shipper.ShipperID,))
#             con.commit()           
#             row = cur.rowcount
#             if row>0:
#                 return "Delete Shipper", 200
#             con.close()
#             return "Shipper ID not found", 404
#         except (Exception, psycopg2.DatabaseError) as error:
#             return str(error)
#         finally:
#             if con is not None:
#                 con.close()

if __name__ == "__main__":
    print('this is data object package')