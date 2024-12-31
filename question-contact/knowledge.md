---
icon: book-bookmark
---

# 知识科普

## 什么是tokens？

Tokens 是 AI 模型处理文本的基本单位，可以理解为模型"思考"的最小单元。它不完全等同于我们理解的字符或单词，而是模型自己的一种特殊的文本分割方式。

#### 1. 中文分词

* 一个汉字通常会被编码为 1-2 个 tokens
* 例如：`"你好"` ≈ 2-4 tokens

#### 2. 英文分词

* 常见单词通常是 1 个 token
* 较长或不常见的单词会被分解成多个 tokens
* 例如：
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. 特殊字符

* 空格、标点符号等也会占用 tokens
* 换行符通常是 1 个 token



{% hint style="info" %}
不同服务商的tokenizer都不一样,甚至同服务商不同模型的tokenizer也有所差别,该知识仅用于明确token的概念。
{% endhint %}

***

## 什么是 Tokenizer？

Tokenizer（分词器）是 AI 模型将文本转换为 tokens 的工具。它决定了如何把输入文本切分成模型可以理解的最小单位。

### 为什么不同模型的 Tokenizer 不一样？

#### 1. 训练数据不同

* 不同的语料库导致优化方向不同
* 多语言支持程度差异
* 特定领域（医疗、法律等）的专门优化

#### 2. 分词算法不同

* BPE (Byte Pair Encoding) - OpenAI GPT 系列
* WordPiece - Google BERT
* SentencePiece - 适合多语言场景

#### 3. 优化目标不同

* 有的注重压缩效率
* 有的注重语义保留
* 有的注重处理速度

### 实际影响

同样的文本在不同模型中的 token 数量可能不同：

```
输入："Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```
