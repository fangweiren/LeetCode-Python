题意:  
编写一个SQL查询获取Employee表中的第二高的薪水值。

解题思路:  
先找出最高的工资，就是括号里面的那条select语句，然后再从不等于最高工资的所有记录里找出最高的。不等于最高工资的所有记录里最高的工资就是第二高的工资啦。