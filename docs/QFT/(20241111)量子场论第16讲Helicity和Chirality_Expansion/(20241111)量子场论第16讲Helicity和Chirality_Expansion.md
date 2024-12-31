# 量子场论第16''讲：Helicity和Chirality

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/6240877165]

![]((20241111)量子场论第16讲Helicity和Chirality_Expansion/v2-4d140cab435c0fb611aaa57f4ce1f6a1_1440w.jpg)  

左手，右手一个......

  
  

我们已经已经知道Dirac场可以通过Lorentz群的(1/2,0)和(0,1/2)表示来构造，也即

$\mathcal{L}=\chi^\dagger i\bar{\sigma}^\mu\partial_\mu\chi+\eta^\dagger i\sigma^\mu \partial_\mu \eta -m(\chi^\dagger\eta+\eta^\dagger\chi)$ ， （\*）

这里 $\chi$ 和 $\eta$ 分别服从(1/2,0)和(0,1/2)表示。

引入 $\psi\equiv\begin{pmatrix}\chi \\\eta\end{pmatrix}$ 和 $\gamma^\mu\equiv\begin{pmatrix} 0 & \sigma^\mu \\\bar{\sigma}^\mu & 0\end{pmatrix}$ ，我们得到通常的Dirac拉氏量

$\mathcal{L}=\bar{\psi}(i\gamma^\mu\partial_\mu-m)\psi$ 。

观察(\*)式，如果没有质量项，我们会发现 $\chi$ 和 $\eta$ 是独立的。为了研究方便研究**空间反射对称性**（我们知道中国人对于弱作用中宇称不守恒定律的发现做出了重大的贡献！），我们需要把 $\chi$ 和 $\eta$ 分开。为什么呢？因为

对于 $p=(E,\bold{p})$ ，我们定义 $\tilde{p}\equiv(E,-\bold{p})$ 。考虑正粒子解

$\begin{pmatrix}\chi \\\eta\end{pmatrix}=\begin{pmatrix}\sqrt{p\cdot\sigma}\xi\\ \sqrt{p\cdot\bar{\sigma}}\xi\end{pmatrix}$ ，

从一个空间反演变换（ $p \to \tilde{p}$ ，但是自旋状态不变），我们得到

$\begin{pmatrix}\chi(p) \\\eta(p)\end{pmatrix}=\begin{pmatrix}\sqrt{p\cdot\sigma}\xi\\ \sqrt{p\cdot\bar{\sigma}}\xi\end{pmatrix} \to \begin{pmatrix}\chi(\tilde{p}) \\\eta(\tilde{p})\end{pmatrix}=\begin{pmatrix}\sqrt{\tilde{p}\cdot\sigma}\xi\\ \sqrt{\tilde{p}\cdot\bar{\sigma}}\xi\end{pmatrix}=\begin{pmatrix}\sqrt{p\cdot\bar{\sigma}}\xi\\ \sqrt{p\cdot\sigma}\xi\end{pmatrix}=\begin{pmatrix}\eta(p) \\\chi(p)\end{pmatrix}$

我们发现空间宇称变换会交换 $\chi$ 和 $\eta$ 。类似的，我们有

$\chi^\dagger i\bar{\sigma}^\mu\partial_\mu\chi\to\eta^\dagger i\sigma^\mu \partial_\mu \eta$

为了分开 $\chi$ 和 $\eta$ ，我们引入 $\gamma^5$ 矩阵

$\gamma^5\equiv\begin{pmatrix} -1 & 0\\0 & 1\end{pmatrix}$

它有这些性质 $\gamma^5\gamma^5=1$ ， $\{\gamma^5,\gamma^\mu\}=0$ 。

显然我们有

$\begin{pmatrix} -1 & 0\\0 & 1\end{pmatrix}\begin{pmatrix} \chi \\0 \end{pmatrix}=-\begin{pmatrix} \chi \\0 \end{pmatrix}$

$\begin{pmatrix} -1 & 0\\0 & 1\end{pmatrix}\begin{pmatrix} 0 \\\eta \end{pmatrix}=+\begin{pmatrix} 0 \\ \eta \end{pmatrix}$

我们看到 $(\chi,0)^T$ 和 $(0,\eta)^T$ 是它的本征态，分别称为左手和右手的chirality态。注意到

$\begin{pmatrix} \chi \\0 \end{pmatrix}=\frac{1-\gamma^5}{2}\psi\equiv\psi_L$ ， $\begin{pmatrix} 0 \\\eta \end{pmatrix}=\frac{1+\gamma^5}{2}\psi\equiv\psi_R$ ，

拉氏量变为

$\mathcal{L}=\bar{\psi}_Li\gamma^\mu\partial_\mu\psi_L+\bar{\psi}_Ri\gamma^\mu\partial_\mu\psi_R-m(\bar{\psi}_L\psi_R+\bar{\psi}_R\psi_L)$ 。

里面用到了

$\bar{\psi}_L\gamma^\mu\psi_R=\bar{\psi}_R\gamma^\mu\psi_L=\bar{\psi}_L\psi_L=\bar{\psi}_R\psi_R=0$ 。

如果没有质量项，我们有守恒流

$j^{\mu5}\equiv\bar{\psi}_R\gamma^\mu\psi_R-\bar{\psi}_L\partial_\mu\psi_L=\bar{\psi}\gamma^\mu\gamma^5\psi$ ，

$\partial_\mu j^{\mu5}=0$ ，

这个守恒流称作轴矢流(axial vector current)，对应的是chiral transformation， $\psi \to e^{i\gamma^5 \theta}\psi$ 。

就像U(1)transformation， $\psi \to e^{i \theta}\psi$ ，对应的是矢量流守恒（电荷守恒） $j^\mu\equiv \bar{\psi}\gamma^\mu\psi$ 。

如果一个理论，只包含左手成分，比如

$\mathcal{L}=(\bar{\psi}_L(v),\bar{\psi}_L(e))i\gamma^\mu(\partial_\mu+ig\frac{\vec{\sigma}}{2}\cdot\vec{W})\begin{pmatrix}\psi_L(v) \\\psi_L(e)\end{pmatrix}$ 。

那么它导致的物理过程显然不会满足宇称守恒（并且是宇称最大破坏的！）。这正是弱作用拉氏量的一部分，它描述了beta衰变（比如吴健雄做实验用的Co-60）等过程。

其中一项是

$\mathcal{L}_I=ig\bar{\psi}_L(v)\gamma^\mu\psi_L(e)W_\mu^++c.c.$ ，

其中 $W_\mu$ 表示自旋为1的 $W^\pm$ 玻色子。

Chirality和Helicity是两个特别相似的物理量。前者理论家喜欢，后者实验家喜欢。

我们来看看Dirac方程的解。

$u(p,s)=\begin{pmatrix}\sqrt{\sigma\cdot p}\xi^s \\\sqrt{\bar{\sigma}\cdot p}\xi^s\end{pmatrix}$

注意到

$\sigma\cdot p=E-\vec{p}\cdot\vec{\sigma}$ ， $\bar{\sigma}\cdot p=E+\vec{p}\cdot\vec{\sigma}$ 。

定义helicity算符(自旋在动量方向的投影)为

$h\equiv \frac{\vec{p}}{|\vec{p}|}\cdot \vec{s}=\frac{1}{2|\vec{p}|}\vec{p}\cdot\vec{\sigma}$ 。

假设 $\xi$ 是它的一个本征态， $h\xi=\frac{1}{2}\xi$ ，那么

$u(p,s)=\begin{pmatrix}\sqrt{E-|\vec{p}|}\xi \\\sqrt{E+|\vec{p}|}\xi^s\end{pmatrix}$ 。

如果E>>m（或者m=0)，我们有

$u(p,s)=\begin{pmatrix}\sqrt{E-|\vec{p}|}\xi \\\sqrt{E+|\vec{p}|}\xi^s\end{pmatrix} \to \begin{pmatrix} 0 \\ \sqrt{2E} \xi\end{pmatrix}$

这正好也是chirality的右手态 $\psi_R$ 。

类似地，如果 $h\xi=-\frac{1}{2}\xi$ ， $u(p,s)=\begin{pmatrix}\sqrt{E+|\vec{p}|}\xi \\\sqrt{E-|\vec{p}|}\xi^s\end{pmatrix} \to \begin{pmatrix}  \sqrt{2E} \xi\\0\end{pmatrix}$ ，这也是chirality的左手态 $\psi_L$ 。

因此如果这个费米子没有质量，那么chirality和helicity的本征态是相同的。如果质量不为0，那么它们在高能情况下是近似相同的。

$  $

