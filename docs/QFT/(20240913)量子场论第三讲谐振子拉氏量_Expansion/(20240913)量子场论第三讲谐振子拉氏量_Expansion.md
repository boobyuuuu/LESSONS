# 量子场论第三讲：谐振子、拉氏量

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/719607939]

[Expansion：量子场论第二讲：电场、库仑定律和格林函数](https://zhuanlan.zhihu.com/p/719109755)

  


![]((20240913)量子场论第三讲谐振子拉氏量_Expansion/v2-77b734ac5020c95b6c0072324b0617eb_1440w.gif)  

经典谐振子

  
  

谐振子（harmonic oscillator）如上图所示，就是一根轻质**弹簧**连接着一个有**质量**的物体。**我们为什么要讲谐振子呢？**

谐振子是一个对于理解场论非常重要的模型，不严谨地说：**所有的量子场，就是空间中一个个谐振子的集合，甚至真空的特性也可以用谐振子的特性来理解**。

我们首先关注一维的谐振子，牛顿方程是：

$F=m\frac{d^2x}{dt^2}=-kx=-mw^2x$

这里 $k$ 是弹簧的弹性系数。一般记 $k\equiv mw^2$ ，其中 $w$ 是圆频率。它的通解是 $x(t)=c_1\sin(wx)+c_2\cos(wx)$ ，也可以写成

$x(t)=c_1e^{-iwt}+c_2e^{iwt}$ 。

我们将它跟一个标量场进行比较（我们很快就会接触到标量场）。

$\phi(x)=\int \frac{d^3k}{(2\pi)^3\sqrt{2E_k}}(a_ke^{-ikx}+a_k^\dagger e^{ikx})$

**可以看出 $\phi(x)$ 和谐振子很像**，有如下对应关系。

$t \leftrightarrow x^\mu=(t,x,y,z)$

$x(t) \leftrightarrow \phi(x^\mu)$

$w\leftrightarrow k^\mu=(E_k,k_x,k_y,k_z)$

$c_1,c_2\leftrightarrow a_k,a_k^\dagger$

但是有**两个很明显的区别**。

* $\phi(x)$ 有一个积分，说明它是一个包含所有不同频率谐振子的集合。
* $a_k,a_k^\dagger$ 是对应频率谐振子的系数，但他们同时是算符，负责单粒子态的湮灭和产生。

这**两个区别也是量子场的特点**！

接着我们来看看对应的**拉格朗日量**(简称拉氏量，Lagrangian)，我假设大家都学过分析力学，对于经典谐振子，它是

$S[x(t),\dot{x}(t)]=\int_{t_0}^{t_1}L[x(t),\dot{x}(t)]dt=\int_{t_0}^{t_1} dt\frac{1}{2}m\dot{x}^2-\frac{1}{2}mw^2x^2$ 。

这里 $S[x(t),\dot{x}(t)]$ 称为**作用量**(action)，$L[x,\dot{x}]=\frac{1}{2}m\dot{x}^2-\frac{1}{2}mw^2x^2$ 是**拉氏量**（Lagrangian）。

**最小作用量原理**（Principle of Least Action），可以导出**Euler-Lagrange方程**：

$\frac{d}{dt}\frac{\partial\cal{L}}{\partial \dot{x}}-\frac{\partial\cal{L}}{\partial x}=0$ ，

我们可以得到上面的牛顿方程。上面讨论的是一维谐振子，推广到三维谐振子，那就是

$L_{h.o.}=\frac{1}{2}m(\dot{x}^2+\dot{y}^2+\dot{z}^2)-\frac{1}{2}m(w_x^2x^2+w_y^2y^2+w_z^2z^2)$ ，

这里 $h.o.$ 表示谐振子。

下面我们来写一个经典场（classical fields），所谓经典场，就是还没有”**强加二次量子化“**（second quantization)的场论。怎么突然蹦出”二次量子化“这个新名词？简单理解，就是上面的 $a_k$ 和 $a_k^\dagger$ 还没有成为算符，还只是复数。

根据上面 $x(t)$ 和 $\phi(x^\mu)$ 之间的对应关系以及 $\cal{L}_{h.o.}$ ，通过猜测(guess)不难写出如下拉氏密度：

$\begin{eqnarray}&&\cal{L}_{guess}[\phi(x),\partial_t \phi(x),\partial_x \phi(x),\partial_y \phi(x),\partial_z \phi(x)]\\=&&\frac{1}{2}m[(\frac{\partial\phi(x)}{\partial t})^2+(\frac{\partial\phi(x)}{\partial x})^2+(\frac{\partial\phi(x)}{\partial y})^2+(\frac{\partial\phi(x)}{\partial z})^2]-\frac{1}{2}m(w_t^2+w_x^2+w_y^2+w_z^2)\phi^2(x) \end{eqnarray}$ 。

这个拉氏量其实是**拉氏密度**（马上会解释，以后我们不加区分拉氏量还是拉氏密度，统称为拉氏量） $\cal{L}_{guess}$ 几乎是正确的。我们需要做出三个修改。

**第一个无关紧要**，做一下代换

$\sqrt{m}\phi(x) \to \phi(x)$

$w_t^2+w_x^2+w_y^2+w_z^2\to m^2$

（这里我还是用了m，其实我应该换一个字母以免歧义，但是我相信大家没问题），拉氏量变为：

$\begin{eqnarray}&&\cal{L}_{guess}[\phi(x),\partial_t \phi(x),\partial_x \phi(x),\partial_y \phi(x),\partial_z \phi(x)]\\=&&\frac{1}{2}[(\frac{\partial\phi(x)}{\partial t})^2+(\frac{\partial\phi(x)}{\partial x})^2+(\frac{\partial\phi(x)}{\partial y})^2+(\frac{\partial\phi(x)}{\partial z})^2]-\frac{1}{2}m^2\phi^2(x) \end{eqnarray}$ 。

**第二个修正很重要**，就是把对 $x,y,z$ 的偏导数前面的**+号变成-号**。也就是

$\begin{eqnarray}&&\cal{L}_{guess}[\phi(x),\partial_t \phi(x),\partial_x \phi(x),\partial_y \phi(x),\partial_z \phi(x)]\\=&&\frac{1}{2}[(\frac{\partial\phi(x)}{\partial t})^2-(\frac{\partial\phi(x)}{\partial x})^2-(\frac{\partial\phi(x)}{\partial y})^2-(\frac{\partial\phi(x)}{\partial z})^2]-\frac{1}{2}m^2\phi^2(x) \end{eqnarray}$ 。

很多同学肯定看出来为什么了，是要满足**狭义相对论**的要求。下一讲或者下下一讲我们会讲这个，目前请暂且忽略。

引入记号 $x^\mu=(t,x,y,z)$ ，

$\partial_\mu\equiv\frac{\partial}{\partial x^\mu}$ ，

$g_{\mu\nu}=Diag(1,-1,-1,-1)$

和 $V_\mu=\sum_\nu g_{\mu\nu}V^\nu\equiv g_{\mu\nu}V^\nu$ （这里采用Einstein求和约定，即相同指标默认求和），上面的拉氏量可以简写成：

$\mathcal{L}_{KG}[\phi,\partial_\mu\phi]=\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{1}{2}m^2\phi^2$ 。

**第三个修正也很重要**，需要把对全空间积分，所以我们把上面的构造称为拉氏密度。

$S[\phi(x),\partial_\mu\phi(x)]=\int_{t_0}^{t_1}L[\phi,\partial_\mu\phi]dt=\int_{t_0}^{t_1}dt\int dxdydz\mathcal{L}[\phi,\partial_\mu\phi]=\int\mathcal{L}[\phi,\partial_\mu\phi]d^4x$

应用Euler-Lagrange方程

$\partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\mathcal{\phi})}-\frac{\partial \mathcal{L}}{\partial\phi}=0$ ，

我们得到**运动方程**

$(\partial_\mu\partial^\mu+m^2)\phi=0$ 。

这就是用来描述标量粒子的**Klein-Gordon方程**。这个方程相当于上面的牛顿方程

$(m\frac{d^2}{dt^2}+mw^2)x=0$ 。

我虽然知道Klein和Gordon是两位物理学家，但是从来没有想过找找他们的照片来看看。只找到Klein。

![]((20240913)量子场论第三讲谐振子拉氏量_Expansion/v2-6bc39eca91f8069bb852aea219acbce8_1440w.jpg)  

Oskar Klein

  
  

家庭作业：请找出Klein-Gordon方程的通解。

下一讲我们会讲授：经典场和量子场

![]((20240913)量子场论第三讲谐振子拉氏量_Expansion/v2-77db2df822e19e73412b559000db2a05_1440w.gif)  

量子的谐振子

  
  

  


【注1】：文中图片均来自wikipedia，特此鸣谢！

