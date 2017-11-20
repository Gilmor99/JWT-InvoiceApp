# JWT-InvoiceApp
Project Title - Invoice Genertaion backend using API

Python Django Rest Framework (http://www.django-rest-framework.org) CRUD application built with JWT authentication & security (https://jwt.io/) to mange accounts with associated invoices and line-items.

Getting Started -

Using your browser's address bar, point to the application @ https://invoicegenerator-jwt.herokuapp.com. For login information please contact gilmor99@gmail.com.

How to use the application -

1. Get security token @ https://invoicegenerator-jwt.herokuapp.com/api/auth/token/obtain/ .
2. After login, you can - Create / Read / Update / Delete Accounts, Invoices and Line-items per invoice.
3. Please note that you will have to associate each invoice with existing account.
4. Simillary, you will need to associate each lineitem with existing invoice.
Deleteing either account or invoice will delete its associated objects.
5. The application claculate the following fields when changes are saved -
    a. Lineitem - Amount,
    b. Invoice - Sub Total,
    c. Invoice - Total,
    d. Invoice - Balance Due,

Prerequisites -

Built With -
    Python 2.7,
    Django,
    Django Rest Framework,
    SQLite3 DB,
    JWT Security,
    JSON API,
