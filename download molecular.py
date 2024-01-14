import pubchempy as pcp
#cid = [529, 234]
#sdfpath = "C:/Users/79403/Desktop/chem/529.sdf" # 本地保存路径
#pcp.download('SDF', sdfpath, overwrite=True, identifier=cid, record_type='3d')
import os
import pubchempy as pcp
import pandas as pd
path = r"C:\Users\79403\Desktop\o(￣▽￣)ｄ\陈皮\relativeIngredient.txt"
data = pd.read_table(path, usecols=["NID", "Pubchem CID"], sep="\t") #, , header=False, index=False, encoding='utf-8'Bsep="\t
data_c = data["Pubchem CID"]
#删除字母
# 定义输出列
mol_cid = []
import openpyxl
import re
# 循环遍历每个单元格
for i in data_c:
	# 去除英文字母
	cleaned_value = re.sub('[a-zA-Z]', '', i) # 利用正则表达式去除英文字母
	mol_cid.append(cleaned_value)
    print(mol_cid)
		# 保存文件
#output_file = 'output.xlsx'
#workbook.save(output_file)

def mol_id_to_cid(x):
	try:
		# Search for the molecule using the Mol ID in PubChem
		compound = pcp.get_compounds(x, 'mol', record_type='3d')[0]

		# Get the CID (Compound Identifier) for the compound
		cid = compound.cid

		return cid
	except Exception as e:
		print(f"An error occurred: {e}")
		return None

import pubchempy as pcp
path = "C:/Users/79403/Desktop/chem/"
cids = mol_id
for cid in cids:
   sdfpath = os.path.join(path, "{}.sdf".format(cid))
   print(sdfpath)
   pcp.download('SDF', sdfpath, overwrite=True, identifier=cid)
   #pcp.download('PDB', sdfpath, overwrite=True, identifier=cid, record_type='3d')




