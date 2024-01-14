import pandas as pd
import pubchempy as pcp
import requests
import openpyxl
import os
#####合并两个表格的所有化合物名称
df = pd.read_excel(r"C:\Users\79403\Desktop\白术抗ad\网络药理学部分\ingredients.xlsx")
#df2 =  pd.read_excel("GDSC2_fitted_dose_response_24Jul22.xlsx")

#####
#合并两个表格的两个列
df.columns
drug = df['Molecule Name'].tolist()
#drug = df['DRUG_NAME'].tolist() + df2['DRUG_NAME'].tolist()

#去重复
drug = list(set(drug))

#转换成dataframe
drug = pd.DataFrame(drug, columns=['DRUG_NAME'])

####获取对应的SMILES
# 定义替换函数
def replace_url(element):
    # 将 {} 替换为元素的值
    return url.format(element)
url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{}/property/CanonicalSMILES/txt"
# 使用 apply 方法替换每个元素
new_urls = drug['DRUG_NAME'].apply(lambda x: replace_url(x))
#新建一个列表保存获取的内容
smi = []

# 遍历新的 URL 列并进行请求或其他操作
for url in new_urls:
    try:
        response = requests.get(url, verify=False)
        smi.append(response.text)
        print(smi)
    except Exception as e:
        print("发生异常:", str(e))
        smi.append("")


#########将smi添加到drug中
drug['SMILES'] = smi

#########保存
drug.to_excel("drug.xlsx", index=False)