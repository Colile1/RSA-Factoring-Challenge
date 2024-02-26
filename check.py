#!/usr/bin/python3
from prime import Prime
"""
cleaning the data set by removing the word from the listing and convert the listing to an integer.
"""

def cleanning(word, listing):
	"""
	Function to clean the input word from the listing, then join the characters in the listing and convert the result to an integer. Returns the cleaned and converted listing.
	"""
	if word in listing:
		listing.remove(word)
	listing = ''.join(listing)
	listing = int(listing)
	return (listing)


""" Function for displaying the result from an analysis """


def result(i, k, y):
	print("{}={}*{}".format(y, k, i))


def obtain_prime_numbers():
    """
    Function to obtain prime numbers from a JSON file and return them.
    """
    with open('prime.json', 'r') as file:
        numbers = json.load(file)
	    prime = numbers['Prime']
	    file.close()
 	    return (prime)


def compute_prime_numbers(value):
	"""
	Compute prime numbers based on the given value.

	Parameters:
	- value: the number to compute prime numbers for

	Returns:
	- Tuple(int, int): a tuple containing the prime numbers
	"""
	prime = Prime()
	i = 2
	while True:
		w = value % i
		if w == 0:
			if i in prime:
				return (i, int(value / i))
		i += 1

def compute_non_prime_numbers(value):
	"""
	Compute non-prime numbers.

	Args:
	    value: The value for which non-prime numbers are computed.

	Returns:
	    Tuple: A tuple containing non-prime numbers.
	"""
	w = 2
	while (value % w != 0):
		w += 1
	return (w, int(value/w))
