题意  
从Person表中找出重复出现的Email

思路  
按照Email分组，然后找出出现次数超过1的Email，即使用group by 和 having 实现。
