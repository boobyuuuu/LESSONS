# 量子场论第八讲：无穷远、无穷未来、传播子

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/721510859]



**内容提要**：

* 因果律，边界条件
* 无穷远处，无穷未来
* 标量场传播子

![]((20240925)量子场论第八讲无穷远无穷未来传播子_Expansion/v2-46b4ab164ff56a82bfd75cc7ec7c14a3_1440w.jpg)  

从A到B

  
  

这一讲主要讲**传播子（propagator**），就是研究一个粒子从时空点 $x=(x^0,\bold{x})$ 传播到 $y=(y^0,\bold{y})$ 处的概率幅。上一讲，我们已经知道这个**概率幅**是

$\langle0|\phi(y)\phi(x)|0\rangle = \int \frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-ik(y-x)}$ 。

这个积分怎么算呢？一般是利用**复变函数的留数定理**，然后选取”合适的“积分路径来计算，数学上虽然可行，但是物理意义不太明确。我的感觉是，是**物理上”合理“的因果律和边界条件决定了”合适“的积分路径**。为了让大家能够理解传播子数学上的一些花哨的trick（正是这些trick会让人眼花缭乱），我们专门花一讲的时间来讨论这个问题。

**狭义相对论要求事件的发生一定要满足因果律**。一个例子就是上一讲讲过的类空间隔两处的测量应该互相不影响，这直接导致量子场应该可以激发产生质量相同、量子数相反的正反粒子，二者的抵消作用保护了因果律。

下面之间说出本讲的核心。

* **因果律要求类时间隔发生的事件必须有时间先后顺序**
* **传播子应该满足边界条件：即传播到无穷远处的概率幅趋于0.**

以下推导方式和理解方式，属于个人心得，我没有在其他书本上看到过。

我们记**标量场传播子为** $D_F(y-x)$ ，那么因果律要求：如果是从 $x$ 处传播到 $y$处，则 $y$ 的时间晚于 $x$ ；反之从 $y$ 传播到 $x$ 处，则则 $x$ 的时间晚于 $y$。因此我引进**如下定义**：

$D_F(y-x)\equiv \langle 0|T\phi(y)\phi(x)|0\rangle=\theta(y^0-x^0)\langle 0|\phi(y)\phi(x)|0\rangle+\theta(x^0-y^0)\langle 0|\phi(x)\phi(y)|0\rangle$ ，

这里 **$T$ 是编时乘积算符**，表示把时间晚的东东往左边排。

那么怎么计算它呢？上一节我们得到

$\langle 0|\phi(y)\phi(x)|0\rangle=\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-ik(y-x)}$ ，

这里 $E_k=\sqrt{m^2+\bold{k}^2}$ ，而且我们已经知道它是洛伦兹不变的。

现在考虑类时间隔且 $y^0-x^0>0$ 的情况，同时考虑 $|\bold{y}-\bold{x}|\to +\infty$ 的极限情况，我们**预期对于类时间隔，从 $x$ 穿传播到无穷远 $y$ 处，需要无穷长的时间，而且概率幅应该趋于0**。

因此我们我们应该添加一个正的小 $\epsilon$ 。

$-ik(y-x)=-i[E_k(y^0-x^0)-\bold{k}\cdot(\bold{y}-\bold{x})]\to -i[(E_k-i\epsilon)(y^0-x^0)-\bold{k}\cdot(\bold{y}-\bold{x})]$

注意到

$\begin{eqnarray} \int \frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2E_k}}=&&\int \frac{d^4k}{(2\pi)^3}\delta(k^2-m^2)|_{k^0>0}\\ =&&\int \frac{d^3k}{(2\pi)^3}\int_0^{+\infty} dk^0\delta(k^{02}-\bold{k}^2-m^2)\\ =&&\int \frac{d^3k}{(2\pi)^3}\int_0^{+\infty} dk^0\delta(k^{02}-E_k^2) \end{eqnarray}$，

因此为了让 $k^0$ 取值 $E_k-i\epsilon$ ，我们可以有

$\int \frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2E_k}}=\int \frac{d^4k}{(2\pi)^3}\delta(k^2-m^2+i\epsilon)|_{k^0>0}$

这样我们得到

$\begin{eqnarray} \langle 0|\phi(y)\phi(x)|0\rangle|_{y^0>x^0}=&&\int\frac{d^4k}{(2\pi)^3}\delta(k^2-m^2+i\epsilon)|_{k^0>0}e^{-ik(y-x)}\\ =&&\int\frac{d^4k}{(2\pi)^3}\frac{1}{2\pi}\int_0^{+\infty} e^{i(k^2-m^2+i\epsilon)T}dTe^{-ik(y-x)}\\ =&&\int\frac{d^4k}{(2\pi)^3}\frac{1}{2\pi}\frac{e^{i(k^2-m^2+i\epsilon)T}|_0^{+\infty}}{i(k^2-m^2+i\epsilon)}e^{-ik(y-x)}\\ =&&\int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2-m^2+i\epsilon}e^{-ik(y-x)} \end{eqnarray}$

那 $x^0>y^0$ 的情况这样呢？我们有

$\begin{eqnarray} \langle 0|\phi(x)\phi(y)|0\rangle=&&\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-ik(x-y)}\\ =&&\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-i[E_k(x^0-y^0)-\bold{k}\cdot(\bold{x}-\bold{y})]}\\ =&& \int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-i[E_k(x^0-y^0)+\bold{k}\cdot(\bold{x}-\bold{y})]} \quad \color{blue}{\bold{k}\to-\bold{k}}\\ =&& \int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-i[-E_k(y^0-x^0)-\bold{k}\cdot(\bold{y}-\bold{x})]} \end{eqnarray}$

注意到

$\begin{eqnarray} \int \frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}=&&\int \frac{d^4k}{(2\pi)^3}\delta(k^2-m^2)|_{k^0<0}\\ =&&\int \frac{d^3k}{(2\pi)^3}\int_{-\infty}^{0} dk^0\delta(k^{02}-\bold{k}^2-m^2)\\ =&&\int \frac{d^3k}{(2\pi)^3}\int_{-\infty}^0 dk^0\delta(k^{02}-E_k^2) \end{eqnarray}$

基于同样的理由，我们预期传播到无穷远的概率幅为0，因此让 $k^0$ 取值为 $-E_k+i\epsilon$ 。因此有

$\begin{eqnarray} \langle 0|\phi(x)\phi(y)|0\rangle|_{x^0>y^0} =&& \int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{-i[(-E_k+i\epsilon)(y^0-x^0)-\bold{k}\cdot(\bold{y}-\bold{x})]}\\ =&& \int\frac{d^3k}{(2\pi)^3}\int dk^0\delta(k^2-m^2+i\epsilon)|_{k^0<0}e^{-i[k^0(y^0-x^0)-\bold{k}\cdot(\bold{y}-\bold{x})]}\\ =&& \int\frac{d^3k}{(2\pi)^3}\int dk^0\delta(k^2-m^2+i\epsilon)|_{k^0<0}e^{-ik(y-x)}\\ =&& \int\frac{d^4k}{(2\pi)^3}\frac{1}{2\pi}\int_0^{+\infty} e^{i(k^2-m^2+i\epsilon)T}dTe^{-ik(y-x)}\\ =&&\int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2-m^2+i\epsilon}e^{-ik(y-x)} \end{eqnarray}$

因此本质上，我们证明了如下结果：

$\langle 0|\phi(x)\phi(y)|0\rangle|_{x^0>y^0}=\langle 0|\phi(y)\phi(x)|0\rangle|_{y^0>x^0}$ ，

它大概表明从 $x$ 处传播到 $y$ 处的概率幅和从 $y$ 处传播到 $x$ 的概率幅相等。对于类空间隔，上一讲我已经知道是成立的了。**对于类空间隔，我们必须加上时间顺序**。我想这是狭义相对论因果律的要求！

鉴于上面的讨论，标量场传播子可以方便地写成一个统一的形式。

$D_F(y-x)=\int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2-m^2+i\epsilon}e^{-ik(y-x)}$

大家可以参考Peskin的书或者留数定理，计算一下这个积分 （家庭作业！）。

以后计算费曼图，我们一般使用传播子的动量表象比较容易，即是

$\tilde{D}_F(p) = \frac{i}{p^2-m^2+i\epsilon}$ 。

如果大家还有印象的话，我们在第二讲讲静电场的时候，特别是求解Poisson方程 $-\triangledown^2\varphi=\frac{\rho}{\epsilon_0}$ 时遇到过。形式和数学本质上都是一样的。

![]((20240925)量子场论第八讲无穷远无穷未来传播子_Expansion/v2-e61c8dc3628adefde97b80b398856597_1440w.jpg)  

传播子积分路径

  
  
![]((20240925)量子场论第八讲无穷远无穷未来传播子_Expansion/v2-38390b85363a5e9e7fb7348e55f465a5_1440w.jpg)  

Richard Feynman

  
  
