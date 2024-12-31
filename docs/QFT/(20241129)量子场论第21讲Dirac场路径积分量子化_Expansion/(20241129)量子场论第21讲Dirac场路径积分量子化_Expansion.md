# 量子场论第21讲：Dirac场路径积分量子化

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/9495047938]



我们在第18讲和第19讲分别讲了标量场和电磁场的路径积分量子化，轮到Dirac场了。这个有点麻烦！需要用到**Grassmann Algebra** (也称外代数Exterior Algebra）。**它的作用效果**跟我们以往理解的数学操作非常不一样！简言之，很多地方是**相反的**！！

内容提要：

* Grassmann代数
* Dirac场传播子
* QED顶点的费曼规则
* S矩阵

![]((20241129)量子场论第21讲Dirac场路径积分量子化_Expansion/v2-4a1fa02eac8a1f41b41b854dc71373c6_1440w.jpg)  

这个人就是Hermann Grassmann，他是一个语言学家，他的数学成果在他六十多岁才为人所知（可惜当时他因为自己的数学著作无人问津，都已经对几何失去兴趣了！）。

我们用c1,c2,...表示通常的复数c-number，用g1,g2,...表示Grassmann数。那么有

对于乘法，我们有

$c_1c_2=c_2c_1$ ， $g_1\wedge g_2=-g_2\wedge g_1$ 。

它们满足反对易性，因此 $g_1\wedge g_1=g_2\wedge g_2=0$ 。

为了容易理解这个代数，我们采用wikepedia的一个例子。

![]((20241129)量子场论第21讲Dirac场路径积分量子化_Expansion/v2-3e3ff4f1236639035f26d23160e5dabe_1440w.jpg)  

这个平行四边形由矢量 $\bold{v}=(a,b)$ 和 $\bold{w}=(c,d)$ 决定，它的面积是

$\det\begin{pmatrix}a & c \\b & d\end{pmatrix}=ad-bc$ 。

我们也可以这么做

$\bold{v}=ag_1+bg_2$ ， $\bold{w}=cg_1+dg_2$

我们发现面积刚好等于 $A=\det(\bold{v},\bold{w})=\bold v\wedge\bold{w}$ 。下面为方便，我们不会明显写出 $\wedge$ 。

由于Grassmann数的反对易性，一个一般的函数的形式是很简单的。

$f(g_1,g_2)=c_0+c_1g_1+c_2g_2+c_{12}g_1g_2$ 。

它的微分和积分是如下定义的（我们采取邻近原则，就是先操作最靠近的。）。

$\frac{\partial }{\partial g_1}f(g_1,g_2)=c_1+c_{12}g_2$ ，

$\frac{\partial }{\partial g_2}f(g_1,g_2)=c_2-c_{12}g_1$ （因为我们需要先交换 $g_1,g_2$ ，在求导），

$\frac{\partial }{\partial g_2}\frac{\partial }{\partial g_1}f(g_1,g_2)=c_{12}=-\frac{\partial }{\partial g_1}\frac{\partial }{\partial g_2}f(g_1,g_2)$ 。

对于积分，我们要求有平移不变性（translation invariance)，即

$\int dg_1f(g_1,g_2)=\int dg_1f(g_1+g,g_2)$ 对任意g成立。

因此有$\int dg_1(c_1g+c_{12}gg_2)=0$ ，也即

$\int dg_1(c_1+c_{12}g_2)=0$ ，对任意 $c_1,c_{12}$ 成立。

所以有 $\int dg_1f(g_1,g_2)=\int dg_1(c_1g_1+ c_{12}g_1 g_2)$ 。

我们进一步定义 $\color{blue}{\int dg_1g_1=1}$ ，因此 $\int dg_1f(g_1,g_2)=c_1+c_{12}g_2=\frac{\partial }{\partial g_1}f(g_1,g_2)$ 。

所以对于grassmann代数，**微分和积分是一样的**（老实说，我也不知道为什么这么定义。知道的同学可以告诉我！谢谢！）。

下一个很重要的性质是考虑如下积分 $\bar{g}$ 和 $g$ 是独立的Grassmann数。

$\int d\bar{g}dge^{-\bar{g}g}=\int d\bar{g}dg(1-\bar{g}g)=\int d\bar{g}dgg\bar{g}=1$ 。

进一步有

$\begin{eqnarray} &&\int d\bar{g}_1dg_1d\bar{g_2}dg_2e^{-\sum_{ij}\bar{g}_iA_{ij}g_j}\\ =&&\int d\bar{g}_1dg_1d\bar{g_2}dg_2(1-\sum_{ij}\bar{g}_iA_{ij}g_j+\frac{1}{2}\sum_{ij}\bar{g}_iA_{ij}g_j\sum_{kl}\bar{g}_kA_{kl}g_l)\\ =&&\int d\bar{g}_1dg_1d\bar{g_2}dg_2\frac{1}{2}\sum_{ijkl}\bar{g}_ig_j\bar{g}_kg_lA_{ij}A_{kl}\\ =&&\int d\bar{g}_1dg_1d\bar{g_2}dg_2\frac{1}{2}\sum_{ijkl}g_j\bar{g}_ig_l\bar{g}_kA_{ij}A_{kl}\\ =&&\frac{1}{2}\sum_{ijkl}\epsilon_{lj}\epsilon_{ki}A_{ij}A_{kl}\\ =&&\det A \end{eqnarray}$

这里 $\epsilon_{mn}$ 是二阶反对称张量，满足 $\epsilon_{12}=-\epsilon_{21}=1$ 。所以我们得到了一个有用的东西。

$\color{blue}{\int d\bar{g}_1dg_1d\bar{g_2}dg_2e^{-\sum_{ij}\bar{g}_iA_{ij}g_j}=\det A}$ 。

显然上式写成矢量形式比较方便，

定义 $\bold{g}=\begin{pmatrix}g_1\\ g_2\end{pmatrix}$ 和 $\bold{\bar{g}}=\begin{pmatrix}\bar{g}_1\\ \bar{g}_2\end{pmatrix}$ ，定义 $d\bold{\bar{g}}d\bold{g}=d\bar{g}_1dg_1d\bar{g_2}dg_2$ ，

我们有 $\color{blue}{\int d\bold{\bar{g}}d\bold{g}e^{-\bold{\bar{g}}^T\bold{A}\bold{g}}=\det\bold{A}}$ ，很多时候上面的 转置$T$ 不会明显的写出来。类似地有

$\begin{eqnarray} &&\int d\bar{g}_1dg_1d\bar{g_2}dg_2g_k\bar{g}_le^{-\sum_{ij}\bar{g}_iA_{ij}g_j}\\ =&&\int d\bar{g}_1dg_1d\bar{g_2}dg_2g_k\bar{g}_l(-1)\sum_{ij}\bar{g}_iA_{ij}g_j\\ =&&\sum_{ij}A_{ij}\epsilon_{jk}\epsilon_{il}\\ =&& (A^{-1})_{kl}\det A \end{eqnarray}$

有了上面的准备，我们可以接触费米子了。我们把 $\psi(x)$ 和 $\psi^*(x)$ (或者更方便的 $\bar{\psi}(x)$ ）看做独立的Grassmann变量。引入Grassmann“源” 项$\eta$ 和 $\bar{\eta}$ 。

$\mathcal{L}_0^J[\psi,\bar{\psi},\eta,\bar{\eta}]=\bar{\psi}(i\not\partial-m)\psi+\bar{\eta}\psi+\bar{\psi}\eta$

运动方程为

$(i\gamma^\mu\partial_\mu-m)\psi=-\eta$

$\bar{\psi}(-i\gamma^\mu\partial_\mu-m)=-\bar{\eta}$

方程经典解为

$\psi_{cl}(x)=i\int d^4y S_F(x-y)\eta(y)=i\int d^4y \int\frac{d^4k}{(2\pi)^2}\frac{i(\gamma^\mu k_\mu+m)}{k^2-m^2+i\epsilon}e^{-ik(x-y)}\eta(y)$ 。

$\bar{\psi}_{cl}(x)=-i\int d^4y \bar{\eta}(y)S_F(y-x)=-i\int d^4y \bar{\eta}(y)\int\frac{d^4k}{(2\pi)^2}\frac{i(\gamma^\mu k_\mu+m)}{k^2-m^2+i\epsilon}e^{-ik(y-x)}$

按照前面的办法 $\psi=\psi_{cl}+\psi'$ ， $\bar{\psi}=\bar{\psi}_{cl}+\bar{\psi}'$

$\begin{eqnarray} \mathcal{L}_0^J[\psi,\bar{\psi},\eta,\bar{\eta}]= &&\bar{\psi}(i\not\partial-m)\psi+\bar{\eta}\psi+\bar{\psi}\eta\\ =&&\bar{\psi}(i\not\partial-m)(\psi_{cl}+\psi')+\bar{\eta}\psi+\bar{\psi}\eta\\ =&&-\bar{\psi}\eta+(\bar{\psi}_{cl}+\bar{\psi}')(i\not\partial-m)\psi'+\bar{\eta}\psi+\bar{\psi}\eta\\ =&&(\bar{\psi}_{cl}+\bar{\psi}')(i\not\partial-m)\psi'+\bar{\eta}\psi\\ =&&\bar{\psi}'(i\not\partial-m)\psi'-\bar{\eta}\psi'+\bar{\eta}\psi\\ =&&\bar{\psi}'(i\not\partial-m)\psi'+\bar{\eta}\psi_{cl} \end{eqnarray}$

$S^J=\int d^4x\mathcal{L}_0^J=\int d^4x[\bar{\psi}'(i\not\partial-m)\psi']+i\int d^4xd^4y\bar{\eta}(x)S_F(x-y)\eta(y)$

因此我们同样可以把生成泛函分成两部分。

$Z_0[\eta,\bar{\eta}]=\int \mathcal{D}\bar{\psi}\mathcal{D}\psi\exp[i\int d^4x[\bar{\psi}(i\not\partial-m)\psi]e^{-\int d^4xd^4y\bar{\eta}(x)S_F(x-y)\eta(y)}$

$\langle\Omega|T\bar{\psi}_H(x_2)\psi_H(x_1)|\Omega\rangle=(Z_0[0,0])^{-1}\frac{\delta}{i\eta(x_2)}\frac{\delta}{i\bar{\eta}(x_1)}Z_0[\eta,\bar{\eta}]|_{\eta=0,\bar{\eta}=0}=S_F(x_1-x_2)$

下面试图推导QED顶点对应的费曼规则。

$Z_0[J]=\int \mathcal{D}A \exp[i\int d^4x(\frac{1}{2}A_\mu(g^{\mu\nu}\partial^2 - (1-\frac{1}{\xi})\partial^\mu\partial^\nu)A_\nu + A_\mu J^\mu )]$

运动方程为

$[g^{\mu\nu}\partial^2 - (1-\frac{1}{\xi})\partial^\mu\partial^\nu]A_\nu=-J^\mu$

定义符号 $\Box^{\mu\nu}\equiv g^{\mu\nu}\partial^2 - (1-\frac{1}{\xi})\partial^\mu\partial^\nu$ ，那么

$-\Box^{-1}J=i\int d^4y D_{\mu\nu}(x-y)J^\mu(y)$

经典解为

$A_{\nu,cl}(x)=i\int d^4y D_{\mu\nu}(x-y)J^\mu(y)=i\int d^4y \int\frac{d^4k}{(2\pi)^4}\frac{-i(g_{\mu\nu}-(1-\xi)\frac{k_{\mu}k_\nu}{k^2})e^{-ik(x-y)}}{k^2+i\epsilon}J^\mu(y)$

$Z_0[J^\mu]=\int \mathcal{D}e^{i\int d^4x\mathcal{L}_0+A_\mu J^\mu}e^{-\frac{1}{2}\int d^4xd^4yJ^\mu D_{\mu\nu}(x-y)J^\nu}$

$Z_0[J^\mu,\eta,\bar{\eta}]=Z_0[0,0,0]\exp[-\frac{1}{2}\int d^4xd^4yJ^\mu D_{\mu\nu}(x-y)J^\nu-\int d^4xd^4y\bar{\eta}(x)S_F(x-y)\eta(y)]$

$Z[J^\mu,\eta,\bar{\eta}]=\exp[i\int d^4x\mathcal{L}_{int}(\frac{\delta}{i\delta J^\mu},\frac{\delta}{i\delta \eta},\frac{\delta}{i\bar\eta})]Z_0[J^\mu,\eta,\bar{\eta}]$

下面我们看一下**QED顶点的费曼规则**。

我们先得到生成泛函至 $e$ 阶。

$Z[J^\mu,\eta,\bar{\eta}]=(1-\int d^4x ie\frac{\delta}{i\delta \eta(x)}\gamma^\mu\frac{\delta(x)}{i\delta\bar\eta(x)}\frac{\delta}{i\delta J^\mu(x)}+\mathcal{O}(e^2))Z_0[J^\mu,\eta,\bar{\eta}]$

得到 $Z[J^\mu,\eta,\bar{\eta}]=[1-(ie)\int d^4x(i\int d^4y\bar\eta(y)S_F(y-x))\gamma^\mu(i\int d^4yS_F(x-y)\eta(y))(i\int d^4yD_{\mu\nu}(x-y)J^\nu(y))+\mathcal{O}(e^2)]Z_0[J^\mu,\eta,\bar{\eta}]$

$\langle\Omega|T\bar{\psi}\psi A_\mu|\Omega\rangle=\frac{1}{Z[0,0,0]}\frac{\delta}{i\delta \eta}\frac{\delta}{i\delta\bar\eta}\frac{\delta}{i\delta J^\mu}Z[J^\mu,\eta,\bar{\eta}]$

耐心计算可以得到：

$\langle\Omega|T\bar{\psi}(x)\psi(x)A_\mu(x)|\Omega\rangle=\color{blue}{-ie\gamma^\nu}\int d^4yS_F(y-x)S_F(x-y)D_{\nu\mu}(y-x)+\mathcal{O}(e^2)$

类似地，对于S矩阵，利用

$(i\not\partial-m)\frac{\delta}{i\delta\bar\eta}Z_0[\eta,\bar\eta]=-\eta Z_0[\eta,\bar\eta]$

和

$(-i\not\partial-m)\frac{\delta}{i\delta\eta}Z_0[\eta,\bar\eta]=\bar\eta Z_0[\eta,\bar\eta]$

我们可以如下计算：

$\Sigma[J^\mu,A_0^\mu;\eta,\bar\psi_0;\bar\eta,\psi_0]=\exp[i\int d^4x(A^\mu_0D_{\mu\nu}\frac{\delta}{i\delta J_\nu}+\bar\psi_0(i\not\partial-m)\frac{\delta}{i\delta\bar\eta}+\frac{\delta}{i\delta\eta}(-i\not\partial-m)\psi_0)]Z[J,\eta,\bar\eta]$

![]((20241129)量子场论第21讲Dirac场路径积分量子化_Expansion/v2-8348556905934f99fbc1a78e353263d1_1440w.jpg)  
