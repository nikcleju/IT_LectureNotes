
# Discrete Information Sources

$$
\newcommand{\snII}[5]{#1: \left( \begin{matrix} {#2} & {#4} \\ #3 & #5 \end{matrix} \right)}
\newcommand{\snIV}[9]{#1: \left( \begin{matrix} {#2} & {#4} & {#6} & {#8} \\ #3 & #5 & #7 & #9 \end{matrix} \right)}
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
$$

## A mathematical definition of information

In order to analyze information generation, encoding and transmission 
with mathematical tools,
we need a solid and clear definition of information.

<!-- ### Block diagram of a communication system

![Block diagram of a communication system](img/CommBlockDiagram.png){width=50%}

- Source: creates information messages 
- Encoder: converts messages into symbols for transmission (i.e bits)
- Channel: delivers the symbols, introduces errors
- Decoder: detects/corrects the errors, rebuilds the information messages -->

### What is information?

Let's start first with some simple examples of messages carrying information.

Consider the sentence:

> "Poli Iași (the local football team) lost the last match"

Does this message carry information? How, why, how much?

When thinking about the information brought by such a phrase, let's consider the following facts:

- the message carries information only when you don't already know the result
- if you already known the result, the message is useless (brings no information)
- if the result was to be expected, there is little information (e.g. suppose Poli Iași plays against FC Barcelona)
- if the result is highly unusual, there is more information in this message

```{admonition} Example

To understand why the amount of information involved here
depends on whether the result is to be expected or is highly unusual,
consider a case when information is valuable, for example:

- in an exam or quiz with multiple-choice answers (e.g. Who Wants to be a Millionaire)
- in sports betting (gambling), 

The amount you gain depends on the amount of information you have on the topic: those who know a lot compared to others win a lot,
those who know little win just a little. But you're not winning a fortune
by answering easy questions which most people know, or betting on result which everybody expects.
We explain this by the fact that there is little information involved in them.
You do win a lot by answering hard questions or betting on surprising results,
and since it's the information which is valuable, it shows that unexpected outcomes have lots of information.
```

#### Information and events

As seen in the example above, the notion of information requires a probabilistic setting.

We define the notion of **information** for a **probabilistic event**:

- an event may or may not happen, and when it does happen, it creates information

- the information is: "this event happened"

- the amount of information depends on the **probability** of that event

```{hint}
As a rule of thumb, keep in mind:

- if you can guess something most of the times, it has little information
- if something is unexpected, it has a lot of information
```

```{admonition} Question
Let's answer some questions:

- does a sure event (p = 1) bring any information?
- does an almost sure event (e.g. P = 0.9999)  bring little or much information?
- does a rare event (e.g. P = 0.0001) bring a little or much information?
```

#### Definition of information

Throughout this class, we refer to a probabilistic event as a **"message"**

The information attached to a message $s_i$ is rigorously defined as:
$$i(s_i) = -\log_2(p(s_i))$$

Consequences of this definition:

- Information of an event is always non-negative:

  $$
  i(s_i) \geq 0
  $$

- Lower probability (rare events) means higher information
- Higher probability (frequent events) means lower information
- The certain event ($p = 1)$ brings no information:

  $$
  -\log(1) = 0
  $$

- An event with probability $0$ brings infinite information (but it never happens...)
- When two independent $s_i$ and $s_j$ events take place, their information gets added:
  
  $$
  \begin{align}
  i(s_i \cap s_j) &= -log_2(p(s_i \cap s_j) \\
  &= -log_2(p(s_i) \cdot p(s_j) \\
  &= -log_2(p(s_i) - log_2(p(s_j)) \\
  &= i(s_i) + i(s_j)
  \end{align}
  $$

#### The choice of logarithm

Using the logarithm function in the definition is crucial,
since it is responsible for most of these properties.
In particular, the fact that logarithm transforms a product into a sum
allows to sum the information of independent events.

Any base of logarithm can be used in the definition, not just base 2,
and all the consequences still hold.

- By convention, we typically use the binary logarithm $\log_2()$.
  In this case, the information $i(s_i)$ is measured in **bits**

- We could use instead the natural logarithm $ln()$, and the result
  is measured in *nats*.

The choice of the algorithm is not critical and doesn't change anything fundamental,
since logarithm bases can always be converted to/from one another:

$$
\log_b(x) = \frac{\log_a(x)}{\log_a(b)}
$$

This means that information defined using different logarithms differ only by a scaling factor:

$$
i_b(s_i) =\frac{i_a(s_i)}{\log_a(b)}
$$

Following the convention of the scientific literature, we shall use the base 2 logarithm $log_2()$ from now on.

### Information Source

A probabilistic event is always part of a set of multiple events, 
containing all the possible outcomes which can happen at a given time.

Each event (known as "message") has its own probability, which are all known beforehand.
At a given time, only one of the events can happen. 
This carries the information that **it** happened (out of all possible events),
and the quantity information quantity is dependent of the probability.

We define an **information source** as the set of all events,
together with their probabilities.

Example:

- a football team can win / lose / draw a match (3 possible events)

The set of all messages forms the "*alphabet*" of the source.

When an event takes place, we say that "the information source generates a message".

#### Sequence of messages

We are very rarely interested in a single message.
Instead, we are interested analyzing large amounts of messages.

An information source creates a **sequence of messages**, by generating
messages one after another, randomly, according to the known probabilities.

- e.g. like throwing a coin or a dice several times in a row

Depending on how the messages are generated, we distinguish between two types
of information sources:

1. **Memoryless** sources: each new message is generated independently on the previous messages
2. Sources **with memory**: when generating a new message, the probabilities depend on one or more of the previous messages

### Discrete memoryless source

A **discrete memoryless source** (DMS) is an information source which produces a sequence of **independent** messages.
The choice of a message at one time does not depend on the previous messages.
Each message has a fixed probability, and every new message is generated randomly based on the probabilities.

The set of probabilities is the **distribution** of the source,
also known as a **probability mass function**.

We represent a DMS as below,
by giving it a name ("S"), listing the messages ($s_1, s_2, s_3$) and the probability distribution:

$$
\sIII{S}{\fIoII}{\fIoIV}{\fIoIV}
$$

A DMS is a discrete, complete and memoryless:

- **Discrete**: the set of messages is a discrete set
- **Complete**: the sum of all probabilities is 1, which means that one and only one event must take place at a given time:
  $$
  \sum p(s_i) = 1
  $$
- **Memoryless**: each message is independent of the previous messages

A good example of a DMS is a coin, or a dice.

One message generated by DMS is also called a **random variable** in statistics.

```{admonition} Example

A coin is a discrete memoryless source (DMS) with two messages:

  $$
  \snII{S}{heads}{\fIoII}{tails}{\fIoII}
  $$

A dice is a discrete memoryless source (DMS) with six messages:

  $$
  \sVI{S}{\fIoVI}{\fIoVI}{\fIoVI}{\fIoVI}{\fIoVI}{\fIoVI}
  $$

Playing the lottery can be modeled as DMS:

  $$
  \sII{S}{0.9999}{0.0001}
  $$

An extreme type of DMS containing the certain event:

  $$
  \sII{S}{1}{0}
  $$

Receiving an unknown *bit* (0 or 1) with equal probabilities:

  $$
  \snII{S}{0}{\fIoII}{1}{\fIoII}
  $$
```

#### Sequence of messages from DMS

A DMS produces a sequence of messages by randomly selecting a message every time,
with the same fixed probabilities, producing a sequence like:

$$
s_3 s_2 s_4 s_1 s_2 s_1 s_3 \dots
$$

For example, throwing a dice several times in a row you can get the following sequence:

$$
4, 2, 3, 2, 1, 6, 1, 5, 4, 5 \dots
$$

In a sequence which is very long, with length $N \to \infty$,
each message $s_i$ appears in the sequence approximately $p(s_i) * N$ times.
This gets more precise as $N$ gets larger.

### Entropy of a DMS

We usually don't care about the information of single message. We are interested in long sequences of messages
(think millions of bits of data).

To analyze this in an easy manner, we need the *average* information of a message from a DMS.

The **entropy of a DMS source** $S$ is **the average information of a message**:

$$
H(S) = \sum_{k} p(s_k) i(s_k) = -\sum_{k} p(s_k) \log_2(p_k)
$$
where $p(s_k)$  is the probability of message $k$

Since information of a message is measured in bits, 
entropy is measured in **bits** (or **bits / message**, to indicate it is an average value).

Entropies using information defined with different logarithms base are differ only by a scaling factor:
$$
H_b(S) =\frac{H_a(S)}{\log_a(b)}
$$

```{admonition} Example

Let's compute the entropies of some of the DMS defined above.

Coin: 

  $$
  H(S) = 1 \textrm{ bit/message}
  $$

Dice: 

  $$
  H(S) = \log(6) \textrm{  bits/message}
  $$

Lottery: 

  $$
  H(S) = -0.9999 \log(0.9999) - 0.0001 \log(0.0001) \textrm{ bits/message}
  $$

Receiving 1 bit with equal probabilities: 

  $$
  H(S) = 1 \textrm{ bit/message}
  $$
 (hence the name!)
```

#### Interpretation of the entropy

The entropy of an information source S is a fundamental quantity.
It allows us to compare two different sources, which model
different scenarios from real life.

All the following interpretations of entropy are true:

- $H(S)$ is the **average uncertainty** of the source S

- $H(S)$ is the **average information** of a message from source S

- A very long sequence of $N$ messages generated by source S has total information $\approx N \cdot H(S)$

We shall see in Chapter III that the entropy $H(S)$ says something very important 
about the **number of bits** requires to represent data in binary form:

- $H(S)$ is the minimum number of bits ($0$, $1$) required to uniquely represent a message from source S, on average

- A very long sequence of $N$ messages generated by source S needs at least $\approx N \cdot H(S)$ bits in order to be represented in binary form

Thus, $H(S)$ is crucial when we discuss how to represent data efficiently.

#### Properties of entropy

We prove the following **properties of entropy**:

1. $H(S) \geq  0$ (non-negative)

    Proof: via definition

2. $H(S)$ is maximum when all $n$ messages have equal probability $\frac{1}{n}$.
The maximum value is $\max H(S) = \log(n)$

    Proof: only for the case of 2 messages, use derivative in definition

3. *Diversification* of the source always increases the entropy

    Proof: compare entropies in both cases

#### The entropy of a binary source

Consider a general DMS with two messages:
  
  $$
  \sII{S}{p}{1-p}
  $$

It's entropy is:
  
  $$
  H(S) = -p \cdot \log(p) - (1-p) \cdot \log(1-p)
  $$

The entropy value as a function of $p$ is represented below:

<!-- ![Entropy of a binary source](img/EntropyBinary.png){height=40%} -->

![Entropy of a binary source](img/EntropyBinary.png)

As an illustration of the property no.2 from above,
we can see that the maximum entropy value of a DMS with two messages is reached
when the two messages have the same probability, $p = 0.5$:

$$
p(s_1) = p = p(s_2) = 1 - p = 0.5
$$

and its value is:

$$
H_{max}(S) = 1
$$

#### Let's play games

Let's analyze the following guessing games with the tools introduced until now.

```{admonition} Exercise

I think of a number between 1 and 8. You have to guess it by asking
yes/no questions.

- How much uncertainty does the problem have?
- How is the best way to ask questions? Why?
- What if the questions are not asked in the best way?
- On average, what is the number of questions required to find the number?

Now suppose I randomly choose a number according to the following distribution:
  
  $$
  \sIV{S}{\fIoII}{\fIoIV}{\fIoVIII}{\fIoVIII}
  $$

- On average, what is the number of questions required to find the number? 
- What questions would you ask?

But what if the distribution is the following?
  
  $$
  \sIV{S}{0.14}{0.29}{0.4}{0.17}
  $$

Let's draw some general conclusions:

- What distribution makes guessing the number the most difficult?
- What distribution makes guessing the number the easiest?

An **optimal decision tree** is best sequence of questions to ask in order to find the number with a minimum number
of questions, represented as a binary tree graph. You will see examples when we solve the exercises.
```

#### Efficiency, redundancy, flow

Using the $H(S)$, we define several other useful characteristics of a DMS.

The **efficiency** of a DMS indicates how close is the entropy to its maximum possible value:
  
  $$
  \eta = \frac{H(S)}{H_{max}} = \frac{H(S)}{\log(n)}
  $$

The **redundancy** of a source is the remaining gap.
  - **Absolute** redundancy of a DMS:
  
  $$
  R = H_{max} - H(S)
  $$

  - **Relative** redundancy of a DMS:

    $$
    \rho = \frac{H_{max} - H(S)}{H_{max}} = 1 - \eta
    $$


Suppose that each message $s_i$ takes some time $t_i$ to be transmitted via some communication channel.
The **information flow** of a DMS $S$ is the average information transmitted per unit of time:

$$
H_\tau(S) = \frac{H(S)}{\overline{t}},
$$

where $\overline{t}$ is the average duration of transmitting a message:

$$
\overline{t} = \sum_{i} p_i t_i 
$$

The information flow is measured in **bps** (bits per second), and is important for data communication.

#### Distance between distributions


- How to measure how similar / how different are two distributions?

    - must have the same number of messages
    - example: $p(s_1), ... p(s_n)$ and $q(s_1), ... q(s_n)$
  
- **Definition**: the **Kullback–Leibler distance** of two distributions P and Q is
    $$D_{KL}(P || Q) = \sum_i p(s_i) \log(\frac{p(s_i)}{q(s_i)})$$

- It is a way to measure the **distance (difference)** between two distributions

- Also known as *relative entropy*, or the Kullback-Leibler *divergence*

### Properties of Kullback-Leibler distance

- Properties:

    - $D_{KL}(P || Q)$ is always $\geq 0$, and is equal to 0 only when P and Q are the same
    - the higher $D_{KL}(P || Q)$ is, the more different the distributions are
    - it is **not commutative**: $D_{KL}(P || Q) \neq D_{KL}(Q || P)$

- Example: at whiteboard

- Example usage: classification systems (cross-entropy loss)

### Extended DMS

- Definition: the **n-th order extension** of a DMS $S$, $S^n$ is a source which
has as messages all the combinations of $n$ messages of $S$:
    $$\sigma_i = \underbrace{s_j s_k ... s_l}_{n}$$

- If $S$ has $k$ messages, $S^n$ has $k^n$ messages
- Since $S$ is DMS, probabilities multiply:
    $$p(\sigma_i) = p(s_j) \cdot p(s_k) \cdot ... \cdot p(s_l)$$

### Extended DMS - Example

- Examples:
$$\sII{S}{\fIoIV}{\frac{3}{4}}$$
$$\snIV{S^2}{\sigma_1 = s_1 s_1}{\frac{1}{16}}{\sigma_2 = s_1 s_2}{\frac{3}{16}}{\sigma_3 = s_2 s_1}{\frac{3}{16}}{\sigma_4 = s_2 s_2}{\frac{9}{16}}$$
$$S^3: \left( \begin{matrix} s_1 s_1 s_1 & s_1 s_1 s_2 & s_1 s_2 s_1 & s_1 s_2 s_2 & s_2 s_1 s_1 & s_2 s_1 s_2 & s_2 s_2 s_1 & s_2 s_2 s_2 \\ ... & ... & ... & ... & ... & ... & ... & ... \end{matrix} \right)$$


### Extended DMS - Another example
- Long sequence of binary messages:
$$0 1 0 0 1 1 0 0 1 1 1  0 0 1 0 1 0 0 ...$$

    - Can be grouped in bits, half-bytes, bytes, 16-bit words, 32-bit long words, and so on
	- Can be considered:
    
		- N messages from a binary source (with 1 bit), or
		- N/2 messages from a source with 4 messages (with 2 bits)...
		- etc


### Property of DMS

- Theorem: The entropy of a $n$-th order extension is $n$ times larger than the entropy of the original DMS
$$H(S^n) = n H(S)$$

- Interpretation: grouping messages from a long sequence in blocks of $n$ does not change total information
(e.g. groups of 8 bits = 1 byte)


### An example [memoryless is not enough]

- The distribution (frequencies) of letters in English:

    ![](img/EngLetterProb.jpg){width=30%}\ 

- Text from a memoryless source with these probabilities:

    ![](img/EnglishFirstOrder.png){width=50%}\

    *(taken from Elements of Information Theory, Cover, Thomas)*

- What's wrong? **Memoryless**

### Sources with memory

- **Definition**: A source has **memory of order $m$** if the probability
of a message depends on the last $m$ messages.

- The last $m$ messages = the **state** of the source (notation $S_i$).

- A source with $n$ messages and memory $m$ => has $n^m$ states in all.

- For every state, messages can have a different set of
probabilities. Notation: $p(s_i | S_k)$ = *"probability of $s_i$ in state $S_k$"*.

- Also known as *Markov sources*.

### Example
- A source with $n=4$ messages and memory $m=1$

    - if last message was $s_1$, choose next message with distribution
        $$\sIV{S_1}{0.4}{0.3}{0.2}{0.1}$$
    - if last message was $s_2$, choose next message with distribution
        $$\sIV{S_2}{0.33}{0.37}{0.15}{0.15}$$
    - if last message was $s_3$, choose next message with distribution
        $$\sIV{S_3}{0.2}{0.35}{0.41}{0.04}$$
    - if last message was $s_4$, choose next message with distribution
        $$\sIV{S_4}{0.1}{0.2}{0.3}{0.4}$$

### Transitions

- When a new message is provided, the source **transitions** to a
new state:
    $$...\underbrace{s_i s_j s_k}_{\text{old state}} s_l$$
    $$...s_i \underbrace{s_j s_k s_l}_{\text{new state}}$$

- The message probabilities = the probabilities of transitions from
some state $S_u$ to another state $S_v$

### Transition matrix
- The transition probabilities are organized in a **transition
matrix** $[T]$
    $$[T] = 
    \begin{bmatrix}
    p_{11} & p_{12} & ... & p_{1N} \\ 
    p_{21} & p_{22} & ... & p_{2N} \\ 
    ... & ... & ... & ... \\ 
    p_{N1} & p_{N2} & ... & p_{NN} \\ 
    \end{bmatrix}$$

- $p_{ij}$ is the transition probability from state $S_i$ to state
$S_j$

- $N$ is the total number of states

### Graphical representation
At whiteboard: draw states and transitions for previous example 
(source with $n=4$ messages and memory $m=1$)

### Entropy of sources with memory

- What entropy does s source with memory have?

- Each state $S_k$ has a different distribution --> each state has a different entropy $H(S_k)$
$$H(S_k) = - \sum_i p(s_i | S_k) \cdot \log(p(s_i | S_k))$$

- Global entropy = average entropy
$$H(S) = \sum_k p_k H(S_k)$$
where $p_k$ = probability that the source is in state $S_i$

    - (i.e. after a very long sequence of messages, the fraction of time when the source was in state $S_k$)

### Ergodic sources

- How to find out the weights $p_k$?

- They are known as the **stationary probabilities**

- $p_k$ = probability that the source is in state $S_i$, after running for a very long time

    - (i.e. after a very long sequence of messages, the fraction of time when the source was in state $S_k$)

- We need to answer the following question:
    
    If we know the state $S_k$ at time $n$, what will be the state at time $n+1$?
    

### Ergodic sources

- Let $p_i^{(n)} =$ the probability that source $S$ is in state $S_i$ at time $n$.

- In what state will it be at time $n+1$? (after one more message) 

    - i.e. what are the probabilities of the states at time $n+1$?

- Just multiply with $T$
    $$[p_1^{(n)}, p_2^{(n)}, ... , p_N^{(n)}] \cdot [T] = [p_1^{(n+1)}, p_2^{(n+1)}, ... , p_N^{(n+1)}]$$

- After one more message:
    $$[p_1^{(n)}, p_2^{(n)}, ... , p_N^{(n)}] \cdot [T] \cdot [T] = [p_1^{(n+2)}, p_2^{(n+2)}, ... , p_N^{(n+2)}]$$

- For every new moment of time, one more multiplication with $T$

### Ergodic sources

- In general, starting from time $0$, after $n$ messages the probabilities that the source is in a certain state are:
    $$[p_1^{(0)}, p_2^{(0)}, ... , p_N^{(0)}] \cdot [T]^{n} = [p_1^{(n)}, p_2^{(n)}, ... , p_N^{(n)}]$$

### Ergodicity

- A source is called **ergodic** if every state can be reached from every state, in a finite number of steps.

- Property of ergodic sources:

  - After many messages, the probabilities of the states *become stationary* (converge to some fixed values), 
  irrespective of the initial probabilities (no matter what state the source started from initially)
  
    $$\lim_{n \to \infty} [p_1^{(n)}, p_2^{(n)}, ... p_N^{(n)}] = [p_1, p_2, ... p_N]$$


### Finding the stationary probabilties

- How to find the value of the stationary probabilities?

- When $n$ is very large, after $n$ messages and after $n+1$ messages the probabilities are the same:
    $$[p_1, p_2, ... p_N] \cdot [T] = [p_1, p_2, ... p_N]$$

- This is an equation system in matrix form

- One line should be removed (linear combination), and replaced with:
    $$p_1 + p_2 + ... + p_N = 1$$

- Solve the resulting system of equations, find values of $p_k$

### Entropy of ergodic sources with memory 

- The entropy of an ergodic source with memory is
    $$H(S) = \sum_k p_k H(S_k) = - \sum_k p_k \sum_i p(s_i | S_k) \cdot \log(p(s_i | S_k)$$

### Exercise

1. Consider a discrete source with memory, with the graphical representation given below.
The states are defined as follows: $S_1: s_1s_1$, $S_2: s_1s_2$, $S_3: s_2s_1$, $S_4: s_2s_2$.

	![Graphical representation of the source](img/MemorySource3.png){.id width=35%}

### Exercise (continued)

Questions:

  a. What are the values of $x$ and $y$?
  b. Write the transition matrix $[T]$;
  c. Compute the entropy in state $S_4$;
  d. Compute the global entropy of the source;
  e. What are the memory order, $m$, and the number of messages of the source, $n$?
  f. If the source is initially in state $S_2$, in what states and with what probabilities 
    will the source be after 2 messages?

### Example English text as sources with memory

*(taken from Elements of Information Theory, Cover, Thomas)*

- Memoryless source, equal probabilities:

    ![](img/EnglishZeroOrder.png){width=40%}\

- Memoryless source, probabilities of each letter as in English:

    ![](img/EnglishFirstOrder.png){width=40%}\

- Source with memory $m=1$, frequency of pairs as in English:

    ![](img/EnglishSecondOrder.png){width=40%}\

### Example English text as sources with memory

- Source with memory $m=2$, frequency of triplets as in English:

    ![](img/EnglishThirdOrder.png){width=40%}\

- Source with memory $m=3$, frequency of 4-plets as in English:

    ![](img/EnglishFourthOrder.png){width=40%}\

### Example application

- Suppose we receive a text with random missing letters
- We need to fill the blanks with the appropriate letters
- How?

  - build a model: source with memory of some order
  - fill the missing letter with the most likely letter given by the model

### Chapter summary

- Information of a message: $i(s_k) = -\log_2(p(s_k))$

- Entropy of a memoryless source: $H(S) = \sum_{k} p_k i(s_k) = -\sum_{k} p_k \log_2(p_k)$

- Properties of entropy:
    
    1. $H(S) \geq  0$

    2. Is maximum when all messages have equal probability ($H_{max}(S) = \log(n)$)

    3. *Diversfication* of the source always increases the entropy

- Sources with memory: definition, transitions

- Stationary probabilities of ergodic sources with memory:
$[p_1, p_2, ... p_N] \cdot [T] = [p_1, p_2, ... p_N]$, $\sum_i p_i = 1$.

- Entropy of sources with memory:
$$H(S) = \sum_k p_k H(S_k) = - \sum_k p_k \sum_i p(s_i | S_k) \cdot \log(p(s_i | S_k)$$

