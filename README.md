### Trend Template
Cover stocks in HKEX, NYSE and Nasdaq Exchanges. NYSE list includes stocks from Nasdaq as well. 

### Kill and Start Web Server
```shell script
cd /home/opc/TrendTemplate
git pull
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
# 10 AM GMT; 6 PM HKT
0 10 * * * root /usr/bin/python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/" "HKEX" >> /var/log/TrendTemplateLogHKEX
# 4 AM GMT; 12 PM HKT
0 4 * * * root /usr/bin/python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/" "NYSE" >> /var/log/TrendTemplateLogNYSE
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

#### Update NYSE / NASDAQ stock list
1. Download *TWO* lists from http://www.eoddata.com/download.aspx (in case forget password, search email from `support@eoddata.com`)
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
- [x] Check if pivot point occurs
- [x] Add a small chart image to every row for quick reference
- [ ] Data point: 'sector', 'longBusinessSummary'
- [ ] Make a good route to the page, e.g. /cheetah
- [ ] ! Add more Pivot Zone test cases to cover
- [ ] Mouse over to display a summary of the stock
- [ ] Filter: Slope of MA_200 in 1,2,3,4,5 month is greater than zero
- [ ] Filter: Price > $10
- [ ] Filter: volume is too low
- [ ] Notify when some criteria occurs
- [ ] Incorporate IBD RS as a filtering rule
- [ ] Add earnings, financials to consideration
- [ ] To map `cheetahlab.app` domain to the VM
- [ ] Configure port 80 instead of 5000
- [ ] Configure https settings 
