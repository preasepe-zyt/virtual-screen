from rdkit import Chem
from rdkit.Chem import Draw
import rdkit
print(rdkit.__version__)
from rdkit.Chem import  Descriptors
import pandas as pd
m = Chem.MolFromMolFile('C:/Users/79403/Desktop/Hesperidin.mol')
des = Chem.MolToSmiles(m)# 结果显示： 'C[C@H](O)c1ccccc1'
mols = []
for smi in des:
    m = Chem.MolFromSmiles(smi)
    mols.append(m)

descrs = [Descriptors.CalcMolDescriptors(mol) for mol in mols]
df = pd.DataFrame(descrs)


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f'Hello, my name is {self.name} and my age is {self.age} my sex is {self.gender}')

class Student(Human):
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def study(self):
        print(f'{self.name} is studying in grade {self.grade}.')

n = Human("asas", 23, "男")
n.say_hello()
n2 = Student("asas", 23, "男", "研一")
n2.study()
n2.say_hello()