import yfinance as yf
from datetime import datetime
import re
import xlsxwriter
import json

stocks = [
    '0001',
    '0002',
    '0003',
    '0004',
    '0005',
    '0006',
    '0007',
    '0008',
    '0009',
    '0010',
    '0011',
    '0012',
    '0014',
    '0016',
    '0017',
    '0018',
    '0019',
    '0021',
    '0022',
    '0023',
    '0024',
    '0025',
    '0026',
    '0027',
    '0028',
    '0029',
    # '0030',
    # '0031',
    # '0032',
    # '0033',
    # '0034',
    # '0035',
    # '0036',
    # '0037',
    # '0038',
    # '0039',
    # '0040',
    # '0041',
    # '0042',
    # '0043',
    # '0045',
    # '0046',
    # '0047',
    # '0048',
    # '0050',
    # '0051',
    # '0052',
    # '0053',
    # '0055',
    # '0056',
    # '0057',
    # '0058',
    # '0059',
    # '0060',
    # '0061',
    # '0062',
    # '0063',
    # '0064',
    # '0065',
    # '0066',
    # '0067',
    # '0068',
    # '0069',
    # '0070',
    # '0071',
    # '0072',
    # '0073',
    # '0075',
    # '0076',
    # '0077',
    # '0078',
    # '0079',
    # '0080',
    # '0081',
    # '0082',
    # '0083',
    # '0084',
    # '0085',
    # '0086',
    # '0087',
    # '0088',
    # '0089',
    # '0090',
    # '0091',
    # '0092',
    # '0093',
    # '0094',
    # '0095',
    # '0096',
    # '0097',
    # '0098',
    # '0099',
    # '0100',
    # '0101',
    # '0102',
    # '0103',
    # '0104',
    # '0105',
    # '0106',
    # '0107',
    # '0108',
    # '0109',
    # '0110',
    # '0111',
    # '0112',
    # '0113',
    # '0114',
    # '0115',
    # '0116',
    # '0117',
    # '0118',
    # '0119',
    # '0120',
    # '0122',
    # '0123',
    # '0124',
    # '0125',
    # '0126',
    # '0127',
    # '0128',
    # '0129',
    # '0130',
    # '0131',
    # '0132',
    # '0133',
    # '0135',
    # '0136',
    # '0137',
    # '0138',
    # '0139',
    # '0141',
    # '0142',
    # '0143',
    # '0144',
    # '0145',
    # '0146',
    # '0147',
    # '0148',
    # '0149',
    # '0150',
    # '0151',
    # '0152',
    # '0153',
    # '0154',
    # '0155',
    # '0156',
    # '0157',
    # '0158',
    # '0159',
    # '0160',
    # '0162',
    # '0163',
    # '0164',
    # '0165',
    # '0166',
    # '0167',
    # '0168',
    # '0169',
    # '0171',
    # '0172',
    # '0173',
    # '0174',
    # '0175',
    # '0176',
    # '0177',
    # '0178',
    # '0179',
    # '0180',
    # '0181',
    # '0182',
    # '0183',
    # '0184',
    # '0185',
    # '0186',
    # '0187',
    # '0188',
    # '0189',
    # '0190',
    # '0191',
    # '0193',
    # '0194',
    # '0195',
    # '0196',
    # '0197',
    # '0198',
    # '0199',
    # '0200',
    # '0201',
    # '0202',
    # '0204',
    # '0205',
    # '0206',
    # '0207',
    # '0208',
    # '0209',
    # '0210',
    # '0211',
    # '0212',
    # '0213',
    # '0214',
    # '0215',
    # '0216',
    # '0217',
    # '0218',
    # '0219',
    # '0220',
    # '0222',
    # '0223',
    # '0224',
    # '0225',
    # '0226',
    # '0227',
    # '0228',
    # '0229',
    # '0230',
    # '0231',
    # '0232',
    # '0234',
    # '0235',
    # '0236',
    # '0237',
    # '0238',
    # '0239',
    # '0240',
    # '0241',
    # '0242',
    # '0243',
    # '0244',
    # '0245',
    # '0247',
    # '0248',
    # '0250',
    # '0251',
    # '0252',
    # '0253',
    # '0254',
    # '0255',
    # '0256',
    # '0257',
    # '0258',
    # '0259',
    # '0260',
    # '0261',
    # '0262',
    # '0263',
    # '0264',
    # '0265',
    # '0266',
    # '0267',
    # '0268',
    # '0269',
    # '0270',
    # '0271',
    # '0272',
    # '0273',
    # '0274',
    # '0275',
    # '0276',
    # '0277',
    # '0278',
    # '0279',
    # '0280',
    # '0281',
    # '0282',
    # '0285',
    # '0286',
    # '0287',
    # '0288',
    # '0289',
    # '0290',
    # '0291',
    # '0292',
    # '0293',
    # '0294',
    # '0295',
    # '0296',
    # '0297',
    # '0298',
    # '0299',
    # '0301',
    # '0302',
    # '0303',
    # '0305',
    # '0306',
    # '0307',
    # '0308',
    # '0309',
    # '0310',
    # '0311',
    # '0312',
    # '0313',
    # '0315',
    # '0316',
    # '0317',
    # '0318',
    # '0320',
    # '0321',
    # '0322',
    # '0323',
    # '0326',
    # '0327',
    # '0328',
    # '0329',
    # '0330',
    # '0331',
    # '0332',
    # '0333',
    # '0334',
    # '0335',
    # '0336',
    # '0337',
    # '0338',
    # '0339',
    # '0340',
    # '0341',
    # '0342',
    # '0343',
    # '0345',
    # '0346',
    # '0347',
    # '0348',
    # '0351',
    # '0352',
    # '0353',
    # '0354',
    # '0355',
    # '0356',
    # '0357',
    # '0358',
    # '0359',
    # '0360',
    # '0361',
    # '0362',
    # '0363',
    # '0364',
    # '0365',
    # '0366',
    # '0367',
    # '0368',
    # '0369',
    # '0370',
    # '0371',
    # '0372',
    # '0373',
    # '0374',
    # '0375',
    # '0376',
    # '0377',
    # '0378',
    # '0379',
    # '0380',
    # '0381',
    # '0382',
    # '0383',
    # '0384',
    # '0385',
    # '0386',
    # '0387',
    # '0388',
    # '0389',
    # '0390',
    # '0391',
    # '0392',
    # '0393',
    # '0395',
    # '0396',
    # '0397',
    # '0398',
    # '0399',
    # '0400',
    # '0401',
    # '0403',
    # '0406',
    # '0408',
    # '0410',
    # '0411',
    # '0412',
    # '0413',
    # '0416',
    # '0417',
    # '0418',
    # '0419',
    # '0420',
    # '0422',
    # '0423',
    # '0425',
    # '0426',
    # '0428',
    # '0430',
    # '0431',
    # '0432',
    # '0433',
    # '0434',
    # '0436',
    # '0438',
    # '0439',
    # '0440',
    # '0442',
    # '0444',
    # '0445',
    # '0449',
    # '0450',
    # '0451',
    # '0455',
    # '0456',
    # '0458',
    # '0459',
    # '0460',
    # '0462',
    # '0464',
    # '0465',
    # '0467',
    # '0468',
    # '0471',
    # '0472',
    # '0474',
    # '0475',
    # '0476',
    # '0479',
    # '0480',
    # '0482',
    # '0483',
    # '0484',
    # '0485',
    # '0486',
    # '0487',
    # '0488',
    # '0489',
    # '0491',
    # '0493',
    # '0495',
    # '0496',
    # '0497',
    # '0498',
    # '0499',
    # '0500',
    # '0503',
    # '0505',
    # '0506',
    # '0508',
    # '0509',
    # '0510',
    # '0511',
    # '0512',
    # '0513',
    # '0515',
    # '0517',
    # '0518',
    # '0519',
    # '0520',
    # '0521',
    # '0522',
    # '0524',
    # '0525',
    # '0526',
    # '0527',
    # '0528',
    # '0529',
    # '0530',
    # '0531',
    # '0532',
    # '0533',
    # '0535',
    # '0536',
    # '0538',
    # '0539',
    # '0540',
    # '0542',
    # '0543',
    # '0544',
    # '0546',
    # '0547',
    # '0548',
    # '0550',
    # '0551',
    # '0552',
    # '0553',
    # '0554',
    # '0555',
    # '0556',
    # '0557',
    # '0558',
    # '0559',
    # '0560',
    # '0563',
    # '0564',
    # '0565',
    # '0567',
    # '0568',
    # '0570',
    # '0571',
    # '0572',
    # '0573',
    # '0574',
    # '0575',
    # '0576',
    # '0577',
    # '0578',
    # '0579',
    # '0580',
    # '0581',
    # '0582',
    # '0583',
    # '0585',
    # '0586',
    # '0587',
    # '0588',
    # '0589',
    # '0590',
    # '0591',
    # '0592',
    # '0593',
    # '0595',
    # '0596',
    # '0598',
    # '0599',
    # '0600',
    # '0601',
    # '0602',
    # '0603',
    # '0604',
    # '0605',
    # '0607',
    # '0608',
    # '0609',
    # '0610',
    # '0611',
    # '0612',
    # '0613',
    # '0616',
    # '0617',
    # '0618',
    # '0619',
    # '0620',
    # '0621',
    # '0622',
    # '0623',
    # '0626',
    # '0627',
    # '0628',
    # '0629',
    # '0630',
    # '0631',
    # '0632',
    # '0633',
    # '0635',
    # '0636',
    # '0637',
    # '0638',
    # '0639',
    # '0640',
    # '0641',
    # '0643',
    # '0645',
    # '0646',
    # '0648',
    # '0650',
    # '0651',
    # '0653',
    # '0655',
    # '0656',
    # '0657',
    # '0658',
    # '0659',
    # '0660',
    # '0661',
    # '0662',
    # '0663',
    # '0665',
    # '0666',
    # '0667',
    # '0668',
    # '0669',
    # '0670',
    # '0672',
    # '0673',
    # '0674',
    # '0675',
    # '0676',
    # '0677',
    # '0678',
    # '0679',
    # '0680',
    # '0681',
    # '0682',
    # '0683',
    # '0684',
    # '0685',
    # '0686',
    # '0687',
    # '0688',
    # '0689',
    # '0690',
    # '0691',
    # '0693',
    # '0694',
    # '0695',
    # '0696',
    # '0697',
    # '0698',
    # '0699',
    # '0700',
    # '0701',
    # '0702',
    # '0703',
    # '0704',
    # '0706',
    # '0707',
    # '0708',
    # '0709',
    # '0710',
    # '0711',
    # '0712',
    # '0713',
    # '0715',
    # '0716',
    # '0717',
    # '0718',
    # '0719',
    # '0720',
    # '0721',
    # '0722',
    # '0723',
    # '0724',
    # '0725',
    # '0726',
    # '0727',
    # '0728',
    # '0729',
    # '0730',
    # '0731',
    # '0732',
    # '0733',
    # '0736',
    # '0737',
    # '0738',
    # '0743',
    # '0745',
    # '0746',
    # '0747',
    # '0750',
    # '0751',
    # '0752',
    # '0753',
    # '0754',
    # '0755',
    # '0756',
    # '0757',
    # '0758',
    # '0759',
    # '0760',
    # '0762',
    # '0763',
    # '0764',
    # '0765',
    # '0766',
    # '0767',
    # '0768',
    # '0769',
    # '0770',
    # '0771',
    # '0772',
    # '0775',
    # '0776',
    # '0777',
    # '0780',
    # '0784',
    # '0787',
    # '0788',
    # '0789',
    # '0794',
    # '0797',
    # '0798',
    # '0799',
    # '0800',
    # '0802',
    # '0803',
    # '0804',
    # '0806',
    # '0807',
    # '0809',
    # '0810',
    # '0811',
    # '0812',
    # '0813',
    # '0814',
    # '0815',
    # '0817',
    # '0818',
    # '0819',
    # '0821',
    # '0822',
    # '0825',
    # '0826',
    # '0827',
    # '0828',
    # '0829',
    # '0830',
    # '0831',
    # '0832',
    # '0833',
    # '0834',
    # '0836',
    # '0837',
    # '0838',
    # '0839',
    # '0840',
    # '0841',
    # '0842',
    # '0844',
    # '0845',
    # '0846',
    # '0848',
    # '0850',
    # '0851',
    # '0852',
    # '0853',
    # '0854',
    # '0855',
    # '0856',
    # '0857',
    # '0858',
    # '0859',
    # '0860',
    # '0861',
    # '0862',
    # '0863',
    # '0864',
    # '0865',
    # '0866',
    # '0867',
    # '0868',
    # '0869',
    # '0871',
    # '0872',
    # '0874',
    # '0875',
    # '0876',
    # '0878',
    # '0880',
    # '0881',
    # '0882',
    # '0883',
    # '0884',
    # '0885',
    # '0886',
    # '0887',
    # '0888',
    # '0889',
    # '0891',
    # '0893',
    # '0894',
    # '0895',
    # '0896',
    # '0897',
    # '0898',
    # '0899',
    # '0900',
    # '0901',
    # '0902',
    # '0904',
    # '0905',
    # '0906',
    # '0907',
    # '0908',
    # '0909',
    # '0910',
    # '0911',
    # '0912',
    # '0913',
    # '0914',
    # '0915',
    # '0916',
    # '0918',
    # '0919',
    # '0921',
    # '0922',
    # '0923',
    # '0924',
    # '0925',
    # '0926',
    # '0927',
    # '0928',
    # '0929',
    # '0931',
    # '0932',
    # '0934',
    # '0935',
    # '0936',
    # '0938',
    # '0939',
    # '0941',
    # '0943',
    # '0945',
    # '0947',
    # '0948',
    # '0950',
    # '0951',
    # '0952',
    # '0953',
    # '0954',
    # '0956',
    # '0959',
    # '0960',
    # '0966',
    # '0967',
    # '0968',
    # '0969',
    # '0970',
    # '0973',
    # '0974',
    # '0975',
    # '0976',
    # '0978',
    # '0979',
    # '0980',
    # '0981',
    # '0982',
    # '0983',
    # '0984',
    # '0985',
    # '0986',
    # '0987',
    # '0988',
    # '0989',
    # '0990',
    # '0991',
    # '0992',
    # '0993',
    # '0994',
    # '0995',
    # '0996',
    # '0997',
    # '0998',
    # '0999',
    # '1000',
    # '1001',
    # '1002',
    # '1003',
    # '1004',
    # '1005',
    # '1006',
    # '1007',
    # '1008',
    # '1009',
    # '1010',
    # '1011',
    # '1013',
    # '1019',
    # '1020',
    # '1022',
    # '1023',
    # '1025',
    # '1026',
    # '1027',
    # '1028',
    # '1029',
    # '1030',
    # '1031',
    # '1033',
    # '1034',
    # '1036',
    # '1037',
    # '1038',
    # '1039',
    # '1041',
    # '1043',
    # '1044',
    # '1045',
    # '1046',
    # '1047',
    # '1049',
    # '1050',
    # '1051',
    # '1052',
    # '1053',
    # '1055',
    # '1057',
    # '1058',
    # '1059',
    # '1060',
    # '1061',
    # '1062',
    # '1063',
    # '1064',
    # '1065',
    # '1066',
    # '1068',
    # '1069',
    # '1070',
    # '1071',
    # '1072',
    # '1073',
    # '1075',
    # '1076',
    # '1079',
    # '1080',
    # '1082',
    # '1083',
    # '1084',
    # '1085',
    # '1086',
    # '1087',
    # '1088',
    # '1089',
    # '1090',
    # '1091',
    # '1093',
    # '1094',
    # '1096',
    # '1097',
    # '1098',
    # '1099',
    # '1100',
    # '1101',
    # '1102',
    # '1103',
    # '1104',
    # '1105',
    # '1106',
    # '1107',
    # '1108',
    # '1109',
    # '1110',
    # '1111',
    # '1112',
    # '1113',
    # '1114',
    # '1115',
    # '1116',
    # '1117',
    # '1118',
    # '1119',
    # '1120',
    # '1121',
    # '1122',
    # '1123',
    # '1124',
    # '1125',
    # '1126',
    # '1127',
    # '1128',
    # '1129',
    # '1130',
    # '1131',
    # '1132',
    # '1133',
    # '1134',
    # '1137',
    # '1138',
    # '1139',
    # '1140',
    # '1141',
    # '1142',
    # '1143',
    # '1145',
    # '1146',
    # '1147',
    # '1148',
    # '1150',
    # '1152',
    # '1155',
    # '1156',
    # '1157',
    # '1158',
    # '1159',
    # '1160',
    # '1161',
    # '1162',
    # '1163',
    # '1164',
    # '1165',
    # '1166',
    # '1168',
    # '1169',
    # '1170',
    # '1171',
    # '1172',
    # '1173',
    # '1175',
    # '1176',
    # '1177',
    # '1178',
    # '1179',
    # '1180',
    # '1181',
    # '1182',
    # '1183',
    # '1184',
    # '1185',
    # '1186',
    # '1188',
    # '1189',
    # '1190',
    # '1191',
    # '1192',
    # '1193',
    # '1194',
    # '1195',
    # '1196',
    # '1198',
    # '1199',
    # '1200',
    # '1201',
    # '1202',
    # '1203',
    # '1205',
    # '1206',
    # '1207',
    # '1208',
    # '1210',
    # '1211',
    # '1212',
    # '1213',
    # '1215',
    # '1216',
    # '1217',
    # '1218',
    # '1219',
    # '1220',
    # '1221',
    # '1222',
    # '1223',
    # '1224',
    # '1225',
    # '1226',
    # '1227',
    # '1229',
    # '1230',
    # '1231',
    # '1232',
    # '1233',
    # '1234',
    # '1235',
    # '1237',
    # '1238',
    # '1239',
    # '1240',
    # '1241',
    # '1243',
    # '1245',
    # '1246',
    # '1247',
    # '1249',
    # '1250',
    # '1251',
    # '1252',
    # '1253',
    # '1255',
    # '1257',
    # '1258',
    # '1259',
    # '1260',
    # '1262',
    # '1263',
    # '1265',
    # '1266',
    # '1268',
    # '1269',
    # '1270',
    # '1271',
    # '1272',
    # '1273',
    # '1277',
    # '1278',
    # '1280',
    # '1281',
    # '1282',
    # '1283',
    # '1285',
    # '1286',
    # '1288',
    # '1289',
    # '1290',
    # '1292',
    # '1293',
    # '1296',
    # '1297',
    # '1298',
    # '1299',
    # '1300',
    # '1301',
    # '1302',
    # '1303',
    # '1305',
    # '1308',
    # '1310',
    # '1312',
    # '1313',
    # '1314',
    # '1315',
    # '1316',
    # '1317',
    # '1319',
    # '1321',
    # '1323',
    # '1326',
    # '1327',
    # '1328',
    # '1329',
    # '1330',
    # '1332',
    # '1333',
    # '1335',
    # '1336',
    # '1337',
    # '1338',
    # '1339',
    # '1340',
    # '1341',
    # '1343',
    # '1345',
    # '1346',
    # '1347',
    # '1348',
    # '1349',
    # '1353',
    # '1355',
    # '1357',
    # '1358',
    # '1359',
    # '1360',
    # '1361',
    # '1362',
    # '1363',
    # '1365',
    # '1366',
    # '1367',
    # '1368',
    # '1369',
    # '1370',
    # '1371',
    # '1372',
    # '1373',
    # '1375',
    # '1376',
    # '1378',
    # '1380',
    # '1381',
    # '1382',
    # '1383',
    # '1385',
    # '1386',
    # '1387',
    # '1388',
    # '1389',
    # '1393',
    # '1395',
    # '1396',
    # '1397',
    # '1398',
    # '1399',
    # '1400',
    # '1401',
    # '1402',
    # '1408',
    # '1410',
    # '1412',
    # '1415',
    # '1416',
    # '1417',
    # '1418',
    # '1419',
    # '1420',
    # '1421',
    # '1425',
    # '1427',
    # '1428',
    # '1429',
    # '1430',
    # '1431',
    # '1432',
    # '1433',
    # '1439',
    # '1442',
    # '1443',
    # '1446',
    # '1447',
    # '1448',
    # '1449',
    # '1450',
    # '1451',
    # '1452',
    # '1455',
    # '1456',
    # '1458',
    # '1459',
    # '1460',
    # '1461',
    # '1462',
    # '1463',
    # '1466',
    # '1468',
    # '1469',
    # '1470',
    # '1472',
    # '1475',
    # '1476',
    # '1477',
    # '1478',
    # '1480',
    # '1483',
    # '1486',
    # '1488',
    # '1492',
    # '1495',
    # '1496',
    # '1498',
    # '1499',
    # '1500',
    # '1501',
    # '1502',
    # '1508',
    # '1509',
    # '1513',
    # '1515',
    # '1518',
    # '1520',
    # '1521',
    # '1522',
    # '1523',
    # '1525',
    # '1526',
    # '1527',
    # '1528',
    # '1529',
    # '1530',
    # '1532',
    # '1533',
    # '1536',
    # '1538',
    # '1539',
    # '1540',
    # '1542',
    # '1543',
    # '1545',
    # '1546',
    # '1547',
    # '1548',
    # '1549',
    # '1551',
    # '1552',
    # '1553',
    # '1555',
    # '1556',
    # '1557',
    # '1558',
    # '1559',
    # '1560',
    # '1561',
    # '1563',
    # '1565',
    # '1566',
    # '1568',
    # '1569',
    # '1570',
    # '1571',
    # '1572',
    # '1573',
    # '1575',
    # '1576',
    # '1577',
    # '1578',
    # '1579',
    # '1580',
    # '1581',
    # '1582',
    # '1583',
    # '1585',
    # '1586',
    # '1587',
    # '1588',
    # '1589',
    # '1591',
    # '1592',
    # '1593',
    # '1596',
    # '1597',
    # '1598',
    # '1599',
    # '1600',
    # '1601',
    # '1606',
    # '1608',
    # '1609',
    # '1610',
    # '1611',
    # '1612',
    # '1613',
    # '1615',
    # '1616',
    # '1617',
    # '1618',
    # '1620',
    # '1621',
    # '1622',
    # '1623',
    # '1626',
    # '1627',
    # '1628',
    # '1629',
    # '1630',
    # '1631',
    # '1632',
    # '1633',
    # '1635',
    # '1636',
    # '1637',
    # '1638',
    # '1639',
    # '1640',
    # '1645',
    # '1647',
    # '1649',
    # '1650',
    # '1651',
    # '1652',
    # '1653',
    # '1655',
    # '1656',
    # '1657',
    # '1658',
    # '1659',
    # '1660',
    # '1661',
    # '1662',
    # '1663',
    # '1665',
    # '1666',
    # '1667',
    # '1668',
    # '1669',
    # '1671',
    # '1672',
    # '1673',
    # '1675',
    # '1676',
    # '1678',
    # '1679',
    # '1680',
    # '1681',
    # '1682',
    # '1683',
    # '1685',
    # '1686',
    # '1689',
    # '1690',
    # '1691',
    # '1692',
    # '1693',
    # '1695',
    # '1696',
    # '1697',
    # '1698',
    # '1699',
    # '1701',
    # '1702',
    # '1703',
    # '1705',
    # '1706',
    # '1707',
    # '1708',
    # '1709',
    # '1710',
    # '1711',
    # '1712',
    # '1713',
    # '1715',
    # '1716',
    # '1717',
    # '1718',
    # '1719',
    # '1720',
    # '1721',
    # '1722',
    # '1723',
    # '1725',
    # '1726',
    # '1727',
    # '1728',
    # '1729',
    # '1730',
    # '1731',
    # '1732',
    # '1733',
    # '1735',
    # '1736',
    # '1737',
    # '1738',
    # '1739',
    # '1740',
    # '1741',
    # '1742',
    # '1743',
    # '1745',
    # '1746',
    # '1747',
    # '1748',
    # '1749',
    # '1750',
    # '1751',
    # '1752',
    # '1753',
    # '1755',
    # '1756',
    # '1757',
    # '1758',
    # '1759',
    # '1760',
    # '1761',
    # '1762',
    # '1763',
    # '1765',
    # '1766',
    # '1767',
    # '1769',
    # '1771',
    # '1772',
    # '1773',
    # '1775',
    # '1776',
    # '1777',
    # '1778',
    # '1780',
    # '1781',
    # '1782',
    # '1783',
    # '1785',
    # '1786',
    # '1787',
    # '1788',
    # '1789',
    # '1790',
    # '1792',
    # '1793',
    # '1796',
    # '1797',
    # '1798',
    # '1799',
    # '1800',
    # '1801',
    # '1802',
    # '1803',
    # '1806',
    # '1808',
    # '1809',
    # '1810',
    # '1811',
    # '1812',
    # '1813',
    # '1815',
    # '1816',
    # '1817',
    # '1818',
    # '1820',
    # '1821',
    # '1822',
    # '1823',
    # '1825',
    # '1826',
    # '1827',
    # '1829',
    # '1830',
    # '1831',
    # '1832',
    # '1833',
    # '1835',
    # '1836',
    # '1837',
    # '1838',
    # '1839',
    # '1841',
    # '1842',
    # '1843',
    # '1845',
    # '1846',
    # '1847',
    # '1848',
    # '1849',
    # '1850',
    # '1851',
    # '1853',
    # '1854',
    # '1856',
    # '1857',
    # '1858',
    # '1859',
    # '1860',
    # '1861',
    # '1862',
    # '1863',
    # '1865',
    # '1866',
    # '1867',
    # '1868',
    # '1869',
    # '1870',
    # '1871',
    # '1872',
    # '1873',
    # '1875',
    # '1876',
    # '1877',
    # '1878',
    # '1882',
    # '1883',
    # '1884',
    # '1885',
    # '1886',
    # '1888',
    # '1889',
    # '1890',
    # '1891',
    # '1894',
    # '1895',
    # '1896',
    # '1897',
    # '1898',
    # '1899',
    # '1900',
    # '1901',
    # '1902',
    # '1903',
    # '1905',
    # '1906',
    # '1907',
    # '1908',
    # '1909',
    # '1910',
    # '1911',
    # '1912',
    # '1913',
    # '1915',
    # '1916',
    # '1917',
    # '1918',
    # '1919',
    # '1920',
    # '1921',
    # '1922',
    # '1925',
    # '1928',
    # '1929',
    # '1930',
    # '1931',
    # '1932',
    # '1933',
    # '1935',
    # '1936',
    # '1937',
    # '1938',
    # '1939',
    # '1941',
    # '1942',
    # '1943',
    # '1949',
    # '1950',
    # '1951',
    # '1952',
    # '1953',
    # '1955',
    # '1957',
    # '1958',
    # '1959',
    # '1960',
    # '1961',
    # '1962',
    # '1963',
    # '1966',
    # '1967',
    # '1968',
    # '1969',
    # '1970',
    # '1971',
    # '1972',
    # '1975',
    # '1977',
    # '1978',
    # '1979',
    # '1980',
    # '1981',
    # '1982',
    # '1983',
    # '1985',
    # '1986',
    # '1987',
    # '1988',
    # '1989',
    # '1990',
    # '1991',
    # '1992',
    # '1993',
    # '1995',
    # '1996',
    # '1997',
    # '1998',
    # '1999',
    # '2000',
    # '2001',
    # '2002',
    # '2003',
    # '2005',
    # '2006',
    # '2007',
    # '2008',
    # '2009',
    # '2010',
    # '2011',
    # '2012',
    # '2013',
    # '2014',
    # '2016',
    # '2017',
    # '2018',
    # '2019',
    # '2020',
    # '2022',
    # '2023',
    # '2025',
    # '2028',
    # '2030',
    # '2031',
    # '2033',
    # '2038',
    # '2039',
    # '2048',
    # '2051',
    # '2057',
    # '2060',
    # '2066',
    # '2068',
    # '2078',
    # '2080',
    # '2083',
    # '2086',
    # '2088',
    # '2096',
    # '2098',
    # '2099',
    # '2100',
    # '2101',
    # '2102',
    # '2103',
    # '2107',
    # '2108',
    # '2111',
    # '2112',
    # '2113',
    # '2115',
    # '2116',
    # '2118',
    # '2119',
    # '2120',
    # '2122',
    # '2123',
    # '2128',
    # '2130',
    # '2132',
    # '2133',
    # '2136',
    # '2138',
    # '2139',
    # '2163',
    # '2166',
    # '2168',
    # '2169',
    # '2178',
    # '2180',
    # '2181',
    # '2182',
    # '2183',
    # '2186',
    # '2188',
    # '2189',
    # '2193',
    # '2196',
    # '2198',
    # '2199',
    # '2202',
    # '2203',
    # '2208',
    # '2211',
    # '2212',
    # '2213',
    # '2218',
    # '2221',
    # '2222',
    # '2223',
    # '2225',
    # '2226',
    # '2227',
    # '2228',
    # '2230',
    # '2231',
    # '2232',
    # '2233',
    # '2236',
    # '2238',
    # '2239',
    # '2255',
    # '2258',
    # '2262',
    # '2263',
    # '2266',
    # '2268',
    # '2269',
    # '2277',
    # '2278',
    # '2280',
    # '2281',
    # '2282',
    # '2283',
    # '2286',
    # '2288',
    # '2289',
    # '2292',
    # '2293',
    # '2296',
    # '2298',
    # '2299',
    # '2300',
    # '2302',
    # '2303',
    # '2307',
    # '2308',
    # '2309',
    # '2310',
    # '2312',
    # '2313',
    # '2314',
    # '2317',
    # '2318',
    # '2319',
    # '2320',
    # '2322',
    # '2323',
    # '2324',
    # '2326',
    # '2327',
    # '2328',
    # '2329',
    # '2330',
    # '2331',
    # '2333',
    # '2336',
    # '2337',
    # '2338',
    # '2339',
    # '2340',
    # '2341',
    # '2342',
    # '2343',
    # '2345',
    # '2346',
    # '2348',
    # '2349',
    # '2355',
    # '2356',
    # '2357',
    # '2358',
    # '2359',
    # '2360',
    # '2362',
    # '2363',
    # '2366',
    # '2368',
    # '2369',
    # '2371',
    # '2377',
    # '2378',
    # '2379',
    # '2380',
    # '2381',
    # '2382',
    # '2383',
    # '2386',
    # '2388',
    # '2389',
    # '2393',
    # '2398',
    # '2399',
    # '2400',
    # '2448',
    # '2488',
    # '2500',
    # '2528',
    # '2552',
    # '2558',
    # '2588',
    # '2600',
    # '2601',
    # '2606',
    # '2607',
    # '2608',
    # '2611',
    # '2616',
    # '2623',
    # '2628',
    # '2633',
    # '2638',
    # '2660',
    # '2662',
    # '2663',
    # '2666',
    # '2668',
    # '2669',
    # '2678',
    # '2680',
    # '2682',
    # '2683',
    # '2686',
    # '2688',
    # '2689',
    # '2696',
    # '2698',
    # '2699',
    # '2700',
    # '2708',
    # '2718',
    # '2722',
    # '2727',
    # '2728',
    # '2738',
    # '2768',
    # '2772',
    # '2777',
    # '2779',
    # '2788',
    # '2789',
    # '2798',
    # '2799',
    # '2858',
    # '2863',
    # '2866',
    # '2868',
    # '2869',
    # '2877',
    # '2878',
    # '2880',
    # '2882',
    # '2883',
    # '2885',
    # '2886',
    # '2888',
    # '2892',
    # '2898',
    # '2899',
    # '2906',
    # '2949',
    # '2950',
    # '2951',
    # '2952',
    # '2954',
    # '2955',
    # '2956',
    # '3300',
    # '3301',
    # '3302',
    # '3303',
    # '3306',
    # '3308',
    # '3309',
    # '3311',
    # '3313',
    # '3315',
    # '3316',
    # '3318',
    # '3319',
    # '3320',
    # '3321',
    # '3322',
    # '3323',
    # '3326',
    # '3328',
    # '3329',
    # '3330',
    # '3331',
    # '3332',
    # '3333',
    # '3335',
    # '3336',
    # '3337',
    # '3339',
    # '3344',
    # '3347',
    # '3348',
    # '3358',
    # '3360',
    # '3363',
    # '3366',
    # '3368',
    # '3369',
    # '3377',
    # '3378',
    # '3380',
    # '3382',
    # '3383',
    # '3389',
    # '3390',
    # '3393',
    # '3395',
    # '3396',
    # '3398',
    # '3399',
    # '3600',
    # '3601',
    # '3603',
    # '3606',
    # '3608',
    # '3613',
    # '3616',
    # '3618',
    # '3623',
    # '3626',
    # '3628',
    # '3633',
    # '3636',
    # '3638',
    # '3639',
    # '3662',
    # '3663',
    # '3666',
    # '3668',
    # '3669',
    # '3678',
    # '3680',
    # '3681',
    # '3683',
    # '3686',
    # '3688',
    # '3689',
    # '3690',
    # '3692',
    # '3698',
    # '3699',
    # '3700',
    # '3708',
    # '3709',
    # '3718',
    # '3728',
    # '3737',
    # '3738',
    # '3759',
    # '3768',
    # '3773',
    # '3778',
    # '3788',
    # '3789',
    # '3798',
    # '3799',
    # '3800',
    # '3808',
    # '3813',
    # '3816',
    # '3818',
    # '3822',
    # '3828',
    # '3830',
    # '3833',
    # '3836',
    # '3838',
    # '3839',
    # '3848',
    # '3860',
    # '3866',
    # '3868',
    # '3869',
    # '3877',
    # '3878',
    # '3882',
    # '3883',
    # '3886',
    # '3888',
    # '3889',
    # '3893',
    # '3898',
    # '3899',
    # '3900',
    # '3903',
    # '3908',
    # '3918',
    # '3919',
    # '3928',
    # '3933',
    # '3938',
    # '3939',
    # '3948',
    # '3958',
    # '3963',
    # '3968',
    # '3969',
    # '3978',
    # '3983',
    # '3988',
    # '3989',
    # '3990',
    # '3991',
    # '3992',
    # '3993',
    # '3996',
    # '3997',
    # '3998',
    # '3999',
    # '4332',
    # '4333',
    # '4335',
    # '4336',
    # '4337',
    # '4338',
    # '4604',
    # '4606',
    # '4607',
    # '4608',
    # '4609',
    # '4610',
    # '4611',
    # '4612',
    # '4613',
    # '4614',
    # '4615',
    # '4616',
    # '4617',
    # '4618',
    # '4619',
    # '4620',
    # '6030',
    # '6033',
    # '6036',
    # '6038',
    # '6049',
    # '6055',
    # '6058',
    # '6060',
    # '6063',
    # '6066',
    # '6068',
    # '6069',
    # '6078',
    # '6080',
    # '6083',
    # '6088',
    # '6090',
    # '6093',
    # '6098',
    # '6099',
    # '6100',
    # '6108',
    # '6110',
    # '6111',
    # '6113',
    # '6116',
    # '6117',
    # '6118',
    # '6119',
    # '6122',
    # '6123',
    # '6128',
    # '6133',
    # '6136',
    # '6138',
    # '6158',
    # '6160',
    # '6161',
    # '6162',
    # '6163',
    # '6166',
    # '6168',
    # '6169',
    # '6178',
    # '6182',
    # '6183',
    # '6185',
    # '6186',
    # '6188',
    # '6189',
    # '6190',
    # '6193',
    # '6196',
    # '6198',
    # '6199',
    # '6288',
    # '6805',
    # '6806',
    # '6808',
    # '6811',
    # '6812',
    # '6816',
    # '6818',
    # '6819',
    # '6820',
    # '6822',
    # '6823',
    # '6826',
    # '6828',
    # '6829',
    # '6830',
    # '6833',
    # '6836',
    # '6837',
    # '6838',
    # '6839',
    # '6855',
    # '6858',
    # '6860',
    # '6862',
    # '6865',
    # '6866',
    # '6868',
    # '6869',
    # '6877',
    # '6878',
    # '6880',
    # '6881',
    # '6882',
    # '6885',
    # '6886',
    # '6888',
    # '6889',
    # '6890',
    # '6893',
    # '6896',
    # '6898',
    # '6899',
    # '6908',
    # '6918',
    # '6919',
    # '6928',
    # '6933',
    # '6958',
    # '6966',
    # '6968',
    # '6969',
    # '6978',
    # '6988',
    # '6989',
    # '6998',
    # '8001',
    # '8003',
    # '8005',
    # '8006',
    # '8007',
    # '8009',
    # '8011',
    # '8013',
    # '8017',
    # '8018',
    # '8019',
    # '8020',
    # '8021',
    # '8022',
    # '8023',
    # '8025',
    # '8026',
    # '8027',
    # '8028',
    # '8029',
    # '8030',
    # '8031',
    # '8032',
    # '8033',
    # '8035',
    # '8036',
    # '8037',
    # '8039',
    # '8040',
    # '8041',
    # '8042',
    # '8043',
    # '8045',
    # '8047',
    # '8048',
    # '8049',
    # '8050',
    # '8051',
    # '8052',
    # '8053',
    # '8055',
    # '8056',
    # '8057',
    # '8059',
    # '8060',
    # '8062',
    # '8063',
    # '8065',
    # '8066',
    # '8067',
    # '8069',
    # '8070',
    # '8071',
    # '8072',
    # '8073',
    # '8075',
    # '8076',
    # '8078',
    # '8079',
    # '8080',
    # '8081',
    # '8082',
    # '8083',
    # '8086',
    # '8087',
    # '8088',
    # '8089',
    # '8090',
    # '8091',
    # '8092',
    # '8093',
    # '8095',
    # '8096',
    # '8098',
    # '8100',
    # '8101',
    # '8103',
    # '8106',
    # '8107',
    # '8108',
    # '8109',
    # '8111',
    # '8112',
    # '8113',
    # '8115',
    # '8116',
    # '8117',
    # '8118',
    # '8119',
    # '8120',
    # '8121',
    # '8123',
    # '8125',
    # '8126',
    # '8128',
    # '8130',
    # '8131',
    # '8132',
    # '8133',
    # '8135',
    # '8136',
    # '8137',
    # '8139',
    # '8140',
    # '8143',
    # '8146',
    # '8147',
    # '8148',
    # '8149',
    # '8150',
    # '8151',
    # '8152',
    # '8153',
    # '8155',
    # '8156',
    # '8158',
    # '8159',
    # '8160',
    # '8161',
    # '8162',
    # '8163',
    # '8165',
    # '8166',
    # '8167',
    # '8168',
    # '8169',
    # '8170',
    # '8171',
    # '8172',
    # '8173',
    # '8175',
    # '8176',
    # '8178',
    # '8179',
    # '8181',
    # '8186',
    # '8187',
    # '8188',
    # '8189',
    # '8190',
    # '8191',
    # '8192',
    # '8193',
    # '8195',
    # '8196',
    # '8198',
    # '8200',
    # '8201',
    # '8202',
    # '8203',
    # '8205',
    # '8206',
    # '8207',
    # '8208',
    # '8210',
    # '8211',
    # '8213',
    # '8215',
    # '8216',
    # '8217',
    # '8218',
    # '8219',
    # '8220',
    # '8221',
    # '8222',
    # '8223',
    # '8225',
    # '8226',
    # '8227',
    # '8228',
    # '8229',
    # '8231',
    # '8232',
    # '8235',
    # '8236',
    # '8237',
    # '8238',
    # '8239',
    # '8241',
    # '8242',
    # '8245',
    # '8246',
    # '8247',
    # '8249',
    # '8250',
    # '8255',
    # '8256',
    # '8257',
    # '8258',
    # '8259',
    # '8260',
    # '8262',
    # '8265',
    # '8266',
    # '8267',
    # '8268',
    # '8269',
    # '8270',
    # '8271',
    # '8272',
    # '8275',
    # '8277',
    # '8279',
    # '8280',
    # '8281',
    # '8282',
    # '8283',
    # '8285',
    # '8286',
    # '8287',
    # '8290',
    # '8291',
    # '8292',
    # '8293',
    # '8295',
    # '8296',
    # '8297',
    # '8299',
    # '8300',
    # '8301',
    # '8305',
    # '8307',
    # '8308',
    # '8309',
    # '8310',
    # '8311',
    # '8313',
    # '8315',
    # '8316',
    # '8317',
    # '8319',
    # '8320',
    # '8321',
    # '8325',
    # '8326',
    # '8328',
    # '8329',
    # '8331',
    # '8333',
    # '8337',
    # '8340',
    # '8341',
    # '8346',
    # '8347',
    # '8348',
    # '8349',
    # '8350',
    # '8351',
    # '8353',
    # '8356',
    # '8357',
    # '8360',
    # '8362',
    # '8363',
    # '8365',
    # '8366',
    # '8367',
    # '8368',
    # '8370',
    # '8371',
    # '8372',
    # '8373',
    # '8375',
    # '8377',
    # '8379',
    # '8383',
    # '8385',
    # '8391',
    # '8392',
    # '8395',
    # '8400',
    # '8401',
    # '8402',
    # '8403',
    # '8405',
    # '8406',
    # '8411',
    # '8412',
    # '8413',
    # '8416',
    # '8417',
    # '8418',
    # '8419',
    # '8420',
    # '8422',
    # '8423',
    # '8425',
    # '8426',
    # '8427',
    # '8428',
    # '8429',
    # '8430',
    # '8431',
    # '8432',
    # '8436',
    # '8437',
    # '8439',
    # '8441',
    # '8445',
    # '8446',
    # '8447',
    # '8448',
    # '8450',
    # '8451',
    # '8452',
    # '8455',
    # '8456',
    # '8460',
    # '8462',
    # '8465',
    # '8471',
    # '8472',
    # '8473',
    # '8475',
    # '8476',
    # '8479',
    # '8480',
    # '8481',
    # '8482',
    # '8483',
    # '8485',
    # '8487',
    # '8490',
    # '8491',
    # '8493',
    # '8495',
    # '8496',
    # '8500',
    # '8501',
    # '8502',
    # '8506',
    # '8507',
    # '8509',
    # '8510',
    # '8511',
    # '8512',
    # '8513',
    # '8516',
    # '8519',
    # '8521',
    # '8523',
    # '8525',
    # '8526',
    # '8527',
    # '8532',
    # '8535',
    # '8536',
    # '8537',
    # '8540',
    # '8545',
    # '8547',
    # '8572',
    # '8601',
    # '8603',
    # '8606',
    # '8607',
    # '8609',
    # '8611',
    # '8612',
    # '8613',
    # '8616',
    # '8617',
    # '8619',
    # '8620',
    # '8621',
    # '8622',
    # '8623',
    # '8627',
    # '8631',
    # '8635',
    # '8645',
    # '8646',
    # '8657',
    # '8659',
    # '8668',
    # '9616',
    # '9618',
    # '9633',
    # '9668',
    # '9677',
    # '9688',
    # '9900',
    # '9906',
    # '9908',
    # '9909',
    # '9911',
    # '9913',
    # '9916',
    # '9918',
    # '9919',
    # '9922',
    # '9923',
    # '9926',
    # '9928',
    # '9929',
    # '9933',
    # '9936',
    # '9938',
    # '9939',
    # '9958',
    # '9966',
    # '9968',
    # '9969',
    # '9977',
    # '9978',
    # '9979',
    # '9983',
    # '9986',
    # '9987',
    # '9988',
    # '9989',
    # '9990',
    # '9991',
    # '9993',
    # '9996',
    # '9997',
    # '9998',
    # '9999'
]

result = []


def create_xlsx_file(file_path: str, headers: dict, items: list):
    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_keys = list(headers.keys())
        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), header_keys)
            worksheet.write_row(row=index + 1, col=0, data=row)


def codify(number):
    def is_digits(x):
        return not (re.search(r'([0-9]*)', x).group() == '')

    if is_digits(number):
        return str(number) + '.HK'
    else:
        return number


def rsi(stock, column="Close", period=14):
    # Wilder's RSI
    close = stock[column]
    delta = close.diff()
    up, down = delta.copy(), delta.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    # Calculate the exponential moving averages (EWMA)
    roll_up = up.ewm(com=period - 1, adjust=False).mean()
    roll_down = down.ewm(com=period - 1, adjust=False).mean().abs()

    # Calculate RS based on exponential moving average (EWMA)
    rs = roll_up / roll_down  # relative strength =  average gain/average loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


def validate(code):
    today = datetime.today().date()
    ticker = yf.Ticker(codify(code))
    history = ticker.history(period='1y')
    close = history['Close'][-1]
    week_low_52 = history['Low'].min()
    week_high_52 = history['High'].max()
    ma_50 = history['Close'][-50:].mean()
    ma_150 = history['Close'][-150:].mean()
    ma_200 = history['Close'][-200:].mean()
    ma_200_series = history['Close'].rolling(window=200).mean().dropna()[-20:]
    if len(ma_200_series) > 1:
        ma_200_slope = (ma_200_series[-1] - ma_200_series[1]) / len(ma_200_series)
    else:
        ma_200_slope = 1
    rsi_14 = rsi(history)[-1]

    conditions = [
        close > ma_150 and close > ma_200,
        ma_150 > ma_200,
        ma_200_slope > 0,
        ma_50 > ma_150 and ma_50 > ma_200,
        close > ma_50,
        close >= 1.3 * week_low_52,
        close * 1.25 >= week_high_52,
        rsi_14 > 70,
        abs((history.index.max().date() - today).days) <= 7  # no trading data for more than 7 days
    ]

    if all(conditions):
        info = ticker.get_info()

        output = {
            'code': code,
            'name': info['longName'],
            'market_capital': info['marketCap'],
            'volume': info['volume'],
            'close': '{:.3f}'.format(close),
            'week_low_52': '{:.3f}'.format(week_low_52),
            'week_high_52': '{:.3f}'.format(week_high_52),
            'ma_50': '{:.3f}'.format(ma_50),
            'ma_150': '{:.3f}'.format(ma_150),
            'ma_200': '{:.3f}'.format(ma_200),
            'ma_200_slope': '{:.3f}'.format(ma_200_slope),
            'rsi_14': '{:.3f}'.format(rsi_14),
            'as_of': str(history.index.max().date())
        }

        result.append(output)
        return True, output
    return False, None


start = datetime.now()
data = {"data": []}
for stock in stocks:
    try:
        validated, output = validate(stock)
        print(str(datetime.now()) + ': ' + stock)
        if validated:
            data["data"].append(output)
    except Exception as e:
        print(e)
print('Start time\t: ' + str(start))
print('End time\t: ' + str(datetime.now()))
fo1 = open('./static/Trend-Template-Result' + '.json', 'w')
fo1.write(json.dumps(data))
fo1.close()
fo2 = open('./history/Trend-Template-Result-' + str(start.date()) + '.json', 'w')
fo2.write(json.dumps(data))
fo2.close()

# Export to excel
headers = {
    'code': 'Code',
    'name': 'Name',
    'market_capital': 'Market Cap',
    'volume': 'Volume',
    'close': 'Close Price',
    # 'week_low_52': '52 Weeks Low',
    # 'week_high_52': '52 Weeks High',
    # 'ma_50': '50 MA',
    # 'ma_150': '150 MA',
    # 'ma_200': '200 MA',
    'ma_200_slope': 'Slope of 200 MA',
    'rsi_14': 'RSI',
    'as_of': 'Retrieved at',
}

create_xlsx_file('./history/Trend-Template-Result-' + str(start.date()) + '.xlsx', headers, result)
