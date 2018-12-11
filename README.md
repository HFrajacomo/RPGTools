# RPGTools
## Classes

### Table
**Atributes**

 - __header__: List of elementes in the header of the table
 -  __content__: List of rows in table
 -  __associated_file__: File used to instantiate the table object

**Indexing**
	
Table[i] gets row element of index i. Slices are supported.

**Functions**

- __Table__([String] filename)
	filename: name of a table to be loaded.
- __len__(Table): returns the amount of lines.
- __str__(Table): returns a string containing column elements separated by tabs and lines separated by linefeeds. Header has two linefeeds.
- __col__([int] index): returns a list of elements in the column pointed by index. Header not included.
	index: index of column.
- __add_col__([list] column, [indexer] key=-1): adds a column to the position pointed by key.
	column: List of elements to be added. Column[0] is the header.
	key: position where the column will be inserted. Default: -1.
- __del_col__([indexer] key): deletes the column pointed by key from the table object.
	key: points to the column to be deleted.	
- __save_table__([String] file=""): Saves table object to a table file.
	 file: if a filename is specified, save to it. If no filename is specified, use *self.associated_file*.
- __print__([bool] ret=False): calls __str__().
	ret: if ret is False, prints to stdout. Else, return as a string.

**Outside functions**

- __read_table__([String] file): Instantiates a Table object.
	file: name of the table file.
- __scalarsum__([numeric] num, [list] lista): sums all elements in lista by num. Returns the resulting list.
	num: Any number.
	lista: Any list containing only numbers. Convertion to int is done if any element of lista is a string.
- __scalarmult__([numeric] num, [list] lista): multiplies all elements in lista by num. Returns the resulting list.
	num: Any number.
	lista: Any list containing only numbers. Convertion to int is done if any element of lista is a string.
- __bitwisesum__([list] lista1, [list] lista2): returns a list resulting the sum of elements of lista1 and lista2 elementwise. Lists must have the same size.
	lista1, lista2: Any list containing only numbers. Convertion to int is done if any element of lista is a string.
- __bitwisemult__([list] lista1, [list] lista2): returns a list resulting the multiplication of elements of lista1 and lista2 elementwise. Lists must have the same size.
	lista1, lista2: Any list containing only numbers. Convertion to int is done if any element of lista is a string.
- __toint__([list] lista): Converts all elements of a list to int.
- __tostr__([list] lista): Converts all elements of a list to string.
