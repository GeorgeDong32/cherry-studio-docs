---
icon: book
---

# Notion Configuration

Cherry Studio supports importing topics into Notion's database.



## Preparation

First you need to create a Notion database and [Notion Integration](https://www.notion.so/profile/integrations) and connect the Integration to the Notion database as shown in the following figure.

{% hint style="info" %}
Note: **The database must have a field with the same name as the "Page Title Field Name" in the settings, the default is Name, otherwise the import will fail.**
{% endhint %}

<figure><img src="https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-7cb8d22ae51aed3d84a933f4f3f46b9519608b49%252Fimage_notion1.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=c177adde&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-13ea6843ab118e0a3990a54934ff85b5114178c1%252Fimage_notion_5.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=df292629&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-eaa1caaec3dc2ee4c466b1818e00b341dababf7d%252Fimage_notion3.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=2ae3b577&#x26;sv=2" alt=""><figcaption></figcaption></figure>



Then you need to configure the Notion database ID and Notion key in Cherry Studio:&#x20;

If your Notion database URL looks something like this:

<mark style="color:blue;">https://www.notion.so/\<long\_hash\_1>?v=\<long\_hash\_2></mark>

So the Notion database ID is `<long_hash_1>` this part.&#x20;

Note that the "page title field name" here needs to be **the same as** the field name in the Notion database, otherwise it will cause import failure.

<figure><img src="https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-33e82ed40485f66c8ba787d7cf70990fa037a4a0%252Fimage_notion6.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=c45c3e7f&#x26;sv=2" alt=""><figcaption></figcaption></figure>

## Using



Right-click the topic and select \[Import to Notion].

<figure><img src="https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-98c014af17616993d271c3bc0b693b92c5be0837%252Fimage_notion_4.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=395eee1c&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.cherry-ai.com/~gitbook/image?url=https%3A%2F%2F3562065924-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F0Ut5BptC3t8CtSU1UWpM%252Fuploads%252Fgit-blob-dc4a87ca136780ad524d6bbb19325fb116a46e23%252Fimage_notion2.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=c35f5539&#x26;sv=2" alt=""><figcaption></figcaption></figure>
