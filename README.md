# Geezer

**Old-school logging for stylish devs.**  
Use `print()` with ✨ taste and purpose — with color, emoji, memory, and style.

[![PyPI version](https://badge.fury.io/py/geezer.svg)](https://pypi.org/project/geezer/)

---

<p align="center">
  <img src="logo.png" alt="Geezer Logo" height="250">
</p>

---

## What is Geezer?

Geezer is a tiny Python logging helper that makes print-style debugging stylish, readable, and safe for dev environments.

Perfect for:
- Teaching or explaining complex code
- Debugging step-by-step logic
- Visual learners or neurodivergent-friendly workflows
- Looking good in the terminal 😎

It hides noise in production — unless you say otherwise.

---

## 🖥️ Terminal Support

Geezer looks best in terminals that support:

- **UTF-8** (for emoji output)
- **ANSI colors** (used by [`rich`](https://github.com/Textualize/rich))

✅ Recommended:
- Windows Terminal  
- macOS Terminal or iTerm2  
- Any modern Linux terminal  

⚠️ *Note:* PyCharm's terminal or legacy consoles may not render colors or emojis properly. Use an external terminal for full effect.

---

## Install

```bash
pip install geezer
```

📦 PyPI: [https://pypi.org/project/geezer/](https://pypi.org/project/geezer/)

---

## Usage

### ✅ Basic logging
```python
from geezer import log, warn, timer

log("Booting system", "⚙️", "startup")
```

### ⚠️ Warnings
```python
warn("No config file found", "config check")
```

### 🏷️ Tags & Emojis
```python
log("Launching rockets", "🚀", "deployment")
log("Inventory loaded", "📦", "warehouse")
log("Shields down! Taking damage!", "💥", "defense")
log("Poop scooped successfully", "💩", "can-doo")
```

### ⏱️ Timed blocks
```python
with timer("checkout flow"):
    run_checkout()
```

### 🧠 Log history
```python
from geezer import get_log_history

for entry in get_log_history():
    print(entry["timestamp"], entry["message"])
```

### 🤖 Auto-tagging
```python
import geezer.log
geezer.log.auto_tagging = True

log("Checkout complete")  # gets auto-tagged ✅
log("Payment gateway choked")  # auto-tagged 🤮
```

---

## More fun examples

```python
log("Connecting to mothership", "🛸", "api")
log("New customer signed up", "🧍", "user event")
log("Refresh token expired", "⏳", "auth")
log("Cache hit for homepage", "🧠", "performance")
log("Dark mode enabled", "🌚", "settings")
log("New dog uploaded to gallery", "🐶", "media")
log("Geezer initialized and logging like a pro", "🧓", "geezer-core")
log("New deal created", "🛒", "deal")
```

---

## Output Example

```text
[🛒 checkout] Starting checkout for user 42  
[✅ card validation] Card info validated  
[🔌 payment gateway] Calling Fortis API...  
[💰 payment] Transaction approved for $49.99  
[➡️ redirect] Redirecting to receipt page  
```

Styled with [rich](https://github.com/Textualize/rich) under the hood.

---

## ✨ Features

### 🟡 `warn()`
```python
warn("User has no saved card", "user check")
```

### ⏱️ `timer()`
```python
with timer("checkout process"):
    run_checkout()
```

### 🧠 Log history
```python
from geezer import get_log_history

logs = get_log_history()
for entry in logs:
    print(entry["timestamp"], entry["message"])
```

### 🤖 Auto-emoji
Enable auto-tagging:
```python
import geezer.log
geezer.log.auto_tagging = True
```

Now this:
```python
log("API call failed due to timeout")
```

Becomes:
```text
[❌ error] API call failed due to timeout
```

---

## Config

By default, `geezer` only prints in dev:
```env
DJANGO_DEBUG=True
```

Or override manually with `"ok"` as the last argument.

---

## Why “Geezer”?

Because sometimes the old ways are the best.  
Geezer gives you raw, readable feedback — with zero setup, and max personality.

---

## Roadmap

- [x] Console styling with `rich`  
- [x] Utility functions (`warn`, `timer`)  
- [x] Emoji + label tagging  
- [x] In-memory log history  
- [x] Auto emoji detection  
- [ ] File logging  
- [ ] Timestamp prefix toggle  
- [ ] Custom output backends (file, webhook, etc)  
- [ ] `geeze()` alias just for fun

---

Pull up a chair.  
Throw in a `prnt()` or `log()`.  
Talk to yourself a little.

You earned it, geezer.
