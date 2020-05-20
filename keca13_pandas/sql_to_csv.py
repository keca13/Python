# https://docs.sqlalchemy.org/en/13/core/engines.html

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:password@host:3306/db')

#you can use
#SELECT `description` FROM `my_voip`.`tariffs`;
#SELECT * FROM `my_voip`.`tariffs` WHERE `description` = 'Bulgaria';
# is DOT not common
#SELECT * FROM `my_voip`.`tariffs` WHERE `voice_rate` LIKE '0.1200';
#SELECT * FROM `my_voip`.`tariffs` WHERE `voice_rate` LIKE '%.12%';

df = pd.read_sql(sql="SELECT `description`,`voice_rate` FROM `my_voip`.`tariffs` WHERE `voice_rate` LIKE '0.1200'", con=engine) \
    .to_csv('tariffs2.csv', index=False)

df_csv = pd.read_csv('tariffs2.csv', sep=',', engine='python')
df_csv.to_csv('tariffs2.csv', sep=',', index=False)

print(df_csv)

# open in notebook CTRL+h, replace 0.12->
# Done
