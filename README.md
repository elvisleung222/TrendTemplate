### Run time
HKEX: 2554 stocks processed: ~10 minutes

NYSE: to be tested

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

Logs Location: `/var/log/pythonLog2`

#### **Remark:**
- All paths in crontab need to be absolute path.


TODO:
- [ ] HKEX, NYSE lists are input as python option
- [ ] Datatable supports both HKEX and NYSE
