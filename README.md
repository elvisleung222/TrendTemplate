### Trend Template
Cover stocks in HKEX, NYSE and Nasdaq Exchanges. NYSE list includes stocks from Nasdaq as well. 

### Kill and Start Web Server
```shell script
pkill flask
nohup flask run --host=0.0.0.0 &
```

### Scheduled Job
- Generate a new list at 0000 eveyday
  - Argument 1: Project home directory, end with "/"
  - Argument 2: Exchange: NYSE / HKEX
```shell script
sudo python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/" "NYSE"
```

### Cron Tab
Edit
```shell script
sudo vim /etc/crontab
```

Run a python script
```shell script
0 0 * * * root /usr/bin/python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/" "HKEX" >> /var/log/TrendTemplateLogHKEX
0 6 * * * root /usr/bin/python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/" "NYSE" >> /var/log/TrendTemplateLogNYSE
```

Logs Location: `/var/log/TrendTemplateLogHKEX`

#### **Remark:**
- All paths in crontab need to be absolute path.

### Housekeeping
#### Update HKEX stock list
1. Download xlsx list from https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx
2. Open xlsx file, set a filter on row 3 (Data > Filter)
3. Set filters on
   - Category: `Equity`
   - Sub-Category: `Equity Securities (Main Board)`
4. Copy the first column (Stock Code), without the last one (80737)
5. Paste the codes to Sublime Text
   - Remove the first zero `09999` -> `9999` for all codes
   - Make it as a list with quotes and commas
```python
[
  "0001",
  "0002"
]
```
6. Copy and paste all codes to `TrendTemplate/HKEX` (~2168 rows)

#### Update NYSE/NASDAQ stock list
1. Download *TWO* lists from http://www.eoddata.com/download.aspx
2. Fill in data as below
   - Exchange: `New York Stock Exchange`
   - Format: `Spreadsheet (eg: Excel)`
   - Period: `End of Day`
3. Copy the first column (Symbol)
4. Paste the codes to Sublime Text
   - Make it as a list with quotes and commas
```python
[
  "DDD",
  "MMM"
]
```
5. Copy and paste all codes to `TrendTemplate/NYSE`

#### Clean up historical generated files
```shell script
rm -f /home/opc/TrendTemplate/history/*
```

### TODO:
- [x] HKEX, NYSE lists are input as python option
- [x] Datatable supports both HKEX and NYSE
- [x] Remove RSI_14 in rules
- [x] Filter fields with no data
- [ ] Check if pivot point occurs
- [ ] Notify when pivot point occurs
