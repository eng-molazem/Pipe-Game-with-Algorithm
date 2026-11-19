# Pipe Game

**🇬🇧 [English](#-english) | 🇸🇦 [العربية](#-العربية)**

---

## 🇬🇧 English

### Overview

**Pipe Game** is a 2D puzzle game built with Python and Pygame, where the player connects pipe pieces to create a continuous path for water flow. The goal is to rotate and place pipe tiles correctly so that all pipes are connected and water can move through the entire system.

### Gameplay

- Rotate pipe pieces to connect them correctly.
- Build a complete path for water to flow.
- Solve multiple puzzle levels, each introducing a new pipe layout.
- Skip and solve any level automatically by pressing the **N** key — the game uses search algorithms to find the solution.

### Game Challenge

- Pipes come in different shapes.
- Some pipes may already be fixed.
- You must find the correct orientation to complete the path.

### Features

- Puzzle-based gameplay.
- Multiple pipe types: straight, elbow, tee, and cross pipes.
- Multiple levels to solve.
- Visual pipe connection system.
- Simple and clean game interface.
- Automatic level solving with the **N** key using search algorithms.

### Project Structure

```
Pipe_Game/
│
├── pipe_game.py      # Main game file
├── Lvl1.txt          # Level 1 data
├── Lvl2.txt          # Level 2 data
├── Lvl3.txt          # Level 3 data
│
└── assets/           # Game images
    ├── straight_empty.png
    ├── straight_full.png
    ├── elbow_empty.png
    ├── elbow_full.png
    ├── tee_empty.png
    ├── tee_full.png
    ├── cross_empty.png
    ├── cross_full.png
    └── stone.png
```

### Getting Started

#### Requirements
- Python 3
- Pygame

#### Install the dependency

```bash
pip install pygame
```

#### Run the game

```bash
python pipe_game.py
```

### Goal

Rotate and place the pipe pieces so that all pipes connect correctly and create a continuous flow path. Complete each level manually by solving the pipe puzzle, or press **N** to solve any level automatically using search algorithms.

### License

This project is open source and free to use under the MIT License.

### Author

**Mohammad Molazem** — [GitHub](https://github.com/eng-molazem) · [LinkedIn](https://www.linkedin.com/in/mohammad-molazem/)

---

## 🇸🇦 العربية

### نظرة عامة

**Pipe Game** لعبة ألغاز ثنائية الأبعاد مبنية بلغة Python ومكتبة Pygame، حيث يصل اللاعب قطع الأنابيب لإنشاء مسار متصل لتدفّق الماء. الهدف هو تدوير وتموضع بلاطات الأنابيب بشكل صحيح بحيث تتصل جميع الأنابيب ويمكن للماء التحرّك عبر النظام بأكمله.

### طريقة اللعب

- دوّر قطع الأنابيب لتوصيلها بشكل صحيح.
- ابنِ مساراً كاملاً لتدفّق الماء.
- حلّ عدة مستويات من الألغاز، كل مستوى يقدّم تخطيط أنابيب جديداً.
- تجاوز وحل أي مستوى تلقائياً بالضغط على مفتاح **N** — تستخدم اللعبة خوارزميات بحث لإيجاد الحل.

### تحدّي اللعبة

- تأتي الأنابيب بأشكال مختلفة.
- بعض الأنابيب قد تكون ثابتة مسبقاً.
- يجب إيجاد الاتجاه الصحيح لإكمال المسار.

### المزايا

- أسلوب لعب قائم على الألغاز.
- أنواع متعددة من الأنابيب: مستقيمة، كوع، تي، وتقاطع.
- مستويات متعددة للحل.
- نظام اتصال بصري للأنابيب.
- واجهة لعبة بسيطة ونظيفة.
- حل تلقائي للمستوى بمفتاح **N** باستخدام خوارزميات البحث.

### بنية المشروع

```
Pipe_Game/
│
├── pipe_game.py      # ملف اللعبة الرئيسي
├── Lvl1.txt          # بيانات المستوى 1
├── Lvl2.txt          # بيانات المستوى 2
├── Lvl3.txt          # بيانات المستوى 3
│
└── assets/           # صور اللعبة
    ├── straight_empty.png
    ├── straight_full.png
    ├── elbow_empty.png
    ├── elbow_full.png
    ├── tee_empty.png
    ├── tee_full.png
    ├── cross_empty.png
    ├── cross_full.png
    └── stone.png
```

### التشغيل محلياً

#### المتطلبات
- Python 3
- Pygame

#### تثبيت المتطلبات

```bash
pip install pygame
```

#### تشغيل اللعبة

```bash
python pipe_game.py
```

### الهدف

دوّر وضع قطع الأنابيب بحيث تتصل جميعها بشكل صحيح وتُنشئ مسار تدفّق متواصلاً. أكمل كل مستوى يدوياً بحل لغز الأنابيب، أو اضغط **N** لحل أي مستوى تلقائياً باستخدام خوارزميات البحث.

### الترخيص

هذا المشروع مفتوح المصدر ومجاني للاستخدام بموجب رخصة MIT.

### المطوّر

**محمد ملازم** — [GitHub](https://github.com/eng-molazem) · [LinkedIn](https://www.linkedin.com/in/mohammad-molazem/)
