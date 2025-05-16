from time import perf_counter
from contextlib import contextmanager
from datetime import datetime
from rich import print as rprint

# In-memory log history
_log_history = []

# Optional auto-tagging (can be toggled)
auto_tagging = False


def prnt(message, *args):
    show_anyway = False
    emoji = ""
    label = ""

    for arg in args:
        if arg is True or arg == "ok":
            show_anyway = True
        elif isinstance(arg, str):
            if not emoji and len(arg) <= 3:
                emoji = arg
            elif not label:
                label = arg

    if auto_tagging and not emoji:
        emoji = auto_detect_emoji(message)

    if not show_anyway and not is_debug():
        return

    prefix = ""
    if emoji and label:
        prefix = f"[{emoji}\u2002{label}] "
    elif emoji:
        prefix = f"[{emoji}] "
    elif label:
        prefix = f"[{label}] "

    log_entry = {
        "timestamp": datetime.now(),
        "emoji": emoji,
        "label": label,
        "message": message,
        "full": f"{prefix}{message}"
    }
    _log_history.append(log_entry)
    if len(_log_history) > 1000:
        _log_history.pop(0)

    style = choose_style(label or emoji)
    rprint(f"[{style}]{prefix}[/]{message}")


def warn(message, *args):
    prnt(message, "⚠️", *args)


@contextmanager
def timer(label=""):
    start = perf_counter()
    yield
    duration = perf_counter() - start
    prnt(f"{label} took {duration:.4f}s", "⏱️", "timing")


def get_log_history():
    return _log_history


def is_debug():
    import os
    return os.environ.get("DJANGO_DEBUG", "True") == "True"


def auto_detect_emoji(message):
    lowered = message.lower()

    keywords = {
        ("error", "fail", "exception", "traceback", "bug"): "❌",
        ("success", "done", "complete", "finished", "passed"): "✅",
        ("payment", "charged", "transaction", "invoice", "billing"): "💰",
        ("api", "request", "response", "endpoint"): "🔌",
        ("load", "cart", "checkout", "order"): "🛒",
        ("db", "database", "query", "sql"): "🧠",
        ("user", "auth", "login", "signup", "register"): "🧍",
        ("cache", "hit", "miss", "memo"): "⚡",
        ("start", "boot", "init", "launch", "spawn"): "🚀",
        ("stop", "shutdown", "terminate", "kill"): "🛑",
        ("email", "mail", "inbox", "notify"): "📬",
        ("file", "upload", "download", "save", "read"): "📁",
        ("image", "photo", "gallery", "pic", "media"): "🖼",
        ("server", "host", "port", "listen", "socket"): "🖥",
        ("debug", "print", "trace", "check"): "🔍",
        ("timeout", "latency", "delay"): "⏳",
        ("retry", "reconnect", "attempt"): "🔁",
        ("event", "webhook", "trigger"): "🎯",
        ("config", "settings", "env", "var"): "⚙",
        ("test", "unit", "spec", "assert"): "🧪",
        ("deploy", "release", "version", "build"): "📦",
        ("log", "history", "record"): "📜"
    }

    for keys, emoji in keywords.items():
        if any(k in lowered for k in keys):
            return emoji.replace("\ufe0f\ufe0f", "")

    return "📄"  # fallback with clean spacing




def choose_style(tag):
    if any(term in tag.lower() for term in ["error", "fail"]):
        return "bold red"
    if any(term in tag.lower() for term in ["success", "done"]):
        return "bold green"
    if any(term in tag.lower() for term in ["api", "external"]):
        return "bold cyan"
    if any(term in tag.lower() for term in ["checkout", "cart"]):
        return "bold magenta"
    if any(term in tag.lower() for term in ["timing"]):
        return "dim"
    return "white"


def enable_auto_tagging():
    global auto_tagging
    auto_tagging = True
