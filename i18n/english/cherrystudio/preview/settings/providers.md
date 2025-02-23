---
icon: cloud-check
---

# Provider Settings

This page is only an introduction to the interface functions. For configuration tutorials, please refer to the [Provider Configuration](https://app.gitbook.com/s/0Ut5BptC3t8CtSU1UWpM/pre-basic/providers) tutorial in the basic tutorials.

{% hint style="info" %}
* When using built-in providers, you only need to fill in the corresponding API keys.
* Different providers may have different names for API keys, such as Secret Key, Key, API Key, Token, etc., but they all refer to the same thing.
{% endhint %}

## API Key

In CherryStudio, a single provider supports multiple API Keys for polling usage. The polling method is a cyclic approach from the front to the back of the list.

* Separate multiple keys with <mark style="color:red;">English</mark> commas when adding them. See the example below:

```
sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
```

## API Address

When using built-in providers, you generally do not need to fill in the API address. If you need to modify it, please strictly follow the address provided in the official documentation.

> If the address provided by the provider is in the format of <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, you only need to fill in the root address part (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> The CherryStudio client will automatically append the remaining path (<mark style="background-color:green;">/v1/chat/completions</mark>). Failure to fill in as required may result in the inability to use it properly.

{% hint style="info" %}
Note: Most providers have unified routes for large language models, and generally, you do not need to perform the following operations. If the API path of the provider is v2, v3/chat/completions, or other versions, you can manually enter the corresponding version ending with "`/`" in the address bar. When the provider's request route is not the conventional <mark style="background-color:green;">/v1/chat/completions</mark>, use the complete address provided by the provider ending with "`#`".

That is:

* When the API address ends with "`/`", only "<mark style="background-color:green;">chat/completions</mark>" is appended.
* When the API address ends with "`#`", no appending operation is performed, and only the entered address is used.
{% endhint %}

## Add Model

Generally, clicking the <mark style="background-color:green;">Manage</mark> button in the lower left corner of the provider configuration page will automatically retrieve all models supported by the provider. Click the "+" sign in the retrieved list to add them to the model list.

> Note: The models in the pop-up list when you click the Manage button need to be added to the model list on the provider configuration page by clicking the "+" sign after the model before they can appear in the model selection list.

## Connectivity Check

Click the check button after the API Key input box to test if the configuration is successful.

{% hint style="info" %}
The model check defaults to using the last dialogue model added in the model list. If there are failures during the check, please check if there are incorrect or unsupported models in the model list.
{% endhint %}

{% hint style="danger" %}
After successful configuration, be sure to turn on the switch in the upper right corner; otherwise, the provider will still be in an unenabled state, and the corresponding models cannot be found in the model list.
{% endhint %}
