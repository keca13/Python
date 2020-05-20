#zetcode.com
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import csv

con = pymysql.connect('192.168.x.x', 'login', 
    'password', 'db')

with con: 

    cur = con.cursor()
    #cur.execute("SELECT ip_number FROM calls2 WHERE id_client like '94'")
    #cur.execute("SELECT cost FROM calls2 WHERE call_end like '2011-03-%'and id_client='94'")
    #cur.execute("SELECT cost FROM calls2 WHERE call_end LIKE '2011-03-%' OR id_client='94' OR id_client='6'")
    #cur.execute("SELECT cost FROM calls2 WHERE call_end LIKE '2011-03-%' and id_client='94'")
    #cur.execute("SELECT cost FROM calls2 WHERE id_client='6' and call_end LIKE '2011-03-%'")
    #SELECT cost FROM calls2 WHERE call_end LIKE '2011-03-%' and id_client='94';
    #SELECT cost FROM calls2 WHERE id_client IN('6','94','662')  and call_end LIKE '2011-03-%'
    #SELECT costR1 FROM calls WHERE id_client IN('952399','954365')  and call_end LIKE '2020-03-1% %'
    #SELECT costR1 FROM calls WHERE id_client IN('952399','954365')  and call_end BETWEEN '2020-03-01' AND '2020-03-31'
    #SELECT company_name FROM clientspbx WHERE company_name LIKE '%@%' AND id_tariff IN('8')
    #SELECT company_name, login, password, web_password, id_client, id_reseller, reseller, company_name, company_dial_prefix, type, id_tariff, id_currency, account_state, max_clients, type2 FROM clientspbx WHERE company_name LIKE '%@%' AND id_tariff IN('8')    
    #SELECT login, id_company, pbx_client FROM pbx_subaccounts
    #SELECT it_getusers.idTariff, pbx_subaccounts.id_company, it_getusers.IdCompany FROM it_getusers, pbx_subaccounts WHERE it_getusers.idTariff = 9 LIMIT 100;
    #SELECT it_getusers.idTariff, pbx_subaccounts.id_company, pbx_subaccounts.id_client, pbx_subaccounts.login FROM it_getusers, pbx_subaccounts WHERE it_getusers.idTariff = 9 LIMIT 100;
    #SELECT it_getusers.IdTariff, it_getusers.login, pbx_subaccounts.caller_id  FROM it_getusers, pbx_subaccounts WHERE it_getusers.IdTariff = ('9') LIMIT 100;
    n = input("Wprowadz polecenie sql:  ")
    print("Wprowadzone polecenie to:\n %s " % n)
    cur.execute(n)


    rows = cur.fetchall()

    #for row in rows:
        #a = (row[1],row[2])    
        #print("{0} {1}".format(row[1], row[3]))

# python write file
f = open('dane.csv', 'w' )
with f:
	writer = csv.writer(f)
	for row in rows:
		writer.writerow(row)

print("Done! lista skladana")
#whitespace removed using list comprehension
with open('dane.csv') as input, open('dane_out.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)


print("Done! part 02")
