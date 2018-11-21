# skype_recover_messages
新版Skype因訊息皆是同步雲端，導致刪除的訊息無法回復。因此本專案的目的為備份Skype歷史訊息並回復被刪除之訊息。

## Installation

### Step1

安裝skpy，詳情請見 https://github.com/Terrance/SkPy

```
pip install skpy
```

### Step 2

創建虛擬環境py2(python 2的環境)

```
$ conda create -n py2 python=2.7
$ source activate py2
```

進入虛擬環境後，安裝Skyperious，詳情請見https://suurjaak.github.io/Skyperious/

```
$ pip install wxpython
$ pip install skyperious
```

### Step 3

將本專案clone下後，請本專案之skyperious資料夾取代pip安裝之skyperious。

### Step 4

配置路徑

