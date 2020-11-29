### Run time
HKEX: 2554 stocks processed: ~10 minutes

NYSE: to be tested

### Kill and Start Web Server
```shell script
pkill flask & nohup flask run --host=0.0.0.0 &
```

### Scheduled Job
- Generate a new list at 0000 eveyday
  - Argument 1: Project home directory, end with "/"
```shell script
python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/"
```

### Cron Tab
Edit
```shell script
sudo vim /etc/crontab
```

Run a python script
```shell script
0 0 * * * root /usr/bin/python3 /home/opc/TrendTemplate/trendTemplateValidater.py "/home/opc/TrendTemplate/" >> /var/log/pythonLog2
```



TODO:
- [ ] HKEX, NYSE lists are input as python option
- [ ] Datatable supports both HKEX and NYSE
