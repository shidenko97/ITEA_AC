# HW
1. Add to BaseInsight class methods:
    * to_dict, from_dict. {}
    * get, set, and del item for `metrics` attribute.
2. Copy your BaseInsight class from previous hw and use method types that best in each case (standard, static, class).
3. Create dict like class which can apply key only once (Develop two classes using `DefaultDict` and `dict`) 
and have 3 main dict methods (update, pop)..
4. Create list like class which can apply only integer values (Develop two classes using `DefaultList` and `list`) 
and have 3 main list methods (pop, append, extend).
5. Write a function that accepts two lists and returns a new iterable with each of the given items 
"interleaved" (item 0 from iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).
Here's an example (which returns lists):
`>>> interleave([1, 2, 3, 4], [5, 6, 7, 8])`
`[1, 5, 2, 6, 3, 7, 4, 8]`
6. Write a function that accepts two lists and returns a generator of squared each item from first list 
by each item from second list. 
"generator_interleaved".
`>>> generator_squared_interleave([1, 2, 3, 4], [5, 6, 7, 8])`
`[1^5, 2^6, 3^7, 4^8]`
