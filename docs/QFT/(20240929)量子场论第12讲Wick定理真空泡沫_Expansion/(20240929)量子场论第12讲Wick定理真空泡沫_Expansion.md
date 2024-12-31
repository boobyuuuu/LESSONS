# 量子场论第12讲：Wick定理、真空泡沫

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/749722056]



**内容提要**：

* Wick定理：它的作用是方便我们推导出费曼规则，我取了一个别名“单身汪透明定理”。
* 真空泡沫：真空-真空跃迁，它的作用是帮我们干掉（cancel)很多费曼图。

我真的很想开始计算散射矩阵元计算截面，可惜还不行！这一讲要铺设提要里面的**一个定理**和**一个有趣的事实**。

Wick定理是Gian Carlo Wick提出来的，他是一位意大利的理论物理学家。虽然我听说过Wick定理，Wick转动等等他的工作，但是从来没有想过去了解他。

![]((20240929)量子场论第12讲Wick定理真空泡沫_Expansion/v2-beaf619a7a842b56d32f06e91df51d31_1440w.jpg)  

Gian Carlo Wick

  
  

要里面这个定理，我们先看下面的例子。假设 $y^0>x^0$ ，我们有

$\phi(y)\phi(x)=\int\frac{d^3k'd^3k}{(2\pi)^6\sqrt{4E_kE_{k'}}}(a_{k'}e^{-ik'y}+a_{k'}^\dagger e^{ik'y})(a_ke^{-ikx}+a_k^\dagger e^{ikx})$

因为我们要它放到 $\langle 0|\cdot|0\rangle$ 里面去，而且我们有 $a_k|0\rangle=\langle 0|a_k^\dagger=0$ ，那么**一个”方便的”操作**，是把 $a$ 、 $a^\dagger$ 进行排序，把 $a^\dagger$ 放到左边，把 $a$ 放到右边。我们把这个操作称为**正则排序**(Normal ordering)。

$N(\phi(y)\phi(x))=\int\frac{d^3k'd^3k}{(2\pi)^6\sqrt{4E_kE_{k'}}}(a_{k'}a_ke^{-i(k'y+kx)}+a_{k'}^\dagger a_k^\dagger e^{i(k'y+kx)}+a_{k'}^\dagger a_ke^{i(k'y-kx)}+a_k^\dagger a_{k'} e^{-i(k'y-kx)})$

它和原来的 $\phi(y)\phi(x)$ 之相差一个对易项（就是上面的最后一项那里），因此有

$\begin{eqnarray} \phi(y)\phi(x)|_{y^0>x^0}=&&N(\phi(y)\phi(x))+\int\frac{d^3k'd^3k}{(2\pi)^6\sqrt{4E_kE_{k'}}}[a_{k'},a_k^\dagger]e^{-i(k'y-kx)}\\ =&&N(\phi(y)\phi(x))+\int\frac{d^3k'd^3k}{(2\pi)^6\sqrt{4E_kE_{k'}}}(2\pi)^3\delta^{(3)}(\bold{k}'-\bold{k})e^{-i(k'y-kx)}\\ =&&N(\phi(y)\phi(x))+\int\frac{d^3k}{(2\pi)^32E_k}e^{-ik(y-x)}\\ =&&N(\phi(y)\phi(x))+\overline{\phi(y)\phi(x)} \end{eqnarray}$

这里我们用 $\overline{\phi(y)\phi(x)}$ 表示**Wick收缩**（Wick contraction)，它就是费曼传播子。

$\overline{\phi(y)\phi(x)}=D_F(y-x)$

类似地，如果 $x^0>y^0$ ，你会推出相同的结果，因此有

$\mathcal{T}(\phi(y)\phi(x)) = N(\phi(y)\phi(x))+\overline{\phi(y)\phi(x)}$ 。

推广到一般情况则是[#ref\_1](#ref\_1)：

$\mathcal{T}(\phi_1\phi_2\phi_3\cdots) = N(\phi_1\phi_2\phi_3\cdots+\overline{\phi_1\phi_2}\phi_3\cdots+\overline{\phi_1\phi_3}\phi_2\cdots+\overline{\phi_2\phi_3}\phi_1\cdots+\cdots)$ 。

**Wick定理的威力在于计算真空期望值**，我们有

$\langle 0|\mathcal{T}(\phi_1\phi_2\phi_3\cdots) |0\rangle= \langle 0| N(\phi_1\phi_2\phi_3\cdots+\overline{\phi_1\phi_2}\phi_3\cdots+\overline{\phi_1\phi_3}\phi_2\cdots+\overline{\phi_2\phi_3}\phi_1\cdots+\cdots)|0\rangle$

如果右边有个 $\phi$ 没有和另外一个 $\phi$ 进行contract，那么它的真空期望值为0 。基于这个事实，我们可以给这个定理取一个别名——单身汪透明定理。

为了看一下Wick定理的威力，我们算几个例子。

例子一：

$\langle 0|\mathcal{T}\phi(x_2)\phi(x_1)|0\rangle=D_F(x_2-x_1)$

例子二：

$\langle 0|\mathcal{T}\phi(x_3)\phi(x_2)\phi(x_1)|0\rangle=0$

例子三：

$\begin{eqnarray} \langle 0|\mathcal{T}\phi(x_4)\phi(x_3)\phi(x_2)\phi(x_1)|0\rangle=&&\langle 0|\overline{\phi_1\phi_2}\overline{\phi_3\phi_4}+\overline{\phi_1\phi_3}\overline{\phi_2\phi_4}+\overline{\phi_1\phi_4}\overline{\phi_2\phi_3}|0\rangle\\ =&&D_F(x_1-x_2)D_F(x_3-x_4)+D_F(x_1-x_3)D_F(x_2-x_4)+D_F(x_1-x_4)D_F(x_2-x_3) \end{eqnarray}$

最后我们来看一下 $\phi(x)$ 和单粒子态 $|p\rangle$ 的收缩。

$\begin{eqnarray} \phi(x)|p\rangle=&&\int\frac{d^3k}{(2\pi)^3\sqrt{2E_k}}(a_ke^{-ikx}+a_k^\dagger e^{ikx})(2\pi)^3\sqrt{2E_p}a_p^\dagger|0\rangle \end{eqnarray}$

想象如果其他 $\phi$ 都不是“单身汪”（其他的 $\phi$ 们都已经contract了），那么有可以再左边添加一个 $\langle 0|$ ，得到

$\begin{eqnarray} \langle 0|\phi(x)|p\rangle=&&\langle 0|\int\frac{d^3k}{(2\pi)^3\sqrt{2E_k}}a_ke^{-ikx}\sqrt{2E_p}a_p^\dagger|0\rangle\\ =&&\langle 0|\int\frac{d^3k}{(2\pi)^3\sqrt{2E_k}}e^{-ikx}\sqrt{2E_p}[a_k,a_p^\dagger]|0\rangle\\ =&&\langle 0|e^{-ipx}|0\rangle \end{eqnarray}$

因此我们可以有如下定义：

$\overline{\phi(x)|p\rangle}=e^{-ipx}|0\rangle$ ， $\overline{\langle p|\phi(x)}\equiv\langle 0|e^{ipx}$ 。

来看几个例子。

例子一：

$\langle p'|\phi(x)|p\rangle=0$

例子二：

$\langle p'|\mathcal{T}\phi(x')\phi(x)|p\rangle=\overline{\langle p'|\phi(x')}\overline{\phi(x)|p\rangle}+\overline{\langle p'|\phi(x)}\overline{\phi(x')|p\rangle}+\langle p'|p\rangle\overline{\phi(x')\phi(x)}$

$\langle p'|\mathcal{T}\phi(x')\phi(x)|p\rangle=e^{-i(px-p'x')}+e^{-i(p'x-px')}+2E_p(2\pi)^3\delta^{(3)}(\bold{p}'-\bold{p})D_F(x'-x)$

我想大家已经看Wick定理的作用了，下面来利用这个定理计算一下真空跃迁概率幅。

---

**真空泡沫**，也称作**真空-真空跃迁**，概率幅为：

$\langle\Omega|\Omega\rangle\propto\langle 0|\mathcal{T}\{e^{-i\int_{-T}^{T}H_I(t)dt}\}|0\rangle$

$H_I(t)=\frac{\lambda}{4!}\int d^3x\phi_I^4(x)$

我们对指数函数**微扰展开**（我们不写下标I了）。

第一项是： $\langle 0|0\rangle=1$

第二项是： $\int_{-T}^Tdt\int d^3x\langle 0|\mathcal{T}\phi^4(x)|0\rangle=\int_{-T}^Tdt\int d^3x3\times D_F^2(0)=2TV(3\times D_F^2(0))$

第三项式： $\langle 0|\mathcal{T}\{\int_{-T}^T dt_2\int d^3x_2\phi^4(x_2)\int_{-T}^T dt_1\int d^3x_1\phi^4(x_1)\}|0\rangle$

我们会发现很难计算了，只能画图（我觉得是很自然的，好像也不需要什么特别的觉悟吧！你们说呢？）。下图画出了前面几项对应的费曼图。

![]((20240929)量子场论第12讲Wick定理真空泡沫_Expansion/v2-a07a9225f2cbb06ffb5d4cd0e14ac7e6_1440w.jpg)  

真空泡沫

  
  

从上面的费曼图我们可以看出，真空-真空跃迁确实很像泡沫。以数字“8”形状的费曼图为例，我们可以看到展开项的每一项都有，加起来就是一个指数贡献。

$1+(-i\lambda) ``8"+\frac{(-i\lambda)^2}{2!}``8"^2+\frac{(-i\lambda)^3}{3!}``8"^3+\cdots=\exp\{(-i\lambda)``8"\}$

实际上每一个泡沫图的贡献都会是指数形式的贡献。进一步，我们有

$\langle\Omega|\Omega\rangle=(e^{-2iE_0T}|\langle 0|\Omega\rangle|^2)^{-1}\langle 0|\mathcal{T}\{e^{-i\int_{-T}^{T}H_I(t)dt}\}|0\rangle=1$ 。

我们得到**真空能量密度**的信息：

$e^{-2iE_0T}=\exp\{(-i)2TV(``8"+\cdots)\}$

我们得到真空密度，而且它与T无关。

$\frac{E_0}{V}=``8"+\cdots$

在下一讲我们会看到真空泡沫（即关联函数的分母项）会抵消掉很多东东西。

## 参考  

1. [#ref\_1\_0](#ref\_1\_0)证明方法可以参考Peskin书上的数学归纳法
