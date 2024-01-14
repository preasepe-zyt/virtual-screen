import pandas as pd
from rdkit.Chem import QED
import os
from rdkit import Chem
from rdkit.Chem import Descriptors
path = r'C:\\Users\\79403\\Desktop\\chem'
#药效团的特征
from rdkit import Geometry
from rdkit import RDConfig
from rdkit.Chem import AllChem
from rdkit.Chem import ChemicalFeatures
from rdkit.Chem.Pharm3D import Pharmacophore
import  numpy as np
#AllChem.EmbedMolecule(mol)
file_name = os.listdir(path)
FEAT = os.path.join(RDConfig.RDDataDir, "BaseFeatures.fdef")
featfact = ChemicalFeatures.BuildFeatureFactory(FEAT)
family = pd.DataFrame()
descriptors = pd.DataFrame()
for i in file_name:
    sdfpath = os.path.join(path, i)
    m = Chem.MolFromMolFile(sdfpath)
    feat = featfact.GetFeaturesForMol(m)
    family_m = pd.Series([feats.GetFamily() for feats in feat])
    family.loc[:, i] = family_m
    family.count()
    print(family)
    print(family.count())
    qed = QED.weights_mean(m)
    tpsa = Descriptors.TPSA(m)
    logp = Descriptors.MolLogP(m)

    descriptors_m = pd.DataFrame({"qed": [qed], "tpsa": [tpsa], "logp": [logp], "group": [i]})
    descriptors = pd.concat([descriptors_m,  descriptors])
    print(descriptors)

