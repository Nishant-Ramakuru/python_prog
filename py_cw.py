"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here


#####################################
# Question 1a


def cadd(c1, c2):
    return(c1[0]+c2[0],c1[1]+c2[1])


def cmult(c1,c2):
    return ((c1[0]*c2[0])-(c1[1]*c2[1]),(c1[0]*c2[1]+c1[1]*c2[0]))
    
    


#####################################
# Question 1b

def tocomplex(x1,y1):
    return(x1+y1*1j)

def fromcomplex(c):
    return(c.real,c.imag)

# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions 
* seqandi and 
* seqxori 
that implement pointwise AND (https://en.wikipedia.org/wiki/Logical_conjunction) and XOR (https://en.wikipedia.org/wiki/Exclusive_or) of boolean sequences.
For instance
 seqandi([True,True,False],[True,False,True])
should compute
 [True, False, False]
and
 seqxori([True,True,False],[True,False,True])
should compute
 [False, True, True]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqandr and seqxorr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqandlc and seqxorlc.
"""

#####################################
# Question 2a


def seqandi(l1, l2):
    
    #error handling if the lengths arent the same
    if len(l1) != len(l2):
        print("Sequences have different lengths")

    else:
        l3=[]
        for i in  range(len(l1)): 
            if l1[i]==True and l2[i]==True:
                l3.append(True)
            else:
                l3.append(False)

        return l3
        




def seqxori(l1, l2):

     #error handling if the lengths arent the same
    if len(l1) != len(l2):
        print("Sequences have different lengths")

    else:
        l3=[]
        for i in  range(len(l1)): 
            if l1[i]==l2[i]:
                l3.append(False)
            else:
                l3.append(True)


        print(l3)



#####################################
# Question 2b


def seqandr(l1, l2):
    pass


def seqxorr(l1, l2):
    pass


#####################################
# Question 2c


def seqandlc(l1,l2):
    l3 = (x for x in l1 if l1[x]==True if l2[x]==True)
              

def seqxorlc(l1,l2):
    pass




# END ANSWER TO Question 2
################################################################################


###############################################################################
# Question 3


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
a. Mutable vs immutable types. Give at least two examples of each, with explanation.
b. Integer vs float types.
c. Assignment = vs equality == vs identity is.
d. The computational effects of a call to list on an element of range type, as in
 list(range(5*5*5)).
e. Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""

"""
a. MUTABLE types are the types that are changable. These are:
-Lists
-Sets
-Dictionaries
1)  If we have a list x=[1,2]  then we write y=x, assigning y to list x, and then we do x.append(3) when we print(y) we gonna get [1,2,3] as well as when we print(x) we gonna get the same value, that means we can change the value, so list is mutable 

2)  If we have a list a = [1,2,3,4] and we assign b = a  after  print(a is b) we are goiing to get a value True, because these two list have the same ID.

IMMUTABLE types - their value is not changable.
-Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
-Strings
-Tuples
-Frozen Sets

1)  If we have string x='dog' if we do y=x, and concatinate strin x with 's'  x += 's', after print(x) we going to  get 'dogs' and after print(y) we going to get 'dog'. String is immutable so it didn't change the value.

2)  If I have a tuple t =('a' , 'b' , 'c') if i try to change the second element t[1]='z' I will get an error 'tuple' object does not support item assignment


b. INTEGER is a number without a decimal point. Example x = 3
FLOAT  is a number with decimal point. Example x = 3.45. If we want to change a float to an integer, we can do so using the int() function. When we do this, the float will lose its decimal and the numbers behind the decimal place. Floating-point real numbers can't be represented with exact precision due to hardware limitations. 


c. Using assignment operator '=' we assing the value to the variable. Example x=2 ,  print(x) will result in printing '2'.

Using exuality operator '==' compares the value of two variables. 
Example
x=5
y=6
if x==y:
    print(True)
else: 
    print(False)

will result in printing False, as the values are not the same.

Using identity operator 'is' checks if the two variables are the same object in the memory. Two variables that are equal does not imply that they are identical.

d. This will result in an OverflowError as the number of elemnts in a list we initialized (2.9802322e+17) is too large. According to the source code, the maximum size of a list is PY_SSIZE_T_MAX/sizeof(PyObject*) . On a regular 32bit system, this is (4294967295 / 2) / 4 or 536870912. Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

e. Slice syntax allows you to return a portion of a characters.
Example 
x = "I love Python!"
print(x[3:6]) #its going to return "ove" starting from 3rd character to sixth (sixth is excluded)
print(x[2:]) # its going to print "ove Python!" starting from the 2nd character all the way to the end 

a = "Actually I hate Python!"
print(a[-7:-1]) #returns 1st charster from the end to 7th character counting from the back, results in printing "Python"

list(range(10**10)[10:10]) #cast to the list after slicing 
list(range(10**10))[10:10] #cast to the list before slicing
"""


# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4

"""
Recall that `map(f, l)` applies a function pointwise to a list, so that 
   map(f, [x, y, z]) 
computes 
   [f(x), f(y), f(z)]
Call a datum something that is either an integer, or a list of data (datums).
Write a generalised mapping function `supermap` that applyies `f` pointwise to any integers inside a datum. 

So for example:
* supermap(f, -5) should return 'f(-5)'
* supermap(f, []) should return '[]'
* supermap(f, [5, [5]) should return '[f(5), [f(5)]]'. 

You may find it useful to consider `isinstance` or the following code fragment
   type(5) == int 

An answer that guts the question (e.g. by calling a supermap-like function in a Python library) may score no marks.
"""


def supermap(dat):
    pass

# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""


def fenc(i):
    if i == 0:
        return [] 
    x = fenc(i - 1) 
    return [x, [x]] 


def fdec(l):
    if l == []: 
        return 0 
    current = l[0] 
    count = 1 
    while current != []: 
        count +=1 
        current = current[0]
    return count


# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
Implement a generator `love` such that if we assign
 x = love()
then repeated calls to
 next(x)
return the strings 
 I love you 
 You love that I love you
 I love that you love that I love you
 You love that I love that you love that I love you
 I love that you love that I love that you love that I love you
 ...
For full marks, your answer should respect correct capitalisation, as above.

Note that this question is not asking you to program an endless loop that prints these values; your answer should be a generator that yields these values.
"""


def love():
    cycles = ['I love you',
              'You love that I love you',
              'I love that you love that I love you',
              'You love that I love that you love that I love you',
              'I love that you love that I love that you love that I love you']
    
    current = 0 
    while True:
        yield cycles[current % 5] 
        current+=1



# END ANSWER TO Question 6
################################################################################


#################################################################################
# Question 7

"""
Consider functions that remove all instances of an integer `i` from a list of integers `l`, implemented in three distinct ways:

1. `removeall_oo` repeatedly applies the list .remove method until there are no instances of `i` left (you may use other programming constructs, such as counting the number of integers in `l`, or using exception raisers and handles).  
2. `removeall_ft` uses `import functools` and `filter`.  
3. `removeall_rd` uses `import functools` and `reduce` (but not filter). 

So for example, 
   removeall_oo(0, [0, 0, 1])
should return
   [1]
and
   removeall_oo(0, [0, 0])
should return
   []
"""

def removeall_oo(i,l):
    flag = True
    while flag:        
        try:
            l.remove(i)
        except:
            flag = False
            pass
    return l

def removeall_ft(i,l):
    return list(filter((i).__ne__, l))

def removeall_rd(i,l):
    #functools.reduce(lambda i, l: if i in l, l) 
    pass

# END ANSWER TO Question 7
################################################################################


##########################################################
# Question 8

"""
The Sudan function is documented here:
   https://en.wikipedia.org/wiki/Sudan_function
Implement the Sudan function as a Python function `sudan(n, x, y)` by orienting the equalities and making recursive calls as appropriate.

Be careful: even `sudan(2,2,2)` freezes up my machine.
"""

def sudan(n, x, y):
    if n==0:
        return x+y
    
    elif y==0:
        return x
    
    elif y!=0 and x!=0:
        return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)


# END ANSWER TO Question 8
################################################################################



###############################################################################
# Question 9 

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""


"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines factual and technical elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 


"""
Python is high-level, dynamically typed, object-oriented and interpreted language. Python has became popular for its simple sinax, being easy to learn and quick to write. Is a beginner fiendly language. Its cross-platform, that means you can run Python on Windows, MacOS and Linux. It has huge community which can help while debugging the code. Python boosts productivity, its simplicity allows developers to concentrate on solving problems rather than studying syntax of the language behavior.

They can get a whole lot done with very less code. This is probably one of the biggest advantages of Python. 
We can use Python has various type of applications like:
* Web development - popular liarbraries: Django and Flask are based on Python. Python's standard library supports many Internet protocols:
 - HTML and XML
 - JSON
 - E-mail processing.
* Machine Learning, which is a field of computer science that uses statistical techniques that gives computer programs the ability to learn from past experiences and improve how they perform specific tasks. Libraries called scikit-learn and TensorFlow were created for Python to build machine learning systems.
* Data Analytics - is a veryimportant field in todays' modern world, extracting relevant information can help companies to take calculated risks and increase profits. We study the data you have, perform operations and extract the information required. Libraries such as Pandas, NumPy are extreamly useful in extracting information.
* Audio or Video-based Applications 
* Automation- Python saves time on repetative tasks
* GUIs

Disadvatages:
* poor memory efficiency- Python needs a hgae amount of memory space, which can be problematic if we want to optimize the memory 
* slow at runtime - The line by line execution of code  leads to slow execution.Since its dinamically typed it is  responsible for the slow speed of Python because it has to do the extra work while executing code. 
* runtime errors: its design has numerous issues, that is why  Python programmers face several issues regarding it. This language requires more testing and also it has errors that only show up at runtime this is because the language is dynamically typed. 
* database access -though it is easy to program with Python, the database access layer is underdeveloped compared to other technologies like ODBC.
For enterprise apps, its imperative that there is an easy interaction of complicated legacy data, since it is not an ideal language for such apps. Python is a robust programming language with minimal stress and worries. But, this language is highly insecure and can be used only at ones own risk. 

Python has been out there since the 1990s. That implies more than just the fact that it has had lots of time to develop. Additionally, it now has a sizable and devoted community.
Therefore, there is a good chance that any problems you have when Python programming can be resolved with only one Google search. for the simple reason that someone else will have already run into your issue and written something useful about it.

The Python community of reputable and esteemed peers, who go above and beyond to support one another, is another factor contributing to the growth in the language's popularity. Python has consistently stayed up to date with the most recent trends, while many other programming languages have lost the capacity to support evolution and enable easier integration with the advances of their day. Python has unquestionably been successful in this regard, and as a result, it is one of the keys to the advancement of technology in the future.
It goes without saying that we are drawing closer to a period when real applications of automation and machine learning will be launched in the form of self-driving automobiles, social administration programs, medical diagnosis, and much more! There is little doubt that Python will be used to create this new world.

Python boasts of hundreds of different libraries that house more than 150,000 packages, making it powerful at eliminating repetitive tasks. As a result, repetitive operations can be eliminated or automated with greater operational efficiency by developers and programmers. Because of this, a recent survey found that more than 85% of participants choose Python for Deep Machine learning.
"""
# END ANSWER TO Question 9 
###############################################################################


###############################################################################
# Question 10

"""
a. Explain in words the difference between 
   ([],[],[]) 
and 
   [[]]*3.
b. Explain in words what x points to in memory after we execute the following two commands:
     x = []
     x.append(x)
"""


"""
a. ([],[],[]) #that is a tuple
[[]]*3 #this operation is gonna create a list

b.  x = []
     x.append(x) #It's a list that contains itself recursively.

"""

# END ANSWER TO Question 10 
###############################################################################

###############################################################################
# Question 11

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first.
[7:28 pm, 23/10/2022] +44 7827 133396: Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    tmp = []
    
    if n>0:
        
        while n!=0:
            
            tmp.append(n%10)
            
            n = (int)(n/10)
    
    return tmp


# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    n=0
    
    for i in range(len(I),0,-1):
        
        n = n*10 + I[i-1]

# add two infinite integers
# e.g. iadd([5], [5]) = [0,1]
def iadd(I,J):
    return I+J
# multiply two infinite integers
# e.g. imult([], [5]) = []
def imult(I,J):
    return I*J

# raise I to the power of J
def ipow(I,J):
    return I**J

# END ANSWER TO Question 11 
###############################################################################


###############################################################################
# Question 12

"""
Recall from Question 4 the notion of a datum.

a. Write a command `abstractsize` which inputs a datum and returns an integer measure of how much memory it occupies (cf. Question 10).
Note this measure should be in an abstract unit in which each integer occupies one unit of memory and each pair of square brackets occupies one unit of memory, modulo sharing, so that (for example) `[5,5]` has measure 3 --- one for the square brackets, and one for the two integer payloads.  (Do not try to return actual memory usage in bytes, since this will depend on implementation and on the size of the integer payload!) 
b. Write a command `compress` which inputs a datum, and outputs a datum that represents it and minimises abstract size.  Your code should be clear and well-commented with an explanation (if required) of the algorithm you use.

We're not looking for precise bytecounts and certainly not looking for speed or optimal performance.  Marks will be awarded for elegance, clear commenting, and understanding of the issues involved. 
"""

# END ANSWER TO Question 12 
###############################################################################

###############################################################################
# Question 13 (bonus question) 

"""
The code below to define `equals23` takes up five lines and 83 characters, by my count. 
It is also ugly, redundant, and indirect.
Rewrite it, so that it is clean, compact, direct --- and takes up one line and 23 characters.
"""

def equals23(x):
   
    return x==23
# END ANSWER TO Question 13 
###############################################################################