题意:  
假设一个网站包含两个表， 顾客表Customers和订单表Orders。编写一个SQL查询找出所有从未下过订单的顾客。

解题思路:  
使用NOT IN，NOT EXISTS，或者LEFT JOIN均可。

SELECT Name AS Customers FROM Customers 
WHERE Id NOT IN (SELECT CustomerId FROM Orders);

SELECT Name AS Customers FROM Customers
LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL;

SELECT Name AS Customers FROM Customers c
WHERE NOT EXISTS (SELECT * FROM Orders o WHERE o.CustomerId = c.Id);

链接资料:http://blog.csdn.net/muxiaoshan/article/details/7617533
