import time
import datetime
try:
    class medical_store:

        id_cus = 0
        id_sup = 0
        id_pro = 1
        totaly = 0
        valuey = 0

        date = datetime.datetime.now()
        customer_details = {}
        suppliers_details = {}
        products_details = {}
        lst = []
        def __init__(self):
            pass
        def enter_customer(self, name, phone, purchased_product  , value):
            f = True
            for values in medical_store.customer_details.values():
                if values['name'] == name:
                    f = False
                    medical_store.totaly = values['total']
                    medical_store.valuey = values['value']+value
                    break

            if f:
                medical_store.totaly = 0
                medical_store.valuey = value
                medical_store.id_cus += 1
                medical_store.customer_details['U{}'.format(medical_store.id_cus)]={'name':name,'phone':phone,'purchased_product':purchased_product,
                                                                                'date':medical_store.date.strftime("%d/%m/%y"),'value':value}


            for valuee in medical_store.products_details.values():
                if valuee['name'] == purchased_product:
                    valuee['stock'] -= 1
                    medical_store.totaly += (value*valuee['price'])
                    break

            flag = False
            for namey in medical_store.customer_details.values():
                if namey['name'] == name:
                    namey['value'] = medical_store.valuey
                    namey['total'] = medical_store.totaly
                    flag = True
                    break

            if flag == False:
                medical_store.customer_details['U{}'.format(medical_store.id_cus)] = {'name':name,'phone':phone,'purchased_product':purchased_product,
                                                    'date':medical_store.date.strftime("%d/%m/%y"),'value':medical_store.valuey,'total':medical_store.totaly}

        def enter_supplier(self , name, phone, price , expire_date , stock , medical_product ):
            f = True
            for i in medical_store.suppliers_details.values():
                if i['name'] == name:
                    f = False
                    i['medical_product'].append(medical_product)
                    # medical_store.id_pro += 1
                    # medical_store.products_details['M{}'.format(medical_store.id_pro)] = {'name': medical_product,
                    #                                                                       'stock': stock,
                    #                                                                       'expire_date': expire_date,
                    #                                                                       'supplier_name': name,
                    #                                                                       'price': price}
                    break

            if f:
                medical_store.lst = []
                medical_store.id_sup += 1
                medical_store.lst.append(medical_product)
                medical_store.suppliers_details['S{}'.format(medical_store.id_sup)]={'name':name,'phone':phone,'price':price,'expireDate':expire_date,
                                                                                         'stock':stock,'medical_product':medical_store.lst}

                # medical_store.id_pro+=1
                # medical_store.products_details['M{}'.format(medical_store.id_pro)] = {'name': medical_product,
                #                                                                       'stock': stock,
                #                                                                       'expire_date': expire_date,
                #                                                                       'supplier_name': name,
                #                                                                       'price': price}
        def display_supplier(self):
            for key,value in medical_store.suppliers_details.items():
                print('supplier {} : {}'.format(key, value))
        def enter_product(self, name , stock , expire_date, supplier, price):
            medical_store.products_details['M{}'.format(medical_store.id_pro)]={'name':name,'stock':stock,
                                                                                'expire_date':expire_date,
                                                                                'supplier_name' : supplier,
                                                                                'price':price}
            medical_store.id_pro+=1
        def display(self):
            for i in medical_store.customer_details.items():
                print(i)
        def products_display(self):
            for key,value in medical_store.products_details.items():
                print('product {} : {}'.format(key,value))
                if value['stock'] < 5: print("This product ( {} ) should be purchased".format(value['name']))
        def discount(self):
           for value in medical_store.customer_details.values():
               if value['total'] > 500:
                   value['total']*=0.5

    while True:
        x = input("Enter your characteristic : ")
        if x == 'admin':
            admin1 = medical_store()
            name = input("Enter the name of the medicine : ")
            stoke = int(input("Enter the stoke of this medicine : "))
            expire_date = input("Enter the expire date of this medicine : ")
            supplier = input("Enter the name of supplier : ")
            price = int(input("Enter the price of this medicine : "))
            admin1.enter_product(name , stoke, expire_date, supplier ,price )
            admin1.products_display()
        else:
            y = input("Do you want to enter customer details or supplier details ? ")
            if y == 'customer':
                name = input("enter name : ")
                phone = input("enter phone : ")
                purchased_product = input("enter purchased product : ")
                value = int(input("enter its value : "))
                p1=medical_store()
                p1.enter_customer(name,phone,purchased_product ,value )
                p1.display()
                p1.discount()
                # p1.bill(value)

            else:
                name = input("Enter name : ")
                phone = input("Enter phone : ")
                medical_product = input("Enter the medical product : ")
                price = int(input("Enter the price of the medical product : "))
                expiration_date = input("Enter the expiration date : ")
                stock = int(input("Enter the the stock : "))
                p2= medical_store()
                p2.enter_supplier(name, phone,price ,expiration_date, stock,medical_product)
                p2.display_supplier()
        answer = input('Do you want to continue? (y/n) : ')
        if answer == 'n':
            break

except:
    print("There was an error")