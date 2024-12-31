# 量子场论第十讲： 表象、相互作用真空

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/731689741]



**内容提要**：

* 相互作用(interaction)
* 表象(picture): 薛定谔表象(Schrodinger Picture)、海森堡表象(Heisenberg Picture)和相互作用表象(Interaction Picture)
* 相互作用真空

从这一讲开始，我们慢慢开始研究相互作用，希望很快就可以计算一点东西。我对场论的理解也很浅薄，但是尽量教会大家如何进行计算。**更深刻地理解和消化量子场论，乃至将来有希望“创造”出新的理论（Please let me know if you make it!），只能交给你们自己了！**

本讲主要是想搞清楚上面**三个基本概念**。

---

我们来看一个带有**相互作用**的拉氏量。

$\mathcal{L}=\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{1}{2}m^2\phi^2-\frac{\lambda}{4!}\phi^4=\mathcal{L}_{KG}-\frac{\lambda}{4!}\phi^4$

写成哈密顿量形式是：

$H=H_{KG}+\int d^3x \frac{\lambda}{4!}\phi^4$ 。

我们看到多了一项 $\phi^4$ ，可以从两个方面理解。

* 它描述了4个标量粒子的相互作用，作用强度由系数 $\lambda$ 决定。
* 它描述了标量粒子的势能形状，经典力学我们知道势能最低最稳定，说明标量粒子的最稳定状态对应于 $\phi=0$ 。

上面是一个典型的例子，其实还可以把相互作用看的更广泛一些，比如将来学习Dirac场，拉氏量如下：

$\mathcal{L}_{Dirac}=\bar\psi i\gamma^\mu\partial_\mu \psi-m\bar{\psi}\psi$

其中质量项可以写成

$m\bar{\psi}\psi=m(\bar{\psi}_L\psi_R+\bar{\psi}_R\psi_L)$ ，

它表明一种“特殊”的相互作用，即左手粒子变成右手粒子或者反过来。作用强度正比于质量。研究中微子时可以会比较重视这个事情。

---

下一个概念是**表象(Picture）**，我只知道有三种表象：薛定谔表象、海森堡表象和相互作用表象。我们学习量子力学的时候，教的是

* 薛定谔表象：态变算符不变，就是说波函数变，而能量动量等算符不变
* 海森堡表象：算符变态不变，就是波函数不变，而能量动量这个算符不变。

延伸到量子场论，有两个问题：

* 从波函数经过二次量子化变成量子场，它本身已经是算符了。
* 薛定谔表象中，我们需要求解薛定谔方程才能得到波函数随着时间的演化。在存在相互作用的情况下，这个几乎不可能（我都是通过微扰展开计算前面几阶最重要的贡献）！

鉴于上面的问题，因此我们一般使用海森堡表象或者相互作用表象。

![]((20240928)量子场论第十讲_表象相互作用真空_Expansion/v2-d8e93575af064023eb1cadab46123717_1440w.jpg)  

Werner Heisenberg

  
  

我们以标量场为例介绍一下。

海森堡表象下量子场是

$\phi_H(t,\bold{x})\equiv e^{iHt}\phi(0,\bold{x})e^{-iHt}$ ,

它满足海森堡运动方程： $\frac{i\partial}{\partial t}\phi(t,\bold{x})=[\phi(t,\bold{x}),H]$ 。

如果哈密顿量不含相互作用（记作 $H_0$ ），那么它就变为

$\phi_{H_0}(t,\bold{x})=e^{iH_0t}\phi(0,\bold{x})e^{-iH_0t}\equiv\phi_I(t,\bold{x})$ ，

这个其实就是相互作用表象下的标量场，也即

$\phi_I(t)=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2E_k}}(a_ke^{-ikx}+a_k^\dagger e^{ikx})$ ，

这其实就是我们一直使用的形式。我查了一下，相互作用表象也叫狄拉克表象，是他最先引入的。

![]((20240928)量子场论第十讲_表象相互作用真空_Expansion/v2-8b6ce2f1701624d713a0bcb57df272af_1440w.jpg)  

Paul Dirac

  
  

---

最后一个概念是**相互作用真空**，我们记作 $|\Omega\rangle$ 。我们用 $|0\rangle$ 记作自由场真空。为了得到二者直接的联系，我们利用H的本征态对 $|0\rangle$ 进行分解。

$e^{-iHT}|0\rangle=e^{-iE_0T}|\Omega\rangle\langle\Omega|0\rangle+\sum_{n>\Omega}e^{-iE_nT}|n\rangle\langle n|0\rangle$ 。

由于 $E_0<E_n$ ，我们可以让 $T \to \infty(1-i\epsilon)$ ，得到

$|\Omega\rangle=\lim_{T\to\infty(1-i\epsilon)}(e^{-iE_0T}\langle\Omega|0\rangle)^{-1}e^{-iHT}|0\rangle$ 。

这里出现了**时间在无穷远是有一个小小的复虚部**，我想大家不会觉得特别陌生，因为在第八讲讲授传播子的时候，我们就遇到了。简单理解，就是为了物理的合理性，即

**一个粒子跑到无穷未来或者无穷过去的时候，周围应该没有其他东西和它作用了，它应该”自由“了。**

[Expansion：量子场论第八讲：无穷远、无穷未来、传播子](https://zhuanlan.zhihu.com/p/721510859)

类似地，我们有

$\langle\Omega|=\lim_{T\to\infty(1-i\epsilon)}(e^{-iE_0T}\langle0|\Omega\rangle)^{-1}\langle 0| e^{-iHT}$ 。

![]((20240928)量子场论第十讲_表象相互作用真空_Expansion/v2-be86db62133d36537e27d5221c8dadce_1440w.jpg)  

freedom

  
  
