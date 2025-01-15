# 字节跳动(豆包)

* 登录[火山引擎](https://console.volcengine.com/)
* 找到火山方舟点击进入,或直接点击[这里直达](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)&#x20;

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### 添加模型

* 进入页面后在侧栏最下方找到开通管理
* 在开通管理页面开通需要使用的模型

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* 全部开通完成后点击`在线管理`，进入后点击`创建推理接入点`

<figure><img src="../../.gitbook/assets/image (2).png" alt="" width="528"><figcaption></figcaption></figure>

* 接入点名称随便写，保证自己能辨识即可，建议跟模型名同步
* 点击`+添加模型`按钮
* ① 选择模型、② 选择版本（主线模型）、③ 确认

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

* 点击`确认接入`

<figure><img src="../../.gitbook/assets/image (4).png" alt="" width="301"><figcaption></figcaption></figure>

* 打开CherryStudio的[模型服务](../../cherrystudio/preview/settings/providers.md)设置找到豆包
* 点击添加模型

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>接入点名称下的ep-xxxxxx即模型ID,模型名称建议填接入模型的名称</p></figcaption></figure>

* 按照此流程依次添加模型

### API Key获取

* 点击侧栏最下方的`API Key管理`
* 创建API Key

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

* 创建成功后，点击创建好的API Key后的小眼睛打开并复制

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

* 将复制的API Key填入到CherryStudio当中后，打开服务商开关就可以使用了。

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>



### API地址

API地址有两种写法

* 第一种为客户端默认的:`https://ark.cn-beijing.volces.com/api/v3/`
* 第二种写法为:`https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
两种写法没什么区别，保持默认即可，无需修改。

关于`/`和`#`结尾的区别参考文档服务商设置的API地址部分，[点击前往](https://docs.cherry-ai.com/cherry-studio/cherrystudio/preview/settings/providers#api-di-zhi)
{% endhint %}

