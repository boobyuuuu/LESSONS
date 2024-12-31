# 量子场论第15讲 ：Dirac方程和Majorana方程

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/3318293030]



**内容提要**：

* 从两个角度推导Dirac方程
* 顺带推导Majorana方程

Dirac方程的推导有很多种方式（我google可以搜索到3种），我在下面的回答中给出了两种比较容易的方式的详细推导过程，供大家参考。

[狄拉克方程是怎样推导出来的，有哪些物理意义？](https://www.zhihu.com/question/752276806/answer/10227011162)

Dirac方程的历史意义非常重要，是量子电动力学（Quantum Electrodynamics, 简称QED)不可或缺的一部分。它准确推导出了电子的自旋和磁矩，并预言了反粒子的存在。

上面的回答虽然导出了Dirac方程，但是没有推导出跟Dirac方程联系紧密的Majorana方程。目前的粒子物理标准模型，带电费米子毫无疑问是用Dirac场描述的，但是对于中微子(neutrino）这样的点中性费米子，它有可能是Dirac粒子，也有可能是Majorna粒子。区别是，对于后者，反粒子是它本身。感兴趣的同学可以调研一下”跷跷板机制“(seesaw mechanics)，它可以比较漂亮地解释为什么中微子的质量那么小。

下面首先我们结合上面回答的推导过程（这个我不想复制了-\_-!！），首先推导出Majorana方程。对于洛伦兹群(1/2,0)表示 $\chi$ ，我们知道，一个无穷小洛伦兹变换是

$\chi \to \chi'=(1+i\frac{\vec{\sigma}}{2}\cdot\vec{\theta}+\frac{\vec{\sigma}}{2}\cdot\vec{\beta})\chi$

其中 $\theta$ 表示转动角度， $\beta$ 表示Lorentz boost。我们先dagger(共轭转置)一下得到

$\chi^\dagger\to \chi^{\prime\dagger}=\chi^{\dagger}(1-i\frac{\vec{\sigma}}{2}\cdot\vec{\theta}+\frac{\vec{\sigma}}{2}\cdot\vec{\beta})$

dagger是很方便的，因为Pauli矩阵是厄米的， $\sigma^\dagger=\sigma$ 。

However，我们一个一个地做试试，转置一下得到

$\chi^T\to \chi^{\prime T}=\chi^{T}(1+i\frac{\vec{\sigma}^T}{2}\cdot\vec{\theta}+\frac{\vec{\sigma}^T}{2}\cdot\vec{\beta})$ ，

或者去复共轭试试，得到

$\chi^* \to \chi^{\prime *}=(1-i\frac{\vec{\sigma}^*}{2}\cdot\vec{\theta}+\frac{\vec{\sigma}^*}{2}\cdot\vec{\beta})\chi^*$ 。

显然我们需要知道Pauli矩阵"转置"或者"取复共轭"有没有”方便“的形式。确实是有的

$\sigma_i^T=-\sigma^2\sigma_i\sigma^2$ ，

对于这个结果，大家验证一下即可（虽然这么说，请大家不要偷懒，夯实基础很重要！）。

把上面的结果dagger一下，得到

$\sigma_i^*=-\sigma^2\sigma_i\sigma^2=\sigma_i^T$ 。

这样 $\chi$ 的变换为

$\chi^T\to \chi^{\prime T}=\chi^{T}\sigma^2(1-i\frac{\vec{\sigma}}{2}\cdot\vec{\theta}-\frac{\vec{\sigma}}{2}\cdot\vec{\beta})\sigma^2$

$\chi^* \to \chi^{\prime *}=\sigma^2(1+i\frac{\vec{\sigma}}{2}\cdot\vec{\theta}-\frac{\vec{\sigma}}{2}\cdot\vec{\beta})\sigma^2\chi^*$

由此我们可以构造如下Lorentz不变的标量

$\chi^T\sigma^2\chi$ 和 $\chi^\dagger \sigma^2\chi^*$

因此，一个普遍的**满足洛伦兹不变**的拉氏量为

$\mathcal{L}=i\chi^\dagger\bar{\sigma}^\mu\partial_\mu\chi+c_1\chi^T\sigma^2\chi+c_2\chi^\dagger\sigma^2\chi^*$ 。

动能项里面的虚数单位i在上面的知乎回答里面有解释，这里不重复了。

**同时拉氏量应该是实数**，我们有

$\mathcal{L}^\dagger=-i\partial_\mu\chi^\dagger\bar{\sigma}^\mu\chi+c_2^*\chi^T\sigma^2\chi+c_1^*\chi^\dagger\sigma^2\chi^*$ 。

$\mathcal{L}^\dagger-\mathcal{L}$ 相差一个全微分项是允许的，所以有

$c_1=c_2^*$ 。

对 $\chi^\dagger$ 应用Euler-Lagrangian，得到

$i\bar{\sigma}^\mu\partial_\mu \chi+(c_1^*+c_2)\sigma^2\chi^*=i\bar{\sigma}^\mu\partial_\mu \chi+2c_2\sigma^2\chi^*=0$ ， (1)

对 $\chi$ 应用，得到

$-i\partial_\mu\chi^\dagger\bar{\sigma}^\mu+(c_1+c_2^*)\chi^T\sigma^2=0$。

额，一样的。

（1）式得到：

$2c_2\chi^*=-i\sigma^2\bar{\sigma}^\mu\partial_\mu\chi$

$2c_2^*\chi=-i\sigma^2\bar{\sigma}^{*\mu}\partial_\mu\chi^*$

利用

$\bar{\sigma}^{*\mu}=\sigma^2\sigma^\mu\sigma^2$

可得

$2c_2^*\chi=-i\sigma^{\mu}\sigma^2\partial_\mu\chi^*$ (2)

将（2）式代入（1）式得到

$2ic_2^*\bar{\sigma}^\mu\partial_\mu\chi=\sigma^\mu\bar{\sigma}^\nu\sigma^2\partial_\mu\partial_\nu\chi^*=-2|c_2|^2\sigma^2\chi^*$

$(g^{\mu\nu}\partial_\mu\partial_\nu+2|c_2|^2)\sigma^2\chi^*=0$

$2|c_2|^2=m^2$

因此如果我们取 $c_2=\frac{-im}{2}$ ，我们得到

$\mathcal{L}=i\chi^\dagger\bar{\sigma}^\mu\partial_\mu\chi+\frac{im}{2}(\chi^T\sigma^2\chi-\chi^\dagger\sigma^2\chi^*)$

以及Majorana方程

$i\bar{\sigma}^\mu\partial_\mu \chi-im\sigma^2\chi^*=0$ 。

同学们想一想，如何 $c_2=\frac{im}{2}$ 可以吗？

---

  


![]((20241026)量子场论第15讲_Dirac方程和Majorana方程_Expansion/v2-4aada1f1b35dfff8a02ea38928f9b42a_1440w.jpg)  

Ettore Majoran

  
  
