# 量子场论第九讲：电磁场及其量子化

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/722149241]



**内容提要**：

* 电磁场拉氏量
* 电磁场量子化

在前面几讲中，我们讲了标量场及其量子化。这一讲和下面一讲，我们讲电磁场的量子化。然后接下来，我会讲相互作用理论。狄拉克场我想放到相互作用之后（它比较复杂，我不想大家陷入太多的数学里面）。电磁场，大家比较熟悉，只比标量场复杂一点点，应该容易接受一些。

![]((20240926)量子场论第九讲电磁场及其量子化_Expansion/v2-cc653d155d81e252b7ace3e1d7c397f1_1440w.jpg)  

电磁波是横波

  
  

我们写下著名的**麦克斯韦方程组**（Maxwell's Equations）。

$\triangledown\cdot\bold{E}=\frac{\rho}{\epsilon_0}$ ， $\triangledown\times\bold{E}=-\frac{\partial \bold{B}}{\partial t}$ ， $\triangledown\cdot\bold{B}=0$ ， $\triangledown\times \bold{B}=\mu_0\bold{J}+\frac{\partial\bold{E}}{\partial t}$

我们引入电势 $\varphi$ 和矢量势 $\bold{A}$ 使得：

$\bold{E}\equiv-\triangledown\varphi-\frac{\partial}{\partial t}\bold{A}$ , $\bold{B}=\triangledown\times\bold{A}$ 。

选择这样的定义，我们看到**法拉第电磁感应定律和磁场无源定理**自动满足了，我们只需要考虑**库仑定律和安培定律**。则麦克斯韦方程组变为

$\triangledown^2\varphi+\frac{\partial }{\partial t}\triangledown\cdot\bold{A}+\frac{\rho}{\epsilon_0}=0$

$\triangledown\times\triangledown\times \bold{A}=\mu_0\bold{J}-\frac{\partial^2}{\partial t^2}\bold{A}-\frac{\partial}{\partial t}\triangledown\varphi$

利用 $\triangledown\times\triangledown\times \bold{A}=\triangledown\triangledown\cdot\bold{A}-\triangledown^2\bold{A}$ ，安培定律变成 $-\triangledown\triangledown\cdot\bold{A}+\triangledown^2\bold{A} +\mu_0\bold{J}-\frac{\partial^2}{\partial t^2}\bold{A}-\frac{\partial}{\partial t}\triangledown\varphi=0$ 。

上面两个方程可以变形为

$\triangledown^2\varphi-\frac{\partial^2}{\partial t^2}\varphi+\frac{\partial}{\partial t}(\frac{\partial}{\partial t}\varphi+\triangledown\cdot\bold{A})=-\frac{\rho}{\epsilon_0}$

$\triangledown^2\bold{A} -\frac{\partial^2}{\partial t^2}\bold{A}-\triangledown(\frac{\partial}{\partial t}\varphi+\triangledown\cdot\bold{A})=-\mu_0\bold{J}$

如果采用洛伦兹规范： $\frac{\partial\varphi}{\partial t}+\triangledown\cdot\bold{A}=0$ ，上面两个方程可以进一步化简。进一步，引入电四矢 $A^\mu\equiv(\varphi,\bold{A})$ 和 $J^\mu=(\rho,\bold{J})$ ，上面两个方程可以合并成一个，即

$-\partial_\mu\partial^\mu A^\nu+\partial^\nu\partial_\mu A^\mu = -\mu_0 J^\nu$

引入 $F^{\mu\nu}\equiv\partial^\mu A^\nu-\partial^\nu A^\mu$ ，麦克斯韦方程组变为一个式子：

$\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ 。

如果没有源项，那么真空电磁场方程为 $\partial_\mu F^{\mu\nu}=0$ 。

$F^{\mu\nu}$ 是一个二阶反对称张量。容易验证，对应的拉氏量为

$\mathcal{L}[A^\mu, \partial_\nu A^\mu]=\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$ 。

值得注意的是如果做如下一个变换，电磁场拉氏量不会发生变化。

$A^\mu\to A^\mu + \partial^\mu\chi$ ，

这里 $\chi(x)$ 是一个任意的函数，这就电磁场的规范不变性。利用这个自由度，我们可以不同的规范固定条件。常用的规范条件有：库伦规范 $\triangledown\cdot\bold{A}=0$ ，洛伦兹规范 $\partial_\mu A^\mu=0$ ，朗道规范等等[#ref\_1](#ref\_1)。

![]((20240926)量子场论第九讲电磁场及其量子化_Expansion/v2-55de14b0e126a0475bc6b24a54c2236f_1440w.gif)  

电磁波是横波

  
  

下面我们重复学过的场量子化步骤。

先求正则动量

$\pi^\mu=\frac{\partial\mathcal{L}}{\partial\partial^0A^\mu}=-F^{0\mu}=F^{0\mu}=-\partial^0A^\mu+\partial^\mu A^0$ ，

运动方程是： $\partial_\mu F^{\mu\nu}=\partial^2 A^\nu-\partial^\nu\partial_\mu A^\mu=0$ 。

为简化计算，我们采用洛伦兹规范 $\partial_\mu A^\mu=0$ ，得到 $\partial^2A^\nu(x)=0$ 。

这个方程和K-G方程 $(\partial^2+m^2)\phi(x)=0$ 本质是一样的，只是由于光子是矢量粒子，有4个分量（由于光子质量为0，其实只有两个独立分量）。一般地，解可以写成

$A^\mu(x)=\sum_{\lambda=1,2}\int\frac{d^3k}{(2\pi)^3\sqrt{2E_k}}(a_\lambda(k)\epsilon_\lambda^\mu(k)e^{-ikx}+a_\lambda^\dagger(k)\epsilon_\lambda^{*\mu}(k)e^{ikx})$

跟标量场相比，我们多了一个极化矢量 $\epsilon_\lambda^\mu$ ，它们表征光子场的极化状态。洛伦兹规范 $\partial_\mu A^\mu =0$ 的限制即

$k_\mu\epsilon_\lambda^\mu = 0$ 。另外对于光子我们有 $k_\mu k^\mu = 0$ 。对于沿着z轴方向运动的光子 $k^\mu=E(1,0,0,1)$ ，可选取如下正交归一的极化矢量基底：

$\epsilon_1^{\mu}=\frac{1}{\sqrt{2}}(0,1,i,0)$ ， $\epsilon_2^{\mu}=\frac{1}{\sqrt{2}}(0,1,-i,0)$ 。

* 请验证如下结论（以后计算费曼图用得着，家庭作业！）

如果 $k_\mu \mathcal{M}^\mu=0$ （这是著名的Ward identity），那么有

$\sum_{\lambda}|\epsilon_{\lambda\mu}^*(k)\mathcal{M}^\mu(k)|=\sum_{\lambda\lambda'}\epsilon_{\lambda \mu}^*\epsilon_{\lambda'\nu}\mathcal{M}^\mu\mathcal{M}^{*\nu}=-g_{\mu\nu}\mathcal{M}^\mu\mathcal{M}^{*\nu}$ ，

从而我们可以看到如下替换是允许的：

$\color{blue}{\sum_{\lambda\lambda'}\epsilon_{\lambda \mu}^*\epsilon_{\lambda'\nu} \to -g_{\mu\nu}}$ 。

* 对于如上基底，请验证如下关系（家庭作业）

$\color{blue}{\epsilon_{\lambda}^\mu\epsilon_{\lambda'\mu}^*=-\delta_{\lambda\lambda'}}$ ， $\color{blue}{\epsilon_{\lambda}^\mu\epsilon_{\lambda'\mu}=\delta_{\lambda\lambda'}-1}$ （1）

光子，因为质量为0，是横向极化的。所以有 $\bold{k}\cdot\bold{A}=0\to k^i\bold{\epsilon}_\lambda^i=0$ ，如果我采用洛伦兹规范 $\partial_\mu A^\mu=0$ ，我们得到 $A^0=0$ 。

正则动量为

$\pi^\mu(x)=\sum_{\lambda=1,2}\int\frac{d^3k}{(2\pi)^3\sqrt{2E_k}}(ik^0)(a_\lambda(k)\epsilon_\lambda^\mu(k)e^{-ikx}-a_\lambda^\dagger(k)\epsilon_\lambda^{*\mu}(k)e^{ikx})$

现在加入等时对易关系

$[A^i(t,\bold{x}),\pi^j(t,\bold{x}')]=i\delta^{ij}\delta^{(3)}(\bold{x}-\bold{x}')$

利用上面蓝色公式（1），我们得到

$a_\lambda(k)=i\int\frac{d^3x}{\sqrt{2E_k}}\epsilon_{\lambda\mu}^*(k)e^{ikx}[(ik^0)A^\mu(t,\bold{x})+\pi^\mu(t,\bold{x})]$

$a_\lambda^\dagger(k)=i\int\frac{d^3x}{\sqrt{2E_k}}\epsilon_{\lambda\mu}(k)e^{-ikx}[(ik^0)A^\mu(t,\bold{x})+\pi^\mu(t,\bold{x})]$

由此可以得到

$[a_\lambda(k),a_{\lambda'}^\dagger(k')]=(2\pi)^3\delta_{\lambda\lambda'}\delta^{(3)}(\bold{k}-\bold{k}')$ ，

其他的对易关系为0。

最后我们来计算一下光子的传播子。

$\begin{eqnarray} \langle 0|A^\nu(y)A^\mu(x)|0\rangle|_{y^0>x^0}=&&\sum_{\lambda}\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}\epsilon_\lambda^\nu(k)\epsilon_\lambda^{*\mu}(k)e^{-ik(y-x)}\\ =&&\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}(-g^{\nu\mu})e^{-ik(y-x)}\\ =&&\int\frac{d^4k}{(2\pi)^4}\frac{-ig^{\nu\mu}}{k^2+i\epsilon}e^{-ik(y-x)} \end{eqnarray}$

因此我们得到光子传播子为

$\tilde{D}_{\mu\nu}(k)= \frac{-ig_{\mu\nu}}{k^2+i\epsilon}$ 。

  


![]((20240926)量子场论第九讲电磁场及其量子化_Expansion/v2-4ddf0e6a8071645af1e4a1eac68d5ef6_1440w.jpg)  

James Clerk Maxwell

  
  
## 参考  

1. [#ref\_1\_0](#ref\_1\_0)各种各样的规范可以参考维基百科 [https://en.wikipedia.org/wiki/Gauge\_fixing](https://en.wikipedia.org/wiki/Gauge\_fixing)
