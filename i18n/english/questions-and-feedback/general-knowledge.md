---
icon: book-bookmark
---

# General Knowledge

## What're tokens?

Tokens are the basic units that AI models use to process text, and can be understood as the smallest units that the model "thinks" with. They are not exactly the same as the characters or words we understand, but rather a special way the model itself divides text.

### 1. Word Splitting for Chinese

* One Chinese character is usually encoded as 1-2 tokens
* For example: `"你好"` ≈ 2-4 tokens

### 2. Word Splitting for English

* Common words are usually 1 token
* Longer or less common words will be broken down into multiple tokens
* For example:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

## 3. Special characters

* Spaces and punctuation also consume tokens
* A line break is usually 1 token

{% hint style="info" %}
Tokenizers differ across service providers, and even across different models from the same provider. This information is only for clarifying the concept of a token.
{% endhint %}

***



## What's a Tokenizer?

A tokenizer is a tool that AI models use to convert text into tokens. It determines how to split input text into the smallest units that the model can understand.

### Why Do Different Models Have Different Tokenizers?

#### 1. Different Training Data

* Different corpora lead to different optimization directions
* Varying degrees of multilingual support
* Specialized optimization for specific domains (medical, legal, etc.)

#### 2. Differences in Participle Algorithms

* BPE (Byte Pair Encoding) - OpenAI GPT Serious
* WordPiece - Google BERT
* SentencePiece - Suitable for multilingual scenarios

#### 3. Different Optimization Goals

* Some prioritize compression efficiency
* Some prioritize semantic preservation
* Some prioritize processing speed

### Practical Effect

The same text may have different token counts in different models:



```
输入："Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***



## What's an Embedding Model?

**Basic concept**: Embedding models are a technology that transforms high-dimensional discrete data (text, images, etc.) into low-dimensional continuous vectors. This transformation allows machines to better understand and process complex data. Imagine it as simplifying a complex jigsaw puzzle into a simple coordinate point, but this point still retains the key features of the puzzle. In the large model ecosystem, it acts as a "translator," converting human-understandable information into a numerical form that AI can compute.

**Working principle**: Taking natural language processing as an example, embedding models can map words to specific locations in a vector space. In this space, words with similar semantics will automatically cluster together. For example:

* The vectors for "king" and "queen" will be very close
* Pet words like "cat" and "dog" can be close together
* Semantically unrelated words like "car" and "bread" will be farther away

#### Main Application Scenarios:

* Text analytics: Document categorization, sentiment analysis
* Recommender system: Personalized content recommendation
* Image processing: Similar image retrieval
* Search engine: Semantic search optimization

#### Core Advantages

1. Dimensionality reduction effect: Simplifies complex data into easily processed vector forms
2. Semantic preservation: Retaining key semantic information from the original data
3. Computational efficiency: Significantly improves the training and inference efficiency of machine learning models.

**Technical Value**: Embedded model is a fundamental component of modern AI systems, providing high-quality data representation for machine learning tasks, and is a key technology that drives the development of natural language processing, computer vision, and other fields.

***



## How Embedding Models Work in Knowledge Retrieval

**Basic workflow:**

1. **Knowledge Base Preprocessing Phase**

* Split the document into chunks of appropriate size
* Convert each chunk into a vector using an embedding model
* Store the vectors and original text in a vector database

2. **Query Processing Phase**

* Convert user questions into vectors
* Retrieve similar content in the vector database
* Provide the retrieved relevant content as context to the LLM
