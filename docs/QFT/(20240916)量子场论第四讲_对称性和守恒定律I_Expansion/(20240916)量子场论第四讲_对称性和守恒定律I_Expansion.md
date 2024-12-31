# 量子场论第四讲: 对称性和守恒定律（I）

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/720076133]

[Expansion：量子场论第三讲：谐振子、拉氏量](https://zhuanlan.zhihu.com/p/719607939)![]((20240916)量子场论第四讲_对称性和守恒定律I_Expansion/v2-0554e7093dbef6fb36742ef1f74d4e55_1440w.jpg)  

我们来看一个经典的例子——**地球绕着太阳转**。我们先写出拉氏量。

$S=\int dt L=\int dt (\frac{1}{2}m(\dot{r}^2+r^2\dot{\varphi}^2)+\frac{GMm}{r})$

这个物理系统大家从中学开始就很熟悉。**它有哪些对称性呢？**

**分立对称性**: 时间反演，空间反演

**连续对称性**: 时间平移，空间平移，转动，……

我们可能都知道这些对称性，但**什么是对称性呢？**对称性，我的理解是，就是进行某种操作，可以分立也可以是连续性的，物理系统不变。**什么叫做物理系统不变呢**？我觉得是物理规律不变，就是说我还是可以用同一个拉氏量来描述它，也就是作用量不变。

上面已经列举了一下对称性，我简单证明一下。

* 时间反演： $t \to -t$
* 空间反演： $\varphi \to \varphi+\pi$
* 转动： $\varphi \to \varphi+\delta\varphi$
* 空间平移： $x \to x+\delta x$ , $r\to r+\cos\varphi\delta x$ , $\varphi\to\varphi-\frac{\sin\varphi}{r}\delta x$
* 时间平移： $t \to t+\delta t$

我们将会看到，**每一个连续对称性都对应着一条守恒定律**，这就是非常有名的**诺特定理**。诺特定理在广义相对论的建立过程中发挥了很大的作用。下面我们来**证明这个定理**。我看过一些经典教材的推导方法，个人觉得我的这种最容易理解！

不失一般性，我把拉氏量写成

$L[t,\bold{x}(t),\delta\bold{x}(t)]$

假定一个**连续微小变化** $\epsilon_r (r=1,2,\cdots,N)$ ,

$\delta t \equiv t'-t= \sum_r T_r\epsilon_r$

$\delta\bold{x}=\bold{x}'(t')-\bold{x}(t)=\sum_r\bold{X}_r\epsilon_r$

$\begin{eqnarray} \bold{x}'(t)-\bold{x}(t)=&& \bold{x}'(t)-\bold{x}'(t')+\bold{x}'(t')-\bold{x}(t)\\ =&&-\dot{\bold{x}}'(t)\delta t+\delta \bold{x}\\ =&&-\dot{\bold{x}}(t)\delta t+\delta \bold{x} \end{eqnarray}$

$\begin{eqnarray} \frac{d}{dt}(\bold{x}'(t)-\bold{x}(t))=&& -\ddot{\bold{x}}(t)\delta t+\delta \dot{\bold{x}} \end{eqnarray}$

$\begin{eqnarray} \delta L=&&L[t,\bold{x}'(t),\dot{\bold{x}}'(t)]-L[t,\bold{x}(t),\dot{\bold{x}}(t)]\\ =&&\frac{\partial L}{\partial \bold{x}}(-\dot{\bold{x}}\delta t+\delta\bold{x})+\frac{\partial L}{\partial\dot{\bold{x}}}(-\ddot{\bold{x}}\delta t +\delta\dot{\bold{x}})\\ =&&\frac{\partial L}{\partial \bold{x}}(-\dot{\bold{x}}\delta t+\delta\bold{x})+\frac{d}{dt}(\frac{\partial L}{\partial\dot{\bold{x}}}(-\dot{\bold{x}}\delta t+\delta\bold{x}))-\frac{d}{dt}\frac{\partial L}{\partial\dot{\bold{x}}}(-\dot{\bold{x}}\delta t +\delta\bold{x})\\ =&&\frac{d}{dt}(\frac{\partial L}{\partial\dot{\bold{x}}}(-\dot{\bold{x}}\delta t+\delta\bold{x})) \end{eqnarray}$

这样**作用量的微小变化**为：

$\begin{eqnarray} \delta S=&&\int_{t_0+\delta t}^{t_1+\delta t}L[t',\bold{x}’(t'),\dot{\bold{x}}'(t')]dt'-\int_{t_0}^{t_1}L[\bold{x}(t),\delta\bold{x}(t)]dt\\ =&&\int_{t_0+\delta t}^{t_1+\delta t}L[t,\bold{x}’(t),\dot{\bold{x}}'(t)]dt-\int_{t_0}^{t_1}L[\bold{x}(t),\delta\bold{x}(t)]dt\\ =&&(L(t_1)-L(t_0))\delta t+(\frac{\partial L}{\partial\dot{\bold{x}}}(-\dot{\bold{x}}\delta t+\delta\bold{x}))|_{t_1}-(\frac{\partial L}{\partial\dot{\bold{x}}}(-\dot{\bold{x}}\delta t+\delta\bold{x}))|_{t_0} \end{eqnarray}$

如果 $\delta S=0$ ，那么我们有如下**守恒定律**

$[(\frac{\partial L}{\partial \dot{\bold{x}}}\dot{\bold{x}}-L)\delta t-\frac{\partial L}{\partial\dot{\bold{x}}}\delta\bold{x}]|_{t_1}=[(\frac{\partial L}{\partial \dot{\bold{x}}}\dot{\bold{x}}-L)\delta t-\frac{\partial L}{\partial\dot{\bold{x}}}\delta\bold{x}]|_{t_0}$。

**守恒荷**是

$\bold{Q}_r=(\frac{\partial L}{\partial \dot{\bold{x}}}\dot{\bold{x}}-L)T_r-\frac{\partial L}{\partial\dot{\bold{x}}}\bold{X}_r$ 。

它满足方程 $\frac{d\bold{Q}_r}{dt}=0$ 。

![]((20240916)量子场论第四讲_对称性和守恒定律I_Expansion/v2-afee22df7da66a43074034ae38a053da_1440w.jpg)  

太阳系

  
  

现在来考虑上面的”地球绕着太阳转“的物理系统。

* **时间平移对称性**给出：

$H=\frac{\partial L}{\partial \dot{r}}\dot{r}+\frac{\partial L}{\partial\dot\varphi}\dot\varphi-L=\frac{1}{2}m(\dot{r}^2+r^2\dot{\varphi}^2)-\frac{GMm}{r}$ ，

这就是能量守恒。

* **空间平移对称性**给出：

$P_x=\frac{\partial L}{\partial\dot r}\cos\varphi+\frac{\partial L}{\partial\dot\varphi}(-\frac{\sin\varphi}{r})=m\dot r\cos\varphi-mr\dot\varphi\sin\varphi=\frac{d}{dt}(mr\cos\varphi)=m\dot x$

**我们再来看一个量子场论的物理系统**。上一讲我们猜到了标量场的拉氏量（准确说是拉氏密度），如下:

$\mathcal{L}[\phi(x),\partial_\mu\phi(x)]=\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{1}{2}m^2\phi^2$ 。

我们考察如下一个场论中普遍形式的拉氏量。

$\mathcal{L}[x^\mu,\phi(x),\partial_\mu\phi(x)]$

微小的对称变换即：

$\delta x^\mu\equiv x'^{\mu}-x^\mu=X^\mu\epsilon$

$\delta\phi\equiv\phi'(x')-\phi(x)=\Phi\epsilon$

$\begin{eqnarray} \phi'(x)-\phi(x)=&&\phi'(x)-\phi'(x')+\phi'(x')-\phi(x)\\ =&&\frac{\partial\phi'(x')}{\partial x'^\mu}(-X^\mu\epsilon)+\delta\phi\\ =&&-\partial_\mu\phi(x)X^\mu\epsilon+\delta\phi \end{eqnarray}$

$\frac{\partial\phi'(x)}{\partial x^\mu}-\frac{\partial\phi(x)}{\partial x^\mu}=-\partial_\mu\partial_\nu\phi(x)X^\nu\epsilon+\delta\partial_\mu\phi$

接着我们来看作用量的差别

$\begin{eqnarray} \delta S=&&\int_{\Omega'}d^4x'\mathcal{L}[x'^\mu,\phi'(x'),\partial_{\mu}'\phi'(x')]-\int_{\Omega}d^4x\mathcal{L}[x^\mu,\phi(x),\partial_{\mu}\phi(x)]\\ =&&\int_{\Omega}d^4x'(x)\mathcal{L}[x'^\mu(x),\phi'(x'(x)),\partial_{\mu}'\phi'(x'(x))]-\int_{\Omega}d^4x\mathcal{L}[x^\mu,\phi(x),\partial_{\mu}\phi(x)] \end{eqnarray}$

这里利用了 $\int_{\Omega'}\cdots d^4x'=\int_\Omega \cdots d^4x'(x)$ ，这样做的好处是积分使得积分区域相同。第一项做如下处理：

$\begin{eqnarray}&&\int_{\Omega}d^4x'(x)\mathcal{L}[x'^\mu(x),\phi'(x'(x)),\partial_{\mu}'\phi'(x'(x))]-\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]+\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\\ =&&\int_\Omega d^4x'(x)(\partial_\mu\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)])\delta x^\mu+\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\\ =&&\int_\Omega d^4x'(x)(\partial_\mu\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)])\delta x^\mu+\int_\Omega d^4x'(x)\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\\ =&&\int_\Omega d^4x(\partial_\mu\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)])\delta x^\mu+\int_\Omega d^4x'(x)\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\\ =&&\int_\Omega d^4x(\partial_\mu\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)])\delta x^\mu+\int_\Omega d^4x(1+\partial_\mu\delta x^\mu)\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\\ =&&\int_\Omega d^4x\partial_\mu(\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\delta x^\mu)+\int_\Omega d^4x\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)] \end{eqnarray}$

因此得到

$\delta S=\int_\Omega d^4x\partial_\mu(\mathcal{L}[x^\mu,\phi'(x),\partial_{\mu}\phi'(x)]\delta x^\mu)+\int_\Omega d^4x \delta \mathcal{L}$

这个和上面经典情况的形式就非常相似了！！

$\begin{eqnarray} \delta\mathcal{L}=&&\frac{\partial\mathcal{L}}{\partial\phi}(-\partial_\nu\phi X^\nu\epsilon+\delta\phi)+\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi}(-\partial_\mu\partial_\nu\phi X^\nu\epsilon+\delta\partial_\mu\phi)\\ =&&\partial_\mu(\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi}(-\partial_\nu\phi X^\nu\epsilon+\delta\phi))+(\frac{\partial\mathcal{L}}{\partial\phi}-\partial_\mu\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi})(-\partial_\mu\phi X^\mu\epsilon+\delta\phi)\\ =&&\partial_\mu(\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi}(-\partial_\nu\phi X^\nu\epsilon+\delta\phi)) \end{eqnarray}$

最终我们得到：

$\delta S=\int_\Omega d^4x\partial_\mu[\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi}(-\partial_\nu\phi X^\nu\epsilon+\delta\phi)+\mathcal{L}\delta x^\mu]$

对应的**守恒流**为：

$j^\mu=(\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi}\partial_\nu\phi X^\nu-\mathcal{L}X^\mu）-\frac{\partial\mathcal{L}}{\partial\partial_\mu\phi}\Phi$

它**满足** $\partial_\mu j^\mu=0$ 。我们把**这个结果应用于标量场**。

我们先来看能动量守恒。

$x'^\mu=x^\mu+a^\mu,\delta x^\mu=a^\mu=X^\mu\epsilon$

$\phi'(x')=\phi(x),\Phi=0$

$P^\mu=\frac{\partial\mathcal{L}}{\partial \partial_\mu\phi}\partial_\nu\phi X^\nu-\mathcal{L}X^\mu=\partial^\mu\phi\partial_\nu\phi X^\nu-(\frac{1}{2}\partial_\sigma\phi\partial^\sigma\phi-\frac{1}{2}m^2\phi^2)X^\mu=T_{\nu}^\mu X^\nu$

它满足 $\partial_\mu T^{\mu}_{\nu}=0$ 。

$T^\mu_\nu=\frac{\partial\mathcal{L}}{\partial \partial_\mu\phi}\partial_\nu\phi-g^\mu_\nu\mathcal{L}$

$T^{\mu\nu}=\frac{\partial\mathcal{L}}{\partial \partial_\mu\phi}\partial^\nu\phi-g^{\mu\nu}\mathcal{L}$

容易验证： $T^{00}=\mathcal{H}=\frac{1}{2}(\partial_0\phi\partial^0\phi-\partial_i\phi\partial^i\phi)+\frac{1}{2}m^2\phi^2$ , $T^{0i}=\partial^0\phi\partial^i\phi$ ，

$\partial_tT^{00}+\partial_xT^{10}+\partial_yT^{20}+\partial_zT^{30}=0$ 。

其中第一项是能量流，后三项式能量流密度。

总结一下，这一讲主要讨论的是**时空对称性**，下一讲，我们介绍其他两种对称性：**内部对称性**和**规范对称性**！

**留一个家庭作业**：请重复上面诺特定理的证明！

  


![]((20240916)量子场论第四讲_对称性和守恒定律I_Expansion/v2-639ecf7f5224a704fbbe324703b0bbca_1440w.jpg)  

Noether

  
  
