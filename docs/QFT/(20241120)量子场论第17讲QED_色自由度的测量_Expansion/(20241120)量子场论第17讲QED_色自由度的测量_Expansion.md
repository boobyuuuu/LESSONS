# 量子场论第17'讲：QED （色自由度的测量）

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/7912622033]



**内容提要**：

* 计算截面 $e^+e^-\to q\bar{q}$
* 实验上如何测量夸克颜色？

![]((20241120)量子场论第17讲QED_色自由度的测量_Expansion/v2-2479d57a902f543e7051ac5a1df68746_1440w.gif)  
![]((20241120)量子场论第17讲QED_色自由度的测量_Expansion/v2-d7aacfba37c7566db58ff0f7a291b6fa_1440w.jpg)  

我想计算 $e^+e^-\to q\bar{q}$ 的截面，首先写下拉氏量。

$\mathcal{L}=\mathcal{L}_e+\mathcal{L}_q+\mathcal{L}_\gamma$

$\mathcal{L}_e=\bar{\Psi}_e(i\not\!D_\mu-m_e)\Psi$

$\mathcal{L}_q=\bar{\Psi}_q(i\not\!D_\mu-m_q)\Psi_q$

$\mathcal{L}_\gamma=-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$

这里 $\not\!D\equiv\gamma^\mu D_\mu$ ， $D_\mu\equiv\partial_\mu-iQA_\mu$ ，对于不同的粒子，电荷Q是不同的。由此可以提取相互作用项。

$\mathcal{L}_{int}=-\mathcal{H}_{int}=Q_e\bar{\Psi}_e\gamma^\mu\Psi_eA_\mu+Q_q\bar{\Psi}_q\gamma^\mu\Psi_qA_\mu$ 。

对于过程 $e^-(p,s)+e^+(p',s')\to q(k,t)+\bar{q}(k',t')$ ，最低阶贡献是

$2\times\frac{(-i)^2}{2!}(-Q_e)(-Q_q)\langle k,t;k',t'|\mathcal{T}\bar{\Psi}_e(x)\gamma^\mu \Psi_e(x)A_\mu(x)\bar{\Psi}_q(y)\gamma^\nu\Psi_q(y)A_\nu(y)|p,s;p',s'\rangle$

按照Wick定理，我们可以得到

$i\mathcal{M}=\frac{iQ_eQ_q}{q^2+i\epsilon}[\bar{v}(p',s')\gamma^\mu u(p,s)][\bar{u}(k',t')\gamma_\mu v(k,t)]$ ，

模平方得到（这里的trick有两个：1）每一个方括号里面是一个复数，对于复数，我们有 $c^*=c^\dagger$；2） $(\gamma^\mu)^\dagger=\gamma^0\gamma^\mu\gamma^0$ ，不信可以验算（反正我自己学习的时候经常不信也是经常验算）。）

$|\mathcal{M}|^2=\frac{Q_e^2Q_q^2}{((p+p')^2)^2}[\bar{v}(p',s')\gamma^\mu u(p,s)\bar{u}(p,s)\gamma^\nu v(p',s')][\bar{u}(k',t')\gamma_\mu v(k,t)\bar{v}(k,t)\gamma_\nu u(k',t')]$

对于初态无极化的电子，我们需要求平均。对于末态夸克，我们不测量极化，需要求和，因此有

$\frac{1}{2}\sum_s\frac{1}{2}\sum_{s'}\sum_{t}\sum_{t'}$ 。

涉及到极化求和，我们自然想到学习Dirac方程时的有用公式。

$\sum_s u(p,s)\bar{u}(p,s)=\not\!p +m$ ， $\sum_s v(p,s)\bar{v}(p,s)=\not\!p -m$ 。

注意到上面的每一个方括号里面是一个复数，对于一个数，我们有 $Tr(c)=c$ 。因此

$\begin{eqnarray} &&[\bar{v}(p',s')\gamma^\mu u(p,s)\bar{u}(p,s)\gamma^\nu v(p',s')]\\ =&&Tr[\bar{v}(p',s')\gamma^\mu u(p,s)\bar{u}(p,s)\gamma^\nu v(p',s')]\\ =&&Tr[\gamma^\mu u(p,s)\bar{u}(p,s)\gamma^\nu v(p',s')\bar{v}(p',s')]\\ \end{eqnarray}$

自旋求和得到

$\sum_s\sum_{s'}Tr[\gamma^\mu u(p,s)\bar{u}(p,s)\gamma^\nu v(p',s')\bar{v}(p',s')]=Tr[\gamma^\mu (\not\!p+m_e)\gamma^\nu (\not\!p'-m_e)]$

类似地有

$\sum_t\sum_{t'}[\bar{u}(k',t')\gamma_\mu v(k,t)\bar{v}(k,t)\gamma_\nu u(k',t')]=Tr[\gamma_\mu(\not\!k-m_q)\gamma_\nu(\not\!k'+m_q)]$ 。

因此得到

$|\mathcal{M}|^2=\frac{1}{4}Tr[\gamma^\mu (\not\!p+m_e)\gamma^\nu (\not\!p'-m_e)]Tr[\gamma_\mu(\not\!k-m_q)\gamma_\nu(\not\!k'+m_q)]$

计算时，考虑到电子质量很小，一般我们会忽略掉。接下来计算需要用到gamma矩阵的性质，这个请参考任何一本量子场论书籍（比如Peskin的，或者Schwartz的附录）。最终结果是

$|\mathcal{M}|^2=\frac{8Q_e^2Q_q^2}{(p+p')^2}[(p\cdot k)(p'\cdot k')+(p\cdot k')(p'\cdot k)+m_q^2(p\cdot p')]$ 。

截面是洛伦兹不变的，我们选取质心系计算较方便。

$p=(E,0,0,E)$

$p'=(E,0,0,-E)$

$k=(E,\bold{k})$

$k'=(E,-\bold{k})$

利用截面振幅关系

$\frac{d\sigma}{d\Omega}=\frac{2}{E_{cm}^2}\frac{|\bold{k}|}{16\pi^2E_{cm}}|\mathcal{M}|^2$

得到

$\sigma=\frac{4\pi \alpha^2Q_q^2}{3E_{cm}^2}\sqrt{1-\frac{m_q^2}{E^2}}(1+\frac{1}{2}\frac{m_q^2}{E})$ 。

这里 $E_{cm}=2E$ 是质心能量，如果能量远远高于夸克质量，截面可以进一步近似为

$\sigma(e^+e^-\to q\bar{q})=\frac{4\pi \alpha^2Q_q^2}{3E_{cm}^2}$ 。

实验上怎么测量夸克带几种颜色的呢？实验上更喜欢测量R值来压低系统误差的影响。

$R_{had}=\frac{\sum_q\sigma(e^+e^-\to q\bar{q})}{\sigma(e^+e^-\to\mu^+\mu-)}=\sum_q Q_q^2$ 。

如果正负电子的对撞能量只能产生u,d,s夸克，那么R值为

$R_{uds}=\frac{2}{3}^2+\frac{1}{3}^2+\frac{1}{3}^2=\frac{6}{9}=\frac{2}{3}$ 。

可是实验测量结果在2附近，说明了夸克带3中颜色，末态有red/green/blue夸克。因此不仅要对自旋求和，也要对色自由度求和。

实验数据如下图所示，很坐标是质心能量，纵坐标是R值测量结果，虚线是上面的简单计算，实线是考虑了3-圈QCD的理论值。更多资料可以参考[#ref\_1](#ref\_1)。

![]((20241120)量子场论第17讲QED_色自由度的测量_Expansion/v2-4232906331915203059650c9ae493313_1440w.jpg)  
## 参考  

1. [#ref\_1\_0](#ref\_1\_0)PDG上面的高清图片 [https://pdg.lbl.gov/2022/reviews/rpp2022-rev-cross-section-plots.pdf](https://pdg.lbl.gov/2022/reviews/rpp2022-rev-cross-section-plots.pdf)
