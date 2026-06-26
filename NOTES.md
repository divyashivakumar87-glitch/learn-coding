# My Coding Notes 📒

My personal notes for learning to code. This is my own practice project — it is
completely separate from the team's `ats` repo, so I can experiment freely and
NOT affect anyone else's work.

---

## Where my stuff lives

- **On my Mac:**  `~/Documents/learn-coding`
- **On GitHub:**  https://github.com/divyashivakumar87-glitch/learn-coding

Both copies stay in sync when I `push` (see below).

---

## How to start coding again (do this each time)

1. Open the Terminal app.
2. Go to my project folder:
   ```
   cd ~/Documents/learn-coding
   ```
3. See my files:
   ```
   ls
   ```
4. Open them to edit (opens the folder in VS Code):
   ```
   code .
   ```

---

## The everyday loop (memorize this!)

```
edit  →  git add  →  git commit  →  git push
```

The exact commands (run from inside ~/Documents/learn-coding):

1. After editing & saving a file, see what changed:
   ```
   git status
   ```
2. Stage the change (mark it to be saved):
   ```
   git add hello.py
   ```
3. Commit (save a snapshot, with a note describing it):
   ```
   git commit -m "describe what I changed here"
   ```
4. Push (upload my saved commits to GitHub):
   ```
   git push
   ```
5. Refresh my GitHub page to see it online.

---

## Handy "what's going on?" commands

- `git status`          → What have I changed? Is everything saved?
- `git diff`            → Show exactly what lines I changed.
- `git log --oneline`   → My history of commits (saves).

---

## Important things I learned

- Saving a file in my editor is NOT the same as saving in git.
  Git only uploads what I `commit` and `push`.
- In Python 3, `print` needs parentheses:  `print("hello")`  ✅
  (Not `print "hello"` ❌ — that's an error.)
- To run a command MYSELF in the Claude chat, I start it with `!`
  Example:  ! git status

---

## How to run my Python program

```
python3 hello.py
```

---

## How to get the Claude chat assistant back

In the terminal, run:
```
claude --resume
```
Then pick this conversation from the list to continue where I left off.
(Or `claude --continue` to jump straight into my most recent chat.)
