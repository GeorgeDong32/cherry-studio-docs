---
icon: message
---

# 对话界面

## 助手和话题

### 助手

`助手`是对所选模型做一些个性化的设置，如提示词预设和参数预设等，通过这些设置让所选模型能更加符合你预期的工作。

<mark style="background-color:yellow;">系统默认助手</mark>的参数是预设好的一个比较通用的参数，您可以直接使用或者到助手市场（智能体界面）寻找你需要的预设来使用。



### 话题

`助手`是`话题`的父集，单个助手下可以创建多个话题（即对话），所有`话题`共用`助手`的参数设置和预设词（prompt）等模型设置。



<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

## 对话设置

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>



***

## 助手设置

在助手界面选择需要设置的助手名称→在右键菜单中选对应设置

### **编辑助手**

{% hint style="info" %}
助手设置作用于该助手下的所有话题。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">提示词设置</mark>

`名称`：可自定义为方便辨识的助手名称；

`提示词`：即prompt，可以参照智能体页面的提示词写法来编辑内容。



#### <mark style="color:blue;">模型设置</mark>

`默认模型`：可以为该助手固定一个默认模型，从智能体页面添加时或复制助手时初始模型为该模型。不设置该项初始模型则为全局初始模型(即[默认助手模型](settings/default-models.md))。

{% hint style="info" %}
助手的默认模型有两种，一为全局默认对话模型，另一为助手默认模型；助手的默认模型优先级高于全局默认对话模型。当不设置助手默认模型时，助手默认模型=全局默认对话模型。
{% endhint %}

`自动重置模型`：打开时 - 当在该话题下使用过程中切换其他模型使用时，再次新建话题会将新话题的重置为助手的默认模型。当该项关闭时新建话题的模型会跟随上一话题所使用的模型。

> 如助手的默认模型为gpt-3.5-turbo，我在该助手下创建话题1，在话题1的对话过程中切换了gpt-4o使用，此时：
>
> 如果开启了自动重置：新建话题2时，话题2默认选择的模型为gpt-3.5-turbo;
>
> 如果未开启自动重置：新建话题2时，话题2默认选择的模型为gpt-4o。

#### <mark style="color:blue;">温度 (Temperature)</mark>&#x20;

模型生成文本的随机程度。值越大，回复内容越赋有多样性、创造性、随机性：

* 0：根据事实严格回答
* 0.7左右：日常对话推荐值
* 1或更大值：更具创造性但可能不够连贯

#### <mark style="color:blue;">Top P (核采样)</mark>&#x20;

默认值为 1，值越小，AI 生成的内容越单调，也越容易理解；值越大，AI 回复的词汇范围越大，越多样化：

* 较小值（如 0.1）：输出更保守可控
* 较大值（如 0.9）：词汇选择更丰富
* 1：考虑所有可能的词汇选择

#### <mark style="color:blue;">上下文数量 (Context Window)</mark>&#x20;

要保留在上下文中的消息数量，数值越大，上下文越长，消耗的 token 越多：

* 5-10：适合普通对话
* \>10：需要更长记忆的复杂任务
* > 注意：消息数越多，token 消耗越大

#### <mark style="color:blue;">开启消息长度限制(MaxToken)</mark>

单次回答最大[Token](https://docs.cherry-ai.com/cherrystudio/question-contact/knowledge#shen-me-shi-tokens)数,在大语言模型中，max token（最大令牌数）是一个关键参数，它直接影响模型生成回答的质量和长度。具体设置多少取决于自己的需要，当然也可以参考以下建议。

> &#x20;如:在CherryStudio当中填写好key后测试模型是否连通时，只需要知道模型是否有正确返回消息而不需特定内容,这种情况下设置MaxToken为1即可。

多数模型的MaxToken上限为4k Tokens，当然也有2k也有16k甚至更多的，具体需要到对应介绍页面查看。



{% hint style="info" %}
建议：

* 普通聊天：500-800
* 短文生成：800-2000
* 代码生成：2000-3600
* 长文生成：4000及以上 (需要模型本身支持)
{% endhint %}



{% hint style="warning" %}
一般情况下模型生成的回答将被限制在MaxToken的范围内，当然也有可能会出现被截断（如写长代码等）或表达不完整等情况出现，特殊情况下也需要根据使用环境来灵活调整。
{% endhint %}



#### <mark style="color:blue;">流式输出（Stream）</mark>

流式输出是一种数据处理方式，它允许数据以连续的流形式进行传输和处理，而不是一次性发送所有数据。这种方式使得数据可以在生成后立即被处理和输出，极大地提高了实时性和效率。

在CherryStudio客户端等类似环境下简单来说就是打字机效果，

关闭后：模型生成完信息后整段一次性输出（想象一下微信收到消息的感觉）；

打开时：逐字输出，可以理解为大模型每生成一个字就立马发送给你，直到全部发送完。



#### <mark style="color:blue;">自定义参数</mark>

在请求体（body）中加入额外请求参数，如`presence_penalty`等字段，一般人一般情况下用不到。

填法：参数名称—参数类型（文本、数字等）—值，参考文档：[点击前往](https://openai.apifox.cn/doc-3222739)

> 上述top-p、maxtokens、stream等参数就是这些参数之一。
