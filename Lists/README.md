<h1>Lists <span>[]</span></h1>
Lists are ordered sequence of elements,in fact a list will be an object in the memory, we can can collect more information about an object in a single list

<h2>Important properties of lists</h2>
<ul>
<li>Lists are mutable,means we can change the elements of the list even after asigning to a the values.
assigning a value to an index changes the value of that index</li>
<li>Lists items are mostly homogenous, means the same kind</li>
</ul>

<h4>Slicing over a list will results to a list, and indexing over a list will results to an exact value(string,number,bool)</h4>

<h5>L[0:1]=>[]</h5>
<h5>L[0]=>value</h5>

<h2>aliasing</h2>
<p>when two variables points to the same object,we call it aliasing. it has the effect of if we change any of the element in the list, the whole list will be mutated for both variables.
in other words,both variables points to the same structure in the memory</p>

<h2>Not Equal</h2>
<p>if we have two different variables, each decalred with the same list. here the case is different, unlike aliasing, here we have two different structure, each with its own memeory location,hence changing one list will not have an affect on the other list</p>

<h2>Cloning</h2>
<p>cloning a list means copying a list without mutating the original list
<h4>syntaxt: newList = oldList[:]</h4></p>

<h2>Hihger Order Programming</h2>
<p>when we use functions with list, it gives more power to the programming, and it is known as higher order programming</p>
