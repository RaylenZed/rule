# rule

自己维护的分流规则。按客户端分目录，同一套域名四种格式。

```
src/                  源，改这里
rule/Clash/           Mihomo / Clash Meta，yaml
rule/Stash/           Stash，.list
rule/Surge/           Surge，.list
rule/Shadowrocket/    小火箭，.list
```

漏了域名：改 `src/<软件>.yaml`，再跑 `python3 scripts/generate.py`。

## 现在有什么

| 文件 | 覆盖 |
| --- | --- |
| openai | ChatGPT / OpenAI / Sora |
| anthropic | Claude |
| xai | Grok / xAI |
| cursor | Cursor |
| copilot | GitHub / Microsoft Copilot |
| google-ai | Gemini / AI Studio / NotebookLM |

只收这个软件自己的域名。

## 订阅

Clash / Mihomo（`behavior: classical`）：

```
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Clash/openai.yaml
```

Stash / Surge / 小火箭：

```
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Stash/openai.list
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Surge/openai.list
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Shadowrocket/openai.list
```

jsDelivr 不稳就换 `testingcf.jsdelivr.net`。
