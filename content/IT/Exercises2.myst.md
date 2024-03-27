---
file_format: mystnb
jupytext:
  formats: ipynb,md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
# kernelspec:
#  display_name: 'Python 3.8.5 64-bit (''base'': conda)'
#  name: python3
---


# Source Coding

## Exercise 1 DMS entropy

Consider the binary codes below:

  Message  |   Code A		|   Code B	 |	 Code C	  |   Code D	 |   Code E	  |   Code F
---------: | :--------: | :--------: | :--------: | :--------: | :--------: | :--------:
  $s_1$    |   $00$		  |	  $0$			 |   $0$		  |   $0$		   |   $0$		  |   $0$
  $s_2$    |   $01$		  |	  $10$		 |   $01$		  |   $100$		 |   $110$		|   $10$
  $s_3$    |   $10$	    |		$110$		 |   $011$		|   $11$		 |   $10$		  |   $11$
  $s_4$    |   $11$		  |	  $1110$	 |	 $0111$	  |   $110$		 |   $111$		|   $110$

For each code:

- a). Verify the Kraft inequality
- b). Determine if the code is instantaneous / uniquely decodable
- c). Draw the graph

### Solution

Let's analyze a) and b) for each code.

The Kraft inequality is:

$$\sum_{i=1}^{n} 2^{-l_i} \leq 1$$

where $l_i$ is the length of the $i$-th codeword.

**Code A**. For the first codeword, all 4 codewords have length 2, so the sum is:

$$2^{-2} + 2^{-2} + 2^{-2} + 2^{-2} = 4 \cdot 2^{-2} = 1 (OK)$$

The code is instaneaneous because no codeword is a prefix of another codeword.
This means it is also uniquely decodable.

**Code B**. For the second codeword the lengths are 1, 2, 3, 4, so the sum is:

$$2^{-1} + 2^{-2} + 2^{-3} + 2^{-4} = 1/2 + 1/4 + 1/8 + 1/16 = 15/16 < 1 (OK)$$

The code is instaneaneous, so it is uniquely decodable.

**Code C**. For the third codeword the lengths are also 1, 2, 3, 4 so the sum is the same as before.

The code is not instantaneous because the codeword for $s_1$ is a prefix of all the other codewods.
However, the code is uniquely decodable, because of the following argument: each 0
marks the begining of a codeword, so given any binary sequence there will be no
problem splitting it into codewords, because we just have to look for the 0s.

**Code D**. For the fourth codeword the lengths are 1, 3, 2, 3, so the sum is:

$$2^{-1} + 2^{-3} + 2^{-2} + 2^{-3} = 1/2 + 1/8 + 1/4 + 1/8 = 1 (OK)$$

The code is not instantaneous because the codeword for $s_3$ is a prefix of the codeword for $s_4$.
It is also not uniquely decodable, because of the following argument:
given the sequence 110, we can't
tell if it is $s_4$ or $s_3 s_1$.

**Code E**. For the fifth codeword the lengths are also 1, 3, 2, 3, so the sum is the same as before.

The code is instantaneous, so it is uniquely decodable.

**Code F**. For the sixth codeword the lengths are 1, 2, 2, 2, so the sum is:

$$2^{-1} + 2^{-2} + 2^{-2} + 2^{-2} = 1/2 + 1/4 + 1/4 + 1/4 > 1 (BAD)$$

The code is not instantaneous nor uniquely decodable, because
no code with these four lenghts can ever be, since the Kraft inequality is violated.

TODO: graphs

## Exercise 2

Consider a memoryless source with the following distribution:
$$\sIV{S}{\frac{1}{2}}{\frac{1}{4}}{\frac{1}{8}}{\frac{1}{8}}$$
	For this source we use two separate codes:

	  Message      Code A	   Code B
	-----------  ----------  ----------
	  $s_1$        $00$			$0$
	  $s_2$        $01$			$10$
	  $s_3$        $10$			$110$
	  $s_4$        $11$			$111$

	Requirements:
	a. Compute the average lengths of the two codes
	b. Compute the efficienty and redundancy of the two codes
	c. Encode the sequence $s_2s_4s_3s_3s_1$ with each code
	d. Decode the sequence `0110101010101111000010101` with each code

### Solution


## Exercise 3

Fill in the missing bits (marked with ?) such that the resulting code is instantaneous.

	  Message       Codeword
	----------- -------------------
		$s_1$       ??
		$s_2$       1??
		$s_3$       11?
		$s_4$       0?
		$s_5$       ??

	(just replace the '?'; do not add additional bits)

### Solution


## Exercise 4

We perform Shannon coding on an information source with $H(S) = 20$b.
    a. What are the possible values for the efficiency of the code?
    b. What are the possible values for the redundancy of the code?
    c. What is the minimum number of messages the source may possibly have?


### Solution


## Exercise 5

A discrete memoryless source has the following distribution:

    $$\sV{S}{0.05}{0.4}{0.1}{0.25}{0.2}$$

    a. Encode the source with Shannon, Shannon-Fano coding and Huffman
    coding and compute the average length in every case.
    b. Find the efficiency and redundancy of the Huffman code
    c. Compute the probabilities of the symbols $0$ and $1$, for the Huffman code

### Solution



## Exercise 6

For the following source, perform Huffman coding and obtain three
different codes with same average length, but different individual codeword length.

    $$\sVI{S}{0.05}{0.05}{0.15}{0.25}{0.25}{0.25}$$

    a. Compute the average length in all three cases and show it is the same

### Solution


## Exercise 7

A discrete memoryless source has the following distribution:

    $$\sIII{S}{0.1}{0.7}{0.2}$$

    a. Find the average code length obtained with Huffman coding on the
    original source and on its second order extension.

    b. Encode the sequence $s_7 s_7 s_3 s_7 s_7 s_7 s_1 s_3 s_7 s_7$
    with both codes.


### Solution


## Exercise 8

A discrete memoryless source has the following distribution

	$$\sVIII{S}{0.4}{0.3}{0.2}{0.04}{0.03}{0.02}{0.009}{0.001}$$

	Find the Huffman code for a code with 4 symbols,
	$x_1$, $x_2$, $x_3$ and $x_4$, and encode the sequence

	$$s_1 s_7 s_8 s_3 s_3 s_1$$
