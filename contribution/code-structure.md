---
hidden: true
icon: code
---

# 代码结构

```yaml
...
├─ docs/ #文档目录
├─ resources/ #资源文件目录
├─ scripts/ #脚本文件目录
└─ src/ #主要源代码目录
    ├─main/ #主进程代码
    ├─preload/ #预加载脚本目录
    └─renderer/ #渲染进程代码
        ├─src/ #渲染进程的源代码
            ├─assets/ #资源文件
                ├─fonts/ #字体文件
                ├─images/ #头像等图片文件
                └─styles/ #样式文件
            ├─components/ #组件
            ├─config/ #配置文件
            ├─context/ #上下文
            ├─databases/ #数据库相关文件
            ├─hooks/ #自定义Hooks
            ├─i18n/ #国际化文件
            ├─pages/ #页面文件
            ├─providers/ #服务商相关配置
            ├─services/ #服务文件
            ├─store/ #状态管理文件
            ├─types/ #TypeScript类型定义文件
            ├─utils/ #工具函数
            ...
        ...
    ...
...

```
