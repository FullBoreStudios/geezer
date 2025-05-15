# Geezer

**Old-school logging for stylish devs.**  
Use `print()` with ✨ taste and purpose — with color, emoji, memory, and style.

[![PyPI version](https://badge.fury.io/py/geezer.svg)](https://pypi.org/project/geezer/)

---

<p align="center">
  <img src="logo.png" alt="Geezer Logo" style="max-height: 250px;">
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

### ✅ Basic
```python
from geezer import prnt

prnt("Fetching user info")
```

### 🎯 With emoji
```python
prnt("Loading cart", "🛒")
```

### 🏷️ With emoji + label
```python
prnt("Card validated", "✅", "card check")
```

### 🔒 Always show (even in production)
```python
prnt("Email sent to customer", "✉️", "notification", "ok")
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
from geezer import warn
warn("User has no saved card", "user check")
```

### ⏱️ `timer()`
```python
from geezer import timer

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
prnt("API call failed due to timeout")
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

Or override manually with `ok`.

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
Throw in a `prnt()`.  
Talk to yourself a little.

You earned it, geezer.
