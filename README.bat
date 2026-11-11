@echo off
:: 1. Fix the git reference issue for README.md
git rm --cached README.md
git reset HEAD README.md

:: 2. Pull down the remote changes from GitHub (merging them safely)
git pull origin main --allow-unrelated-histories

:: 3. Stage your latest changes (.gitignore and README.bat)
git add .

:: 4. Commit and push again
git commit -m "Sync repository and update ignore rules"
git push -u origin main