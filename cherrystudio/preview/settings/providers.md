---
icon: cloud-check
---

# 服务商设置

当前页面仅做界面功能的介绍，配置教程可以参考基础教程中的[服务商配置](../../../pre-basic/providers/)教程。

{% hint style="info" %}
* 在使用内置服务商时只需要填写对应的秘钥即可；
* 不同服务商对秘钥的叫法可能有所不同，秘钥、Key、API Key、令牌等都指的是同一个东西。
{% endhint %}



### API 秘钥

在CherryStudio当中，单个服务商支持多Key轮询使用，轮询方式为从前到后列表循环的方式。

* 多Key用<mark style="color:red;">英文</mark>逗号隔开添加。如以下示例方式：

```
sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
```



### API 地址

在使用内置服务商时一般不需要填写API地址，如果需要修改请严格按照官方文档给的地址填写。

> 如果服务商给的地址为<mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>这种格式，只需要填写根地址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）即可。
>
> CherryStudio客户端会自动拼接剩余的路径（<mark style="background-color:green;">/v1/chat/completions</mark>），未按要求填写可能会导致无法正常使用。

{% hint style="info" %}
特殊情况说明：如果服务商的API路径是v2、v3/chat/completions或者其他拼接方式时,可在地址栏手动输入对应版本以"/"结尾。

![](../../../.gitbook/assets/image.png)
{% endhint %}



### 连通性检查

点击API 秘钥输入框后的检查按钮即可测试是否成功配置。

{% hint style="danger" %}
配置成功后务必打开右上角的开关，否则该服务商仍处于未启用状态，无法在模型列表中找到对应模型。
{% endhint %}

