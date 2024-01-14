import os
from openbabel import openbabel


def multi_file_convert(file_PATH, input_format, output_format, tar):

    """
    file_PATH是指文件夹所在位置，本份代码使用了相对路径
    input_format是指输入文件的格式，本分代码待转换的文件格式是poscar
    output_format是指输出文件的格式，本份代码想得到的文件格式是xyz
    tar 判断是否为目标类别
    """
    tqdm = os.listdir(file_PATH)  # 文件夹中的文件列表
    for i in range(0, len(tqdm)):  # 逐次遍历文件夹下的文件
        if (tar in tqdm[i]):
                inputfile = os.path.join(file_PATH, tqdm[i]) # 对应文件夹下的某份文件
                print("您将把以下文件进行格式转换"+tqdm[i])
                conv = openbabel.OBConversion()  # 调用转换函数
                conv.OpenInAndOutFiles(inputfile, inputfile + "new" + ".pdb")  # 输入待转换的文件名及定义转换成功后的文件名
                conv.SetInAndOutFormats(input_format, output_format)
                conv.Convert()
                conv.CloseOutFile()

multi_file_convert(r"C:\Users\79403\Desktop\shi\ligandprotein\re",'pdbqt','pdb','pdbqt')
#记得修改def里面的东西