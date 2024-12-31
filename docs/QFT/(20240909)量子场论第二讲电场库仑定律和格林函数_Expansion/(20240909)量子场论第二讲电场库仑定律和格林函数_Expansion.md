# 量子场论第二讲：电场、库仑定律和格林函数

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/719109755]

[Expansion：量子场论第一讲：真空、粒子场、产生和湮灭。](https://zhuanlan.zhihu.com/p/719001546)

**电场**，我们从中学时代就开始接触了，是我们非常熟悉的物理概念。可能很多人会奇怪我为什么想在量子场论这门课程里面专门抽出一讲来讲电场和库仑定律？我来解释我**这么做的动机**。

* 引入**场(field)的概念**：场是时空坐标的函数，所以宇宙中任何地点任何时刻都应该有一个”值“？这个”值“有什么物理意义呢？
* 引入诸如**格林函数(Green's function)**的数学技巧：格林函数是什么？它在数学上有什么作用？它在物理上有什么作用？

考虑一个正的点电荷和一个负的点电荷，空间中的电场线如下。

![]((20240909)量子场论第二讲电场库仑定律和格林函数_Expansion/v2-31fb27aa0d054f19a9aa4879d7619679_1440w.jpg)  

用电场线的直观表示电场是法拉第(Michael Faraday)最先提出来的。我们知道：电场线的疏密表示电场强度的大小，上面的小箭头表示电场的方向（即正电荷的受力方向）。所以电场可以写作 $\vec{E}(x)$ ，表示电场是空间坐标的函数，而且有方向。

事实上，量子场论（QFT）里面研究的场(field)，是时空的函数，在宇宙中的任何地点任何时刻都应该有一个”值“。**这个”值“需要表达很多物理信息**：1）可以仅有大小，比如描述希格斯玻色子Higgs的标量场 $\phi(x)$ ；2）可以有方向 ，比如描述电磁波也即光子的矢量场$A_\mu(x)=(\varphi(x),\vec{A}(x))$ ；3）还可以有其他属性，比如描述电子等自旋 $\frac{1}{2}$ 粒子的旋量场 $\psi(x)=\begin{pmatrix}\sqrt{p\cdot\sigma}\\\sqrt{p\cdot\bar{\sigma}}\end{pmatrix}\chi^s$ ，其中 $\chi^s=\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}0\\1\end{pmatrix}$ 表示费米子自旋状态；4）可以是实数，也可以是复数，复数一般表示带电粒子。以上这些，在以后的学习过程中我们都会遇到。

对于场是时空的函数，可能大家都不会觉得惊讶。但是如果将来你们学习量子规范场论，特别是**希格斯机制**(Higgs Mechanism)时，你就有发现一个问题。希格斯机制，数学上简单不负责任地（英语里面叫做naive）讲就是，在宇宙大爆炸之后某一个时刻，希格斯场 $\phi(x)$ **”突然“变成** $\frac{1}{\sqrt{2}}(v+h(x))$ 。忽略掉 $\frac{1}{\sqrt{2}}$ 因子， $v$ 是真空期望值，约等于246GeV，是一个常数； $h(x)$ 是变了之后的希格斯场。这是一个很难理解的事情，因为场是时空的函数，**定义域是整个宇宙**。如果整个宇宙范围内的希格斯场”同时“”突然“发生一个变化，我觉得太不可思议了，除非当时的宇宙特别小！这里不做展开了，研究宇宙学(cosmology)的专家提出了很多理论模型来解释宇宙的演化（但是很多推论难以在地球上验证！）。

接下来讲一下**库仑定律**(Coulomb's Law），这里面会有一些数学，这是难以避免的!而且没有必要避免，想想牛顿爵士(Sir Isaac Newton)为啥发明”流数术“，即微积分？上一讲我们留了一个家庭作业：库仑定律有哪些描述方式？我想大概有如下几种：

* **平方反比定律**：$\vec{F}=k\frac{e_1e_2}{r^2}\vec{e}_r$ ，这个是最熟悉的，电场力正比于两个点电荷所携带电荷量的大小，反比于他们距离的平方。
* **电场强度散度**： $\nabla \cdot \vec{E}(x)=\frac{\rho(x)}{\epsilon_0}$ ，这是麦克斯韦方程组（Maxwell's equations）中的一个。其中 $\rho(x)$ 表示电荷密度。
* **电势**：引入 $\vec{E}(x)=-\nabla\varphi(x)$ ，它的作用脱掉 $\vec{E}$ 上面的”箭头“帽子，数学上方便操作。得到 $-\nabla^2\varphi(x)=\frac{\rho(x)}{\epsilon_0}$ 。
* **哈密顿量**： $H_I=e\bar{\psi}\gamma^\mu\psi A_\mu$ ，这是量子电动力学(Quantum Electrodynamics)里面的相互作用哈密顿量。这个大家肯定比较陌生，我们以后肯定会遇到。

第一种我们最熟悉，我们现在尝试从其他描述方式推导出第一种来。

* 第二种到第一种：

$\begin{eqnarray} &&\nabla\cdot \vec{E}=\frac{\rho}{\epsilon_0}\Rightarrow\int\nabla\cdot\vec{E}dV=\frac{1}{\epsilon_0}\int \rho dV\\ &&\Rightarrow\oint\vec{E}\cdot d\vec{S}=\frac{e_1}{\epsilon_0}\quad\text{using}\quad\rho(x)=e_1\delta(\vec{x})\\ &&\Rightarrow |\vec{E}|4\pi r^2=\frac{e_1}{\epsilon_0}\\ &&\Rightarrow \vec{F}=\vec{E}e_2=\frac{1}{4\pi\epsilon_0}\frac{e_1e_2}{r^2}\vec{e}_r \end{eqnarray}$

里面用到了散度定理和Dirac-delta函数的性质 $\int_{-\infty}^{+\infty}\delta(x)dx=1$ 。

* 从第三种到第一种：我们需要求解 $\nabla^2\varphi(x)=-\frac{e_1\delta(\vec{x})}{\epsilon_0}$ ，这是一个**典型求格林函数**的方程。一般是利用**傅里叶展开（Fourier expansion）**来求解。

令 $\varphi(\vec{x})=\frac{1}{(2\pi)^3}\int\tilde{\varphi}(\vec{k})e^{-i\vec{k}\cdot\vec{x}}d^3k$ 和delta函数性质 $\delta(\vec{x})=\frac{1}{(2\pi)^3}\int e^{-i\vec{k}\cdot\vec{x}}d^3k$ ，代入得到：

$\tilde{\varphi}(\vec{k})=\frac{e_1}{\epsilon_0}\frac{1}{k^2}$ ，

然后进行傅里叶逆变换得到：

$\varphi(\vec{x})=\frac{1}{(2\pi)^3}\frac{e_1}{\epsilon_0}\int \frac{1}{k^2}e^{-i\vec{k}\cdot\vec{x}}d^3k=\frac{1}{4\pi\epsilon_0}\frac{e_1}{r}$ （\*）。

里面的计算涉及到一个有名的积分 $\int_0^\infty\frac{\sin x}{x}dx=\frac{\pi}{2}$ ，可以用Feynman's trick来做。接下来 $\vec{F}=-e_2\nabla\varphi$ 就得到第一种形式了。

这里我们看到格林函数 $\tilde\varphi(k)\propto\frac{1}{k^2}$ ，接下来的学习过程中你会看到许多这种类似的东西。它实际上就是**传播子(propagator)**在动量空间中的形式。很多人知道传播子理论是Feynman在它的博士论文中首先提出来的（大概是1945左右，相比之下，格林函数本身是是数学家George Green早在19世纪20年代就被提出来了）。物理上，简单说来，它表示的是一个粒子从 $x$ 处跑到 $x'$ 处的概率幅。下面看几个传播子的例子。

* 标量场： $\frac{i}{k^2-m^2+i\epsilon}$ ，我们暂时忽略掉 $i\epsilon$ ，但是它是非常重要的，叫做Feynman prescription，后续学习中肯定会遇到。
* 旋量场： $\frac{i(\gamma^\mu k_\mu+m)}{k^2-m^2+i\epsilon}$ ，我们暂时忽略掉 $\gamma^\mu$ ，它是描述费米子自旋的(BTW，知乎貌似打不出来slash!)。
* 矢量场： $\frac{-i(g_{\mu\nu}-\frac{k_\mu k_\nu}{m^2})}{k^2-m^2+i\epsilon}$ ，我们暂时忽略掉分子，它跟规范的选择有关系，将来学习量子规范场论肯定会讲。

我们可以看到，这些传播子的形式都几乎是 $\propto\frac{1}{k^2}$ ，为什么呢？

我们知道库伦定律、牛顿的万有引力定律都是平方反比定律，这二者之间都什么联系吗？

我想，本质是因为我们生活在一个**3维空间**里面，场向四面八方传播。导致场的源（电荷或者质量）是守恒的，因而总的场通量守恒，而某一处的场强就反比于面积的增长率了。这是普适的，只和空间维度有关。

至于上面第四种库仑定律的描述方式，等我们学习了Dirac方程再细说。

下一讲，我们会讲拉格朗日量(Lagrangian)和对称性。

留一个家庭作业：请完整推导出（\*）式！

