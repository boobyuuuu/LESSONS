# 量子场论第26讲：跑动耦合常数-phi4

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/11384776661]



跑动耦合常数(running coupling constant)是非常有意思的物理现象。相信大家在很多物理科普文章里面已经接触到了。它说的是一个常数(constant，顾名思义，应该是不动的）会随着能标的变化而变化。我们知道自然界的四大相互作用中的电磁作用和弱作用统一了，形成了电弱统一理论。里面有两个耦合常数 $g_1$ 和$g_2$ 。强相互作用有一个耦合常数 $g_S$ 。有意思的是 $g_{1,2}$ 随着能标的增大而增大， $g_S$ 随着能标的增大而减小（就是著名的渐近自由！）。很多人相信在某一个很高的能标（超对称理论预言在 $10^{16}GeV$ 作用），它们会融合成一个能标。那个能标对应的是三个相互作用统一（Grand Unification）的能标。请看下图[#ref\_1](#ref\_1)。

![]((20241210)量子场论第26讲跑动耦合常数-phi4_Expansion/v2-52975864640837d48fec488a646c3a3e_1440w.jpg)  

  


我们现在开始接触 $\phi^4$ 理论的重整化。

$\mathcal L_{int}=-\frac{1}{4!}\lambda\phi^4$

画出费曼图（树图1个，一圈图3个）， $k_1+k_2 \to p_1+p_2$ ，根据费曼规则，读出振幅。

树图贡献： $i\mathcal M_{tree}=-i\lambda$

s道贡献:

$i\mathcal M_s=\frac{1}{2}(-i\lambda)\int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2-m_0^2+i\epsilon}\frac{i}{(k_1+k_2-q)^2-m_0^2+i\epsilon}(-i\lambda)$

t道贡献：

$i\mathcal{M}_t=\frac{1}{2}(-i\lambda)\int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2-m_0^2+i\epsilon}\frac{i}{(k_1-p_1-q)^2-m_0^2+i\epsilon}(-i\lambda)$

u道贡献：

$i\mathcal{M}_u=\frac{1}{2}(-i\lambda)\int\frac{d^4q}{(2\pi)^4}\frac{i}{q^2-m_0^2+i\epsilon}\frac{i}{(k_1-p_2-q)^2-m_0^2+i\epsilon}(-i\lambda)$

我们发现s,t,u道的振幅是非常相似的，我们只计算s道的积分。这里我们需要用到一个trick。

$\frac{1}{A_1A_2\cdots A_n}=\int_0^1 dx_1dx_2\cdots dx_n\delta(x_1+x_2+\cdots+x_n-1)\frac{(n-1)!}{(x_1A_1+x_2A_2+\cdots+x_nA_n)^n}$

证明过程在最底下。

$i\mathcal M_s=(-i\lambda)^2\int dx dy\delta(x+y-1)\int\frac{d^4q}{(2\pi)^4}\frac{i^2}{[x(q^2-m_0^2+i\epsilon)+y((k_1+k_2-q)^2-m_0^2+i\epsilon)]^2}$

我们重点看分母部分

$\begin{eqnarray} &&x(q^2-m_0^2+i\epsilon)+y((k_1+k_2-q)^2-m_0^2+i\epsilon)\\ =&&q^2-2yq(k_1+k_2)+y(k_1+k_2)^2-m_0^2+i\epsilon\\ =&&(q-y(k_1+k_2))^2+y(1-y)(k_1+k_2)^2-m_0^2+i\epsilon \end{eqnarray}$

我们定义

$\Delta\equiv y(y-1)(k_1+k_2)^2+m_0^2$ ，

然后进行变量代换 $q-y(k_1+k_2)\to l$ ，这样得到

$\begin{eqnarray} i\mathcal M_s=&&\frac{1}{2}(-i\lambda)^2\int_0^1 dx dy\delta(x+y-1)\int\frac{d^4l}{(2\pi)^4}\frac{i^2}{(l^2-\Delta+i\epsilon)^2}\\  =&&\frac{1}{2}(-i\lambda)^2\int_0^1 dx dy\delta(x+y-1)\int\frac{d^4l_E}{(2\pi)^4}\frac{i^3}{(l_E^2+\Delta)^2}\\ =&&\frac{i\lambda^2}{2}\mu^{4-d}\int_0^1 dx dy\delta(x+y-1)\int\frac{d^dl_E}{(2\pi)^4}\frac{1}{(l_E^2+\Delta)^2}\\ =&&\frac{i\lambda^2}{2}\mu^{4-d}\int_0^1 dx dy\delta(x+y-1)\frac{1}{(4\pi)^{d/2}}\frac{1}{\Delta^{2-d/2}}\frac{\Gamma(2-d/2)}{\Gamma(2)} \end{eqnarray} $

上面为了保存量纲不变，我们引入一个能标参数 $\mu$ 。

整理一下得到：

$i\mathcal M_s=\frac{i\lambda^2(4\pi)^2}{2}\Gamma(2-\frac{d}{2})\int_0^1dy(\frac{4\pi\mu^2}{y(y-1)(k_1+k_2)^2+m_0^2})^{2-d/2}$

定义 $\epsilon\equiv 4-d$ ，在 $\epsilon \to 0$ 时得到

$i\mathcal M_s=\frac{i\lambda^2}{2(4\pi)^2}(\frac{2}{\epsilon}-\gamma_E+\mathcal O(\epsilon^2))\int_0^1dy(1+\epsilon\frac{1}{2}\ln|\frac{4\pi\mu^2}{y(y-1)(k_1+k_2)^2+m_0^2}|+\mathcal O(\epsilon^2))$

整理得到

$i\mathcal M_s=\frac{i\lambda^2}{32\pi^2}\int_0^1dy(\frac{2}{\epsilon}-\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)(k_1+k_2)^2+m_0^2}|+\mathcal O(\epsilon))$

我们定义 $s=(k_1+k_2)^2$ ， $t=(k_1-p_1)^2$ ， $u=(k_1-p_2)^2$ ，易知

$i\mathcal M_s=\frac{i\lambda^2}{32\pi^2}\int_0^1dy(\frac{2}{\epsilon}-\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)s+m_0^2}|+\mathcal O(\epsilon))$

$i\mathcal M_t=\frac{i\lambda^2}{32\pi^2}\int_0^1dy(\frac{2}{\epsilon}-\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)t+m_0^2}|+\mathcal O(\epsilon))$

$i\mathcal M_u=\frac{i\lambda^2}{32\pi^2}\int_0^1dy(\frac{2}{\epsilon}-\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)u+m_0^2}|+\mathcal O(\epsilon))$

注意到上面的 $\lambda$ 是naked parameter，我们把它写成 $\lambda_0$ ，最终得到

$\lambda(s,t,u)=\lambda_0[1-\frac{\lambda_0}{32\pi^2}\int_0^1dy(\frac{6}{\epsilon}-3\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)s+m_0^2}|+\ln|\frac{4\pi\mu^2}{y(y-1)t+m_0^2}|+\ln|\frac{4\pi\mu^2}{y(y-1)u+m_0^2}|)]$

这个结果给出了“物理的”耦合常数 $\lambda(s,t,u)$ 和“裸露的”耦合常数 $\lambda_0$ 之间的关系。如果我们在 $k_1=k_2=(m,0,0,0)$ 时测量得到耦合常数，记作 $\lambda_{ref}$ 。那么有 $s=4m^2,t=u=0$ ，以及

$\lambda_{ref}=\lambda_0[1-\frac{\lambda_0}{32\pi^2}\int_0^1dy(\frac{6}{\epsilon}-3\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)4m^2+m_0^2}|+\ln|\frac{4\pi\mu^2}{m_0^2}|+\ln|\frac{4\pi\mu^2}{m_0^2}|)]$

反解得到

$\lambda_0\approx\frac{\lambda_{ref}}{1-\frac{\lambda_{ref}}{32\pi^2}\int_0^1dy(\frac{6}{\epsilon}-3\gamma_E+\ln|\frac{4\pi\mu^2}{y(y-1)4m^2+m_0^2}|+\ln|\frac{4\pi\mu^2}{m_0^2}|+\ln|\frac{4\pi\mu^2}{m_0^2}|)}$

那么在 $k_1,k_2$ 取其他值的实验条件下，耦合常数的测量值为

$\lambda(s,t,u)\approx\frac{\lambda_{ref}}{1+C(s,t,u)\lambda_{ref}}$ ，

$C(s,t,u)=\frac{1}{32\pi^2}\int_0^1dy(\ln\frac{y(y-1)4m^2+m^2}{y(y-1)s+m^2}+\ln\frac{m^2}{y(y-1)t+m^2}+\ln\frac{m^2}{y(y-1)u+m^2})$ 。

这样我们计算得到的耦合常数是有限的，并且会发现 $\lambda(s,t,u)$ 确实随着能标在“跑动”！注意到 $s\geq 4m^2$ , $y(y-1)t\ge 0$ 和 $y(y-1)u\ge 0$ ，**我们发现** $C(s,t,u)\leq 0,$**$\lambda(s,t,u)$ 是随着能标的增大而增大的**。很快你会发现QED也有这样的问题(Landau Pole)。请见下图[#ref\_2](#ref\_2)。

![]((20241210)量子场论第26讲跑动耦合常数-phi4_Expansion/v2-d339c1753d76bb57edb32e8bbdb0635e_1440w.jpg)  

  


---

$\begin{eqnarray} \frac{1}{A_1A_2}=&&\int_0^1 dx_1dx_2\delta(x_1+x_2-1)\frac{1}{(x_1A_1+x_2A_2)^2}\\ =&&\int_0^1 dx_1 \frac{1}{(x_1A_1+(1-x_1)A_2)^2}\\ =&&\frac{-1}{(A_1-A_2)}\frac{1}{x_1A_1+(1-x_1)A_2}|_0^1\\ =&&\frac{1}{A_1A_2} \end{eqnarray}$

上式对 $A_2$ 求导得到

$\frac{1}{A_1A_2^2}=\int_0^1 dx_1dx_2\delta(x_1+x_2-1)\frac{2x_2}{(x_1A_1+x_2A_2)^3}$

继续求导得到

$\frac{1}{A_1A_2^3}=\int_0^1 dx_1dx_2\delta(x_1+x_2-1)\frac{3\cdot x_2^2}{(x_1A_1+x_2A_2)^4}$

因此有

$\frac{1}{A_1A_2^n}=\int_0^1 dx_1dx_2\delta(x_1+x_2-1)\frac{n\cdot x_2^{n-1}}{(x_1A_1+x_2A_2)^{n+1}}$

依归纳法，假设对n成立

$\frac{1}{A_1A_2\cdots A_n}=\int_0^1 dx_1dx_2\cdots dx_n\delta(x_1+x_2+\cdots+x_n-1)\frac{(n-1)!}{(x_1A_1+x_2A_2+\cdots+x_nA_n)^n}$ ，

我们考察n+1的情况，利用

$\frac{1}{A_{n+1}(x_1A_1+x_2A_2+\cdots+x_nA_n)^n}=\int_0^1dy_1dy_2\delta(y_1+y_2-1)\frac{ny_2^{n-1}}{[y_1A_{n+1}+y_2(x_1A_1+x_2A_2+\cdots+x_nA_n)]^{n+1}}$ ，

得到

$\begin{eqnarray} &&\frac{1}{A_1A_2\cdots A_nA_{n+1}}\\ =&&\int_0^1 dx_1dx_2\cdots dx_n\delta(x_1+x_2+\cdots+x_n-1)\frac{(n-1)!}{A_{n+1}(x_1A_1+x_2A_2+\cdots+x_nA_n)^n}\\ =&&\int_0^1 dx_1dx_2\cdots dx_n\delta(x_1+x_2+\cdots+x_n-1)\int_0^1dy_1dy_2\delta(y_1+y_2-1)\frac{n!y_2^{n-1}}{[y_1A_{n+1}+y_2(x_1A_1+x_2A_2+\cdots+x_nA_n)]^{n+1}} \end{eqnarray}$

变量代换 $y_2x_1 \to x_1, y_2x_2\to x_2,\cdots,y_2x_n \to x_n$ 得到

$\int_0^1 dx_1dx_2\cdots dx_n\delta(\frac{x_1}{y_2}+\frac{x_2}{y_2}+\cdots+\frac{x_n}{y_2}-1)\int_0^1dy_1dy_2\delta(y_1+y_2-1)\frac{1}{y_2}\frac{n!}{[y_1A_{n+1}+x_1A_1+x_2A_2+\cdots+x_nA_n]^{n+1}}$

把 $y_2$ 积掉得到

$\int_0^1 dx_1dx_2\cdots dx_n\delta(\frac{x_1}{1-y_1}+\frac{x_2}{1-y_1}+\cdots+\frac{x_n}{1-y_1}-1)\int_0^1dy_1\frac{1}{1-y_1}\frac{n!}{[y_1A_{n+1}+x_1A_1+x_2A_2+\cdots+x_nA_n]^{n+1}}$

利用delta函数的那个性质证毕！

![]((20241210)量子场论第26讲跑动耦合常数-phi4_Expansion/v2-e8f8d6b756e89cb1a84c08a9fb1a978a_1440w.jpg)  

请看Feynman的黑板，上面有好多积分。

## 参考  

1. [#ref\_1\_0](#ref\_1\_0)来自于这个问题 [https://physics.stackexchange.com/questions/379747/whats-the-running-coupling-of-gravity](https://physics.stackexchange.com/questions/379747/whats-the-running-coupling-of-gravity)
2. [#ref\_2\_0](#ref\_2\_0)来自于这里 [https://x.com/martinmbauer/status/1683186392950603776](https://x.com/martinmbauer/status/1683186392950603776)
