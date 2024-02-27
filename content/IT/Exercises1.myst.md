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


# Exercises: Memoryless Sources

## Exercise 1

Compute the entropy of the following distribution:

$$
\sV{S}{\frac{1}{2}}{0}{\frac{1}{8}}{\frac{1}{4}}{\frac{1}{8}}
$$

### Solution

The entropy of a DMS is given by:

$$
H(S) = - \sum_{i=1}^{n} p(s_i) \log_2 p(s_i)
$$

In this case, we have:

$$
\begin{aligned}
H(S) & = - \frac{1}{2} \log_2 \frac{1}{2} + 0 \log_2 0 + \frac{1}{8} \log_2 \frac{1}{8} + \frac{1}{4} \log_2 \frac{1}{4} + \frac{1}{8} \log_2 \frac{1}{8} \\
& = - \frac{1}{2} (-1) - 0 - \frac{1}{8} (-3) - \frac{1}{4} (-2) - \frac{1}{8} (-3) \\
& = \frac{1}{2} + \frac{3}{8} + \frac{1}{2} + \frac{3}{8} \\
& = 1.75 \, \text{bits}
\end{aligned}
$$

```{admonition} When probability is zero
Note the situation when a probability is 0, as we have here $p(s_2) = 0$. This is a special case, because simply applying the formula would result in a term $0 \log_2 0 = 0 \cdot \infty$, which is undefined.

The value of this term can be found as a limit, using l'Hôpital's rule:

$$
\begin{aligned}
\lim_{p \to 0} p \log_2 p &= \lim_{p \to 0} \frac{\log_2 p}{\frac{1}{p}} \\
&= \lim_{p \to 0} \frac{\frac{1}{p \ln 2}}{-\frac{1}{p^2}} \\
&= \lim_{p \to 0} \frac{-p}{\ln 2} \\
&= 0
\end{aligned}
$$

Thus, a probability of zero does not contribute at all to the entropy, and can
be safely ignored.
```

## Exercise 2

Consider the following game: I think of a number between 1 and 8 (each number
has equal chances), and you have to guess it by asking yes/no questions.

Answer the following questions:

- a). How much uncertainty does the problem have?
- b). How is the best way to ask questions? Why?
- c). What if the questions are not asked in the best way?
- d). On average, what is the number of questions required to find the number?

### Solution

a). The problem can be modeled as a DMS with 8 equiprobable messages:

$$
\sVIII{S}{\fIoVIII}{\fIoVIII}{\fIoVIII}{\fIoVIII}{\fIoVIII}{\fIoVIII}{\fIoVIII}{\fIoVIII}
$$

The uncertainty of the problem is given by the entropy of this source:

$$
H(S) = - \sum_{i=1}^{8} \frac{1}{8} \log_2 \frac{1}{8} = 3 \, \text{bits}
$$

b). The best way to ask questions is to ask questions that split the set of possible numbers in two sets of equal probability.
This is because every answer you obtain to a question behaves like a
binary source, and this provides maximum information when the probabilities are equal:

$$
\snII{S}{Yes}{\frac{1}{2}}{No}{\frac{1}{2}}
$$

Thus, the best way to ask questions is to maximize the entropy of the source at each step.

```{figure} img/Exercises1_Ex2.png
---
width: 70%
name: fig-ex2
---
Optimal decision tree for guessing a number between 1 and 8
```

## Exercise 3

What is the optimal decision tree for guessing a number chosen according to the following distribution:

$$
\sIV{S}{\fIoII}{\fIoIV}{\fIoVIII}{\fIoVIII}
$$

### Solution

The difference with the previous case is that the probabilities are not equal.
But we still use the same principle: we want to maximize the entropy at each step,
which means that we want to split the set of possible numbers in two sets of equal probability. This corresponds to the following optimal decision tree:

```{figure} img/Exercises1_Ex3.png
---
width: 50%
name: fig-ex3
---
Optimal decision tree for guessing a number between 1 and 4
```


## Exercise 4

What is the optimal decision tree for guessing a number chosen according to the following distribution:

$$
\sIV{S}{0.14}{0.29}{0.4}{0.17}
$$

### Solution

We still use the same principle as before.
However, we cannot split the set of probabilities into
equal amounts every time. Instead, we try to split them
into sums which are **as close to each other as possible**,
even though a perfect split is not always possible.

A good way to ask questions is shown below:

```{figure} img/Exercises1_Ex4.png
---
width: 50%
name: fig-ex3
---
Optimal decision tree for guessing a number between 1 and 4
```

## Exercise 5

A DMS has the following distribution

$$
\sV{S}{\frac{1}{2}}{0}{\frac{1}{8}}{\frac{1}{4}}{\frac{1}{8}}
$$

- a). Compute the information of message $s_1$, $s_2$ and $s_3$
- b). Compute the average information of a message of the source
- c). Compute the efficiency, absolute redundancy and relative redundancy of the source

### Solution

a). The information of a message is given $- \log_2 p(s_i)$, so we have:

$$
\begin{aligned}
i(s_1) & = - \log_2 \frac{1}{2} = 1 \, \text{bit} \\
i(s_2) & = - \log_2 0 = \infty \, \text{bits} \\
i(s_3) & = - \log_2 \frac{1}{8} = 3 \, \text{bits}
\end{aligned}
$$

b). The average information of a message is the entropy:

$$
H(S) = - \sum_{i=1}^{5} p(s_i) \log_2 p(s_i) = 1.75 \, \text{bits}
$$

c). For a DMS with 5 messages, the maximum entropy is $\log_2 5 = 2.32 \, \text{bits}$.

Therefore we have:

$$
\begin{aligned}
\eta &= \frac{H(S)}{H_{max}} = \frac{1.75}{2.32} = ... \\
R &= H_{max} - H(S) = 2.32 - 1.75 = 0.57 \text{bits} \\
\rho &= \frac{H_{max} - H(S)}{H_{max}} = \frac{0.57}{2.32} = ...
\end{aligned}
$$

## Exercise 6

Compute the KL distance between the following two probability distributions:

$$
P = [0 \;\;\; 0 \;\;\; 0 \;\;\; 1], \;\;\;\;\;\;\;\;\; Q = [0.1 \;\;\; 0.05 \;\;\; 0.05 \;\;\; 0.8]
$$

### Solution

Recall the definition of the KL distance:

$$
D_{KL}(P,Q) = \sum_{i=1}^{n} p_i \log_2 \frac{p_i}{q_i}
$$

In our case, we have:

$$
\begin{aligned}
D_{KL}(P,Q) & = 0 \log_2 \frac{0}{0.1} + 0 \log_2 \frac{0}{0.05} + 0 \log_2 \frac{0}{0.05} + 1 \log_2 \frac{1}{0.8} \\
& = 0 + 0 + 0 + 1 \cdot 0.3219 \\
& = 0.3219 \, \text{bits}
\end{aligned}
$$

Again, we have used the limit

$$\lim_{p \to 0} p \log_2 \frac{p}{q} = 0$$

for the terms where $p_i = 0$.
