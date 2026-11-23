#!/usr/bin/env python3
"""Builds the ShortcutManager website: index.html (language redirect) and <lang>/index.html, privacy.html, support.html.

All text lives in TEXT below (English and Korean). Run after changing it:  python3 build.py
The pages are plain static files for GitHub Pages (https://archivelab-kr.github.io/shortcutmanager/)."""
import html
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://archivelab-kr.github.io/shortcutmanager"
STORE = "https://apps.apple.com/app/id1469338310"
MAIL = "archivelabapps@gmail.com"
LANGS = {"en": "English", "ko": "한국어"}
UPDATED = {"en": "November 24, 2026", "ko": "2026년 11월 24일"}

TEXT = {
    "en": {
        "tagline": "Command twice. Then one key.",
        "description": "ShortcutManager is a pie menu for your Mac: press Command twice and one of Q W E R A S D F opens your app, folder or file. One hand, two beats.",
        "lead": "Press Command twice and a pie of your favorite apps opens under the pointer. Press Q, W, E, R, A, S, D or F and the app is in front. One hand, two beats, no looking for icons.",
        "download": "Download on the Mac App Store", "requires": "macOS 14 or later · Apple silicon and Intel",
        "nav_support": "Support", "nav_privacy": "Privacy",
        "how": "How it works",
        "steps": [("Press Command twice", "Two quick taps of the left Command key open the pie where your pointer is. Holding the key, or using it in a shortcut like ⌘C, never opens it."),
                  ("Press the key on a slice", "Eight slices, eight keys under your left hand: Q W E R and A S D F. The app comes to the front. Press the same key again and it hides."),
                  ("Folders open once more", "Put a folder on a slice and its files appear on a second ring. One more key opens the file.")],
        "setup": "Set up in a minute",
        "setup_text": "The first time, the pie is filled with the apps you are using. In Settings you see the pie itself: click a slice and choose what goes there. Apps that are running are listed first.",
        "shortcut": "Any app, a shortcut of its own",
        "shortcut_text": "Besides the pie, any app can have its own global shortcut. ShortcutManager tells you when it collides with a macOS shortcut or with another of your apps. Shortcuts from ShortcutManager 1.0 are carried over.",
        "price": "Free, and one purchase",
        "price_items": ["Free: three slices of the pie (Q, W, E) and one shortcut of your own.",
                        "One purchase, once, unlocks all eight slices and as many shortcuts as you like.", "No subscription. No account."],
        "private": "Private by design",
        "private_text": "The app asks for no permission at all: no Accessibility, no Input Monitoring, no Screen Recording. What is on your pie stays on your Mac.",
        "private_link": "Read the privacy policy",
        "footer": "© 2026 ArchiveLab",
        "privacy_title": "Privacy policy", "updated": "Last updated",
        "privacy_lead": "ShortcutManager keeps your setup on your Mac. This page explains what the app stores, what it sends, and how to turn sending off.",
        "privacy": [
            ("What stays on your Mac", ["What is on your pie, your shortcuts and your settings are saved on your Mac only, inside the app's own folder.",
                                        "For a folder or file you put on the pie, the app keeps a bookmark macOS gives it so it can open that folder or file again. It does not read or copy other files.",
                                        "There is no account and no sync. Nothing of the above is sent to us or to anyone else."]),
            ("What is sent", ["To find and fix problems, the app sends anonymous crash reports and usage statistics through Google's Firebase (Crashlytics and Analytics).",
                              "This includes: crash details, which features are used (for example that the pie was opened or a slice was changed, and the number of the slice), the app version, the macOS version, the Mac model, the language and the country, and a random ID for this installation.",
                              "It never includes: the names of your apps, folders or files, your shortcuts, or anything you type.",
                              "The data is not linked to your identity, is not used to track you across apps or websites, and is not sold or used for advertising."]),
            ("Turning it off", ["Open Settings › General and switch off \"Send anonymous crash reports and usage statistics\". From then on the app sends nothing."]),
            ("Purchases", ["The purchase that unlocks all slices is handled by Apple. We do not receive your name, your Apple Account or your payment details; the app only learns whether the purchase is active."]),
            ("Permissions", ["The app does not ask for Accessibility, Input Monitoring, Screen Recording or any other permission. It notices the Command key being tapped twice through the modifier-key state macOS reports; it cannot see what you type."]),
            ("Children", ["The app is not directed at children and collects no personal information from anyone."]),
            ("Changes and contact", ["If this policy changes, the new version is posted here with a new date.", f"Questions: {MAIL}"]),
        ],
        "support_title": "Support",
        "support_lead": f"Write to <a href=\"mailto:{MAIL}\">{MAIL}</a> and we'll help. Please include your macOS version and what you were doing when the problem happened.",
        "faq": [
            ("The pie does not open", "Tap the left Command key twice, quickly, without pressing anything else. Holding the key does not count. You can choose another key in Settings › Options. Check that ShortcutManager is running: its icon is in the menu bar."),
            ("How do I change what is on a slice?", "Open Settings from the menu bar icon (or press comma while the pie is open). On the Pie tab, click a slice and choose an app, a folder or a file. \"Leave it empty\" clears it."),
            ("A shortcut is not accepted", "A shortcut needs Command or Control; macOS does not give apps from the App Store shortcuts with only Option or Shift. If nothing happens when you press the keys, another app is already using that combination."),
            ("Some slices show a lock", "Three slices (Q, W, E) and one shortcut are free. Choose a locked slice, or Settings › General › \"Unlock everything…\", to buy the unlock once."),
            ("I bought the unlock on another Mac", "Open the unlock window and choose \"Restore Purchase\" while signed in to the same Apple Account."),
            ("It is not running after I restart my Mac", "Switch on Settings › General › \"Open at login\"."),
            ("A folder or file slice stopped working", "The folder or file was moved or renamed. Click its slice in Settings and choose it again."),
            ("How do I hide the menu bar icon, and get back to Settings?", "Switch off Settings › General › \"Show in the menu bar\". Open ShortcutManager again from Finder or Spotlight to show Settings."),
            ("How do I remove the app?", "Quit ShortcutManager from its menu bar icon and move it from Applications to the Trash."),
        ],
    },
    "ko": {
        "tagline": "⌘ 두 번, 그리고 키 하나",
        "description": "ShortcutManager는 Mac용 파이 메뉴 런처입니다. Command를 두 번 누르고 Q W E R A S D F 중 하나를 누르면 앱 · 폴더 · 파일이 열립니다. 한 손으로, 두 박자에.",
        "lead": "Command를 두 번 누르면 자주 쓰는 앱이 담긴 파이가 커서 자리에 열립니다. Q, W, E, R, A, S, D, F 중 하나를 누르면 그 앱이 앞으로 옵니다. 한 손으로, 두 박자에, 아이콘을 찾지 않고.",
        "download": "Mac App Store에서 받기", "requires": "macOS 14 이상 · Apple Silicon과 Intel",
        "nav_support": "지원", "nav_privacy": "개인정보",
        "how": "쓰는 방법",
        "steps": [("Command를 두 번 누릅니다", "왼쪽 Command를 빠르게 두 번 누르면 커서 자리에 파이가 열립니다. 키를 길게 누르거나 ⌘C 같은 단축키로 쓸 때는 열리지 않습니다."),
                  ("칸에 적힌 키를 누릅니다", "여덟 칸에 왼손 자리의 키 여덟 개, Q W E R과 A S D F. 그 앱이 앞으로 옵니다. 같은 키를 한 번 더 누르면 숨습니다."),
                  ("폴더는 한 번 더 펼쳐집니다", "칸에 폴더를 넣으면 안의 파일이 바깥 고리에 나옵니다. 키를 하나 더 누르면 그 파일이 열립니다.")],
        "setup": "1분이면 끝나는 설정",
        "setup_text": "처음 실행하면 지금 쓰는 앱으로 파이가 채워져 있습니다. 설정에는 파이가 그대로 그려져 있어서, 칸을 누르고 넣을 것을 고르면 됩니다. 실행 중인 앱이 맨 위에 나옵니다.",
        "shortcut": "원하는 앱에 원하는 단축키",
        "shortcut_text": "파이와 별개로, 어느 앱에든 전용 전역 단축키를 줄 수 있습니다. macOS 단축키나 다른 앱의 단축키와 겹치면 알려 줍니다. ShortcutManager 1.0의 단축키는 그대로 이어받습니다.",
        "price": "무료와 한 번의 결제",
        "price_items": ["무료: 파이 세 칸(Q, W, E)과 전용 단축키 하나.", "한 번 결제하면 여덟 칸 전부와 전용 단축키를 원하는 만큼 쓸 수 있습니다.", "구독이 아닙니다. 계정도 없습니다."],
        "private": "개인정보를 지키는 설계",
        "private_text": "어떤 권한도 묻지 않습니다. 손쉬운 사용, 입력 모니터링, 화면 기록 권한이 필요 없습니다. 파이에 담은 것은 Mac에만 남습니다.",
        "private_link": "개인정보 처리방침 보기",
        "footer": "© 2026 ArchiveLab",
        "privacy_title": "개인정보 처리방침", "updated": "마지막 수정",
        "privacy_lead": "ShortcutManager는 설정을 Mac에만 보관합니다. 이 문서는 앱이 무엇을 저장하고, 무엇을 보내고, 보내기를 어떻게 끄는지 설명합니다.",
        "privacy": [
            ("Mac에만 남는 것", ["파이에 담은 것, 단축키, 설정은 Mac 안의 앱 전용 폴더에만 저장됩니다.",
                             "파이에 넣은 폴더나 파일은, 다시 열 수 있도록 macOS가 주는 북마크만 보관합니다. 다른 파일을 읽거나 복사하지 않습니다.",
                             "계정이 없고 동기화도 없습니다. 위 내용은 저희나 다른 누구에게도 보내지 않습니다."]),
            ("보내는 것", ["문제를 찾아 고치기 위해, 익명 충돌 보고와 사용 통계를 Google의 Firebase(Crashlytics, Analytics)로 보냅니다.",
                        "포함되는 것: 충돌 내용, 어떤 기능을 썼는지(예: 파이를 열었다, 칸을 바꿨다, 몇 번째 칸인지), 앱 버전, macOS 버전, Mac 모델, 언어와 국가, 이 설치를 구분하는 임의의 ID.",
                        "포함되지 않는 것: 앱 · 폴더 · 파일의 이름, 단축키, 입력한 내용.",
                        "이 데이터는 사용자의 신원과 연결되지 않으며, 다른 앱이나 웹사이트에 걸친 추적에 쓰이지 않고, 판매하거나 광고에 쓰지 않습니다."]),
            ("끄는 방법", ["설정 › 일반에서 '익명 충돌 보고와 사용 통계 보내기'를 끄면, 그때부터 아무것도 보내지 않습니다."]),
            ("구입", ["모든 칸을 여는 구입은 Apple이 처리합니다. 저희는 이름, Apple 계정, 결제 정보를 받지 않으며, 앱은 구입이 유효한지만 압니다."]),
            ("권한", ["손쉬운 사용, 입력 모니터링, 화면 기록을 비롯한 어떤 권한도 요청하지 않습니다. Command를 두 번 누른 것은 macOS가 알려 주는 수식 키 상태로 알아채며, 입력하는 글자는 볼 수 없습니다."]),
            ("어린이", ["어린이를 대상으로 한 앱이 아니며, 누구에게서도 개인정보를 수집하지 않습니다."]),
            ("변경과 문의", ["이 방침이 바뀌면 새 날짜와 함께 이 페이지에 올립니다.", f"문의: {MAIL}"]),
        ],
        "support_title": "지원",
        "support_lead": f"<a href=\"mailto:{MAIL}\">{MAIL}</a>로 보내 주시면 도와 드리겠습니다. macOS 버전과, 문제가 생겼을 때 무엇을 하고 있었는지 함께 적어 주세요.",
        "faq": [
            ("파이가 열리지 않습니다", "왼쪽 Command를 다른 키 없이 빠르게 두 번 누릅니다. 길게 누르는 것은 해당하지 않습니다. 설정 › 옵션에서 다른 키로 바꿀 수 있습니다. ShortcutManager가 실행 중인지도 확인해 주세요(메뉴 막대에 아이콘이 있습니다)."),
            ("칸에 넣은 것을 바꾸려면?", "메뉴 막대 아이콘에서 설정을 엽니다(파이가 열린 채 쉼표를 눌러도 됩니다). 파이 탭에서 칸을 누르고 앱 · 폴더 · 파일을 고릅니다. '비워 두기'를 누르면 비웁니다."),
            ("단축키가 지정되지 않습니다", "단축키에는 Command나 Control이 들어가야 합니다. macOS는 App Store 앱에 Option이나 Shift만으로 된 단축키를 주지 않습니다. 키를 눌러도 반응이 없으면 다른 앱이 그 조합을 이미 쓰고 있는 것입니다."),
            ("자물쇠가 붙은 칸이 있습니다", "세 칸(Q, W, E)과 전용 단축키 하나가 무료입니다. 잠긴 칸을 고르거나 설정 › 일반 › '전부 잠금 해제…'에서 한 번 결제하면 모두 열립니다."),
            ("다른 Mac에서 이미 결제했습니다", "같은 Apple 계정으로 로그인한 상태에서 잠금 해제 창의 '구입 복원'을 누릅니다."),
            ("Mac을 재시동하면 실행되지 않습니다", "설정 › 일반 › '로그인할 때 실행'을 켭니다."),
            ("폴더나 파일 칸이 동작하지 않습니다", "그 폴더나 파일이 옮겨졌거나 이름이 바뀐 것입니다. 설정에서 그 칸을 눌러 다시 골라 주세요."),
            ("메뉴 막대 아이콘을 숨기려면? 숨긴 뒤 설정은 어떻게 여나요?", "설정 › 일반 › '메뉴 막대에 보이기'를 끕니다. Finder나 Spotlight에서 ShortcutManager를 다시 열면 설정이 나옵니다."),
            ("앱을 지우려면?", "메뉴 막대 아이콘에서 ShortcutManager를 종료한 뒤, 응용 프로그램 폴더에서 휴지통으로 옮깁니다."),
        ],
    },
}

e = html.escape


def page(lang, name, title, description, body):
    t = TEXT[lang]
    path = "" if name == "index" else f"{name}.html"
    alternates = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}/{l}/{path}">\n' for l in LANGS)
    options = "".join(f'<option value="../{l}/{path or "./"}"{" selected" if l == lang else ""}>{n}</option>' for l, n in LANGS.items())
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{BASE}/{lang}/{path}">
{alternates}<link rel="alternate" hreflang="x-default" href="{BASE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ShortcutManager">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{BASE}/{lang}/{path}">
<meta property="og:image" content="{BASE}/assets/pie-{lang}.jpg">
<link rel="icon" type="image/png" href="../assets/favicon.png">
<link rel="apple-touch-icon" href="../assets/icon-256.png">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="top">
  <a class="brand" href="./"><img src="../assets/icon-256.png" alt="" width="34" height="34">ShortcutManager</a>
  <nav>
    <a href="support.html">{e(t["nav_support"])}</a>
    <a href="privacy.html">{e(t["nav_privacy"])}</a>
    <select aria-label="Language" onchange="location.href=this.value">{options}</select>
  </nav>
</header>
<main>
{body}
</main>
<footer><span>{e(t["footer"])}</span> · <a href="./">ShortcutManager</a> · <a href="support.html">{e(t["nav_support"])}</a> · <a href="privacy.html">{e(t["nav_privacy"])}</a></footer>
</body>
</html>
"""


def video(lang, name, label):
    return (f'<video class="demo" autoplay muted loop playsinline preload="metadata" poster="../assets/{name}-{lang}.jpg" aria-label="{e(label)}">'
            f'<source src="../assets/{name}-{lang}.mp4" type="video/mp4"></video>')


def home(lang):
    t = TEXT[lang]
    steps = "".join(f'<li><h3>{e(a)}</h3><p>{e(b)}</p></li>' for a, b in t["steps"])
    prices = "".join(f"<li>{e(p)}</li>" for p in t["price_items"])
    body = f"""<section class="hero">
  <h1>{e(t["tagline"])}</h1>
  <p class="lead">{e(t["lead"])}</p>
  <p><a class="button" href="{STORE}">{e(t["download"])}</a></p>
  <p class="small">{e(t["requires"])}</p>
  {video(lang, "pie", t["tagline"])}
</section>
<section><h2>{e(t["how"])}</h2><ol class="steps">{steps}</ol></section>
<section class="split"><div><h2>{e(t["setup"])}</h2><p>{e(t["setup_text"])}</p></div>
  <img src="../assets/settings-{lang}.jpg" alt="{e(t["setup"])}" loading="lazy" width="1440" height="900"></section>
<section><h2>{e(t["shortcut"])}</h2><p>{e(t["shortcut_text"])}</p>{video(lang, "shortcut", t["shortcut"])}</section>
<section class="cards"><div><h2>{e(t["price"])}</h2><ul>{prices}</ul></div>
  <div><h2>{e(t["private"])}</h2><p>{e(t["private_text"])}</p><p><a href="privacy.html">{e(t["private_link"])}</a></p></div></section>
<section class="hero"><p><a class="button" href="{STORE}">{e(t["download"])}</a></p></section>"""
    return page(lang, "index", f'ShortcutManager: {t["tagline"]}', t["description"], body)


def privacy(lang):
    t = TEXT[lang]
    sections = "".join(f"<h2>{e(h)}</h2>" + "".join(f"<p>{e(p)}</p>" for p in ps) for h, ps in t["privacy"])
    body = f'<article><h1>{e(t["privacy_title"])}</h1><p class="lead">{e(t["privacy_lead"])}</p>{sections}<p class="small">{e(t["updated"])}: {UPDATED[lang]}</p></article>'
    return page(lang, "privacy", f'{t["privacy_title"]} | ShortcutManager', t["privacy_lead"], body)


def support(lang):
    t = TEXT[lang]
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    body = f'<article><h1>{e(t["support_title"])}</h1><p class="lead">{t["support_lead"]}</p>{faq}</article>'
    return page(lang, "support", f'{t["support_title"]} | ShortcutManager', html.unescape(t["support_lead"]).split("<")[0] + MAIL, body)


INDEX = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ShortcutManager</title>
<meta name="description" content="{e(TEXT["en"]["description"])}">
<link rel="alternate" hreflang="en" href="{BASE}/en/">
<link rel="alternate" hreflang="ko" href="{BASE}/ko/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<link rel="icon" type="image/png" href="assets/favicon.png">
<script>
(function () {{
  var prefs = navigator.languages || [navigator.language || "en"], pick = "en";
  for (var i = 0; i < prefs.length; i++) {{ if (prefs[i].toLowerCase().indexOf("ko") === 0) {{ pick = "ko"; break; }} if (prefs[i].toLowerCase().indexOf("en") === 0) break; }}
  location.replace(pick + "/");
}})();
</script>
</head>
<body><p><a href="en/">English</a> · <a href="ko/">한국어</a></p></body>
</html>
"""

STYLE = """:root { --bg: #fffaf5; --text: #23181c; --muted: #6d5c62; --card: #ffffff; --line: #f0dfd8; --accent: #f0527c; --accent2: #ffa63d; }
@media (prefers-color-scheme: dark) { :root { --bg: #1b1517; --text: #f6ecee; --muted: #b9a7ad; --card: #261d20; --line: #3a2c30; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text); font: 17px/1.65 -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Segoe UI", sans-serif; word-break: keep-all; }
a { color: var(--accent); }
.top, main, footer { max-width: 980px; margin: 0 auto; padding: 0 20px; }
.top { display: flex; align-items: center; justify-content: space-between; padding-top: 18px; padding-bottom: 18px; gap: 12px; flex-wrap: wrap; }
.brand { display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 19px; color: var(--text); text-decoration: none; }
.brand img { border-radius: 8px; }
nav { display: flex; align-items: center; gap: 16px; }
nav a { color: var(--muted); text-decoration: none; }
nav select { font: inherit; font-size: 15px; padding: 4px 8px; border-radius: 8px; border: 1px solid var(--line); background: var(--card); color: var(--text); }
section, article { padding: 34px 0; }
.hero { text-align: center; }
h1 { font-size: clamp(34px, 6vw, 58px); line-height: 1.12; margin: 18px 0 14px; letter-spacing: -0.02em;
     background: linear-gradient(100deg, var(--accent2), var(--accent)); -webkit-background-clip: text; background-clip: text; color: transparent; }
article h1 { font-size: clamp(30px, 5vw, 44px); }
h2 { font-size: 26px; margin: 0 0 10px; letter-spacing: -0.01em; }
article h2 { font-size: 21px; margin-top: 30px; }
h3 { font-size: 19px; margin: 0 0 4px; }
.lead { font-size: 20px; color: var(--muted); max-width: 720px; margin: 0 auto 22px; }
article .lead { margin-left: 0; }
.small { font-size: 14px; color: var(--muted); }
.button { display: inline-block; padding: 14px 28px; border-radius: 999px; color: #fff; font-weight: 700; text-decoration: none;
          background: linear-gradient(100deg, var(--accent2), var(--accent)); box-shadow: 0 8px 24px rgba(240, 82, 124, .28); }
.demo, .split img { width: 100%; height: auto; border-radius: 18px; margin-top: 26px; box-shadow: 0 18px 50px rgba(120, 40, 60, .22); display: block; }
.steps { list-style: none; padding: 0; margin: 18px 0 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; counter-reset: step; }
.steps li { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 20px; counter-increment: step; }
.steps li::before { content: counter(step); display: inline-grid; place-items: center; width: 30px; height: 30px; border-radius: 50%; color: #fff; font-weight: 700; margin-bottom: 10px;
                    background: linear-gradient(100deg, var(--accent2), var(--accent)); }
.steps p, .cards p, .cards li { color: var(--muted); margin: 0; }
.split { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 28px; align-items: center; }
.split img { margin-top: 0; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
.cards > div { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 24px; }
.cards ul { margin: 0; padding-left: 20px; }
.cards p + p { margin-top: 10px; }
article { max-width: 720px; }
details { border-bottom: 1px solid var(--line); padding: 14px 0; }
summary { cursor: pointer; font-weight: 600; }
details p { color: var(--muted); margin: 8px 0 0; }
footer { padding-top: 26px; padding-bottom: 40px; color: var(--muted); font-size: 14px; border-top: 1px solid var(--line); margin-top: 30px; }
footer a { color: var(--muted); }
@media (prefers-reduced-motion: reduce) { video { display: none; } }
"""


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


write("index.html", INDEX)
write("assets/style.css", STYLE)
for lang in LANGS:
    write(f"{lang}/index.html", home(lang))
    write(f"{lang}/privacy.html", privacy(lang))
    write(f"{lang}/support.html", support(lang))
urls = [f"{BASE}/{lang}/{p}" for lang in LANGS for p in ("", "privacy.html", "support.html")]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built", 1 + 3 * len(LANGS), "pages")
