This is a new spinoff of Python which I am calling KerbalSpace (KS). This
language is meant for the sole purpose of writing more efficient code
while still adopting the general form of Python. The only official compiler will
be written in Python itself, and it will compile KS code directly to Python.

Python 3 code can be inserted inside tags which resemble HTML, like so:
<python>
	print("Hello world!")
</python>

The same code in KS would appear:
	>"Hello world!"

Additionally, the compiler can be placed inside a KS program,
then compiled into Python and used to compile its own KS source.

Support for inserting other languages, such as JavaScript, may eventually come.
However, such support is not currently planned.