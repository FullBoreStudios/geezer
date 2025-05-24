<table>
<tr>
<td>

# Geezer

**Old-school logging for stylish Python devs.**  
Built with Django in mind — but works anywhere `print()` does.

Use `print()` with ✨ taste and purpose — with color, emoji, and style.

<p>
  <a href="https://pypi.org/project/geezer/"><img src="https://badge.fury.io/py/geezer.svg" alt="PyPI version"></a>
  <img src="https://img.shields.io/pypi/pyversions/geezer.svg" alt="Python Versions">
  <img src="https://img.shields.io/badge/status-stable-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/log-style%20matters-hotpink.svg" alt="Style">
</p>

</td>
<td align="right" width="250">

<img src="logo.png" alt="Geezer Logo" height="200"/>

</td>
</tr>
</table>

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

### ✅ Custom print / log name
```python
from geezer import log as prnt

prnt("Loading NIBBLES.BAS", "🐍", "games")
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

## 📦 Dynamic Logging

Just like `print()`, you can log variables — but you **must** use an f-string or string concatenation to include dynamic content.

### ✅ Using f-strings

```python
snake_count = 3
log(f"User has {snake_count} snakes left", "🐍", "reptile-room")
```

### ✅ Multiple variables

```python
user = "ben"
count = 7
log(f"{user} collected {count} tickets", "🎟️", "cinema")
```

### ❌ Don’t do this:

```python
log("User has", "🐍", snake_count)  # ❌ This won't work like you expect
```

Use f-strings instead to keep it clean and readable.



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


<p align="center">
  <img src="screenshot.png" alt="Screen Shot">
</p>



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
- [ ] Framework agnostic setting for when to show geezer prints in production or dev
- [ ] Set custom / override auto emoji library

---

Pull up a chair.  
Throw in a `prnt()` or `log()`.  
Talk to yourself a little.

You earned it, geezer.
