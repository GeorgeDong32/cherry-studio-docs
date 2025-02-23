---
icon: seal-question
description: Problems
---

# FAQ

## Common Error Codes

* **4xx (client error status code)**: Generally indicate that the request cannot be completed because of request syntax error, authentication failure, or authentication failure.
* **5xx (server error status code)**: generally server-side errors, server downtime, request processing timeout, etc.

<table><thead><tr><th>Error Status Code</th><th width="249">Possible Scenarios</th><th>Solution</th></tr></thead><tbody><tr><td>400</td><td>Wrong request format, etc.</td><td>Check the contents of the error returned by the dialog or <a href="faq.md#how-to-view-console-errors">the console</a> to see what is reported as an error, and follow the prompts.<br><mark style="color:purple;"><strong>[Common Case 1]</strong></mark>: If it is a <strong>Gemini</strong> model, you may need bind a card;<br><mark style="color:purple;"><strong>[Common Case 2]</strong></mark>: Data volume exceeds the limit. Commonly in <strong>Visual Models</strong>, the image volume exceeds the upper limit of the upstream single request traffic will return the error code;<br><mark style="color:purple;"><strong>[Common Case 3]</strong></mark>: Add unsupported parameters or fill in the parameters incorrectly. Try to create a new pure assistant to test whether it is normal;<br><mark style="color:purple;"><strong>[Common Scenario 4]</strong></mark>: Context exceeds the limit, clear the context or create a new dialog or reduce the number of context entries.</td></tr><tr><td>401</td><td>Authentication failed: Model not supported or the server account is banned, etc.</td><td>Contact or check the status of the corresponding service provider's account</td></tr><tr><td>403</td><td>Operation not authorized</td><td>Act according to the error messages returned by the dialog or <a href="faq.md#how-to-view-console-errors">the console</a> error message prompts.</td></tr><tr><td>404</td><td>Resource not found</td><td>Checking request paths, etc.</td></tr><tr><td>429</td><td>Request rate limit reached</td><td>Request rate (TPM or RPM) has reached the limit, please try again after a while.</td></tr><tr><td>500</td><td>Internal server error, unable to complete request</td><td>Contact upstream service provider if persistent</td></tr><tr><td>501</td><td>The server does not support the requested function and cannot complete the request</td><td></td></tr><tr><td>502</td><td>A server working as a gateway or proxy receives an invalid response from a remote server when it tries to execute a request</td><td></td></tr><tr><td>503</td><td>The server is temporarily unable to process client requests due to overload or system maintenance. The length of the delay can be included in the server's Retry-After header information</td><td></td></tr><tr><td>504</td><td>Servers acting as gateways or proxies that do not get requests from remote servers in a timely manner</td><td></td></tr></tbody></table>

***



## How to View Console Errors

* Click on the CherryStudio client window and press the shortcut <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (Mac: <kbd>Command</kbd>+<kbd>Option</kbd>+<kbd>I</kbd>).

{% hint style="info" %}
- The currently active window must be a CherryStudio client window to bring up the console.&#x20;
- You need to open the console and then click on a request such as test or initiate a dialog to collect the request information.
{% endhint %}

In the pop-up console window, click <mark style="color:blue;background-color:orange;">`Network`</mark> → Click to view the last "<mark style="color:red;background-color:orange;">`completions`</mark>" (for errors encountered in dialogue, translation, model connectivity checks, etc.) or "generations" (_for errors encountered in drawing_) marked with a red <mark style="color:red;background-color:orange;">`×`</mark> at ② → Click <mark style="color:blue;background-color:orange;">`Response`</mark> to view the complete return content (the area in ④ in the image).

> If you can't determine the cause of the error, please send a screenshot of this screen to [the Official Communication Group](https://t.me/CherryStudioAI) for help.

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0Ut5BptC3t8CtSU1UWpM%2Fuploads%2FVjfmUQNESMgNJikCYwss%2Fimage.png?alt=media&#x26;token=d5bdfe72-6904-4319-b7c7-c01f13d828a6" alt=""><figcaption></figcaption></figure>

This checking method can be used to get error information not only during dialogs, but also during model testing, when adding knowledge bases, when painting, etc. In either case it is necessary to open the debugging window first and then perform the request operation to get the request information.

{% hint style="info" %}
The name in the Name (② above) column will be different in different scenarios.&#x20;

Dialog, translation, model checking: <mark style="color:red;">`completions`</mark>&#x20;

Painting: <mark style="color:red;">`generations`</mark>&#x20;

Knowledge base creation: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***



## Formula Not Rendered / Formula Rendering Error

* Check if the formula has delimiters when the formula code is displayed directly instead of being rendered.

> **Usage of delimiter**
>
> _Inline formula_
>
> * Use a single dollar sign: `$formula$`
> * Or use `\(` and `\)`: `\(formula\)`
>
> _Independent formula block_
>
> * Use double dollar symbols: `$$formula$$`&#x20;
> * Or use `\[formula\]`
> * Example: `$$\sum_{i=1}^n x_i$$`, $$\sum_{i=1}^n x_i$$

Formula rendering error/gibberishni commonly when the formula contains Chinese(CJK) content, try to switch the formula engine to KateX.

***



## Failed to Create Knowledge Base / Failed to Get Embedding Dimensions

1. Model state unavailable
2. Non-embedding model is used

{% hint style="danger" %}
Attention:

1. Embedding models, dialog models, drawing models, etc. have their own functions, and their request methods and return contents and structures are different, so please don't force other types of models to be used as embedded models;
2. CherryStudio will automatically categorize the embedding models in the embedding model list (as shown in the above figure). If the model is confirmed to be an embeding model but has not been categorized correctly, you can go to the model list and click on the Settings button at the back of the corresponding model to check the embedding option;
3. If you cannot confirm which models are embedding models, you can check the model information from the corresponding service provider.
{% endhint %}

***

## Model Cannot Recognize Images / Unable to Upload or Select Images

First, you need to confirm whether the model supports image recognition. CherryStudio categorizes popular models, and those with a small eye icon after the model name support image recognition.

Image recognition models will support uploading image files. If the model function is not correctly matched, you can find the model in the model list of the corresponding service provider, click the settings button after its name, and check the _image_ option.

You can find the specific information of the model from the corresponding service provider. Like embedding models, models that do not support vision do not need to enable the image function, and selecting the image option will have no effect.
