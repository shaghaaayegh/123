import pandas as pd
import re
IN_PATH = "C:\\Users\\Asus\\Desktop\\fake_chat.xlsx"
OUT_PATH = "C:\\Users\\Asus\\Desktop\\output.xlsx"

data = pd.ExcelFile(IN_PATH)
df = data.parse("Sheet1",encoding="utf-8")
print(df)

l = []
for rownum in range(len(df)):
    row = df.iat[rownum,1]
    l.extend(x for x in row.split('|') if  re.match(r"[^|0-9|]\D+", x))
df2 = pd.DataFrame(l)
print(df2)

with pd.ExcelWriter(OUT_PATH) as writer:
    df2.to_excel(writer, sheet_name='Sheet1')
