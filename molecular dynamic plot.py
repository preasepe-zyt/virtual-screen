import matplotlib.pyplot as plt
import matplotlib
import numpy
import sys
sys.path.append(r"C:\Users\79403\Desktop\python script\分子对接和动力学模拟")
from mean import mean
from mean import mean
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use("TKAgg")
#字体
#matplotlib.rcParams['font.family'] = 'Arial'
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"
#linux 计算
"""
#rmsd
gmx rms -s /home/zyfone/hard-disk/sAs/md_0_1.tpr -f /home/zyfone/hard-disk/sAs/md_0_1.xtc -n CA.ndx -o rmsd.xvg -fit rot+trans -xvg none
#rmsf
gmx rmsf -s /home/zyfone/hard-disk/sAs/md_0_1.tpr -f /home/zyfone/hard-disk/sAs/md_0_1.xtc -n  /home/zyfone/hard-disk/sAs/RMSD/CA.ndx -o rmsf.xvg -fit -xvg none
#distance
mkdir -p dist/I52_K145 && cd dist/I52_K145
gmx make_ndx -f /home/zyfone/hard-disk/sAs/md_0_1.tpr -o I52_K145.ndx
gmx distance -s /home/zyfone/hard-disk/sAs/md_0_1.tpr -f /home/zyfone/hard-disk/sAs/md_0_1.xtc -n /home/zyfone/hard-disk/sAs/dist/I52_K145/I52_K145.ndx -o dist.xvg -xvg none
#Radius of gyration
gmx gyrate -s /home/zyfone/hard-disk/sAs/md_0_1.tpr -f /home/zyfone/hard-disk/sAs/md_0_1.xtc -o gyrate.xvg -xvg none
"""

path = r'C:\Users\79403\Desktop\chinese-medicine\md'
group = ["ALOX5-24-epicampesterol", "ALOX5-8,11,14-Docosatrienoic acid, methyl ester", "ALOX5-3-phenylpropyl acetate",
         "ALOX5-beta-sitosterol", "ALOX5-sitosterol", "ALOX5-Stigmasterol"]
# 定义颜色列表
colors = ['blue', 'green', 'red', 'purple', 'orange', "olive"]
dis = "dist.xvg"
gyr = "gyrate.xvg"
hb = "hbond_num.xvg"
#RMSD
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)
for index, i in enumerate(group):
    t, rmsd = numpy.loadtxt(path + "\\" + "rmsd" + "_" + i + ".xvg", unpack=True)
    t_m, rmsd_m = mean(rmsd)
    ax.plot(t/1000, rmsd, linestyle="-", label=i, alpha=0.2, color=colors[index])
    ax.plot(t_m/100, rmsd_m, linestyle="-", color=colors[index])

ax.set_xlabel("$t/ns$", fontsize=20)
ax.set_ylabel(r"RMSD (nm)", fontsize=20) #r"C$_\alpha$ RMSD (nm)"
ax.legend(loc='upper right', frameon=False)
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
ax.set_yticks(numpy.arange(0, 0.5, 0.1))
plt.show()
fig.savefig(path+"\\"+"rmsd.png", dpi=300)

#rmsf
import matplotlib.pyplot as plt
import numpy as np
residue = ("LEU289", "VAL244", "ALA454", "LEU67",
           "VAL27", "VAL111", "HIS131", "ILE127",
           "ARG102", "GLN142")
residue_lo = [list(range(3699, 3703)), list(range(2035, 2041)), list(range(2401, 2416)),  list(range(469, 476)),
              list(range(196, 202)), list(range(900, 906)), list(range(1064, 1079)), list(range(1030, 1073))
              , list(range(825, 835)), list(range(1167, 1175))]
style = {'color': 'black', 'fontsize': 11, 'fontweight': 'bold'}
resisue_h = [0.4, 0.42, 0.55, 0.4, 0.53, 0.68, 0.52, 0.3, 0.6, 0.73]

fig, axs = plt.subplots(2, 3, figsize=(12, 8))
fig.subplots_adjust(wspace=0.4, hspace=0.4)
for index, i in enumerate(group):
    # 计算子图的索引位置
    row = index // 3 #整数除法
    col = index % 3 #求余数

    # 加载数据，这里使用随机数据代替
    resid, rmsf = np.loadtxt(path+"\\"+"rmsf"+"_"+i+".xvg", unpack=True)

    # 在相应的子图中绘制数据
    axs[row, col].plot(resid, rmsf, linestyle="-", linewidth=0.5, color=colors[index])
    axs[row, col].set_xlabel("Residue number", fontsize=20)
    axs[row, col].set_title(i)
    axs[row, col].set_ylabel("RMSF (nm)", fontsize=20)
    axs[row, col].tick_params(axis='both', labelsize=10)
    axs[row, col].spines['top'].set_linewidth(2)
    axs[row, col].spines['right'].set_linewidth(2)
    axs[row, col].legend(loc='upper right', frameon=False)
plt.show()
fig.savefig(path+"\\"+"rmsf.png", dpi=300)


#distance
import matplotlib.pyplot as plt
import numpy

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

for index, i in enumerate(group):
   t, d= numpy.loadtxt(path+"\\"+"distave_"+i+".xvg", unpack=True)
   ax.plot(t / 1000, d, linestyle="-")


ax.set_xlabel("$t/ns$", fontsize=20)
ax.set_ylabel("Distance (nm)", fontsize=20)
ax.tick_params(axis='both', labelsize=20)
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()
fig.savefig("dis.png", dpi=300)

#Radius of gyration
import matplotlib.pyplot as plt
import numpy


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

for index, i in enumerate(group):
    t, data, x, y, z = numpy.loadtxt(path+"\\"+"gyrate"+"_"+i+".xvg", unpack=True)
    t_m, data_m = mean(data)
    ax.plot(t / 1000, data, linestyle="-", label=i, color=colors[index], alpha=0.2)
    ax.plot(t_m / 100, data_m, linestyle="-", color=colors[index])


ax.set_xlabel("$t/ns$", fontsize=20)#$s$ 可以斜体
ax.set_ylabel(r"RoG (nm)", fontsize=20)# _\mathrm{hb} 可以把字体下标
ax.legend(loc='upper right', frameon=False)
ax.set_yticks(numpy.arange(2.70, 3.00, 0.05))
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()
fig.savefig(path+"\\"+"rgyr.png", dpi=300)

#fig.savefig("rgyr.svg")
#fig.savefig("rgyr.pdf")


#hbond
import matplotlib.pyplot as plt
import numpy
import seaborn as sns#调色

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

t, x, hbond = numpy.loadtxt(path+"\\"+"hbond"+"_"+group[0]+".xvg", unpack=True)
t2, x2, hbond2 = numpy.loadtxt(path+"\\"+"hbond"+"_"+group[1]+".xvg", unpack=True)

#sns.color_palette()
ax.hist(t/1000,  x, density=True, rwidth=0.8)
# ax.hist(t2/1000,  hbond2, color="purple", label=group[1])


#plt.legend(loc='upper left', frameon=False)

ax.set_xlabel("t/ns", fontsize=20)#$s$ 可以斜体
ax.set_ylabel("Number of Hbond", fontsize=20)# _\mathrm{hb} 可以把字体下标
#ax.set_yticks(numpy.arange(0, 2, 0.5))
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()

fig.savefig("hbond", dpi=300)
#
'tab:blue'
'tab:orange'
'tab:green'
'tab:red'
'tab:purple'
'tab:brown'
'tab:pink'
'tab:gray'
'tab:olive'
'tab:cyan'

#绘制二级结构
import numpy as np
import matplotlib.pyplot as plt
# color_map = ["总结构 (Structure)", "区卷 (Coil)", "β-折叠 (B-Sheet)","β-桥 (B-Bridge)", "弯曲 (Bend)",
#               "转弯 (Turn)", "α-螺旋 (A-Helix)", "5-螺旋 (5-Helix)", "分链器 (3-Helix)"]
color_map = ["Structure", "Coil", "B-Sheet", "B-Bridge", "Bend",
              "Turn", "A-Helix", "5-Helix", "3-Helix"]
# 替换为你的 DSSP 输出文件路径
fig, axs = plt.subplots(2, 3, figsize=(12, 12))
fig.subplots_adjust(wspace=0.45, hspace=0.6)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

for index, i in enumerate(group):
    # 计算子图的索引位置
    row = index // 3  # 整数除法
    col = index % 3  # 求余数
    # 加载数据，这里使用随机数据代替
    data = np.loadtxt(path + "\\" + "scount" + "_" + i + ".xvg", unpack=True)
    for a in range(1, 9):
        axs[row, col].plot(data[0], data[a], linestyle="-", label=color_map[a-1], linewidth=0.5)
    axs[row, col].set_xlabel("t/ns", fontsize=20)
    axs[row, col].set_title(i)
    axs[row, col].set_ylabel("Residue", fontsize=20)
    axs[row, col].tick_params(axis='both', labelsize=9)
    axs[row, col].spines['top'].set_linewidth(2)
    axs[row, col].spines['right'].set_linewidth(2)
    axs[row, col].legend(loc='upper center', bbox_to_anchor=(0.5, 1.4), frameon=False, title="Second Structure", ncol=3)
plt.show()
fig.savefig(path+"\\"+"second_structure.png", dpi=300)


#溶剂可及面积 SASA
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

for index, i in enumerate(group):
    t, sasa = numpy.loadtxt(path+"\\"+"area"+"_"+i+".xvg", unpack=True)
    t_m, sasa_m = mean(sasa)
    ax.plot(t/1000, sasa, linestyle="-", label=i, color=colors[index], alpha=0.2)
    ax.plot(t_m / 100, sasa_m, linestyle="-", color=colors[index])

ax.set_xlabel("$t/ns$", fontsize=20)
ax.set_ylabel(r"SASA (nm²)", fontsize=20) #r"C$_\alpha$ RMSD (nm)"
ax.legend(loc='upper right', frameon=False)
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
ax.set_yticks(numpy.arange(270, 330, 10))
plt.show()
fig.savefig(path+"\\"+"area.png", dpi=300)