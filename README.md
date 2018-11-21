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

在config.py檔中更新各絕對路徑。

```
# config.py
username = 'SK帳號'
password = 'SK密碼'

# skype資料夾路徑
src = '/Users/apple/Library/Application Support/Skype/你的SK ID/main.db'

# 所要儲存之備份路徑
dst = '備份目錄位置'

# skyperious之main.py位置
skyperious_main_path = '~/../skyperious/main.py'

env_name = '虛擬環境名稱'

```

在skype_backup.sh檔中修改(以文字編輯器編輯)。
```

# skype_backup.sh
python sk_backup.py的絕對位置 &

```

### Step 5

將skype_backup.sh開啟方式更改為以終端機開啟。

接著透過以下指令將skype_backup.sh更改為可執行檔。
```
$ chmod -x skype_backup.sh的路徑
```

在修正完後，之後僅需在開機後點擊兩下此檔案，即可在背景程式內執行。(僅需開啟一次)

### Step 6

配置，定時合併備份資料庫任務

輸入以下指令後，會進入至vim編輯器來新增定時任務。
```
sudo crontab -e
```

進入編輯器後，輸入以下指令。(此指令代表著每天的11點會執行。)
```
0 11 * * * merge_skype_db.py的絕對位置
```
