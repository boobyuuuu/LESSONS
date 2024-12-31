# 量子场论第27讲：跑动耦合常数-QED

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/12313018851]



上一讲讨论了 $\phi^4$ 理论中跑动耦合常数的情况，这一讲看一下QED。我们会发现无论是 $\phi^4$ 理论还是QED理论，耦合常数都是随着能量的增大而增大的。将来如果你们有机会接触量子色动力学QCD的话，你会发现相反的情况，即渐进自由！

我们需要考虑的是光子传播子的1圈图修正，也即真空极化的贡献。

![]((20241213)量子场论第27讲跑动耦合常数-QED_Expansion/v2-99b818675739b0653fb7bc1b82e0f071_1440w.jpg)  

真空极化

  
  

$\begin{eqnarray} &&(-ie\gamma^\mu)\frac{-ig_{\mu\nu}}{p^2+i\epsilon}(-ie\gamma^\nu)\\ =&&(-ie_0\gamma^\mu)\frac{-ig_{\mu\nu}}{p^2+i\epsilon}(-ie_0\gamma^\nu)\\ &&+(-ie_0\gamma^\mu)\frac{-ig_{\mu\rho}}{p^2}(-1)tr[\int\frac{d^4q}{(2\pi)^4}\frac{i(\not q+m)}{q^2-m^2 }(-ie_0\gamma^\rho)\frac{i(\not q-\not p+m)}{(q-p)^2-m^2}(-ie_0\gamma^\sigma)]\frac{-ig_{\sigma\nu}}{p^2}(-ie_0\gamma^\nu)\\ &&+\cdots \end{eqnarray}$

费米子圈里面利用了trace技巧和费米交换的-1，原因如下。

$\cdots (-iQ)A_\rho(x)\bar\psi(x)\gamma^\rho\psi(x)\bar\psi(y)\gamma^\sigma\psi(y)A_\sigma(y)(-iQ)\cdots$

只有一种缩并， $\color{blue}{\bar\psi(x)}\gamma^\rho\color{red}{\psi(x)\bar\psi(y)}\gamma^\sigma\color{blue}{\psi(y)}$ ，红色和红色，蓝色和蓝色，但是要让蓝色相遇，必须交换(交换3次，因此有一个-1)和取trace。

为方便，我们定义

$\begin{eqnarray} i\Pi_2^{\rho\sigma}(p)\equiv&& (-1)tr[\int\frac{d^4q}{(2\pi)^4}\frac{i(\not q+m)}{q^2-m^2 }(-ie_0\gamma^\rho)\frac{i(\not q-\not p+m)}{(q-p)^2-m^2}(-ie_0\gamma^\sigma)]\\ =&&-e_0^2tr[\int\frac{d^4q}{(2\pi)^4}\frac{(\not q+m)\gamma^\rho (\not q-\not p+m)\gamma^\sigma}{(q^2-m^2)((q-p)^2-m^2)}]\\ =&&-e_0^2tr[\int\frac{d^4q}{(2\pi)^4}\frac{\not q\gamma^\rho (\not q-\not p)\gamma^\sigma+m^2\gamma^\rho\gamma^\sigma}{(q^2-m^2)((q-p)^2-m^2)}]\\ =&&-4e_0^2\int\frac{d^4q}{(2\pi)^4}\frac{q^\rho(q^\sigma-p^\sigma)-(q^2-q\cdot p)g^{\rho\sigma}+q^\sigma(q^\rho-p^\rho)+m^2g^{\rho\sigma}}{(q^2-m^2)((q-p)^2-m^2)} \end{eqnarray}$

也即有

$e^2\frac{-ig_{\mu\nu}}{p^2}=e_0^2[\frac{-ig_{\mu\nu}}{p^2}+\frac{-ig_{\mu\rho}}{p^2}i\Pi_2^{\rho\sigma}\frac{-ig_{\sigma\nu}}{p^2}+\cdots]$

下面来计算 $i\Pi_2^{\rho\sigma}(p)$ ，我们采用维度正规化。引入 $\int dxdy\delta(x+y-1)$ 。

分母变为

$[x(q^2-m^2)+y((q-p)^2-m^2)+i\epsilon]^2=(l^2-\Delta)^2$

这里 $l=q-yp$ ， $\Delta=m^2-y(1-y)p^2-i\epsilon$ 。

分子变为（去掉 $l$ 的奇数项，因为积分等于0）

$2l^\rho l^\sigma-l^2g^{\rho\sigma}-2y(1-y)p^\rho p^\sigma+[m^2+y(1-y)p^2]g^{\rho\sigma}$

然后进行Wick转动，让 $l^0=il_E^0$

$l^2=-l_E^2$ ，

分母变为 $(l_E^2+\Delta)^2$ 。

分子的第一项比较麻烦，注意到

$l^0 l^0=-l_E^0l_E^0 g^{00}$ ， $l^il^i=l_E^il_E^i(-g^{ii})$ ，

从积分完成的意义上我们有如下等价关系（因为分母只依赖于 $l_E^2$ ，每一个指标的积分是平权的。）

$l^\rho l^\sigma \to -\frac{1}{4}l_E^2g^{\rho\sigma}$

因此分子变为

$-\frac{2}{4}l_E^2g^{\rho\sigma}+l_E^2g^{\rho\sigma}-2y(1-y)p^\rho p^\sigma+[m^2+y(1-y)p^2]g^{\rho\sigma}$

把维度从4变为d。这是有很多改变， $\int \frac{d^4q}{(2\pi)^4}\to\mu^{4-d}\int\frac{d^dq}{(2\pi)^d}$ ， $l^\rho l^\sigma \to -\frac{1}{d}l_E^2g^{\rho\sigma}$ ，gamma矩阵的操作也应该相应变化（我们暂时不这么做，因为最终会抵消掉）。

分子$l_E^2$ 部分的积分为

$(1-\frac{2}{d})g^{\rho\sigma}\frac{1}{(4\pi)^{d/2}}\frac{d}{2}\Gamma(1-\frac{d}{2})(\frac{1}{\Delta})^{1-\frac{d}{2}}=-\frac{g^{\rho\sigma}\Delta}{(4\pi)^{d/2}}\Gamma(2-\frac{d}{2})(\frac{1}{\Delta})^{2-\frac{d}{2}}$ 。

右边为什么这么整理呢？是把 $\epsilon=4-d$ $\to 0$ 的发散部分放在一起方便后续操作！

分子不依赖 $l_E$ 部分的积分为

$[-2y(1-y)p^\rho p^\sigma+(m^2+y(1-y)p^2)g^{\rho\sigma}]\frac{1}{(4\pi)^{d/2}}\Gamma(2-\frac{d}{2})(\frac{1}{\Delta})^{2-\frac{d}{2}}$ 。

里面利用了如下积分公式。

![]((20241213)量子场论第27讲跑动耦合常数-QED_Expansion/v2-10950ffb2fdd9708184a973b9c368782_1440w.jpg)  

最终我们得到

$i\Pi_2^{\rho\sigma}(p)=\frac{-i4e_0^2}{(4\pi)^2}\Gamma(2-\frac{d}{2})\int dy2y(1-y)(\frac{4\pi \mu^2}{\Delta(p^2)})^{2-\frac{d}{2}}\times (p^2g^{\rho\sigma}-p^\rho p^\sigma)$

这个振幅也是满足Ward Identity的，因为 $p_\rho (i\Pi_2^{\rho\sigma})=0$ 。我们把左边那一块记作 $i\Pi_2(p^2)$ ，因此有

$i\Pi_2^{\rho\sigma}(p)=i\Pi_2(p^2)(p^2g^{\rho\sigma}-p^\rho p^\sigma)$ 。

$\Pi_2(p^2)=\frac{-8e_0^2}{(4\pi)^2}(\frac{2}{\epsilon}+\gamma_E)\int dyy(1-y)[1+\frac{1}{2}\ln\frac{4\pi\mu^2}{m^2-y(1-y)p^2}\epsilon]$

$\color{blue}{\Pi_2(p^2)=\frac{-8e_0^2}{(4\pi)^2}\int dyy(1-y)[\frac{2}{\epsilon}+\gamma_E+\ln\frac{4\pi\mu^2}{m^2-y(1-y)p^2}]}$

好不容易计算完了，回到最开始的地方。

$\begin{eqnarray} e^2\frac{-ig_{\mu\nu}}{p^2}=&&e_0^2[\frac{-ig_{\mu\nu}}{p^2}+\frac{-ig_{\mu\rho}}{p^2}i\Pi_2^{\rho\sigma}\frac{-ig_{\sigma\nu}}{p^2}+\cdots]\\ =&&e_0^2[\frac{-ig_{\mu\nu}}{p^2}+\Pi_2(p^2)(\frac{-ig_{\mu\nu}}{p^2}+\frac{ip^\mu p^\nu}{(p^2)^2})+\cdots]\\ \end{eqnarray}$

如果我告诉你由于Ward Identify上面右边正比于 $p^\mu p^\nu$ 对于S矩阵没有贡献，**你能接受吗？**如果不能接受，我们采用一般的光子传播子形式

$\frac{-i(g_{\mu\nu}-(1-\xi)\frac{p_\mu p_\nu}{p^2})}{p^2+i\epsilon}$ ，

我们知道**S矩阵的计算一定不依赖于规范 $\xi$ 的选择**。上面的结果即为

$\begin{eqnarray} e^2\frac{-i(g_{\mu\nu}-(1-\xi)\frac{p_\mu p_\nu}{p^2})}{p^2}=&&e_0^2[\frac{-i(g_{\mu\nu}-(1-\xi)\frac{p_\mu p_\nu}{p^2})}{p^2}+\Pi_2(p^2)(\frac{-ig_{\mu\nu}}{p^2}+\frac{ip^\mu p^\nu}{(p^2)^2})+\cdots]\\ \end{eqnarray}$

我们可以**选取 $\xi$ 使得下面的表达式成立**

$\color{red}{e^2(1-\xi)=e_0^2[(1-\xi)+\Pi_2(p^2)+\cdots]}$

那么有

$e^2=\frac{e_0^2}{1-\Pi_2(p^2)}=\frac{e_0^2}{1-\frac{-8e_0^2}{(4\pi)^2}\int dyy(1-y)[\frac{2}{\epsilon}+\gamma_E+\ln\frac{4\pi\mu^2}{m^2-y(1-y)p^2}]}$ 。

这里 $\Pi_2(p^2)$ 是无穷大的，如何理解这个结果呢？真正实验测量的电荷肯定是有限大小的。比如，我们在 $p^2\to 0$ 的实验环境下测量电荷记作 $e_{ref}$ 。那么有

$e_{ref}^2=\frac{e_0^2}{1-\frac{-8e_0^2}{(4\pi)^2}\int dyy(1-y)[\frac{2}{\epsilon}+\gamma_E+\ln\frac{4\pi\mu^2}{m^2}]}$

解之得到

$e_0^2=\frac{e_{ref}^2}{1+\frac{-8e_{ref}^2}{(4\pi)^2}\int dyy(1-y)[\frac{2}{\epsilon}+\gamma_E+\ln\frac{4\pi\mu^2}{m^2}]}$

那么对于其他实验条件下的电荷的观测值为

$e^2(p^2)=\frac{e_{ref}^2}{1-e_{ref}^2\frac{8}{(4\pi)^2}\int dyy(1-y)\ln\frac{m^2}{m^2-y(1-y)p^2}}$

这个表达式里面所有的量都是有限大的。我们计算得到的无穷大是因为我们不知道高能标下的新物理情况（一个完整的新物理，肯定不会出现无穷大。所以无穷大体现了我们真实的ignorance。我们要接受它！），我们把无穷大都扔给 $e_0$ ，因为实验上 $e_0$ 是不可观测的！

如果 $|p^2|<<m^2$ ，那么有

$e^2(p^2)\approx\frac{e_{ref}^2}{1-e_{ref}^2\frac{8}{(4\pi)^2}\int dyy(1-y)\frac{y(1-y)p^2}{m^2}}$

也即

$\alpha(p^2)\approx\frac{\alpha_{ref}}{1-\alpha_{ref}\frac{2}{\pi}\frac{p^2}{m^2}\int dyy^2(1-y)^2}$

我们看到对于s道，随着能量的增大，电磁耦合强度变大。

另外一方面，注意到**分母可能等于0，存在Landau pole的问题。说明QED在高能一定会有新物理出现，即电弱统一理论**。

---

![]((20241213)量子场论第27讲跑动耦合常数-QED_Expansion/v2-1548fe284179edb91078c9591b1cbbb9_1440w.jpg)  
