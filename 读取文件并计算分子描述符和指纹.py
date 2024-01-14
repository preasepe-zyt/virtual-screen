import os
from rdkit import Chem
import numpy as np
import pandas as pd
#分子描述符
from rdkit.Chem import Descriptors
from rdkit.Chem import MACCSkeys
from rdkit.Chem import AllChem
from rdkit import DataStructs

CalcMol = pd.Series()
class Drug:
     def __int__(self):
         print("开始了")
     def read(self, path):
            global CalcMol
            file_name = os.listdir(path)
            for i in file_name:
               sdfpath = os.path.join(path, "{}".format(i))
               print(sdfpath)
               # time.sleep(1)
               m = Chem.MolFromMolFile(sdfpath)
               # des = Chem.MolToSmiles(m)
               # time.sleep(1)
               #mols.append(m)
               CalcMol_m = Descriptors.CalcMolDescriptors(m, silent=True)
               MACCS_m = MACCSkeys.GenMACCSKeys(m).ToBitString()
               fpgen = AllChem.GetRDKitFPGenerator()
               RDK = fpgen.GetFingerprint(m).ToList()
               ecfp4_m = AllChem.GetMorganFingerprint(m, 2).GetNonzeroElements()
               print(CalcMol)
               print(ecfp4_m)
               print(MACCS_m)
               print(RDK)
               #logp.append(logp_m)
               CalcMol_f = pd.DataFrame(CalcMol_m, index=[i])
               CalcMol = pd.concat([CalcMol_f,  CalcMol])
            return CalcMol

path = r"C:\Users\79403\Desktop\chem"
start = Drug()
start.__int__()

se = start.read(path)
#两种方式形成列表 1.xx.append 2.xx[sss(x) for x in xx]
#series 是一维度数组
#datafram 是维度
#array 是数组