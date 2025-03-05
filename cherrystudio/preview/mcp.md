---
icon: monero
---

# MCP

**MCP(Model Context Protocol)** 是一种开源协议，旨在以标准化的方式向大语言模型（LLM）提供上下文信息。更多关于 MCP 的介绍请见 [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## 在 Cherry Studio 中尝试使用 MCP

目前，MCP 在 Cherry Studio 中还处于测试阶段，但我们可以通过克隆主分支（main）来提前体验！下面以 `fetch` 功能为例，演示如何在 Cherry Studio 中使用 MCP，可以在[文档](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)中查找详情。

### **准备工作：安装 uv**

uv 是一个快速的 Python 包管理器，我们需要用它来安装 MCP Server。

*   **macOS/Linux 系统：**

    打开终端，运行以下命令：

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
*   **Windows 系统：**

    以管理员身份打开 PowerShell，运行以下命令：

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### **配置 Cherry Studio**&#x20;

<figure><img src="../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

1. 打开 Cherry Studio 设置。
2. 找到 "MCP Servers" 选项。
3. 点击 "Add Server"。
4. 将 MCP Server 的相关参数填入（[参考链接](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。可能需要填写的内容包括：
   * Server Name（服务器名称）：自定义一个名称，例如 `fetch-server`
   * Server URL（服务器地址）：MCP Server 的地址
   * （可能还有其他参数，视具体 Server 而定）
5. 点击“确定”保存。

{% hint style="success" %}
完成上述配置后，Cherry Studio 会自动下载所需的 MCP Server - `fetch server`。下载完成后，我们就可以开始使用了！
{% endhint %}

### **使用效果展示**

<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

从上图可以看出，结合了 MCP 的 `fetch` 功能后，Cherry Studio 能够更好地理解用户的查询意图，并从网络上获取相关信息，给出更准确、更全面的回答。

### **总结与展望**

随着各大 AI 客户端逐渐开始支持 MCP，相信 MCP 的应用范围会越来越广泛。Cherry Studio 作为一个积极拥抱前沿技术的开源项目，也在不断完善 MCP 相关功能。希望大家多多关注 Cherry Studio，一起见证 MCP 为 AI 带来的更多可能性！
