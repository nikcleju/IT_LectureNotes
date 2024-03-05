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
#kernelspec:
#  display_name: 'Python 3.8.5 64-bit (''base'': conda)'
#  name: python3
---

```{math}
\newcommand{\snII}[5]{#1: \left( \begin{matrix} {#2} & {#4} \\ #3 & #5 \end{matrix} \right)}
\newcommand{\snIII}[7]{#1: \left( \begin{matrix} {#2} & {#4} & {#6} \\ #3 & #5 & #7 \end{matrix} \right)}
\newcommand{\snIV}[9]{#1:  \left( \begin{matrix} {#2} & {#4} & {#6} & {#8} \\ #3 & #5 & #7 & #9 \end{matrix} \right)}

\newcommand{\sII}[3] {#1: \left( \begin{matrix} s_1 & s_2 \\ #2 & #3 \end{matrix} \right)}
\newcommand{\sIII}[4] {#1: \left( \begin{matrix} s_1 & s_2 & s_3 \\ #2 & #3 & #4 \end{matrix} \right)}
\newcommand{\sIV}[5] {#1: \left( \begin{matrix} s_1 & s_2 & s_3 & s_4 \\ #2 & #3 & #4  & #5 \end{matrix} \right)}
\newcommand{\sVI}[7] {#1: \left( \begin{matrix} s_1 & s_2 & s_3 & s_4 & s_5 & s_6 \\ #2 & #3 & #4 & #5 & #6 & #7\end{matrix} \right)}
\newcommand{\sVIII}[9] {#1: \left( \begin{matrix} s_1 & s_2 & s_3 & s_4 & s_5 & s_6 & s_7 & s_8\\ #2 & #3 & #4 & #5 & #6 & #7 & #8 & #9 \end{matrix} \right)}
\newcommand{\fIoII}{\frac{1}{2}}
\newcommand{\fIoIII}{\frac{1}{3}}
\newcommand{\fIoIV}{\frac{1}{4}}
\newcommand{\fIoV}{\frac{1}{5}}
\newcommand{\fIoVI}{\frac{1}{6}}
\newcommand{\fIoVII}{\frac{1}{7}}
\newcommand{\fIoVIII}{\frac{1}{8}}
```

# Source Coding

In this chapter we take a look at the basic principles
and algorithms for data compression.

## The role of coding

In the general block diagram of a communication system,
the coding block is situated
between the information source and the communication channel.

![Communication system](img/CommBlockDiagram.png){width=35%}

It's role is to prepare the raw information in order to be transmitted
over the channel. It has two main jobs:

1. **Source coding**:
   - Convert source messages to channel symbols, i.e. the actual
     symbols which the channel knows to transmit.

     For example, express the messages in binary form (zeros and ones), for sending over a binary channel.

   - Minimize the number of symbols needed to be transmitted (i.e., data compression).
     We don't want to transmit more symbols than necessary to recover the messages at the receiving end.

   - Adapt probabilities of symbols in order to maximize to maximize mutual information.
   We will discuss this more in Chapter IV.

2. **Error control coding**
    - Protect the information against channel errors
    - Also known as "*channel coding*"

Basically, source coding refers to all the procedures required to express
the source messages as channel symbols in the most efficient way possible,
while error control coding refers to all the algorithms used to
protect the data against errors.

The coding block has a corresponding decoding block on the receiving end.
Its job is to "*undo*" all the coding operations:

- detect and fix the errors in the received data, based on the algorithms introduced by the coding block
- convert the channel symbols back into the message representations that the receiver expects

Is it possible to do these two jobs separately, one after another,
in two consecutive operations? Yes, as the **source-channel separation theorem** establishes.

We give below only an informal statement of the theorem:

```{prf:theorem} Source-channel separation theorem
It is possible to obtain the best reliable communication by performing the
two tasks **separately**:

1. Source coding: to minimize number of symbols needed
2. Error control coding (channel coding): to provide protection against errors happening on the channel
```

In this chapter, we consider only the source coding algorithms, without any error control.
Basically, we assume that data transmission is done over an ideal channel with no noise,
and therefore the transmitted symbols are perfectly recovered at the receiver.

In this context, our main concern is how to minimize the number of symbols needed to represent the messages, while making sure that the receiver can decode the messages correctly.
The advantages of data compression are self-evident:

- Efficiency
- Short communication times
- Can decode easily


## What is a code

Let's define what coding means from a mathematical perspective.

Consider an input information source with the set of messages:

$$S = \left\lbrace s_1, s_2, ... s_N \right\rbrace$$

and suppose we would like to express the messages as a sequence of the following **code symbols**:

$$X = \left\lbrace x_1, x_2, ... x_M \right\rbrace$$

The set $X$ is known as the **alphabet of the code**.

For example, for a binary code we have $X = \lbrace 0, 1\rbrace$
and a possible sequence of symbols is $c = 00101101$

```{prf:definition} Code definition
A **code** is a mapping from the set $S$ of $N$ messages
to a set of $N$ sequences of symbols, known as **codewords**:

$$C = \left\lbrace c_1, c_2, ... c_N \right\rbrace$$

An example code mapping is given below:

 Message   |               | Codeword
---------: | :----------:  | :----------
$s_1$      | $\rightarrow$ | $c_1 = x_1x_2x_1...$
$s_2$      | $\rightarrow$ | $c_2 = x_1x_2x_2...$
$\dots$    | $\rightarrow$ | $\dots$
$s_N$      | $\rightarrow$ | $c_N = x_2x_2x_2...$

```

The codewords are the sequences of symbols used by the code.

The **codeword length**, which we denote as $l_i$,
is the the number of symbols in a given codeword $c_i$.


**Encoding** a given message or sequences of messages means
replacing each message with its codeword.

**Decoding** means deducing back the original sequence of messages,
given a sequence of symbols.

As an example, the ASCII code is a widely-used code for encoding characters,
consisting of 256 codewords (stored on 1 byte):

<!-- ![ASCII code (partial)](img/ASCIIcode.png){width=50%} -->
![ASCII code (partial)](img/ASCIIcode.png)

Nowadays, ASCII is usually replaced by Unicode (UTF-8), which is a more general code using 65536 codewords (stored on 2 bytes), allowing for many more letters used in languages around the globe.

### The graph of a code

The codewords of a code can represented as a binary tree.
We call this representation **the graph of the code**.

TODO: Example at blackboard

### Average code length

There are many ways to define the codewords for messages,
but some are better than others.

The most basic quantity indicating efficiency of a code is the average code length.

```{prf:definition} Average code length
Given a code, the **average code length** is the average of the codeword lengths:

$$\overline{l} = \sum_i p(s_i) l_i$$
```

For every codeword $c_i$, we multiply the probability of the corresponding message $p(s_i)$ with its length $l_i$.

A code with smaller average length is better,
because it represents sequences of messages
with less symbols, on average.
However, there is a certain lower limit
to how small the average length can be (for example, it cannot be 0, for self-evident reasons).

This raises the following interesting question:

> Given a source $S$, how small can the average length be?

This is a fundamental question, to which we will provide an answer later in this chapter.

### Instantaneous codes

We introduce another set of useful definitions regarding the codeword structure.

A code can be:

- **non-singular**: all codewords are different
- **uniquely decodable**: no two sequences of messages translate
  to the same sequence of symbols
  - i.e. there is never a confusion at decoding: there can be only one
  sequence of messages corresponding to a given sequence of symbols

- **instantaneous** (also known as **prefix-free**): no codeword is prefix to another code
  - A **prefix** = a codeword which is the beginning of another codeword

Examples: at the blackboard

The follwing relations exist between these types of codes.

```{prf:theorem} Instantaneous codes are uniquely decodable
An instantaneous code is uniquely decodable
```

```{prf:proof}

There is exactly one codeword matching the beginning of the sequence:

- Suppose the true initial codeword is **c**
- There can't be a shorter codeword **c'**, since it would be prefix to **c**
- There can't be a longer codeword **c''**, since **c** would be prefix to it

Once we find the first codeword, write down the corresponding message and remove the codeword from the sequence.

The remaining part is another sequence and, by the same argument, there is exactly one codeword matching the new beginning, and so on.
```

```{note}
The converse is not necessary true; there exist uniquely decodable codes which
are not instantaneous.
```

```{prf:theorem} Uniquely decodable codes are non-singular
An uniquely decodable code is non-singular
```

```{prf:proof}
The proof is by contradiction:

- If the code is singular, some codewords are not unique (different messages have the same codeword)
- This means that at decoding we can't decide which of those messages is there.
  This means that the code is not uniquely decodable
- Therefore, if the code is uniquely-decodable, it must also be non-singular ($A \rightarrow B \Leftrightarrow \overline{B} \rightarrow \overline{A}$)
```

We can summarize the relation between these three code types as follows:

Instantaneous $\subset$ uniquely decodable $\subset$ non-singular


#### Graph-based decoding of instantaneous codes

Using the graph of the code, we can use a very simple procedure for decoding any instantaneous code:

```{prf:algorithm} Graph-based decoding of instantaneous codes
:label: graph-based-decoding

**Inputs** An input symbol sequence, the graph of an instantaneous code

**Output** The decoded message sequence

1. Start at the root of the tree graph
2. Follow the edges in the tree according to the next symbols in the sequence
3. When a message is reached in the tree, write it down and go back to the root
4. Continue until the end of the symbol sequence
```

TODO: TBD: Illustrate at whiteboard

This procedure shows the advantage of instantaneous codes over other codes which
might be uniquely decodable, but are not instantaneous.
Instantaneous codes allow for **simple decoding**.
There is never any doubt about the next message in the sequence.

This decoding scheme is also showing why these codes are named "*instantaneous*":
a codeword can be decoded as soon as it is fully received, immediately, without any delay, because the decoding takes place on-the-fly while the bits are
received one-by-one.

As a counter example, consider the following uniquely decodable, but non-instantaneous code: $\left\lbrace 0, 01, 011, 1110 \right\rbrace$. When you read the first $0$, you cannot decode it yet, because you need to wait the next bits to understand how to segment the sequence. This implies that the decoding has some delay.

### The Kraft inequality theorem

When can an instantaneous code exist? Given a DMS $S$, are we sure we can find an
instantaneous code for it, and if yes, under which conditions?

The answers to these questions is provided by the Kraft inequality.

```{prf:theorem} Kraft inequality theorem
Given a code alphabet of $D$ symbols, there exists an instantaneous code with codeword lengths ${l_1, l_2, \ldots l_n}$
if and only if the lengths satisfy the following inequality:

$$\sum_i D^{-l_i} \leq 1$$
```

```{prf:proof}
TODO: At blackboard
```

Comments on the Kraft inequality:

- If lengths do not satisfy the relation, no instantaneous code exists with these lengths
- If the lengths of a code satisfy the relation, that code can be instantaneous or not (there   exists an instantaneous code, but not necessarily that one).
  Keep in mind that the Kraft inequality only looks at the lengths of the codewords, not
  at their actual symbols, so it can only say something about the lengths, not about the actual codewords
- The Kraft inequality implies that the codewords lengths cannot be all very small, because if
  all $l_i$ values are too small the sum exceeds 1. Thus, implicitly, it sets a lower limit to the permissible lengths.

- From the proof, it follows that we have equality in the relation

  $$ \sum_i D^{-l_i} = 1$$

  only if the lowest level of the tree is fully covered.
  Thus, for an instantaneous code which satisfies Kraft with equality,
  all the graph branches terminate with codewords and there are no unused branches.

  This makes sense intuitively, since is most economical way: codewords are as short as they can be. Any unused branch means that we can actually make the code shorter by moving some message up the tree.

We have seen that instantaneous codes must obey the Kraft inequality
But how about uniquely decodable codes?
The answer is given by the next theorem.

```{prf:theorem} McMillan theorem
Any uniquely decodable code **also** satisfies the Kraft inequality:

$$ \sum_i D^{-l_i} \leq 1.$$
```

```{prf:proof}
No proof given
```

Consequences of the McMillan theorem:

- For every uniquely decodable code, there exists in instantaneous code
with the same lengths. This is because the lengths $l_i$ must satisfy the same
relation both for unique-decodable and for instantanous codes.

- Thus, even though the class of uniquely decodable codes is larger than that of
instantaneous codes (because any instantaneous code is uniquely decodable, but not
any uniquely decodable code is instantaneous), using uniquely-decodable codes
brings **no additional benefit** in average codeword length

- Instead of an uniquely decodable code, we can always use an instantaneous code,
which has the same lengths, but is much easier to decode.

#### Finding an instantaneous code for given lengths

How to find codewords with code lengths $\{l_i\}$?

In general, we may use the following procedure:

```{prf:algorithm}
1. Check that lengths satisfy Kraft relation
2. Draw graph with the specified lengths
3. Assign codewords to the graph terminations
```

Note that this procedure only gives us the codewords, not the mapping
to a particular set of messages.

In practice, there might be more elaborate ways to find the codewords and map them
to the messages of the source, with additional benefits.

### Minimum average length

We will discuss now one of the most important aspect of this chapter,

Given a DMS $S$, suppose we want to find an instantenous code for it,
but in such a way as to **minimize the average length** of the code:

$$\overline{l} = \sum_i p(s_i) l_i$$

How can we find such an optimal code?

Given that it should be instantaneous, the codeword lengths must obey the Kraft inequality.

In mathenatical terms, we formulate the problem as a **constrained optimization problem**:

$$\begin{aligned} \textbf{minimize } &\sum_i p(s_i) l_i \\
\textrm{subject to } &\sum_i D^{-l_i} \leq 1
\end{aligned}$$

This means that we want to find the unknowns $l_i$
in order to minimize a certain quantity ($\sum_i p(s_i) l_i$),
but the unknowns must satisfy a certain constraint ($\sum_i D^{-l_i} \leq 1$).

#### The method of Lagrange multipliers

To solve this problem, we use a standard mathematical tool known as the **method of Lagrange multipliers**.

```{prf:definition} Lagrange multipliers for constrained optimization problems

To solve the following constrained optimization problem:

$$\begin{aligned} \textbf{minimize } & f(x) \\
\textrm{subject to } & g(x) = 0
\end{aligned}$$

one must build a new function $L(x, \lambda)$ (known as the **Lagrangean function**):

$$L(x, \lambda) = f(x) - \lambda g(x)$$

The solution $x$ of the original problem is among the solutions of the system:

$$
\begin{cases} \frac{\partial L(x, \lambda)}{\partial x} &= 0 \\
\frac{\partial L(x, \lambda)}{\partial \lambda} &= 0
\end{cases}
$$

If there are multiple variables $x_i$ in the problem, we take the partial derivative
$\frac{\partial L(x, \lambda)}{\partial x_i}$ for each one of them, resulting in a larger system.
```

Let's use this mathematical formulation to our problem.
In our case, the functions and the variables involved are the following:

- The unknowns $x_i$ are the lengths $l_i$
- The function to minimize is $f(x) = f(l_i) = \overline{l} = \sum_i p(s_i) l_i$
- The constraint is $g(x) = g(l_i) = \sum_i D^{-l_i} - 1$

```{note}
The method of Lagrange multipliers, as presented below, specifies an equality constraint:

$$
\textrm{subject to } g(x) = 0
$$

But in our optimization problem, we have an inequality constraint ($\leq$ instead of $=$):

$$
\textrm{subject to } \sum_i D^{-l_i} \leq 1
$$

However, as we discussed earlier, having the Kraft inequality smaller than $1$ means that we have
some coding inefficiency, since some branches of the graph code remaining unconnected.
When we seek to minimize the average length, this cannot happen. For this reason,
we can safely use equality here in the Kraft constraint:

$$
\textrm{subject to } \sum_i D^{-l_i} = 1
$$
```

```{note}
A keen reader might observe a requirement which our optimization problem does not
take into account: the variables $l_i$ cannot just take any value, they must be positive integers,
since they are the length of some codewords.

We will discuss this problem in the next paragraphs.
```

**TBD: Solve at blackboard**

The resulting optimal codeword lengths are:

$$
l_i = -\log(p(s_i))
$$

```{prf:theorem}
The optimal codeword lenghts $l_i$ for the messages of a DMS in order to minimize the average codeword length $\overline{l}$ are:

$$l_i = -\log(p(s_i))$$

```

Let us discuss some intuitions and consequences related to this result:

- Using $l_i = -\log(p(s_i))$ satisfies Kraft with equality, so the lengths cannot be any shorter than that, in general:

  $$
  \textrm{subject to } \sum_i D^{-(-\log(p(s_i))))} = 1
  $$


- A message with higher probability must have a shorter codeword, while a message with lower probability has a longer codeword.
  This makes sense because messages we can afford to use a longer codeword for messages which appear rarely in a sequence.

```{admonition} Example
Think of examples in languages. Words which are very common are usually short: "yes", "no", "and", "the" "with". We often use abbreviations to replace longer words which we must use often.
```


#### Entropy is the limit

The most important consequence of this result gives us a functional
definition of the entropy, i.e. it tells us what the entropy really
says about an information source.

If the optimal values are $l_i = -\log(p(s_i))$, then the minimal average length is:

$$\min \overline{l} = \sum_i p(s_i) l_i = -\sum_i p(s_i) \log(p(s_i)) = H(S)$$

```{prf:corollary}
The entropy of a discrete memoryless information source is the **minimum average length** that can ever be achieved by a instantaneous or uniquely-decodable code used to encode the messages.
```

This result tells us what the entropy really means, besides the formulaic definition provided in chapter I. The entropy gives us the minimum number of bits required to represent the data generated by an information source in binary form. Although we rigorously proved this result only for a discrete memoryless source, it holds for sources with memory as well.

```{margin}
Question:

Can you sketch the proof for this for sources with memory?
```

Immediate consequences:

- Messages from a source with small entropy can be written (encoded) with few bits
- A source with with large entropy requires more bits for encoding the messages

Reformulating this in a different way, we can say that he average length of an uniquely decodable code must be at least as large as the source entropy. One can never represent messages, on average, with a code  having average length less than the entropy.

$$H(S) \leq \overline{l}$$

```{prf:example}
You can think of the relation between information (entropy) and code length
using the analogy of water and a bottle.

We use a bottle to carry and store some quantity of water,
but the bottle capacity must be larger or equal than the quantity of water.

We use a code to carry and store information, and the
code average length must be larger or equal than the quantity of information.

Information is not the codewords, information is a mathematical quantity implied by the random occurrence of messages. The codewords are just means of transportation of information, like a bottle.
```

#### Efficiency and redundancy of a code

Considering a code for an information source, comparing the average code length
with the entropy indicates the efficiency of the encoding. These quantities indicate how close is the average length to the optimal value.

```{prf:definition} Efficiency and redundancy of a code
**Efficiency** of a code is defined as:

$$\eta = \frac{H(S)}{\overline{l} \cdot \log(M)}$$

where $M$ is size of code alphabet (number of symbols in the code).

The **redundancy** of a code is:

$$\rho = 1- \eta$$

For binary codes $M = 2$ so $\eta$ is simply the ratio $\eta = \frac{H(S)}{\overline{l}}$.

For $M > 2$, the factor of $\log_2(M)$ is needed because we need to express both quantities with the same unit. The entropy $H(S)$ in bits (due to the binary logarithm), but $\overline{l}$ is not in bits if there are $M > 2$ symbols, hence the need for $\log(M)$.
```


#### Coding with the wrong code

An interesting question arises in practice.
Consider a source with probabilities $q(s_i)$. We design a code for this source, but we use it to encode messages from a different source, with probabilities $p(s_i)$.

This happens in practice when we estimate the probabilities from a sample
data file, and then we use the code for general of similar files.
Those files might not have exactly the same frequencies of messages
as the sample file used to design the code.

How does this affect us? We lose some efficiency, because
the codeword lengths $\overline{l_i} \approx -\log_2(q_i) $ are not optimal for the source with probabilities $p_i$, which
leads to increased average length.

If the codewords were optimal, the codeword lengths would have been
$\approx -log_2(p_i)$, leading to an average length equal
to the entropy $H(S)$:
$$\overline{l_{optimal}} = -\sum{p(s_i) \log{p(s_i)}}$$

But the actual average length we obtain is:
$$\overline{l_{actual}} = \sum{p(s_i) l_i} = -\sum{p(s_i) \log{q(s_i)}}$$

The difference between average lengths is what we lose due to the mismatch:

$$\overline{l_{actual}} - \overline{l_{optimal}} = \sum_i{p(s_i) \log(\frac{p(s_i)}{q(s_i)})} = D_{KL}(p || q)$$

The difference is exactly **the Kullback-Leibler distance** between the two distributions $p$ and $q$.

Therefore we have a functional definition of the KL distance:
the KL distance between two distributions $p$ and $q$
is the number of extra bits spent
when we encode messages from $p$ using a code
optimized for a different distribution $q$.

Due to the KL distance properties, the distance is always $\geq 0$,
which shows that such a mismatch always increases the average length.
The more different the two distributions are, the larger the increase
in average length becomes.

```{prf:example}
TODO
```

#### Optimal and non-optimal codes

A code for which $\eta = 1$ is known as an **optimal code**.
Such a code attains the minimum average length:

$$\overline{l} = H(S)$$

However, this is only possible if the probabilities are powers of 2,
such that $l_i = -log2(p(s_i))$ is an integer number, because the codeword
lengths must always be natural numbers.

- e.g. probabilities like $1/2$, $1/4$, $1/2^n$, known as *dyadic distribution*
- the lengths $l_i = -\log(p(s_i))$ are all natural numbers

An optimal code can always be found for a source where all $p(s_i)$ are powers of 2, using for example the graph-based procedure explained earlier.

However, in the general case  $l_i = -\log(p(s_i))$ might not be an integer number. This happens when $p(s_i)$ is not a power of 2. What to do in this case?

A simple solution to this problem is to round every logarithm to next largest natural number:

$$l_i = \lceil -\log(p(s_i)) \rceil$$

for example:

$$-\log(p(s_i)) = 2.15 => l_i = 3$$

This leads to the Shannon coding algorithm described below.

### Shannon coding

The Shannon coding procedure is a simple algorithm for finding an instantaneous code for a DMS.

```{prf:algorithm} Shannon coding algorithm
**Inputs** A DMS source with probabilities $p(s_i)$

**Outputs** Codewords $l_i$

1. Arrange probabilities in descending order
2. Compute the codeword lengths $l_i = \lceil -\log(p(s_i)) \rceil$
3. For every message $s_i$ find the codeword as follows:

    1. sum all the probabilities up to this message (not including current)
    2. multiply the sum value with $2^{l_i}$
    3. floor the result, convert to binary, retain first $l_i$ bits

```

The code obtained with this procedure is known as a **Shannon code**.

Shannon coding is one of the simplest algorithms, and some other better schemes are available. However, this simplicity allows to prove fundamental results
in coding theory, as we shall see below.

```{annotation} Bad example
As an example of Shannon coding deficiency, compute the Shannon algorithm for the following source:

$$S: (0.9, 0.1)$$
```

One such fundamental result shows that the average length of a Shannon code is actually close to the entropy of the source.

```{prf:theorem}
The average length $\overline{l}$ of a Shannon code satisfies:

$$H(S) \leq \overline{l} < H(S) + 1$$
```

```{prf:proof}
The first inequality, $H(S) \leq \overline{l}$, is because $H(S)$ is
the minimum average length.


To prove the second inequality, consider the lenghts $l_i$ obtained with the
Shannon algorithm:

$$l_i = \lceil -\log(p(s_i)) \rceil = -\log(p(s_i)) + \epsilon_i$$

where the values are rounded upwards with a quantity $\epsilon_i$
which is smaller than 1, $0 \leq \epsilon_i < 1$.

Computing the average length, we have:

$$\begin{aligned}
\overline{l} &= \sum_i p(s_i) l_i \\
&= \sum_i p(s_i) (-\log(p(s_i)) + \epsilon_i) \\
&= H(S) + \underbrace{\sum_i p(s_i) \epsilon_i}_{< 1} \\
&\leq H(S) + \sum_i p(s_i) \cdot 1 \\
&= H(S) + 1
\end{aligned}$$

We have used the fact that $\epsilon_i < 1$, which makes
the sum $\sum_i p(s_i) \epsilon_i$ smaller or equal to $\sum_i p(s_i)$,
which is 1.
```

Although a Shannon code is not optimal, in the sense that it
does not lead to the minimum achievable average length,
we see that it's also not very bad.
The average length of Shannon code is **at most 1 bit longer** than the minimum possible value, which is quite efficient.
However, better procedures do exist.

#### Shannon's first theorem

Shannon's first theorem (coding theorem for noiseless channels)
shows us that, in theory, we can approach the entropy as close as we want,
using extended sources.

```{prf:theorem} Shannon's first theorem
It is possible to encode an infinitely long sequences of messages
from a source S with an average length
as close as desired to H(S),
but never below H(S).
```

```{prf:proof}
First, note that the average length can never go below H(S),
because this is minimum. We only consider getting close to H(S) from above.

Let's consider the **$n$-th order extension** $S^n$ of the source S.

$S^n$ is a source like any other,
with its own probabilities $p(\sigma_i)$,
and it can undergo Shannon coding as well.
When we use Shannon coding for $S^n$, it satisfies the same condition:

$$H(S^n) \leq \overline{l_{S^n}} < H(S^n) + 1$$

where $\overline{l_{S^n}}$ is the average length of the codewords for $S^n$.

We have $H(S^n) = n H(S)$, due to the theorem for extended sources.

Because a message of $S^n$ is just a group of $n$ messages of $S$,
we have the average length **per message of $S$** as:

$$\overline{l_{S}} = \frac{\overline{l_{S^n}}}{n}$$

Therefore, dividing by $n$, we obtain:

$$\boxed{H(S) \leq \overline{l_{S}} < H(S) + \frac{1}{n}}$$

which means that the average length used for a message
of the original source $S$ is
at most $1/n$ away from the entropy $H(S)$.

At the limit, if we consider the extension order $n \to \infty$, we have:

$$\overline{l_{S}} \to H(S)$$

```

The theorem shows that, in principle, we can always obtain
$\overline{l} \to H(S)$,
if we consider longer and longer sequences of messages from the source,
modeled as larger and larger extensions of the source.

However, this result is mostly theoretical, because in practice the size of $S^n$ gets too large for large $n$.
Other (better) algorithms than Shannon coding are used in practice to approach $H(S)$.


```{admonition} Analogy
When you buy things online and you want to avoid paying for delivery,
you bundle many things into one order, so that the delivery cost per unit
becomes smaller and smaller.

This is exactly how Shannon's first theorem works. It bundles many
messages into one (using $n$-th order extensions), so that the
overhead of maximum +1 incurred by the Shannon code becomes smaller and smaller, when considered per message.
```


### Shannon-Fano coding (binary)

The Shannon-Fano (binary) coding procedure is presented below.

```{prf:algorithm} Shannon-Fano coding (binary)
**Inputs** A DMS source with probabilities $p(s_i)$

**Outputs** Codewords $l_i$

1. Sort the message probabilities in descending order
2. Split into two subgroups as nearly equal as possible
3. Assign first bit $0$ to first group, first bit $1$ to second group
4. Repeat on each subgroup
5. When reaching one single message => that is the codeword

```

Example: blackboard

Remarks:

- Shannon-Fano coding does not always produce the shortest code lengths
- Connection: yes-no answers (example from first chapter)

### Huffman coding (binary)

```{prf:algorithm} Huffman coding procedure (binary)

**Inputs** A DMS source with probabilities $p(s_i)$

**Outputs** Codewords $l_i$

1. Sort the message probabilities in descending order
2. Join the last two probabilities, insert result into existing list, preserve descending order
3. Repeat until only two messages are remaining
4. Assign first bit $0$ and $1$ to the final two messages
5. Go back step by step: every time we had a sum, append $0$ and $1$ to the end of existing codeword

```

Properties of Huffman coding:

* Produces a code with the **smallest average length** (better than Shannon-Fano)
* Assigning $0$ and $1$ can be done in any order => different codes, same lengths
* When inserting a sum into an existing list, may be equal to another value => options
    * we can insert above, below or in-between equal values
    * leads to codes with different *individual* lengths, but same *average* length
* Some better algorithms exist which do not assign a codeword to every single message
(they code a while sequence at once, not every message)

### Huffman coding (M symbols)

General Huffman coding procedure for codes with $M$ symbols:

* Have $M$ symbols $\left\lbrace x_1, x_2, ... x_M \right\rbrace$
* Add together the last $M$ symbols
* When assigning symbols, assign all $M$ symbols
* **Important**: at the final step must have $M$ remaining values
    * May be necessary to add *virtual* messages with probability 0 at the end of the initial list,
    to end up with exactly $M$ messages in the last step

* Example : blackboard

### Example: compare Huffman and Shannon-Fano

Example: compare binary Huffman and Shannon-Fano for:
$$p(s_i) = \left\lbrace 0.35, 0.17, 0.17, 0.16, 0.15 \right\rbrace$$

### Probability of symbols

* For every symbol $x_i$
we can compute the average number of symbols $x_i$ in a code
$$\overline{l_{x_i}} = \sum_i p(s_i) l_{x_i}(s_i)$$
    * $l_{x_i}(s_i) =$ number of symbols $x_i$ in the codeword of $s_i$
    * e.g.: average number of 0's and 1's in a code
* Divide by average length => probability (frequency) of symbol $x_i$
$$p(x_i) = \frac{\overline{l_{x_i}}}{\overline{l}}$$

* These are the probabilities of the input symbols for the transmission channel
    * they play an important role in Chapter IV (transmission channels)

### Source coding as data compression

* Consider that the messages are already written in a binary code
    * Example: characters in ASCII code

* Source coding  = remapping the original codewords to other codewords
    * The new codewords are shorter, on average

* This means data **compression**
    * Just like the example in lab session

* What does data compression remove?
    * Removes **redundancy**: unused bits, patterns, regularities etc.
    * If you can guess somehow the next bit in a sequence, it means the bit is not really necessary,
    so compression will remove it
    * The compressed sequence looks like random data: impossible to guess,
    no discernable patterns

### Discussion: data compression with coding

* Consider data compression with Shannon or Huffman coding, like we did in lab
    * What property do we *exploit* in order to obtain compression?
    * How does *compressible data* look like?
    * How does *incompressible data* look like?
    * What are the limitation of our data compression method?
    * How could it be improved?

### Other codes: arithmetic coding

* Other types of coding do exist (info only)
	* Arithmetic coding
	* Adaptive schemes
	* etc.

### Chapter summary

* Average length: $\overline{l} = \sum_i p(s_i) l_i$
* Code types: instantaneous $\subset$ uniquely decodable $\subset$ non-singular
* All instantaneous or uniqualy decodable code must obey Kraft:
$$ \sum_i D^{-l_i} \leq 1$$
* Optimal codes: $l_i = -\log(p(s_i))$, $\overline{l_{min}} = H(S)$
* Shannon's first theorem: use $n$-th order extension of $S$, $S^n$:
$$\boxed{H(S) \leq \overline{l_{S}} < H(S) + \frac{1}{n}}$$
    * average length always larger, but as close as desired to $H(S)$
* Coding techniques:
    * Shannon: ceil the optimal codeword lengths (round to upper)
    * Shannon-Fano: split in two groups approx. equal
    * Huffman: group last two. Is best of all.
