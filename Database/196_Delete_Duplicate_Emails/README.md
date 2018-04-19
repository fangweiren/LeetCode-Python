题意:  
编写SQL删除Person表中所有的重复email条目，只保留Id最小的唯一email记录。其中，Id是表的主键。

思路:  
按照邮箱群组起来，然后用Min关键字挑出较小的

DELETE FROM Person WHERE Id NOT IN
(SELECT Id FROM (SELECT MIN(Id) Id FROM Person GROUP BY Email) p);
