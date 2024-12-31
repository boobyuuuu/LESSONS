# 量子场论第六讲：标量场、场量子化

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/720625814]

[Expansion：量子场论第五讲：对称性和守恒定律 （II）](https://zhuanlan.zhihu.com/p/720429674)

**内容提要**：

* 谐振子量子解
* 标量场解
* 二次量子化
* 为什么要做二次量子化？

这一讲我们会讨论**如何量子化(quantize)一个标量场**。场的量子化有**两种途径**。

* **正则量子化**：就是今天要讲的”二次量子化“，把经典场算符化，成为量子场。
* **路径积分量子化**：直接导出各种场的传播子。

在[https://zhuanlan.zhihu.com/p/719607939](https://zhuanlan.zhihu.com/p/719607939)的时候，我们已经展示了经典谐振子和标量场的相似性。我们依然从谐振子开始，计算一下它的能级。

![]((20240920)量子场论第六讲标量场场量子化_Expansion/v2-77db2df822e19e73412b559000db2a05_1440w.gif)  

Quatum Oscillator

  
  

  


首先写出它的拉氏量：

$L[x(t),\dot{x}(t)]=\frac{1}{2}m\dot{x}^2-\frac{1}{2}m\omega^2x^2$ 。

然后导出正则动量(canonical momentum)和哈密顿量(hamiltonian):

$p(t)\equiv\frac{\partial\mathcal{L}}{\partial\dot{x}}=m\dot{x}$ ，

$H[x(t),p(t)]\equiv p\frac{\partial L}{\partial\dot{x}}-L=\frac{p^2}{2m}+\frac{1}{2}m\omega^2x^2$ 。

我们用”梯子算符“（ladder operator method[#ref\_1](#ref\_1))的方法来推导出它的能级。引入两个算法 $a$ 和 $a^\dagger$ 使得

$H-\epsilon_0=\omega a^+a=\omega(Ax-iBp)(Ax+iBp)=w(A^2x^2+iAB[x,p]+B^2p^2)$

利用对易关系 $[x,p]=i$ 得到：

$\omega A^2=\frac{1}{2}m \omega^2x^2$ ， $\omega B^2=\frac{1}{2m}$

解得：

$A=\sqrt{\frac{m\omega}{2} }$ ， $B=\sqrt{\frac{1}{2m\omega}}$ ， $\epsilon_0=\frac{1}{2}\omega$ 。

因此有

$a=\sqrt{\frac{m\omega}{2}}(x+\frac{i}{m\omega}p)$ ， $a^\dagger=\sqrt{\frac{m\omega}{2}}(x-\frac{i}{m\omega}p)$ ， $H=\omega a^+a+\frac{1}{2}\omega$ ，

并且有

$[a,a^\dagger]=1$ ， $[H,a^+]=\omega a^+$ ， $[H,a]=-\omega a$ 。

注意到 $a$ 算符减少能量（即下降一个能级，相当于粒子消失）， $a^\dagger$ 提升能量（即提升一个能级，相当于粒子产生），因此它们分别被称为**湮灭算符和产生算符**。

$H$ 的本征态也是 $N\equiv aa^\dagger$ 的本征态（ $N$ 也被称作粒子数算符）。我们 $|n\rangle$ 为能级 $n$ 的本征态，我们有

$H|n\rangle=E_n|n\rangle$ ， $Ha^\dagger |n\rangle=(E_n+\omega)a^\dagger|n\rangle$ ， $Ha |n\rangle=(E_n-\omega)a|n\rangle$ 。

利用 $\langle n|n\rangle=1$ 和基态 $|0\rangle$ 的定义，我们有

$a|0\rangle=0$ ，

可以得到（细节参见末尾）

$a|n\rangle=\sqrt{n}|n-1\rangle$ ， $a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle$

$H|0\rangle=\frac{1}{2}\hbar\omega|0\rangle$ ， $H|n\rangle=(n+\frac{1}{2})\hbar\omega|n\rangle$ 。

我们发现了**两个重要事情**。

* 谐振子的能级是分立的，且等间距的
* 谐振子的最低能级是非零的，即 $E_0=\frac{1}{2}\hbar\omega$ ，非零的真空能量有什么物理含义吗？这是一个值得思考的问题。我们在第三讲讲到量子场和谐振子很像，我们马上也会遇到的标量场的最低能级也非零。
* 现实中，我们目前只发现了一种标量粒子，即希格斯玻色子(Higgs boson)，希格斯场的真空能量有什么物理含义吗？有人说是暗能量。同学们感兴趣的可以调研相关文献，考察一番，探讨一下希格斯场真空有没有有趣的事情。

根据 $a$ 和 $a^\dagger$ ，坐标 $x$ 和正则动量可以写成

$x=\sqrt{\frac{1}{2m\omega}}(a+a^\dagger), p=\frac{1}{i}\sqrt{\frac{1}{2m\omega}}(a-a^\dagger)$ 。

![]((20240920)量子场论第六讲标量场场量子化_Expansion/v2-8b6ce2f1701624d713a0bcb57df272af_1440w.jpg)  

发展了ladder operator method的狄拉克(Paul Dirac)

  
  

有了上面的铺垫，我想我们可以比较容易讨论**量子场论的情况**。先写下标量场的拉氏量

$\mathcal{L}=\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{1}{2}m^2\phi^2$ 。

我们**把 $\phi(x)$ 视作正则坐标**，正则动量为：

$\pi(x)\equiv\frac{\partial \mathcal{L}}{\partial\partial_0\phi}=\partial_0\phi(x)$ ，

对应的哈密顿量密度为：

$\mathcal{H}\equiv\pi\frac{\partial\mathcal{L}}{\partial\partial_0\phi}-\mathcal{L}=\frac{1}{2}\pi^2+\frac{1}{2}\triangledown^2\phi+\frac{1}{2}m^2\phi^2$ ，

它包含3项：时间移动的动能、空间移动的势能和全局势能。

运动方程为： $(\partial^2+m^2)\phi=0$ ，这里 $\partial^2\equiv\partial_\mu\partial^\mu$ ，方程的解为

$\phi(x)=\int\frac{d^3p}{(2\pi)^3\sqrt{2E_p}}(a_pe^{-ipx}+a_p^\dagger e^{ipx})$

正则动量为

$\pi(x)=\partial_0\phi(x)=\int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_p}{2}}(a_pe^{-ipx}-a_p^\dagger e^{ipx})$ ，

这里 $px=E_pt-\bold{p}\cdot\bold{x}$ 且 $E_p=\sqrt{m^2+\bold{p}^2}$ 。我们也可以用 $\phi(x)$ 和 $\pi(x)$ 来表示 $a_p$ 和 $a_p^\dagger$ 。注意到

$\int_{-\infty}^{\infty}\phi(x)e^{ikx}d^3\bold{x}=\frac{1}{\sqrt{2E_k}}(a_k+a_{-k}^\dagger)$ ，

以及

$\int_{-\infty}^{\infty}\pi(x)e^{ikx}d^3\bold{x}=(-i)\sqrt{\frac{E_k}{2}}(a_k-a_{-k}^\dagger)$ ，

这里 $k^0=E_k=\sqrt{m^2+\bold{k}^2}$ ，我们可以得到

$a_k=\int_{-\infty}^{+\infty}[\sqrt{\frac{E_k}{2}}\phi(x)+i\sqrt{\frac{1}{2E_k}}\pi(x)]e^{ikx}d^3\bold{x}$ ，

$a_k^\dagger=\int_{-\infty}^{+\infty}[\sqrt{\frac{E_k}{2}}\phi(x)-i\sqrt{\frac{1}{2E_k}}\pi(x)]e^{-ikx}d^3\bold{x}$ 。

类比于 $[x(t),p(t)]=i\hbar$ ，我们现在强行加上如下”**等时“对易关系**(equal time commutation relations)：

$[\phi(t,\bold{x}),\pi(t,\bold{x}')]=i\delta^{(3)}(\bold{x}-\bold{x}')$ 。

**为什么必须采用等时对易关系呢？它是不是洛伦兹协变（covariant）的呢**（即在不同惯性系下形式不变）[#ref\_2](#ref\_2)？

利用上面的对易关系，我们可以得到关于 $a_p$ 和 $a_p^\dagger$ 之间的对易关系。

因此有

$[a_k,a_{k'}]=[a_k^\dagger,a_{k'}^\dagger]=0$ ， $[a_k,a_{k'}^\dagger]=(2\pi)^3\delta^{(3)}(\bold{k}-\bold{k}')$ 。

这个跟谐振子的形式非常相似的。现在我们继续考察哈密顿量，把它写成产生湮灭算符的函数（留作家庭作业）。

$H=\int d^3\bold{x}\mathcal{H}(x)=\int\frac{d^3p}{(2\pi)^3}E_p(a_p^\dagger a_p+\frac{1}{2}[a_p,a_p^\dagger])$ ，

这里第二项正比于 $\delta^{(3)}(0)$ 是无穷大的真空零点能。一般理解是，实验上无法探测真空零点能，因此对我们没有影响。类似的我们有

$[H,a_p]=-E_pa_p$ ， $[H,a_p^\dagger]=E_pa_p^\dagger$ 。

现在我们回过来想一想我们**为什么要做二次量子化**？

* **从结果看**，经典场因为有了**产生算符和湮灭算符**，升级为为量子场。量子场就可以用来描述粒子的湮灭和产生，进而可以描述各种各样的相互作用和复杂的物理过程。
* **从形式看**，”等时“对易关系是**洛伦兹协变**的，这是构建一个相对论性的量子理论的关键。
* **从等价性看**，很快（下一讲）我们会导出标量场的传播子，我们就容易看出正则量子化和路径积分量子化是等价的。
* **从技术层面看**，这个量子化的方法相对于路径积分量子化，更加传统，更加容易接受。路径积分量子化是直接导出把各个场的传播子，物理图像上更直观。如果你能接受路径积分，那么基于上面提到的二者的等价性，我们应该也是欢迎正则量子化这一途径的。

![]((20240920)量子场论第六讲标量场场量子化_Expansion/v2-9c6e195ae99491241af27fa56d74bc43_1440w.jpg)  

暗能量驱动宇宙加速膨胀，真空能会是暗能量吗？

  
  

  


---

补充一点推导系数的细节。

$a|n\rangle=A_n|n-1\rangle,a^\dagger|n\rangle=B_n|n+1\rangle$

利用 $\langle k|k\rangle=1$ ，我们有

$\langle n|aa^\dagger|n\rangle=B_n^2$

另一方面有：

$\langle n|aa^\dagger|n\rangle=\langle n|(a^\dagger a+1)|n\rangle=A_n^2+1=B_{n-1}A_n+1$ 。

因此有

$B_{n-1}=A_n$ ， $A_{n+1}^2=A_n^2+1$ 。

利用 $a|0\rangle=0$ 即 $A_0=0$ ，可以得到

$A_n=\sqrt{n}$ ， $B_n=\sqrt{n+1}$ 。

## 参考  

1. [#ref\_1\_0](#ref\_1\_0)该方法是狄拉克(Paul Dirac)发展出来的 [https://en.wikipedia.org/wiki/Quantum\_harmonic\_oscillator](https://en.wikipedia.org/wiki/Quantum\_harmonic\_oscillator)
2. [#ref\_2\_0](#ref\_2\_0)为什么采用”等时“对易关系？ [https://physics.stackexchange.com/questions/95796/equal-time-commutation-relations-in-canonical-quantization-of-relativistic-free](https://physics.stackexchange.com/questions/95796/equal-time-commutation-relations-in-canonical-quantization-of-relativistic-free)
