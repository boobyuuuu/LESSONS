# 量子场论第28讲：质量重整化-QED

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/12518684501]



今天算一下QED中电子的质量修正，也即电子传播子的1圈修正。里面有两个无穷大，低动量的（也叫红外发散）和高动量的（也叫紫外发散）。

![]((20241218)量子场论第28讲质量重整化-QED_Expansion/v2-22a01f96e3c1a44abcf4c25e178612b5_1440w.jpg)  

电子自能修正

  
  

$\frac{i}{\not p-m}=\frac{i}{\not p-m_0}+\frac{i}{\not p -m_0}\int \frac{d^4q}{(2\pi)^4}\frac{-ig_{\mu\nu}}{(q-p)^2+i\epsilon}(-ie\gamma_\mu)\frac{i(\not q+m_0)}{q^2-m_0^2+i\epsilon}(-ie\gamma_\nu)\frac{i}{\not p -m_0}+\cdots$

一般我们把中间的积分记作 $-i\Sigma_2(p)$ 。

$\frac{i}{\not p-m}=\frac{i}{\not p-m_0}+\frac{i}{\not p -m_0}(-i\Sigma_2(p))\frac{i}{\not p -m_0}+\cdots$

$-i\Sigma_2(p)=\int \frac{d^4q}{(2\pi)^4}\frac{-ig_{\mu\nu}}{(q-p)^2+i\epsilon}(-ie\gamma_\mu)\frac{i(\not q+m_0)}{q^2-m_0^2+i\epsilon}(-ie\gamma_\nu)$

$-i\Sigma_2(p)=(-ie)^2\int \frac{d^4q}{(2\pi)^4}\frac{\gamma^\mu(\not q+m_0)\gamma_\mu}{((q-p)^2-a^2+i\epsilon)(q^2-m_0^2+i\epsilon)}$

这里我们因为有红外发散，假设光子有一个质量a来“正规化”（这个发散最终和顶点的红外发散以及辐射修正抵消掉。是一个非常物理的结果！）。

利用Feynman's trick， $\int dxdy\delta(x+y-1)\cdots$ 。分母为

$[x((q-p)^2-a^2)+y(q^2-m_0^2)]^2=[q^2-2xp\cdot q+xp^2-xa^2-ym_0^2]^2=(l^2-\Delta)^2$

这里定义 $l=q-xp$ ， $\Delta=xa^2+ym_0^2-x(1-x)p^2$ 。

分子为

$\gamma^\mu(\not q+m_0)\gamma_\mu=\gamma^\mu( \not l+x\not p+m_0)\gamma_\mu$ 。

$l$ 的奇数次幂的积分为0，因此积分为

$-i\Sigma_2(p)=-e^2\int dxdy\delta(x+y-1)\int \frac{d^4l}{(2\pi)^4}\frac{\gamma^\mu (x\not p + m_0 )\gamma_\mu}{(l^2-\Delta)^2}$ 。

接着进行Wick rotation，引入 $l^0=il_E^0$ ，得到

$\Sigma_2(p)=e^2\int dx\int \frac{d^4l_E}{(2\pi)^4}\frac{\gamma^\mu (x\not p + m_0 )\gamma_\mu}{(l_E^2+\Delta)^2}$ ，

$\Delta=xa^2+(1-x)m_0^2-x(1-x)p^2$

最后进行维度正规化，我们需要进行 $4 \to d$ 。这里有如下变化 $\epsilon\equiv 4-d$ 。

$\int d^4l_E \to \mu^{4-d}\int d^dl_E$ ，

Dirac gamma矩阵也要推广到d维，一共有d个，满足 $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ 和tr(1)=d。

$\gamma^\mu\gamma_\mu=\gamma^\mu\gamma^\nu g_{\mu\nu}=g^{\mu\nu}g_{\mu\nu} = 4 \to d$

$\gamma^\mu\gamma^\nu\gamma_\mu=2g^{\mu\nu}\gamma_\mu-\gamma^\nu\gamma^\mu\gamma_\mu=2\gamma^\nu-d\gamma^\nu=(2-d)\gamma^\nu$

利用如下积分公式

![]((20241218)量子场论第28讲质量重整化-QED_Expansion/v2-10950ffb2fdd9708184a973b9c368782_1440w.jpg)  

那么积分结果为

$\begin{eqnarray} \Sigma_2(p)=&&\frac{e^2}{(4\pi)^{2}}\int dx\Gamma(2-\frac{d}{2})(\frac{4\pi \mu^2}{\Delta})^{2-\frac{d}{2}}((2-d)x\not p+dm_0)\\ =&&\frac{e^2}{(4\pi)^{2}}\int dx(\frac{2}{\epsilon}+\gamma_E)(1+\frac{\epsilon}{2}\ln\frac{4\pi\mu^2}{\Delta})((-2+\epsilon)x\not p+(4-\epsilon)m_0)\\ =&&\frac{e^2}{(4\pi)^{2}}\int dx(\frac{2}{\epsilon}+\gamma_E)(1+\frac{\epsilon}{2}\ln\frac{4\pi\mu^2}{\Delta}(-2x\not p+4m_0)+(-2+\epsilon)x\not p+(4-\epsilon)m_0)\\ =&&\frac{e^2}{(4\pi)^{2}}\int dx((\frac{2}{\epsilon}+\gamma_E)(1-2x\not p+4m_0)+\ln\frac{4\pi\mu^2}{\Delta}(-2x\not p+4m_0)+2x\not p-2m_0) \end{eqnarray}$ 。

我们回到原来的地方。

$\frac{i}{\not p-m}=\frac{i}{\not p-m_0}+\frac{i}{\not p -m_0}(-i\Sigma_2(p))\frac{i}{\not p -m_0}+\cdots=\frac{i}{(\not p-m_0)(1+i\Sigma_2(p)\frac{i}{\not p-m_0})}=\frac{i}{\not p-m_0-\Sigma_2(p)}$

比较可以得到

$m(p)=m_0+\Sigma_2(p)$ ，

我们发现电子质量在不同动量下有一个修正，而且这个修正是无穷大的。怎么理解这个呢？一样的思想，实验上不可能抹除高阶效应，因此不可能测量 $m_0$ 。我们耍赖把这个无穷大推给 $m_0$ （这反应了我们的ignorance，因为我们不知道高能标下面有什么新物理会阻止这些无穷大）。

按照原来我们的做法，如果我们定义一个作为参考的**物理质量**（低动量区域，我们可以直接测量的）为 $m_{ref}\equiv m_0+\Sigma(p)|_{\not p=m_{ref}}$ 。

那么高动量下的质量为

$\begin{eqnarray} m(p)=&&m_{ref}+\Sigma_2(p)-\Sigma_2(p)|_{\not p=m_{ref}}\\ \end{eqnarray}$

**奇怪的是，不同于电荷重整，我们仍然有一个无穷大 $\sim \frac{1}{\epsilon}$ ，这是为什么呢？这个问题留到后面去解决**。

实际上，我们讨论了电荷重整化、质量重整化，还没有讨论场强重整化。对于动量空间传播子

$\int d^4x e^{ip(x-y)}\langle\Omega|T\psi(x)\bar\psi(y)|\Omega\rangle=\frac{iZ_2\sum_s u(p,s)\bar u(p,s)}{p^2 -m_0^2+i\epsilon}+\cdots\equiv\frac{iZ_2}{\not p-m}$

这里引入 $\langle\Omega|\psi(x)|p,s\rangle = \sqrt{Z_2}\langle 0|\psi(x)|p,s\rangle=\sqrt{Z_2}u(p,s)e^{-ipx}$ ，它可以看做是相互作用引入的对场强的重整化因子。

我们同时考虑场强和质量的修正，应该有

$\frac{iZ_2}{\not p-m}=\frac{i}{\not p-m_0-\Sigma_2(p)}$ ，

我们仍然定义物理质量 $m$ 为 $\not p=m$ 时的极点（注意这是定义，那么它也就没有动量的依赖性了）。

$(\not p-m_0-\Sigma_2(p))|_{\not p=m}=0$ ，

$\not p-m_0-\Sigma_2(p)=0+(1-\frac{d\Sigma_2}{dp}|_{\not p=m})(\not p-m)\color{blue}{-\frac{1}{2}\frac{d^2\Sigma_2(p)}{dp^2}|_{\not p=m}(\not p-m)^2+\cdots}$

我们得到 $Z_2\approx\frac{1}{1-\frac{d\Sigma_2}{dp}|_{\not p=m}}\approx 1+\frac{d\Sigma_2}{dp}|_{\not p=m}$ 。我们写下具体表达式：

$m=m_0+\frac{e^2}{(4\pi)^{2}}\int dx((\frac{2}{\epsilon}+\gamma_E)(1+2(2-x)m_0)+2(2-x)m_0\ln\frac{4\pi\mu^2}{xa^2+(1-x)^2m_0^2}+2(x-1)m_0)$

右边我没有区分m和m0。

$Z_2=1+\frac{e^2}{(4\pi)^{2}}\int dx(-2x(\frac{2}{\epsilon}+\gamma_E+\ln\frac{4\pi\mu^2}{xa^2+(1-x)^2m^2}-1)+\frac{4x(1-x)(2-x)m^2}{xa^2+(1-x)^2m^2})$

**由于m和Z2都是物理观测量，他们都是有限的**。那么高能情况下的依赖性都是上面的蓝色部分，即

$\color{blue}{-\frac{1}{2}\frac{d^2\Sigma_2(p)}{dp^2}|_{\not p=m}(\not p-m)^2+\cdots}$

**这个是有限的**！

希望大家能懂这个重整化的思想，就是用观测量（测量得到的质量，电荷，场强）表征的话，那么截面、衰变宽度等都是有限值，不会出现无穷大！如果时间允许，我会讲counter term的重整，那里就再也不会出现裸的物理量了。

---

![]((20241218)量子场论第28讲质量重整化-QED_Expansion/v2-573b01e58306dbf26c7e367ed49855a4_1440w.jpg)  
