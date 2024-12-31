# 量子场论第21‘讲：Ward-Takahashi恒等式

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/10596597980]



我们在最开始推导光子传播子时用到过Ward-Takahashi Identity。它说的是：涉及一个动量为 $k^\mu$ 在壳光子的振幅 $\mathcal M=\epsilon_\mu^*(k,\lambda)\mathcal M^\mu$ ，满足

$k_\mu \mathcal M^\mu=0$ 。

![]((20241214)量子场论第21讲Ward-Takahashi恒等式_Expansion/v2-83107b60c29968627b1dd0dedafb592d_1440w.jpg)  

John Civil Ward

  
  
![]((20241214)量子场论第21讲Ward-Takahashi恒等式_Expansion/v2-9f6b64e450486aa62869b7130b493936_1440w.jpg)  

在讲这个之前，我们考察一下如下的拉氏量。

$\mathcal L=\bar\psi(i\gamma^\mu\partial_\mu-M)\psi +\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{1}{2}m^2\phi^2+ Q\bar\psi\gamma^\mu\psi\partial_\mu\phi$

它描述的是一个Dirac量、一个标量场以及它们之间的相互作用。

* 注意到如果标量场的质量为0的话，我们如下global对称性。

$\psi \to e^{i\theta_1}\psi$ ， $\bar\psi \to e^{-i\theta_1}\bar\psi$ ， $\phi \to \phi+\theta_2$

对应的守恒流是

$j_1^\mu = \bar\psi \gamma^\mu \psi$ ， $j_2^\mu=\partial^\mu\phi+Q\bar\psi\gamma^\mu\psi$

二者等价于 $\bar\psi\gamma^\mu\psi$ 和 $\partial^\mu\phi$ 都是守恒流。

下面计算一个物理过程 $\phi (k)+\psi(p) \to \phi(k')+\psi(p')$ 的散射振幅。这个过程有两张费曼图的贡献，类似于康普顿散射（Compton scattering），仔细计算可以得到：

$i\mathcal M=-iQ^2\bar u(p',s')[(1+\frac{m^2}{2p\cdot k’})\not k'+(-1+\frac{m^2}{2p\cdot k}\not k)]u(p,s)$

如果 $m \neq 0$ ，这个振幅不会等于0。**但是如果这个标量粒子质量为0的话**，注意到 $p+k=p'+k'$ 我们有

$\begin{eqnarray} i\mathcal M&=&-iQ^2\bar u(p',s')(\not k'-\not k)u(p,s)\\ &=&-iQ^2\bar u(p',s')(\not p-\not p')u(p,s)\\ &=&-iQ^2\bar u(p',s')[(\not p-M)-(\not p'-M)]u(p,s)\\ &=& 0 \end{eqnarray}$

上面我们利用了 $(\not p-M)u(p,s)=0$ 和 $\bar u(p',s')(\not p'-M)=0$ 。

**这个结果看起来是不可思议的，因为上面的拉氏量看起来是那么的人畜无害。我认为这是Ward-Takahashi Identity的结果**。

**一个naive的理解**是，我们有守恒流 $\partial_\mu j_1^\mu=\partial_\mu(\bar\psi\gamma^\mu\psi)=0$ ，那么相互作用项为

$\begin{eqnarray} \mathcal L_{int}&=&Q\bar\psi\gamma^\mu\psi\partial_\mu\phi\\ &=&Q\bar\psi\gamma^\mu\psi\partial_\mu\phi+Q\partial_\mu(\bar\psi\gamma^\mu\psi)\phi\\ &=&Q\partial_\mu(\bar\psi\gamma^\mu\psi\phi)\\ &=&0 \end{eqnarray}$

上面的推导利用了 $\partial_\mu j_1^\mu=0$ 和“抛弃”全微分项。**Magically，我们发现相互作用消失了**。

我们已经知道S矩阵的振幅“约等于”n点关联函数。下面利用路径积分和Schwinger-Dyson的思想，推导这个等式。我感觉Schwinger-Dyson equation像是量子力学版本的Euler-Lagrangian方程。

考虑QED的路径积分。

$G(x_1,x_2)=\int \mathcal D\bar\psi\mathcal D\psi\mathcal A\exp[i\int d^4x \bar\psi i\gamma^\mu\partial_\mu\psi-m\bar\psi\psi-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}-Q\bar\psi\gamma^\mu\psi A_\mu]\psi(x_2)\bar\psi(x_1)$

考虑一个无穷小的平移操作： $\psi(x) \to \psi(x)+iQ\theta(x)\psi(x)$ ， $\bar\psi(x) \to \bar\psi(x)-iQ\theta(x)\bar\psi(x)$ ，我们得到

$\begin{eqnarray} G(x_1,x_2)=&&\int \mathcal D\bar\psi\mathcal D\psi\mathcal A\exp[i\int d^4x(\mathcal L_0+iQ\bar\psi(x)i\gamma^\mu\partial_\mu\theta(x)\psi(x))]\\ &&\times (1+iQ\theta(x_2))\psi(x_2)(1-iQ\theta(x_1))\bar\psi(x_1) \end{eqnarray}$

因为这是一个平移，而路径积分会遍及所有路径，因此不影响物理结果。我们要求 $\frac{\delta G(x_1,x_2)}{\delta\theta(x)}=0$ 。展开到 $\theta(x)$ 的一阶有：

$\begin{eqnarray} \delta G(x_1,x_2)=&&\int \mathcal D\bar\psi\mathcal D\psi\mathcal Ae^{i\int d^4x\mathcal L_0}\\ &&\times (-i\int d^4x Q\bar\psi(x)\gamma^\mu\partial_\mu\theta(x)\psi(x)\psi(x_2)\bar\psi(x_1)-iQ\theta(x_1)\psi(x_2)\bar\psi(x_1)+iQ\theta(x_2)\psi(x_2)\bar\psi(x_1))\\ =&&\int \mathcal D\bar\psi\mathcal D\psi\mathcal Ae^{i\int d^4x\mathcal L_0}\\ &&\times (i\int d^4x \theta(x) Q\partial_\mu(\bar\psi(x)\gamma^\mu\psi(x))\psi(x_2)\bar\psi(x_1)-iQ\theta(x_1)\psi(x_2)\bar\psi(x_1)+iQ\theta(x_2)\psi(x_2)\bar\psi(x_1))\\ \end{eqnarray}$

也即

$\color{blue}{\langle 0|iQ\partial_\mu(\bar\psi(x)\gamma^\mu\psi(x))\psi(x_2)\bar\psi(x_1)|0\rangle=\delta(x-x_1)\langle 0|iQ\psi(x_2)\bar\psi(x_1)|0\rangle-\delta(x-x_2)\langle 0|iQ\psi(x_2)\bar\psi(x_1)|0\rangle}$ 为了得到散射振幅信息，我们插入完备性关系。

$\begin{eqnarray} &&\langle 0|\psi(x_2)f(\psi(x),\bar\psi(x))\bar\psi(x_1)|0\rangle\\ =&&\sum_{s_2,s_1}\int dp_2dp_1\langle 0|\psi(x_2)|p_2,s_2\rangle \langle p_2,s_2|f(\psi(x),\bar\psi(x))|p_1,s_1\rangle\langle p_1,s_1|\bar\psi(x_1)|0\rangle\\ =&&\sum_{s_2,s_1}\int dp_2dp_1 u(p_2,s_2)e^{-ip_2x_2}\langle p_2,s_2|f(\psi(x),\bar\psi(x))|p_1,s_1\rangle\bar u(p_1,s_1)e^{ip_1x_1} \end{eqnarray}$

然后进行Fourier变换，进入动量空间

$\int d^4xe^{-ikx}\int dx_1 e^{-ip_1'x_1}\int dx_2e^{ip_2'x_2}$

得到（原则上我得到p1',p2'，但是我仍然写成p1,p2。相信大家懂我！）

$\sum_{s_2,s_1} u(p_2,s_2)\int d^4x \langle p_2,s_2|f(\psi(x),\bar\psi(x))|p_1,s_1\rangle\bar u(p_1,s_1)$

左边乘以 $\bar u(p_2,s_2')$ ，右边乘以 $u(p_1,s_1')$ ，利用正交关系 $\bar u(p,s)u(p,t)=2m\delta_{st}$ ，得到（原则上我得到s1',s2'，但是我任然写成s1,s2，相信大家懂我！）

$\int d^4x \langle p_2,s_2|f(\psi(x),\bar\psi(x))|p_1,s_1\rangle$

把上面蓝色的公式的每一项按照上面的操作步骤走一遍（**Peskin书上9.104立刻跳到9.105，不是特别友好！**），得到：

$\int d^4x e^{-ikx}\langle p_2,s_2|iQ\partial_\mu(\bar\psi(x)\gamma^\mu\psi(x))|p_1,s_1\rangle=\langle p_2,s_2|iQ|p_1+k,s_1\rangle-\langle p_2-k,s_2|iQ|p_1,s_1\rangle$

左边代入 $\psi(x)$ 和 $\bar\psi(x)$ 的具体表达式得到：

$\int d^4x e^{-ikx}\partial_\mu[\bar u(p_2,s_2)iQ\gamma^\mu u(p_1,s_1)e^{-i(p_1-p_2)x}]$

$-i(p_1-p_2)_\mu\delta(p_1-p_2+k)\bar u(p_2,s_2)iQ\gamma^\mu u(p_1,s_1)$

$ik_\mu\bar u(p_2,s_2)iQ\gamma^\mu u(p_1,s_1)$ $\delta(p_1-p_2+k)$

跟初态有一个光子的振幅是一模一样的

$-\epsilon_\mu(k,\lambda)\bar u(p_2,s_2)iQ\gamma^\mu u(p_1,s_1) \equiv \epsilon_\mu(k,\lambda)\mathcal M^\mu(k;p_1,s_1; p_2,s_2)$

因此我们有

$-ik_\mu\mathcal M^\mu(k;p_1,s_1 \to p_2,s_2)=iQ\mathcal M(p_1+k,s_1 \to p_2,s_2)-iQ\mathcal M(p_1,s_1 \to p_2-k,s_2)$

对于在壳的光子和电子， $p_1+k$ 或者 $p_2-k$ 都不可能是一个在壳电子的四动量 $(p_1+k)^2\ne m^2$ ，因此右边的振幅对于S矩阵没有贡献，从而得到 $k_\mu\mathcal M^\mu =0$ 。

---

![]((20241214)量子场论第21讲Ward-Takahashi恒等式_Expansion/v2-573b01e58306dbf26c7e367ed49855a4_1440w.jpg)  
