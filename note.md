python
  + [] 方法：
    - [].append(object) -- append object to end
    - [].count(value) -> integer -- return number of occurrences of value
    - [].extend(iterable) -- extend list by appending elements from the iterable
    - [].index(value, [start, [stop]]) -> integer -- return first index of value.
    - [].insert(index, object) -- insert object before index
    - [].pop([index]) -> item -- remove and return item at index (default last)
    - [].remove(value) -- remove first occurrence of value.
    - [].reverse() -- reverse *IN PLACE*
    - [].sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
  + {} 方法
    - {}.has_key(k) -> True if D has a key k, else False
    - {}.items D.items() -> list of D's (key, value) pairs, as 2-tuples
    - {}.update([E, ]**F) -> None.  Update D from dict/iterable E and F.


  + 位运算
    - 按位与 & :两位同为 1 结果为1
    - 按位或 | :两位有一位为1 结果为 1
    - 异或 ^ : 两位不同则为 1

    注意：上述操作返回的是二进制后的数据，如果想看5('0b101')有几个'1' bin(5).count('1')

  + 计算机中数字存储方式
    - 原码：在数值前直接加符号位的表示法。
        + +2 0000 0010
        + -2 1000 0010
    - 反码：
        + +2  0000 0010 与原码一样
        + -2  1111 1101 符号位为1，数值部分按位取反。
    - 补码
        + +2 0000 0010 与原码一样
        + -2 1111 1110 原码符号位不变，数值部分按位取反再加1。即：反码+1
        
    + 在计算机系统中，数值都是以补码来表示和存储的， 先转换成补码，再按位运算。
    
     java 中 Interger.signum(int i)实现：return (i >> 31) | (-i >>> 31); faster than if - else conditionals. [more on stackoverflow](https://stackoverflow.com/questions/6628495/fint-x-return-x-0-0-1-in-java-without-conditionals) 
     （仅java中有无符号右移，即无论正负数，都用0补全）


    
        