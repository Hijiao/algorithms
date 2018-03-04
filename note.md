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