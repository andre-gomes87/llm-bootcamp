# Week 1 --- LLM Basics Assessment

------------------------------------------------------------------------

## Part 1 --- Conceptual Understanding

### 1.

In your own words, what does the `temperature` parameter control in an
LLM?

------------------------------------------------------------------------

### 2.

You run the exact same prompt twice with `temperature=0`, but get
slightly different answers.

Give **two possible reasons** why this might happen.

------------------------------------------------------------------------

### 3.

Explain what a **system prompt** is and how it differs from a user
prompt.

------------------------------------------------------------------------

### 4.

Why is this prompt weak?

    tell me about AI

Rewrite it into a **strong prompt**.

------------------------------------------------------------------------

### 5.

What does `max_tokens` control?\
What happens if it's too low?

------------------------------------------------------------------------

## Part 2 --- Practical Reasoning

### 6.

You want the model to generate **consistent and reliable outputs** for a
backend system.

What temperature would you use and why?

------------------------------------------------------------------------

### 7.

You want the model to generate **creative story ideas**.

What temperature would you use and why?

------------------------------------------------------------------------

### 8.

You notice that changing only the system prompt drastically changes the
output.

Explain why this happens.

------------------------------------------------------------------------

## Part 3 --- Code Understanding

Consider the following function:

``` python
def ask_llm(question):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=1.2,
        max_tokens=50
    )
    return response.choices[0].message.content
```

### 9.

What are **two problems or limitations** in this implementation?

------------------------------------------------------------------------

### 10.

Modify the function to: - include a system prompt - allow temperature as
a parameter

Write the improved version below:

``` python
```

------------------------------------------------------------------------

## Part 4 --- Reflection

### 11.

What surprised you the most while experimenting with the LLM?

------------------------------------------------------------------------

### 12.

What is one thing you still don't fully understand?

------------------------------------------------------------------------

## Extra Challenge (Optional)

### 13.

Explain why LLMs do not always return the same answer, even when the
input is the same.

Use the idea of probability in your explanation.
