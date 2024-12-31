# 量子场论第五讲：对称性和守恒定律 （II）

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/720429674]

[Expansion：量子场论第四讲: 对称性和守恒定律（I）](https://zhuanlan.zhihu.com/p/720076133)

**为什么对称性如此重要呢？**大家想一想有什么物理定律运用了对称性原理？可能有同学立刻想到了**爱因斯坦的狭义相对论**。它的基础是两条公设：

* 光速在任何惯性系下不变；
* 物理规律在任何惯性系下不变。

这两条公设无疑充满了**哲学的思辨**，尤其是里面的第二条。进一步，爱因斯坦在1915年左右提出**广义相对性原理**，即：

* 物理规律在任意坐标变化下不变！

爱因斯坦的相对论就是两个鲜明的例子：**对称性原理导致物理规律**。今天这一讲，我们继续讨论对称性和守恒定律，并给出**规范对称性的重要性**！我们知道自然存在四种相互作用，目前**除了引力之外的三中相互作用力都是由规范对称性描述的**。

![]((20240918)量子场论第五讲对称性和守恒定律_II_Expansion/v2-7870604f872f821aaaca030100eca3e4_1440w.jpg)  

电荷不会凭空产生，也不会凭空消失

  
  

在上一讲中，我们证明了有名的**诺特定理**，并重点讨论了时空对称性。其中连续对称性主要分为两种：

* **时空对称性**：狭义相对论成立的庞加莱（Poincare）群对称（包括，时间平移、空间平移、转动、洛伦兹变换），费米子-玻色子之间转换的超对称
* **内部对称性**：电动力学里面的电磁规范变换、杨振宁-米尔斯提出的Yang-Mills理论（题外话，这是杨老最有名的工作）。内部对称性又有全部(global symmetry)和局域对称性(local symmetry)之分，简单说，就是对称性变换是否依赖于时空坐标（依赖则是local的）。规范对称性(Gauge symmetry)，就属于局域的对称性。

![]((20240918)量子场论第五讲对称性和守恒定律_II_Expansion/v2-3ff85acb52573f4035c656770e123fa3_1440w.jpg)  

一个转动

  
  

我们考虑**两个具有相同质量的实标量场** $\phi_1$ 和 $\phi_2$ ，拉氏量如下：

$\mathcal{L}=\sum_{i=1,2}\frac{1}{2}\partial_\mu\phi_i\partial^\mu\phi_i-\frac{1}{2}m^2\phi_i^2$

如果进行如下的 $U(1)$ 变换：

$\begin{pmatrix}\phi'_1\\\phi'_2\end{pmatrix}=\begin{pmatrix}\cos \theta & -\sin\theta \\\sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix}\phi_1\\\phi_2\end{pmatrix}$ ，

这里 $\theta$ 是一个实数。我们会得到

$\mathcal{L}'=\sum_{i=1,2}\frac{1}{2}\partial_\mu\phi_i'\partial^\mu\phi_i'-\frac{1}{2}m^2\phi_i'^2=\mathcal{L}$ 。

我们发现拉氏量的形式完全不变，我们说这个系统满足U(1)的内部对称性。这里面的关键点是 $\phi_1$ 和 $\phi_2$ 质量相同，否则的话U(1)对称性是没办法满足的。进一步，如果没有其他的区别，我们是**没办法区分 $\phi_1$ 和 $\phi_2$ ，那有没有可能他们就是同一种粒子**？事实上，如果采用如下定义

$\phi(x)\equiv\frac{1}{\sqrt{2}}(\phi_1(x)+i\phi_2(x))$ ，

这里 $i$ 是虚数单位，拉氏量变为

$\mathcal{L}=\partial_\mu\phi^*\partial^\mu\phi-m^2\phi^*\phi$ ，

这就是一个复标量场，描述的是带电的标量粒子（实标量场描述的是电中性的标量粒子）。对于复数的 $\phi$ ，U(1)变换即为

$\phi'(x)=\phi(x)e^{i\theta}$ 。

那么U(1)全部变换的守恒量是什么呢？按照上一讲的公式，无穷小变换为

$\delta x^\mu = 0, \delta\phi=i\theta\phi,\delta\phi^*=-i\theta\phi^*$ ，

因此**守恒流**是

$j^\mu=i(\phi\partial^\mu\phi^*-\phi^*\partial^\mu\phi)$ ，

由于 $(\partial_\mu\partial^\mu+m^2)\phi=0$ ，显然它满足 $\partial_\mu j^\mu=0$ ，马上我会看到这个是**电荷守恒**。

上面的讨论中 $\theta$ 是一个实数，因此这是一个全局的变换。如果变换是局域的，即依赖于时空坐标的。我们有

$\phi'(x)=\phi(x)e^{iq\theta(x)}$ ，

为方便后续讨论，引入一个实数 $q$ ，我们马上会知道它的物理意义。那么质量项不变，动能项变为

$\partial_\mu\phi'(x)=e^{i\theta(x)}(\partial_\mu\phi(x)+iq\partial_\mu\theta(x)\phi(x))$

拉氏量变为

$\mathcal{L}'=(\partial_\mu\phi^*(x)-iq\partial_\mu\theta(x)\phi^*(x))(\partial^\mu\phi(x)+iq\partial^\mu\theta(x)\phi(x))-m^2\phi^*(x)\phi(x)$ ，

很显然，目前的**拉氏量不满足U(1)的局域对称性**。为此，我们引入如下的相互作用项

$\mathcal{L}_{int}=-iqA_\mu(x)\phi^*(x)\partial^\mu\phi(x)+iqA_\mu(x)\phi(x)\partial^\mu\phi^*(x)$ ，

这里 $A_\mu(x)$ 是额外的矢量场，它的U(1)局域变换是

$A'_\mu(x)=A_\mu(x)+\partial_\mu\theta(x)$ 。

那么我们会发现如下拉氏量是满足U(1)局域对称性的

$\mathcal{L}=(D_\mu\phi)^*(D^\mu\phi)-m^2|\phi|^2$ ，

这里符号 $D_\mu\equiv\partial_\mu+iqA_\mu$ ，乘坐协变导数，它的变换性质如下：

$D'_\mu\phi'=e^{iq\theta(x)}(D_\mu\phi)$ 。

你们肯定会发现 $A_\mu$ 的变化性质和电磁场一样，是的，它就是电磁场。这个例子展示一个非常重要的物理原理，即

”**规范对称性导致相互作用“**！

这正是**Weyl和Yang-Mills**的贡献。我们自然界存在四种相互作用

值得一提的是，上面的拉氏量确实电磁场的动能项，完整的拉氏量如下：

$\mathcal{L}[\phi,A_\mu]=|(\partial_\mu+iqA_\mu)\phi|^2-m^2|\phi|^2-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$ ，

这里 $F_{\mu\nu}\equiv\partial_\mu A_\nu-\partial_\nu A_\mu$ ，我们以后会讲到如何得到 $F_{\mu\nu}$ 及如何得到电磁场的拉氏量。

由 $\partial_\mu\phi^*\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi^*}-\frac{\partial\mathcal{L}}{\partial\phi^*}=0$ 得到运动方程为：

$(D^*_\mu D^\mu+m^2)\phi=0$ 。

由 $\partial_\mu \frac{\partial\mathcal{L}}{\partial\partial_\mu A_\nu}-\frac{\partial\mathcal{L}}{\partial A_\nu}=0$ 得到运动方程为：

$\partial_\mu F^{\mu\nu}=iq(\phi^*D^\nu\phi-\phi D^{*\nu}\phi^*)$ 。

此时规范对称性导致的守恒流会是下面的形式吗？

$j^\mu=iq(\phi D^{*\mu}\phi^*-\phi^*D^\mu\phi)$

---

实际上， $\delta S=0$ 给出

$\begin{eqnarray} \delta S=&&\int_\Omega d^4x \partial_\mu[iq(\phi D^{*\mu}\phi^*-\phi^*D^\mu\phi)\theta-F^{\mu\nu}\partial_\nu\theta]\\ =&&\int_\Omega d^4x \partial_\mu[iq(\phi D^{*\mu}\phi^*-\phi^*D^\mu\phi)\theta]-\partial_\mu(F^{\mu\nu}\partial_\nu\theta)\\ =&&\int_\Omega d^4x \partial_\mu[iq(\phi D^{*\mu}\phi^*-\phi^*D^\mu\phi)\theta]-\partial_\mu F^{\mu\nu}\partial_\nu\theta\\ =&&\int_\Omega d^4x \partial_\mu[iq(\phi D^{*\mu}\phi^*-\phi^*D^\mu\phi)]\theta+(iq(\phi D^{*\nu}\phi^*-\phi^*D^\nu\phi)-\partial_\mu F^{\mu\nu})\partial_\nu\theta\\ \end{eqnarray}$

所以 $\delta S=0$ 给出两个要求：

$\partial_\mu j^\mu=\partial_\mu[iq(\phi D^{*\mu}\phi^*-\phi^*D^\mu\phi)]=0$

和

$\partial_\mu F^{\mu\nu}=iq(\phi^*D^\nu\phi-\phi D^{*\nu}\phi^*)$ ，

这两个要求其实是和运动学方程式等价的。

留一个**家庭作业**：参考文献[#ref\_1](#ref\_1)请导出U(1)局域对称性对应的守恒流，并和全局对称性的守恒量进行比较。看看你发现了什么？

![]((20240918)量子场论第五讲对称性和守恒定律_II_Expansion/v2-e30c6477f1f54bca92cd7bf5ee72e1aa_1440w.jpg)  

杨振宁和米尔斯

  
  
## 参考  

1. [#ref\_1\_0](#ref\_1\_0)Noether's theorems and gauge symmetries [https://arxiv.org/pdf/hep-th/0009058](https://arxiv.org/pdf/hep-th/0009058)
