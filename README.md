# rule

自己维护的分流规则。按客户端分目录，同一套域名四种格式。

```
src/ai.yaml           源，改这里
rule/Clash/           Mihomo / Clash Meta，yaml
rule/Stash/           Stash，.list
rule/Surge/           Surge，.list
rule/Shadowrocket/    小火箭，.list
```

漏了域名：改 `src/ai.yaml`，再跑 `python3 scripts/generate.py`。

## 现在有什么

一份 AI 规则，覆盖 ChatGPT / OpenAI / Sora、Claude、Grok / xAI、Cursor、GitHub / Microsoft Copilot、Gemini / AI Studio / NotebookLM。

只收这些软件自己的域名。

## 订阅

Clash / Mihomo（`behavior: classical`）：

```
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Clash/AI.yaml
```

Stash / Surge / 小火箭：

```
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Stash/AI.list
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Surge/AI.list
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Shadowrocket/AI.list
```

jsDelivr 不稳就换 `testingcf.jsdelivr.net`。
