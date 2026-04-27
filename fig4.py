import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.dpi'] = 200

foldseek = pd.read_csv("")
petases = pd.read_csv("")
ec311 = pd.read_csv("")

data = pd.DataFrame({
    "α/β-гидролазы":ec311["Length"],
    "ПЭТазы":petases[petases["Length"]>50]["Length"],
    "FoldSeek":foldseek[foldseek["evalue"]<1e-6]["tlen"]
}).melt(var_name="group", value_name="Length")

pal = ["#BFBFFF", "#FF777C","#CD1C18"]
g = sns.FacetGrid(data, row="group", hue="group", aspect=5, height=1, palette=pal)

# Плотности
g.map(sns.kdeplot, "Length",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "Length", clip_on=False, color="w", lw=2, bw_adjust=.5)

# passing color=None to refline() uses the hue mapping
g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)


# Функция для обозначения дорожек
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)


g.map(label, "Length")

# Set the subplots to overlap
g.figure.subplots_adjust(hspace=-.25)

g.map(plt.axvline, x=261, color='orange', linewidth = 0.8, linestyle='--')

# Удаление лишних деталей
g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)
plt.tight_layout()
plt.xlabel("Длина, ак")
