# 學商測驗分類爬蟲


## 用途
利用爬蟲建立自動作答程式，爬取 Manpowergroup 網站上的 Learnability Quotient 測驗，利用大量搜集的結果回推該測驗背後的分類模型。


## 開發重點
#### 測驗網址
https://www.manpowergroup.com/workforce-insights/expertise/learnability-quotient

#### 架構
1. 產生測驗答案組合
2. 將答案組合回傳至該網站
3. 爬取分類結果
4. 根據分類結果回推，重建分類模型