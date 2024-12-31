# 量子场论第16讲：Dirac方程的解和量子化

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/3428332354]



**内容提要**：

* 求解Dirac方程
* Dirac场的量子化

首先来一个预备知识，如果M是一个矩阵，如果求它的平方根呢？假设M可以对角化

$M=P^{-1}DP$ ，

其中D是对角矩阵，P是可逆矩阵。那么我们有

$(P^{-1}\sqrt{D}P)^2=P^{-1}\sqrt{D}PP^{-1}\sqrt{D}P=M$ ，

因此我们可以定义

$\sqrt{M}=P^{-1}\sqrt{D}P$ 。

Peskin书上面求解Dirac方程的方法，是首先得到质心系（即粒子静止参考系）下的解，然后通过Lorentz Boost得到一般参考系的解。这里我们**用一个稍微不同的方法**。

首先写下Dirac方程。

$(i\gamma^\mu\partial_\mu -m)\psi=0$ ，

一般的解可以写成

$\psi(x)=\sum_s\int\frac{d^3p}{(2\pi)^3\sqrt{2E_p}}[u(p,s)a(p,s)e^{-ipx}+v(p,s)b^\dagger(p,s)e^{ipx}]$ ，

$\psi^\dagger(x)=\sum_s\int\frac{d^3p}{(2\pi)^3\sqrt{2E_p}}[v^\dagger(p,s)b(p,s)e^{-ipx}+u^\dagger(p,s)a^\dagger(p,s)e^{ipx}]$

$\bar{\psi}(x)=\sum_s\int\frac{d^3p}{(2\pi)^3\sqrt{2E_p}}[\bar{v}(p,s)b(p,s)e^{-ipx}+\bar{u}(p,s)a^\dagger(p,s)e^{ipx}]$

这里 $a(p,s)$ 和 $b^\dagger(p,s)$ 是湮灭产生算符，s表示自旋状态。

这里我们考虑 $u(p,s)$ 。它满足

$(\gamma^\mu p_\mu-m)u(p,s)=0$

写成矩阵为

$\begin{pmatrix}-m & \sigma^\mu p_\mu \\ \bar{\sigma}^\mu p_\mu & -m\end{pmatrix}\begin{pmatrix}\chi \\ \eta\end{pmatrix} = 0$

也即

$(\sigma\cdot p )\eta\equiv \sigma^\mu p_\mu \eta=m\chi$ ，

$(\bar{\sigma}\cdot p)\chi \equiv\bar{\sigma}^\mu p_\mu \chi=m\eta$

Formally，我们得到

$\frac{\chi}{\eta}=\frac{\sqrt{\sigma\cdot p}}{\sqrt{\bar{\sigma}\cdot p}}$ ，

因此有

$u(p,s)=\begin{pmatrix}\sqrt{\sigma\cdot p}\xi^s \\\sqrt{\bar{\sigma}\cdot p}\xi^s \end{pmatrix}$ ，

这里如果我们选取归一化 $\xi^{s\dagger}\xi^t=\delta^{st}$ ，这样得到 $\bar{u}(p,s)u(p,t)=2m\delta^{st}$ ，这个是洛伦兹不变的。

类似地，我们可以得到

$v(p,s)=\begin{pmatrix}\sqrt{\sigma\cdot p}\zeta^s \\-\sqrt{\bar{\sigma}\cdot p}\zeta^s \end{pmatrix}$ ，且 $\bar{v}(p,t)v(p,s)=-2m\delta^{st}$ 。

作为**家庭作业**，请证明：

$\bar{u}(p,s)v(p,t)=\bar{v}(p,t)u(p,s)=0$

$\sum_s u(p,s)\bar{u}(p,s)=\gamma^\mu p_\mu +m$

$\sum_s v(p,s)\bar{v}(p,s)=\gamma^\mu p_\mu -m$ 。

它们在计算散射振幅时经常用到。

下面量子化的过程跟标量场是类似的，但是我们需要强加**反对易关系**。

按照我们原来对标量场的处理方式，先从拉氏量得到正则动量

$\mathcal{L}=\bar{\psi}(i\gamma^\mu\partial_\mu-m)\psi$

然后强加反对易关系

$\pi\equiv \frac{\partial \mathcal{L}}{\partial \dot{\psi}}=\bar{\psi}i\gamma^0=i\psi^\dagger$

$\{\psi_a(t,\bold{x}),\pi_b(t,\bold{y})\}=i\delta^{(3)}(\bold{x}-\bold{y})\delta_{ab}$

也即

$\{\psi_a(t,\bold{x}),\psi_b^\dagger (t,\bold{y})\}=\delta^{(3)}(\bold{x}-\bold{y})\delta_{ab}$ ，

其他对易关系为0。

为了得到产生湮灭算符之间的反对易关系，我们需要利用如下结果

$u^\dagger(p,s)u(p,t)=\xi^{s\dagger}(\sigma\cdot p+\bar{\sigma}\cdot p)\xi^t=2E_p\delta^{st}=v^\dagger(p,s)v(p,t)$ ,

$u^\dagger(\bold{p},s)v(-\bold{p},t)=\xi^{s\dagger}(m-m)\zeta^t=0=v^\dagger(\bold{p},s)u(-\bold{p},t)$

得到

$\int d^3x u^\dagger(k,t)\psi(x)e^{ikx}=\sqrt{2E_k}a(k,t)$

$\int d^3x \psi^\dagger(x)u(k,t)e^{-ikx}=\sqrt{2E_k}a^\dagger(k,t)$

$\int d^3x v^\dagger(k,t)\psi(x)e^{-ikx}=\sqrt{2E_k}b^\dagger(k,t)$

$\int d^3x \psi^\dagger(x)v(k,t)e^{ikx}=\sqrt{2E_k}b^\dagger(k,t)$

最后利用 $\psi$ 和 $\psi^\dagger$ 的反对易关系，我们可以得到

$\{a(p,s),a^\dagger(q,t)\}=\{b(p,s),b^\dagger(q,t)\}=(2\pi)^3\delta^{(3)}(\bold{p}-\bold{q})\delta^{st}$

以及

$\{a(p,s),a(q,t)\}=\{a^\dagger(p,s),a^\dagger(q,t)\}=\{b(p,s),b(q,t)\}=\{b^\dagger(p,s),b^\dagger(q,t)\}=0$ 。

反对易关系和对易关系的差别是很大的。如果 $p=q,s=t$ ，我们可以得到

$aa=a^\dagger a^\dagger=bb=b^\dagger b^\dagger=0$ 。

说明两个费米子不能占据相同的状态。

我们也可以定义如下的单粒子态

$|p,s\rangle=\sqrt{2E_p}a^\dagger(p,s)|0\rangle$ 是产生一个动量为p，自旋状态为s的费米子。

有兴趣的同学可以调研一下**spin-statistics relation**。

* 洛伦兹不变性
* 正能量
* 正的norm
* 因果性

如果以上四点满足，Pauli等人得出：整数自旋的粒子服从Bose-Einstein统计关系，半整数粒子服从Fermi-Dirac统计关系。

Dirac场的传播子定义为

$S_F(x-y)\equiv \theta(x^0-y^0)\langle 0|\psi(x)\bar{\psi}(y)|0\rangle-\theta(y^0-x^0)\langle 0|\bar{\psi}(y)\psi(x)|0\rangle$

$\begin{eqnarray}\langle 0 |\psi_a(x)\bar{\psi}_b(y)|0\rangle=&&\int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p}(\gamma^\mu p_\mu+m)e^{-ip(x-y)}\\ =&&(i\gamma^\mu\frac{\partial}{\partial x^\mu}+m)\int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p}e^{-ip(x-y)}\\ =&&(i\gamma^\mu\frac{\partial}{\partial x^\mu}+m)\int\frac{d^3p}{(2\pi)^4}\frac{i}{p^2-m^2+i\epsilon}e^{-ip(x-y)}\\ =&&\int\frac{d^3p}{(2\pi)^4}\frac{i(\gamma^\mu p_\mu+m)}{p^2-m^2+i\epsilon}e^{-ip(x-y)}\\ \end{eqnarray}$

因此动量空间的Dirac传播子为

$S_F(p)=\frac{i(\gamma\cdot p+m)}{p^2-m^2+i\epsilon}$ 。

