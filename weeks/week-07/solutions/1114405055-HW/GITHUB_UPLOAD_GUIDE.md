# 三國武將遊戲 - GitHub 上傳指南

## 快速指南：上傳到 GitHub Pull Request

### 第 1 步：配置 Git 用户信息

```powershell
git config --global user.name "d14405055-hsieh"
git config --global user.email "d14405055@ems.npu.edu.tw"
```

驗證配置：
```powershell
git config --global user.name
git config --global user.email
```

---

### 第 2 步：添加 Remote（如果還沒有）

檢查現有的 remote：
```powershell
git remote -v
```

如果沒有 origin，或需要更改倉庫地址：
```powershell
git remote add origin https://github.com/DevSecOpsLab-CSIE-NPU/2026-python.git
```

或者更新現有 origin：
```powershell
git remote set-url origin https://github.com/DevSecOpsLab-CSIE-NPU/2026-python.git
```

---

### 第 3 步：創建新分支（推薦方式）

```powershell
git checkout -b feature/sanguo-warlords-game
```

或使用你的學號：
```powershell
git checkout -b 1114405055/sanguo-game
```

---

### 第 4 步：添加遊戲文件到 Git

添加所有遊戲文件：
```powershell
git add chibi_warlords_game.py generals.txt battles.txt launch_game.bat README_GAME.md
```

驗證要提交的文件：
```powershell
git status
```

---

### 第 5 步：提交代碼

```powershell
git commit -m "feat: Add Chibi Three Kingdoms Warlords game

- Implemented turn-based battle system
- Added animated sprites with combat effects
- Supports single-player (easy/hard modes) and local duel mode
- Includes desktop launcher and comprehensive documentation
- Student ID: 1114405055"
```

---

### 第 6 步：推送到遠程倉庫

推送你的分支：
```powershell
git push -u origin feature/sanguo-warlords-game
```

或：
```powershell
git push -u origin 1114405055/sanguo-game
```

---

### 第 7 步：在 GitHub 上創建 Pull Request

1. 訪問: https://github.com/DevSecOpsLab-CSIE-NPU/2026-python
2. 點擊 **"Pull requests"** 選項卡
3. 點擊綠色的 **"New pull request"** 按鈕
4. 選擇你的分支作為 **compare** 分支
5. 填寫 PR 信息：
   - **Title**: "Add Chibi Three Kingdoms Warlords Game - Student 1114405055"
   - **Description**: 
     ```
     ## 遊戲概述
     三國武將迷你遊戲實現
     
     ## 功能
     - ✅ 回合制戰鬥系統
     - ✅ 動畫精靈與戰鬥特效
     - ✅ 單人模式（新手/老手難度）
     - ✅ 本地雙人對戰模式
     - ✅ 桌面快捷啟動器
     - ✅ 完整說明文檔
     
     ## 文件清單
     - chibi_warlords_game.py - 遊戲主程式
     - generals.txt - 武將數據
     - battles.txt - 戰役組成
     - launch_game.bat - 啟動器
     - README_GAME.md - 操作說明
     ```
6. 點擊 **"Create pull request"**

---

## 常見問題

### 問題 1：Pull request 失敗，顯示 Permission denied

**解決方案**：使用 Personal Access Token

1. 在 GitHub 上生成 Token：
   - 去 https://github.com/settings/tokens
   - 點 "Generate new token"
   - 選擇 "repo" 權限
   - 複製 token

2. 重新推送時使用 token：
   ```powershell
   git push -u origin feature/sanguo-warlords-game
   ```
   - 用户名：d14405055-hsieh
   - 密码：粘貼剛才複製的 token

### 問題 2：現有分支衝突

```powershell
git fetch origin
git rebase origin/main
git push -u origin feature/sanguo-warlords-game
```

### 問題 3：需要刪除錯誤的推送

```powershell
git push -u origin --delete feature/sanguo-warlords-game
```

---

## 驗證清單

- [ ] Git 用户名和郵箱已配置
- [ ] Remote 已指向正確的 GitHub 倉庫
- [ ] 已創建新分支
- [ ] 所有遊戲文件已添加
- [ ] 已提交 commit
- [ ] 已推送到遠程倉庫
- [ ] GitHub 上看到新分支和 Pull Request
- [ ] Pull Request 標題清晰，描述完整

---

## 後續步驟

1. **等待 Code Review**：教授/TA 會審查你的代碼
2. **回應反饋**：如果有要求改進，在本地修改後重新推送
3. **合併 PR**：获得批准後，PR 將被合併到 main 分支

