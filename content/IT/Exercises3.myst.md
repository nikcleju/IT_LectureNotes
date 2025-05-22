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


# Error Control Coding

## Exercise 1

Consider the following error control code

     Message      Codeword
    ---------   -------------------
    $s_1$           $c_1$ = 00000
    $s_2$           $c_2$ = 10011
    $s_3$           $c_3$ = 11100
    $s_4$           $c_4$ = 00111


Requirements:

- a). compute the minimum Hamming distance and indicate
  how many errors it can detect and how many errors it can correct,
  with the nearest neighbor decoding algorithm;
- b). considering two received codewords, $\mathbf{r_1} = 11100$ and
  $\mathbf{r_2} = 00011$, perform decoding and say if there are errors,
   and if so then correct the errors (find the correct codeword and
   indicate where the errors are located);
- c). Give an example of errors the code cannot detect, and another
    example of errors it can detect but it cannot correct, using
    the nearest neighbor decoding algorithm.


### Solution

The Hamming distance between two codewords is the number of bit differences between them.
For example, the Hamming distance between $000$ and $110$ is $d_H = 2$, because
the first two bits are different.

The minimum Hamming distance of a code is is the smallest Hamming distance between any
pair of codewords.

Therefore, we have:

$$
d_H(c_1, c_2) = 3 (\textrm{ the first bit and the last two are different})
d_H(c_1, c_3) = 3
d_H(c_1, c_4) = 3
d_H(c_2, c_3) = 4
d_H(c_2, c_4) = 2
d_H(c_3, c_4) = 4
$$
The minimum Hamming distance is $d_H_{min} = 2$, between $c_2$ and $c_4$.


## Exercise 2

a). Design a block code consisting of 4 codewords, with minimum codeword length,
which is able to detect 3 errors in a codeword.

b). Design a block code consisting of 4 codewords, with minimum codeword length,
which is able to correct 2 errors in a codeword.





1. Consider a systematic code with generator matrix
$$[G] =
\begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 1 & 0 \\
0 & 1 & 0 & 0 & 1 & 1 & 1 \\
0 & 0 & 1 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 & 1 & 1 \\
\end{bmatrix}$$

    a. Compute the codeword for sending the information bits $\mathbf{i_2} = [1 0 1 1]$
    a. Compute the parity-check matrix $[H]$;
    c. We receive a sequence $\mathbf{r} = 1010111$, which was encoded with
        this code. Find if there are errors in the
        received data, and, if yes, perform correction and retrieve the
        transmitted information bits.
    b. Find out how many errors this code can detect, and how many it can correct.

2. Compute the codewords for transmitting the information words
 $\mathbf{i_1} = [1 0 0 1]$ with the Hamming (7,4) code, and $\mathbf{i_2} = [1 1 1 0]$
  with the Hamming (8,4) SECDED code.

3. We receive a sequence $\mathbf{r} = 1010111$, which was encoded with
the Hamming (7,4) code. Find if there are errors in the
received data, and, if yes, perform correction and retrieve the
transmitted information bits.

3. We receive a sequence $\mathbf{r} = 10101010$, which was encoded with
the Hamming (8,4) SECDED code. Find if there are errors in the
received data, and, if yes, perform correction and retrieve the
transmitted information bits.

4. Give an example of errors which the Hamming (15, 11) is not able to detect.
Give another example of errors which the Hamming (15, 11) is able to detect, but is not able to correct.





1. Find the non-systematic and then the systematic cyclic codeword for the sequence $\mathbf{i} = [1 0 1 0 0 0 1 1 0 0]$,
considering a cyclic code with generator polynomial $g(x) = 1\oplus x \oplus x^3$.
    a. Do it "the mathematical way" (with polynomials)
    b. Do it "the programming way" (XOR-ing bit sequences)

\

2. We receive a sequence $\mathbf{r} = 101011100101$, which was encoded with
a systematic cyclic code with generator polynomial $g(x) = 1\oplus x^2 \oplus x^3$.
Find if there are errors in the received data, and, if yes, perform correction and retrieve the
transmitted information bits.
    a. Do it "the mathematical way" (with polynomials)
    b. Do it "the programming way" (XOR-ing bit sequences)

\

3. We do cyclic coding on information words of length $k = 8$ bits.
We want the coding rate $R$ to be at most $0.6$. What degree must the generator polynomial $g(x)$ have?

