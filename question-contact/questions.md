---
icon: seal-question
---

# 常见问题

### 什么是tokens？

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
