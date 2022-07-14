def read_data_func_F90(DADO,nt,nr=1,ns=1):
  import numpy as np
  # Leitura do campo de velocidades em binário\n",
  arq2 = open(DADO,"rb")
  pulso2=np.fromfile(arq2,dtype=np.float32).tolist()
  arq2.close()
  if (ns == 1):
    if (nr == 1):
      # Colocando o campo em um Vetor\n",
      c1= np.zeros(shape=(nt))
      for i in range(0,nt):
        c1[i]=pulso2[i]
    else:
      # Colocando o campo em uma matriz\n",
      c1= np.zeros(shape=(nt,nr))  ##c1[nz][nx]\n",
      t=-1
      for j in range(0,nr):
        for i in range(0,nt):
          t=t+1
          c1[i,j]=pulso2[t]
  else:
    # Colocando o campo em um cubo\n",
    c1= np.zeros(shape=(nt,nr,ns)) ##c1[nz][nx]\n",
    t=-1
    for k in range(0,ns):
      for j in range(0,nr):
        for i in range(0,nt):
          t=t+1
          c1[i,j,k]=pulso2[t]
  return c1

def read_data_func(DADO,nt,nr=1,ns=1):
  import numpy as np
  # Leitura do campo de velocidades em binário\n",
  arq2 = open(DADO,"rb")
  pulso2=np.fromfile(arq2,dtype=np.float32).tolist()
  arq2.close()
  s,w,h=ns,nr,nt  ### nx numero de colunas, nz numero de linhas\n",
  if (ns == 1):
    if (nr == 1):
      c1=[0 for y in range(h)]
      for i in range(0,nt):
        c1[i]=pulso2[i]
    else:
      # Colocando o campo em uma matriz\n",
      c1=[[0 for x in range(w)] for y in range(h)]  ##c1[nz][nx]\n",
      t=-1
      for j in range(0,nr):
        for i in range(0,nt):
          c1[i][j]=pulso2[t]
          t=t+1
  else:
    # Colocando o campo em uma matriz\n",
    c1=[[[0 for x2 in range(s)] for x in range(w)] for y in range(h)]  ##c1[nz][nx]\n",
    t=0
    for k in range(0,ns):
      for j in range(0,nr):
        for i in range(0,nt):
          c1[i][j][k]=pulso2[t]
          t=t+1
  return c1

def plot_sismograma(rec,perc=0.1,rec2=None, rec3=None, Hori=4,Ver=7,sismic=None):
  from matplotlib import pyplot, transforms
  import numpy as np
  from matplotlib import cm
  import matplotlib.pyplot as plt
  scale = perc * np.max(rec)
  if rec2 is not None:
    scale2 = perc * np.max(rec2)
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(3*Hori, Ver))
    if sismic is None:
      img1 = ax[0].imshow(rec, vmin=-scale, vmax=scale,cmap="gray", interpolation='lanczos')
    else:
      img1 = ax[0].imshow(rec, vmin=-scale, vmax=scale,cmap="seismic", interpolation='lanczos')
    ax[0].set_title("$G_{ref}$", fontsize=3*Hori)
    ax[0].set_xlabel("Receptores (m)", fontsize=3*Hori)
    ax[0].set_ylabel("Tempo (s)", fontsize=3*Hori)
    ax[0].set_aspect('auto')
    if sismic is None:
      img1 = ax[1].imshow(rec2, vmin=-scale, vmax=scale, cmap='gray', interpolation='lanczos')
    else:
      img1 = ax[1].imshow(rec2, vmin=-scale, vmax=scale, cmap='seismic', interpolation='lanczos')
    ax[1].set_title("$G_{k}$", fontsize=3*Hori)
    ax[1].set_xlabel("Receptores (m)", fontsize=3*Hori)
    ax[1].set_ylabel(" ", fontsize=3*Hori)
    ax[1].set_aspect('auto')
    if sismic is None:
      img1 = ax[2].imshow(rec3, vmin=-scale, vmax=scale, cmap='gray', interpolation='lanczos')
    else:
      img1 = ax[2].imshow(rec3, vmin=-scale, vmax=scale, cmap='seismic', interpolation='lanczos')
    ax[2].set_title("$G_{ref} - G_{k}$", fontsize=3*Hori)
    ax[2].set_xlabel("Receptores (m)", fontsize=3*Hori)
    ax[2].set_ylabel(" ", fontsize=3*Hori)
    ax[2].set_aspect('auto')
  else:
    fig, ax = plt.subplots(figsize=(Hori, Ver))
    if sismic is None:
      img1 = ax.imshow(rec, vmin=-scale, vmax=scale,cmap="gray", interpolation='lanczos')
    else:
      img1 = ax.imshow(rec, vmin=-scale, vmax=scale,cmap="seismic", interpolation='lanczos')
    ax.set_title("$G_{ref}$", fontsize=3*Hori)
    ax.set_xlabel("Receptores (m)", fontsize=3*Hori)
    ax.set_ylabel("Tempo (s)", fontsize=3*Hori)
    ax.set_aspect('auto')
