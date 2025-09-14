Node.js 安裝與使用指南
Node.js 是一個強大的 JavaScript 執行環境，經常用於開發網頁應用程式的後端伺服器，或是在本地端執行各種開發工具，例如我們在專案中用它來啟動一個本地伺服器。

一、Node.js 安裝教學
本教學以 Windows 上的 .msi 安裝檔為例。

下載安裝檔：
前往 Node.js 官方網站 下載最新版本的 .msi 安裝檔。建議選擇 LTS (長期支援版)，它更加穩定。

執行安裝程式：
雙擊下載的 .msi 檔案，啟動安裝精靈。

遵循安裝步驟：

在授權頁面，勾選 I accept the terms in the License Agreement。

在 Custom Setup (自訂安裝) 頁面，保持所有預設選項，這會確保 Node.js 核心與 npm (套件管理器) 都被安裝。

在最後的安裝頁面，您會看到一個名為 Tools for Native Modules 的選項。請務必勾選「Automatically install the necessary tools...」。

完成安裝：
點擊 Next 和 Install，等待安裝程式自動完成所有工具的安裝。

二、Node.js 使用教學
安裝完成後，您就可以在終端機 (Terminal) 或命令提示字元 (Command Prompt) 中使用 Node.js。

開啟終端機：
在 Windows 上，您可以按下 Windows + R，輸入 cmd，然後按下 Enter。

驗證安裝：
在終端機中輸入以下指令，如果成功，您將會看到版本號。這代表 Node.js 已成功安裝在您的電腦上。

Bash

node -v
npm -v
使用 http-server 啟動本地伺服器：
http-server 是一個輕量級的伺服器模組，非常適合用來測試您的網頁專案。

安裝 http-server： 由於它不是 Node.js 的內建功能，您需要先用 npm 全域安裝它一次。

Bash

npm install -g http-server
啟動伺服器：

使用 cd 指令進入您的專案資料夾。

輸入以下指令來啟動伺服器：

Bash

http-server
開啟網頁：
當伺服器啟動後，您會看到類似 http://127.0.0.1:8080 的網址。將此網址複製並貼到您的瀏覽器中，即可在本地伺服器環境中運行您的網頁。