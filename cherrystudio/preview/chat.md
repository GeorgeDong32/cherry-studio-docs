---
icon: message
---

# 对话界面

## 助手和话题

### 助手

<mark style="background-color:yellow;">助手</mark>是对所选模型做一些个性化的设置来使用模型，如提示词预设和参数预设等，通过这些设置让所选模型能更加符合你预期的工作。

<mark style="background-color:yellow;">`系统默认助手`</mark>预设了一个比较通用的参数（无提示词），您可以直接使用或者到[智能体页面](agents.md)寻找你需要的预设来使用。



### 话题

<mark style="background-color:yellow;">助手</mark>是<mark style="background-color:yellow;">话题</mark>的父集，单个助手下可以创建多个话题（即对话），所有`话题`共用`助手`的参数设置和预设词（prompt）等模型设置。



<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 对话设置

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 模型设置

模型设置与助手设置当中的`模型设置`参数同步,详见[助手设置](chat.md#bian-ji-zhu-shou)部分文档。

{% hint style="info" %}
在对话设置当中，仅该模型设置作用于当前助手，其余设置作用于全局。如：设置消息样式为气泡后在任何助手的任何话题下都是气泡样式。
{% endhint %}



### 消息设置

#### <mark style="color:blue;">**`消息分割线`**</mark>:

使用分割线将消息正文与操作栏隔开。

{% tabs %}
{% tab title="打开时" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="关闭时" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}



#### <mark style="color:blue;">**`使用衬线字体`**</mark>：

字体样式切换，现在你也可以通过[自定义css](../../advanced-basic/personalization/)来更换字体。



#### <mark style="color:blue;">**`代码显示行号`**</mark>：

模型输出代码片段时显示代码块行号。

{% tabs %}
{% tab title="关闭时" %}
<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="打开时" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}



#### <mark style="color:blue;">**`代码块可折叠`**</mark>：

打开后当输出长代码在代码片段当中时，可自动折叠代码块。



#### <mark style="color:blue;">**`消息样式`**</mark>：

可切对话界面换为气泡样式或列表样式。



#### <mark style="color:blue;">**`代码风格`**</mark>：

#### 可切换代码片段的显示风格。



#### <mark style="color:blue;">**`数学公式引擎`**</mark>：

* KaTeX 渲染速度更快，因为它是专门为性能优化设计的；
* MathJax 渲染较慢，但功能更全面，支持更多的数学符号和命令。

#### <mark style="color:blue;">**`消息字体大小`**</mark>：

#### 调整对话界面字体的大小。



### 输入设置

#### <mark style="color:blue;">**`显示预估Token数`**</mark>：

在输入框显示输入文本预估消耗的Token数（非实际上下文消耗的Token，仅供参考）。



#### <mark style="color:blue;">**`长文本粘贴为文件`**</mark>：

当从其他地方复制长段文本粘贴到输入框时会自动显示为文件的样式，减少后续输入内容时的干扰。



#### <mark style="color:blue;">**`Markdown渲染输入消息`**</mark>：

关闭时只渲染模型回复的消息，不渲染发送的消息。

{% tabs %}
{% tab title="关闭时" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="打开时" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}



#### <mark style="color:blue;">**`快速敲击3次空格翻译`**</mark>：

在对话界面输入框输入消息后，连敲三次空格可翻译输入的内容为英文。的

{% hint style="info" %}
注意：该操作会覆盖原文。
{% endhint %}

***

## 助手设置

在助手界面选择需要设置的<mark style="background-color:yellow;">助手名称</mark>→在<mark style="background-color:yellow;">右键菜单中</mark>选对应设置

### 编辑助手

{% hint style="info" %}
助手设置作用于该助手下的所有话题。
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 提示词设置

#### <mark style="color:blue;">**`名称`**</mark>：

可自定义为方便辨识的助手名称；

#### <mark style="color:blue;">**`提示词`**</mark>：

#### 即prompt，可以参照智能体页面的提示词写法来编辑内容。



#### 模型设置

#### <mark style="color:blue;">**`默认模型`**</mark>：

#### 可以为该助手固定一个默认模型，从智能体页面添加时或复制助手时初始模型为该模型。不设置该项初始模型则为全局初始模型(即[默认助手模型](settings/default-models.md#mo-ren-zhu-shou-mo-xing))。

{% hint style="info" %}
助手的默认模型有两种，一为[全局默认对话模型](settings/default-models.md#mo-ren-zhu-shou-mo-xing)，另一为助手默认模型；助手的默认模型优先级高于全局默认对话模型。当不设置助手默认模型时，助手默认模型=全局默认对话模型。
{% endhint %}



#### <mark style="color:blue;">**`自动重置模型`**</mark>：

#### 打开时 - 当在该话题下使用过程中切换其他模型使用时，再次新建话题会将新话题的重置为助手的默认模型。当该项关闭时新建话题的模型会跟随上一话题所使用的模型。

> 如助手的默认模型为gpt-3.5-turbo，我在该助手下创建话题1，在话题1的对话过程中切换了gpt-4o使用，此时：
>
> 如果开启了自动重置：新建话题2时，话题2默认选择的模型为gpt-3.5-turbo;
>
> 如果未开启自动重置：新建话题2时，话题2默认选择的模型为gpt-4o。



#### <mark style="color:blue;">**`温度 (Temperature)`**</mark> ：

温度参数控制模型生成文本的随机性和创造性程度（默认值为0.7）。具体表现为：

* 低温度值(0-0.3)：
  * 输出更确定、更专注
  * 适合代码生成、数据分析等需要准确性的场景
  * 倾向于选择最可能的词汇输出
* 中等温度值(0.4-0.7)：
  * 平衡了创造性和连贯性
  * 适合日常对话、一般性写作
  * 推荐用于聊天机器人对话(0.5左右)
* 高温度值(0.8-1.0)：
  * 产生更具创造性和多样性的输出
  * 适合创意写作、头脑风暴等场景
  * 但可能降低文本的连贯性



#### <mark style="color:blue;">**`Top P (核采样)`**</mark>：

默认值为 1，值越小，AI 生成的内容越单调，也越容易理解；值越大，AI 回复的词汇范围越大，越多样化。

核采样通过控制词汇选择的概率阈值来影响输出：

* 较小值(0.1-0.3)：
  * 仅考虑最高概率的词汇
  * 输出更保守、更可控
  * 适合代码注释、技术文档等场景
* 中等值(0.4-0.6)：
  * 平衡词汇多样性和准确性
  * 适合一般对话和写作任务
* 较大值(0.7-1.0)：
  * 考虑更广泛的词汇选择
  * 产生更丰富多样的内容
  * 适合创意写作等需要多样化表达的场景

{% hint style="info" %}


* 这两个参数可以独立使用或组合使用
* 根据具体任务类型选择合适的参数值
* 建议通过实验找到最适合特定应用场景的参数组合
* 以上内容仅供参考和了解概念，所给参数范围不一定适合所有模型，具体可参考模型相关文档给出的参数建议。
{% endhint %}



#### <mark style="color:blue;">**`上下文数量 (Context Window)`**</mark>&#x20;

要保留在上下文中的消息数量，数值越大，上下文越长，消耗的 token 越多：

* 5-10：适合普通对话
* \>10：需要更长记忆的复杂任务（例如：按照写作提纲分步生成长文的任务，需要确保生成的上下文逻辑连贯）
*   > 注意：消息数越多，token 消耗越大





#### <mark style="color:blue;">**`开启消息长度限制(MaxToken)`**</mark>

单次回答最大[Token](https://docs.cherry-ai.com/cherrystudio/question-contact/knowledge#shen-me-shi-tokens)数,在大语言模型中，max token（最大令牌数）是一个关键参数，它直接影响模型生成回答的质量和长度。具体设置多少取决于自己的需要，当然也可以参考以下建议。

> &#x20;如:在CherryStudio当中填写好key后测试模型是否连通时，只需要知道模型是否有正确返回消息而不需特定内容,这种情况下设置MaxToken为1即可。

多数模型的MaxToken上限为4k Tokens，当然也有2k也有16k甚至更多的，具体需要到对应介绍页面查看。

{% hint style="success" %}
建议：

* 普通聊天：500-800
* 短文生成：800-2000
* 代码生成：2000-3600
* 长文生成：4000及以上 (需要模型本身支持)
{% endhint %}

{% hint style="warning" %}
一般情况下模型生成的回答将被限制在MaxToken的范围内，当然也有可能会出现被截断（如写长代码时）或表达不完整等情况出现，特殊情况下也需要根据实际情况来灵活调整。
{% endhint %}



#### <mark style="color:blue;">**`流式输出（Stream）`**</mark>

流式输出是一种数据处理方式，它允许数据以连续的流形式进行传输和处理，而不是一次性发送所有数据。这种方式使得数据可以在生成后立即被处理和输出，极大地提高了实时性和效率。

在CherryStudio客户端等类似环境下简单来说就是打字机效果，

关闭后(非流)：模型生成完信息后整段一次性输出（想象一下微信收到消息的感觉）；

打开时：逐字输出，可以理解为大模型每生成一个字就立马发送给你，直到全部发送完。

{% hint style="info" %}
如果某些特殊模型不支持流式输出需要将该开关关闭，比如**刚开始**只支持非流的o1-mini等。
{% endhint %}



#### <mark style="color:blue;">**`自定义参数`**</mark>

在请求体（body）中加入额外请求参数，如`presence_penalty`等字段，一般人一般情况下用不到。

填法：参数名称—参数类型（文本、数字等）—值，参考文档：[点击前往](https://openai.apifox.cn/doc-3222739)

> 上述top-p、maxtokens、stream等参数就是这些参数之一。



{% hint style="info" %}
自定义参数优先级高于内置参数。即自定义参数如果与内置参数重复，则自定义参数会覆盖内置参数。

如：自定义参数中设置`model`为`gpt-4o`后，在对话中无论选择哪个模型都使用的是`gpt-4o`模型。
{% endhint %}
