@echo off
setlocal

set "repository-name=pdf-2-text"

echo [1/5] Initializing Git and configuring local user...
git init
git config user.name "catx-commits"
git config user.email "catx-commits@users.noreply.github.com"

echo [2/5] Staging and committing files...
git add pdf-2-text.py .gitignore
git commit -m "Add pdf-2-text.py and ignore rules"

echo [3/5] Configuring remote repository...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/catx-commits/%repository-name%.git
git branch -M main

echo [4/5] Staging any remaining project files...
git add .
git commit -m "Update project files"

echo [5/5] Pushing to GitHub...
git push -u origin main

echo ========================================================
echo Git setup and push completed successfully!
echo ========================================================
pause
endlocal