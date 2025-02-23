---
icon: book-open-cover
---

# Knowledge Base Tutorial

In version 0.9.1, CherryStudio introduces the long-awaited knowledge base feature.

Below, we will present a step-by-step guide on how to use CherryStudio's knowledge base in detail.

## Adding Embedding Models

1. Find models in the model management service. You can quickly filter by clicking "Embedding";
2. Find the desired model and add it to My Models.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Creating a Knowledge Base

1. Knowledge Base Entry: In the CherryStudio toolbar on the left, click the knowledge base icon to enter the management page;
2. Add Knowledge Base: Click "Add" to start creating a knowledge base;
3. Naming: Enter the name of the knowledge base and add an embedding model. Taking bge-m3 as an example, you can complete the creation.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Adding Files and Vectorizing

1. Add Files: Click the "Add Files" button to open the file selection dialog;
2. Select Files: Choose supported file formats such as pdf, docx, pptx, xlsx, txt, md, mdx, etc., and open them;
3. Vectorization: The system will automatically perform vectorization. When "Completed" (green ✓) is displayed, it indicates that vectorization is complete.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Adding Data from Multiple Sources

CherryStudio supports multiple ways to add data:

1. Folder Directory: You can add an entire folder directory. Files in supported formats under this directory will be automatically vectorized;
2. Website Link: Supports website URLs, such as [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Sitemap: Supports sitemap in xml format, such as [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Plain Text Notes: Supports entering custom content in plain text.

{% hint style="info" %}
Hints:

1. Illustrations in the imported knowledge base documents are temporarily not supported for conversion to vectors and need to be manually converted to text;
2. Using a website URL as a knowledge base source may not always be successful. Some websites have strict anti-scraping mechanisms (or require login, authorization, etc.), so this method may not be able to obtain accurate content. It is recommended to test search after creation.
3. Generally, websites provide sitemaps. For example, CherryStudio's [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). In most cases, you can get relevant information by adding `/sitemap.xml` after the root address of the website (i.e., URL). For example, `aaa.com/sitemap.xml`.
4. If the website does not provide a sitemap or the URLs are complex, you can create a sitemap xml file yourself. The file temporarily needs to be filled in using a direct link that is directly accessible on the public network. Local file links will not be recognized.

> 1) You can let AI generate sitemap files or have AI write a sitemap HTML generator tool;
> 2) Direct links can be generated using OSS direct links or cloud drive direct links, etc. If there is no ready-made tool, you can also go to the [ocoolAI](https://one.ocoolai.com/login) official website, log in and use the free file upload tool in the website top bar to generate direct links.
{% endhint %}

## Searching the Knowledge Base

Once files and other materials are vectorized, you can perform queries:

1. Click the "Search Knowledge Base" button at the bottom of the page;
2. Enter the content to be queried;
3. The search results are presented;
4. And the matching score of the result is displayed.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Generating Replies by Referencing the Knowledge Base in Conversations

1. Create a new topic. In the conversation toolbar, click "Knowledge Base". The list of created knowledge bases will expand. Select the knowledge base you need to reference;
2. Enter and send a question. The model will return an answer generated through retrieval results;
3. At the same time, the data source of the reference will be attached below the answer, allowing you to quickly view the source file.
