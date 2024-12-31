# 量子场论第七讲：单粒子态、因果律、反粒子

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/721075207]

[Expansion：量子场论第六讲：标量场、场量子化](https://zhuanlan.zhihu.com/p/720625814)

**内容提要**：

* 标量场洛伦兹变换、单粒子态
* 复标量场量子化
* 因果律 $\Rightarrow$ 反粒子

![]((20240921)量子场论第七讲单粒子态因果律反粒子_Expansion/v2-74fda8b78c8327f113eab38ea2cbe9ad_1440w.jpg)  

光锥

  
  

这一讲我们讨论标量场的**洛伦兹变换性质，**以及为什么**因果律导致反粒子**的存在！！

考虑一个沿着 $z$ 方向的洛伦兹变换。我们有

$E'=\gamma(E-\beta p_z)$

$p_z'=\gamma(p_z-\beta E)$

$p'_x=p_x,\quad p_y'=p_y$ 。

注意到 $E=\sqrt{m^2+p_x^2+p_y^2+p_z^2}$ ，我们有$\frac{\partial E}{\partial p_z}=\frac{p_z}{E}$ 。因此有

$\frac{dp_z'}{E'}=\frac{\gamma(1-\beta\frac{p_z}{E})dp_z}{\gamma(E-\beta p_z)}=\frac{dp_z}{E}$ 。

我们发现 $\int\frac{d^3p}{(2\pi)^32E_p}$ 是**洛伦兹不变的**。另外一种理解方式是

$\int\frac{d^3p}{(2\pi)^32E_p}=\int\frac{d^4p}{(2\pi)^4}\delta(p^2-m^2)|_{p^0>0}$ ，

因为 $d^4p$ 、 $p^2$ 和 $p^0>0$ 都是洛伦兹不变的，所以原积分也是洛伦兹不变的。利用用到了如下性质

$\delta(f(x)-f(x_0))=\frac{\delta(x-x_0)}{|f'(x_0)|}$ 。

类似的证明可以得到

$\delta^{(3)}(\bold{p}-\bold{q})E=\delta^{(3)}(\bold{p}'-\bold{q}')E'$

也是洛伦兹不变 （家庭作业！）。现在我们来看标量场在两个不同惯性参考系。

$\phi(x)=\int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}(a_pe^{-ipx}+a_p^\dagger e^{ipx})$ 。

$\phi’(x‘)=\int \frac{d^3p’}{(2\pi)^3}\frac{1}{\sqrt{2E_{p'}}}(a_pe^{-ip'x'}+a_p^\dagger e^{ip'x'})$

注意到**标量场满足 $\phi'(x')=\phi(x)$** 以及上面的积分的洛伦兹不变性，我们有

$\sqrt{2E_p}a_p^{(\dagger)} = \sqrt{2E_{p'}}a_{p'}^{(\dagger)} $ 。

从上一讲，我们知道动量为 $p$ 的标量粒子态正比于 $a_p^\dagger|0\rangle$ ，因此**为了保证 $\langle q|p\rangle$ 的洛伦兹不变性**，我们选取如下的**单粒子态归一化规定**。

$|p\rangle\equiv\sqrt{2E_p}a_p^\dagger|0\rangle$

我们有

$\langle q|p\rangle=(2\pi)^3(2E_p)\delta^{(3)}(\bold{p}-\bold{q})$ ，

它是洛伦兹不变的，而且 $|p\rangle$ 的洛伦兹变换[#ref\_1](#ref\_1)为

$U(\Lambda)|p\rangle=|\Lambda p\rangle$ 。

我们把 $\phi(x)$ 作用于真空 态$|0\rangle$ 得到

$\phi(x)|0\rangle=\int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p}e^{ipx}|p\rangle$ ，

它可以**理解为在时空坐标 $x$ 处产生一个标量粒子**。类似于 $\langle \bold{p}|\bold{x}\rangle\propto e^{-i\bold{p}\cdot\bold{x}}$ ，我们有

$\langle p|\phi(x)|0\rangle=e^{ipx}$ 。

下面我们考察一下复的标量场，不难猜到，量子化的复标量场为

$\phi(x)=\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}(a_pe^{-ipx}+b_p^\dagger e^{ipx})$

$\phi^\dagger(x)=\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}(b_pe^{-ipx}+a_p^\dagger e^{ipx})$

利用 $\phi(x)=\frac{1}{\sqrt{2}}(\phi_1(x)+i\phi_2(x))$ ，我们可以得到

$a_p=\frac{1}{\sqrt{2}}(a_{1p}+ia_{2p})$ ， $b_p^\dagger=\frac{1}{\sqrt{2}}(a_{1p}^\dagger+ia_{2p}^\dagger)$

$[a_p,a_{p'}^\dagger]=(2\pi)^3\delta^{(3)}(\bold{p}-\bold{p}')$

$[b_p,b_{p'}^\dagger]=(2\pi)^3\delta^{(3)}(\bold{p}-\bold{p}')$

$[a_p,b_{p'}^\dagger]=0$ 还有其他的对易关系都为0。

类似地，哈密顿量为

$\begin{eqnarray} H=&&\int\frac{d^3p}{(2\pi)^3}E_p(a_{1p}^\dagger a_{1p}+\frac{1}{2}[a_{1p},a_{1p}^\dagger]+a_{2p}^\dagger a_{2p}+\frac{1}{2}[a_{2p},a_{2p}^\dagger])\\ =&&\int\frac{d^3p}{(2\pi)^3}E_p(a_p^\dagger a_p+b_p^\dagger b_p+\frac{1}{2}[a_p,a_p^\dagger]+\frac{1}{2}[b_p,b_p^\dagger]) \end{eqnarray}$

我们讲复标量场作用于真空态得到

$\phi(x)|0\rangle=\int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p} e^{ipx}|p\rangle_b$

$\phi^\dagger(x)|0\rangle=\int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p} e^{ipx}|p\rangle_a$

下面考虑下面一个**关于因果性(causality)的问题**：计算在 $x$ 处产生的粒子在 $y$处被探测到的概率。

$\langle 0|\phi(y)\phi(x)|0\rangle=0$

$\begin{eqnarray} \langle 0|\phi^\dagger(y)\phi(x)|0\rangle=&&\langle 0|\int\frac{d^3k}{(2\pi)^3}\frac{d^3p}{(2\pi)^3}\frac{1}{2\sqrt{E_kE_p}}b_kb_p^\dagger e^{i(px-ky)}|0\rangle\\ =&&\langle 0|\int\frac{d^3k}{(2\pi)^3}\frac{d^3p}{(2\pi)^3}\frac{1}{2\sqrt{E_kE_p}}[b_k,b_p^\dagger]e^{i(px-ky)}|0\rangle\\ =&&\int\frac{d^3k}{(2\pi)^3}\frac{d^3p}{(2\pi)^3}\frac{1}{2\sqrt{E_kE_p}}(2\pi)^3\delta^{(3)}(\bold{k}-\bold{p})e^{i(px-ky)}\\ =&&\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{ik(x-y)} \end{eqnarray}$

$\langle 0|\phi(y)\phi^\dagger(x)|0\rangle=\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{ik(x-y)}$

$\langle 0|\phi^\dagger(y)\phi^\dagger(x)|0\rangle=0$

首先我可以看到这些**概率幅都是洛伦兹不变的**。

然后我们来具体计算这个概率幅。

$\begin{eqnarray} \int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{ik(x-y)}=&&\int\frac{k^2 dkd\cos\theta d\varphi}{(2\pi)^3}\frac{1}{2\sqrt{m^2+k^2}}e^{ik^0(x^0-y^0)-ikr\cos\theta}\\ =&&\int\frac{k^2 dk}{(2\pi)^2}\frac{1}{2\sqrt{m^2+k^2}}e^{ik^0(x^0-y^0)}\frac{2\sin(kr)}{kr} \end{eqnarray}$

* 如果是类时间隔，我们总是可以找到一个洛伦兹变换使得 $\bold{x}-\bold{y}=0$ ，因此有

$\begin{eqnarray} \int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{ik(x-y)} =&&\int\frac{k^2 dk}{(2\pi)^2}\frac{1}{\sqrt{m^2+k^2}}e^{ik^0(x^0-y^0)} \end{eqnarray}$

* 如果是类空间隔，我们总是可以找到一个洛伦兹变换是的 $x^0-y^0=0$ ，因此有

$\begin{eqnarray} \int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}e^{ik(x-y)} =&&\int\frac{k^2 dk}{(2\pi)^2}\frac{1}{2\sqrt{m^2+k^2}}\frac{2\sin(kr)}{kr}\\ =&&\int\frac{dk}{(2\pi)^2r}\frac{k\sin(kr)}{\sqrt{m^2+k^2}}\\ =&&\int_0^\infty\frac{dx}{(2\pi)^2r^2}\frac{x\sin x}{\sqrt{m^2r^2+x^2}}\neq 0 \end{eqnarray}$

这就很麻烦了，**狭义相对论要求类空间隔不能传递物理信号，但是概率幅不等于0如何理解呢？量子力学告诉我们不应该考虑粒子能不能传播到类空间隔处，而应该考虑类空间隔两处的测量会不会互相影响**。因此应该考虑

$\begin{eqnarray} \langle 0|[\phi^\dagger(y),\phi(x)]|0\rangle=\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k}(e^{ik(x-y)}-e^{-ik(x-y)})=0 \end{eqnarray}$ 。

结果等于0是因为对于类空间隔，我们总是可以进行一次洛伦兹变换使得 $x-y \to y-x$ （对于类时间隔，这是办不到的）。因此我们发现两个概率幅抵消了。

$\langle 0|\phi^\dagger(y)\phi(x)|0\rangle-\langle 0|\phi(x)\phi^\dagger(y)|0\rangle=0$

这两个概率幅分别是什么呢？

$\langle 0|\phi^\dagger(y)\phi(x)|0\rangle=\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k} \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p} e^{i(px-ky)}\langle k|p\rangle_b$

$\langle 0|\phi(x)\phi^\dagger(y)|0\rangle=\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E_k} \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_p} e^{i(py-kx)}\langle k|p\rangle_a$

变为物理的语言就是，**正粒子顺着时间的方向从 $x$ 处到达类空间隔的 $y$ 的概率幅，刚好抵消掉反粒子逆着时间的方向从 $y$ 处到达类空间隔的 $x$ 处的概率幅**。

这个关于因果性的有趣的事实历史上被称作“**Feynman–Stückelberg interpretation**"[#ref\_2](#ref\_2)。

此外，我们注意到，这个抵消要求**反粒子必须存在，而且跟正粒子具有相同的质量而相反的电荷**。

![]((20240921)量子场论第七讲单粒子态因果律反粒子_Expansion/v2-446f222eb5d5b23e672369964f73fe19_1440w.jpg)  

Ernest Stuckelberg

  
  
![]((20240921)量子场论第七讲单粒子态因果律反粒子_Expansion/v2-7d552949659235e65009e72cead14143_1440w.jpg)  

Richard Feynman

  
  

---

对于复标量场，我们可以重复上一讲的方法。

$\mathcal{L}[\phi,\partial_\mu\phi;\phi^*,\partial_\mu\phi^*]=\partial_\mu\phi^*\partial^\mu\phi-m^2\phi^*\phi$

$\pi=\frac{\partial\mathcal{L}}{\partial_0\phi}=\partial^0\phi^*$ ， $\pi^*=\frac{\partial\mathcal{L}}{\partial_0\phi^*}=\partial^0\phi$

$\mathcal{H}=\pi\partial_0\phi+\pi^*\partial_0\phi^*-\mathcal{L}=\pi^*\pi+\triangledown\phi^*\triangledown\phi+m^2\phi^*\phi$

$\phi(x)=\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}(a_pe^{-ipx}+b_p^\dagger e^{ipx})$

$\pi^*(x)=\int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_p}{2}}(a_pe^{-ipx}-b_p^\dagger e^{ipx})$

$\phi^*(x)=\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}(b_pe^{-ipx}+a_p^\dagger e^{ipx})$

$\pi(x)=\int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_p}{2}}(b_pe^{-ipx}-a_p^\dagger e^{ipx})$

强加如下"等时"对易关系

$[\phi(t,\bold{x}),\pi(t,\bold{x}')]=i\delta^{(3)}(\bold{x}-\bold{x}')$ ， $[\phi^*(t,\bold{x}),\pi^*(t,\bold{x}')]=i\delta^{(3)}(\bold{x}-\bold{x}')$

其他对易关系为零。

$a_k=\int_{-\infty}^{+\infty}[\sqrt{\frac{E_k}{2}}\phi(x)+i\sqrt{\frac{1}{2E_k}}\pi^*(x)]e^{ikx}d^3\bold{x}$

$b_k^\dagger=\int_{-\infty}^{+\infty}[\sqrt{\frac{E_k}{2}}\phi(x)-i\sqrt{\frac{1}{2E_k}}\pi^*(x)]e^{-ikx}d^3\bold{x}$

$a_k^\dagger=\int_{-\infty}^{+\infty}[\sqrt{\frac{E_k}{2}}\phi^*(x)-i\sqrt{\frac{1}{2E_k}}\pi(x)]e^{-ikx}d^3\bold{x}$

$b_k=\int_{-\infty}^{+\infty}[\sqrt{\frac{E_k}{2}}\phi^*(x)+i\sqrt{\frac{1}{2E_k}}\pi(x)]e^{ikx}d^3\bold{x}$

由此得到：

$[a_k,a_{k'}^\dagger]=\int d^3xd^3x'(\frac{-i}{2}[\phi(x),\pi(x')]e^{i(kx-k'x')}+\frac{i}{2}[\pi^*(x),\phi^*(x')]e^{i(kx-k'x')}=(2\pi)^3\delta^{(3)}(\bold{k}-\bold{k}')$

$[b_k,b_{k'}^\dagger]=(2\pi)^3\delta^{(3)}(\bold{k}-\bold{k}')$

其他对易关系为0。

## 参考  

1. [#ref\_1\_0](#ref\_1\_0)Weinberg书第1册第1章专门集中讨论粒子在Poincare群里面的分类，感兴趣的同学可以自行研究。
2. [#ref\_2\_0](#ref\_2\_0)Feynman–Stückelberg interpretation [https://en.wikipedia.org/wiki/Antiparticle](https://en.wikipedia.org/wiki/Antiparticle)
