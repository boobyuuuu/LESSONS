# 量子场论第30讲：电子反常磁矩II

 **Author:** [Expansion]

 **Link:** [https://zhuanlan.zhihu.com/p/12737959782]



上一讲我们已经得到QED顶点可以写成

$(-ie)\bar u(p',s')(F_1(q^2)\gamma^\mu+F_2(q^2)\frac{i\sigma^{\mu\nu}q_\nu}{2m})u(p,s)$ ，

而且电子反常磁矩g是

$g=2+2F_2(0)$ 。

下面来具体计算，因为 $F_1(0)=1$ ， $F_2(0)=0$ ，那么 $F_2(0)$ 的贡献来自于下面的1圈图。

![]((20241220)量子场论第30讲电子反常磁矩II_Expansion/v2-0f7fee76348be53263bd73fdb1d825d1_1440w.jpg)  

QED顶点

  
  

读出费曼规则

$\begin{eqnarray} &&\bar u(p',s')(-ie\delta\Gamma_\mu(p',p))u(p,s) \\ =&&\int\frac{d^4k}{(2\pi)^4}\bar u(p',s')(-ie\gamma^\rho)\frac{i(\not k+\not q+m)}{(k+q)^2-m^2}(-ie\gamma^\mu)\frac{-ig_{\rho\sigma}}{(p-k)^2-a^2}\frac{i(\not k +m)}{k^2-m^2}(-ie\gamma^\sigma)u(p,s) \end{eqnarray}$

上面传播子里面的 $+i\epsilon$ 省略掉了，并且引入一个光子质量 $a$ （因为有红外发散）。整理一下分母

$\begin{eqnarray} &&\bar u(p',s')\delta\Gamma_\mu(p',p)u(p,s) \\ =&&-ie^2\int\frac{d^4k}{(2\pi)^4}\frac{\bar u(p',s')\gamma^\nu(\not k+\not q+m)\gamma^\mu(\not k+m)\gamma_\nu u(p,s)}{((k+q)^2-m^2)((p-k)^2-a^2)(k^2-m^2))}\\ =&&-ie^2\int\frac{d^4k}{(2\pi)^4}\frac{\bar u(p',s')\gamma^\nu(\not k\gamma^\mu\not k+\not q\gamma^\mu\not k+m\gamma^\mu\not k+\not k\gamma^\mu m+\not q\gamma^\mu m + m^2\gamma^\mu)\gamma_\nu u(p,s)}{((k+q)^2-m^2)((p-k)^2-a^2)(k^2-m^2))}\\ =&&-ie^2\int\frac{d^4k}{(2\pi)^4}\frac{\bar u(p',s')\gamma^\nu(\not k\gamma^\mu\not k+\not q\gamma^\mu\not k+2mk^\mu+\not q\gamma^\mu m + m^2\gamma^\mu)\gamma_\nu u(p,s)}{((k+q)^2-m^2)((p-k)^2-a^2)(k^2-m^2))}\\ \end{eqnarray}$

分子里面那一堆gamma矩阵可以化简（一般参考书附录都有）

$Num.=(2-d)\not k\gamma^\mu\not k-2\not k\gamma^\mu \not q+(4-d)\not q\gamma^\mu\not k+2mdk^\mu+4mq^\mu-m(4-d)\not q\gamma^\mu+(2-d)m^2\gamma^\mu$

这里是推广到d维的结果。

$\begin{eqnarray} &&x((k+q)^2-m^2)+y((p-k)^2-a^2)+z(k^2-m^2)\\ =&&x(k^2+q^2+2kq-m^2)+y(p^2+k^2-2pk-a^2)+z(k^2-m^2)\\ =&&k^2+2k(xq-yp)+xq^2+ym^2-(xm^2+ya^2+zm^2)\\ =&&(k+xq-yp)^2-(xq-yp)^2+xq^2+ym^2-(xm^2+ya^2+zm^2)\\ =&&(k+xq-yp)^2-\Delta \end{eqnarray}$

定义 $l=k+xq-yp$ ， $\Delta=(xq-yp)^2-xq^2-ym^2+(xm^2+ya^2+zm^2)$

因为

$m^2=p'^2=(p+q)^2=p^2+2p\cdot q+q^2=m^2+2p\cdot q+q^2$

所以有 $-2p\cdot q = q^2$ 。

$\begin{eqnarray} \Delta=&&x^2q^2-2xyp\cdot q+y^2m^2-xq^2-ym^2+(xm^2+ya^2+zm^2)\\ =&&-xzq^2+(1-y)^2m^2+ya^2 \end{eqnarray}$

我们将 $k=l-xq+yp$ 代入分子。利用 $\bar u(p')\not p'=m\bar u(p')$ ， $\not p u(p)=mu(p)$， $\bar u(p')\not q u(p)=\bar u(p')(\not p'-\not p)u(p)=0$ ， $P\cdot q=0$ ，奇数次 $l^\mu$ 积分为0以及积分意义下 $\not l l^\mu =\frac{1}{d}l^2\gamma^\mu$ 。我们把分子展开为 $P^\mu=p'^\mu+p^\mu$ ， $q^\mu$ 和 $\gamma^\mu$ 的函数。**我算了10页草稿纸才觉得自己算对**（包括检验在内，如果一次通过的话，3页草稿可以搞定。同学们自己计算的时候最好准备一堆干净的草稿纸，特别认真仔细的推导，不然很容易出错！）。最终得到

$\not k\gamma^\mu\not k=-(\frac{d-2}{d}l^2+x(1-z)q^2+y^2m^2)\gamma^\mu+y^2mP^\mu-(2x+y)ymq^\mu$

$\not k\gamma^\mu \not q = ((1-z)q^2-2ym^2)\gamma^\mu+ym(P^\mu+q^\mu)$

$2dmk^\mu+4mq^\mu+(2-d)m^2\gamma^\mu=(4-d(2x+y))mq^\mu+ydmP^\mu+(2-d)m^2\gamma^\mu$

$\not q\gamma^\mu\not k =(xq^2+2ym^2)\gamma^\mu-ymP^\mu+ymq^\mu$

$\not q\gamma^\mu=2m\gamma^\mu-P^\mu+q^\mu$

将分子 $Num.$ 写成 $A\gamma^\mu+BP^\mu+Cq^\mu$ ，得到

$A=\frac{(2-d)^2}{d}l^2+2(x-1)(1-z)q^2+2(-1+2y+y^2)m^2+[xzq^2+(1+2y-y^2)m^2]\epsilon$

$B=[2y(1-y)+(1+y)^2\epsilon]m$

$C=[2(y-2)(x-z)+(1-y)(x-z)\epsilon]m$

其中 $\epsilon=4-d$ 。（注意这里 $\frac{(2-d)^2}{d}$ 是非常重要的，before 2024-12-20，我最后计算得到 $\delta F_1(0)+\delta Z_2(0)\neq 0$ 就是这个地方没弄对。）

这样我们得到

$\begin{eqnarray} &&\bar u(p',s')[\gamma^\mu(F_1(q^2)-1)+\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)]u(p,s)\\ =&&-2ie^2\int dxdydz\delta(x+y+z-1)\int\frac{d^4l}{(2\pi)^4}\frac{\bar u(p',s')(A\gamma^\mu+BP^\mu+Cq^\mu)u(p,s)}{(l^2-\Delta)^3} \end{eqnarray}$

其中C的积分因为 $C\propto (x-z)$ 交换反对称，因此积分为0。利用Gordon Identity，

$\bar u(p')\gamma^\mu u(p)=\bar u(p')[\frac{p'^\mu+p^\mu}{2m}+\frac{i\sigma^{\mu\nu}q_\nu}{2m}]u(p)$ 。

我们可以得到

$\begin{eqnarray} &&F_1(q^2)-1\\ =&&-2ie^2\int dxdydz\delta(x+y+z-1)\int\frac{d^4l}{(2\pi)^4}\frac{A+2mB}{(l^2-\Delta)^3} \end{eqnarray}$

和

$\begin{eqnarray} &&F_2(q^2)\\ =&&-2ie^2\int dxdydz\delta(x+y+z-1)\int\frac{d^4l}{(2\pi)^4}\frac{-2mB}{(l^2-\Delta)^3} \end{eqnarray}$ 。

要完成A和B的积分，我们需要用到下面的积分。

![]((20241220)量子场论第30讲电子反常磁矩II_Expansion/v2-25d705aec1a8bf6de7e27be40e5fd6f0_1440w.jpg)  

$\int \frac{d^4l}{(2\pi)^4}\frac{l^2}{(l^2-\Delta)^3}=\mu^\epsilon\int \frac{d^dl_E}{(2\pi)^d}\frac{il_E^2}{(l_E^2+\Delta)^3}=\mu^\epsilon\frac{i}{(4\pi)^{2}}\frac{d}{2}\frac{\Gamma(2-d/2)}{2}(\frac{4\pi}{\Delta})^{2-d/2}$

$\int \frac{d^4l}{(2\pi)^4}\frac{1}{(l^2-\Delta)^3}=\mu^\epsilon\int \frac{d^dl_E}{(2\pi)^d}\frac{-i}{(l_E^2+\Delta)^3}=\mu^\epsilon\frac{-i}{(4\pi)^{2}}(2-\frac{d}{2})\frac{\Gamma(2-d/2)}{2}(\frac{4\pi}{\Delta})^{2-d/2}\frac{1}{\Delta}$

$\begin{eqnarray} I_A\equiv&&\int\frac{d^4l}{(2\pi)^4}\frac{\frac{(2-d)^2}{d}l^2+2(x-1)(1-z)q^2+2(-1+2y+y^2)m^2+[xzq^2+(1+2y-y^2)m^2]\epsilon}{(l^2-\Delta)^3}\\ =&&\frac{i}{(4\pi)^2}[\frac{2}{\epsilon}-2+\gamma_E+\ln\frac{4\pi\mu^2}{\Delta}-\frac{(x-1)(1-z)q^2+(-1+2y+y^2)m^2}{\Delta}] \end{eqnarray}$

$\begin{eqnarray} I_B\equiv &&\int\frac{d^4l}{(2\pi)^4}\frac{[2y(1-y)+(1+y)^2\epsilon]m}{(l^2-\Delta)^3}\\ =&&\frac{-i}{(4\pi)^2}\frac{y(1-y)m}{\Delta} \end{eqnarray}$

$\begin{eqnarray} F_2(q^2)=&&-2ie^2\int_0^1dxdydz\delta(x+y+z-1)(-2m)I_B\\ =&&\frac{e^2}{4\pi^2}\int_0^1dxdydz\delta(x+y+z-1)\frac{y(1-y)m^2}{-xzq^2+(1-y)^2m^2+ya^2} \end{eqnarray}$

Fortunately, there is no UV or IR divergence for F\_2。利用

$\int_0^1dxdydz\delta(x+y+z-1)=\int_0^1dydz\theta(x+y+z-1)|_{x=0}^{x=1}=\int_0^1dydz(\theta(y+z)-\theta(y+z-1))=\int_{0<y+z<1}dydz$

容易计算得到

$a_e=\frac{g-2}{2}=F_2(0)=\frac{\alpha}{2\pi}\approx0.0011614$ ，

这就是历史上著名的电子反常磁矩，最先有Schwinger于1948年计算出来的。

$\begin{eqnarray} &&F_1(q^2)-1\\ =&&-2ie^2\int_0^1dxdydz\delta(x+y+z-1)(I_A+2mI_B)\\ =&&\frac{e^2}{8\pi^2}\int_0^1dxdydz\delta(x+y+z-1)[\frac{2}{\epsilon}-2+\gamma_E+\ln\frac{4\pi\mu^2}{-xzq^2+(1-y)^2m^2+ya^2}\\ &&-\frac{(x-1)(1-z)q^2+(-1+4y-y^2)m^2}{-xzq^2+(1-y)^2m^2+ya^2}] \end{eqnarray}$

这里存在UV发散，我们计算一下 $F_1(0)$ 。

$\begin{eqnarray} &&F_1(0)-1\\ =&&\frac{e^2}{8\pi^2}\int_0^1dxdydz\delta(x+y+z-1)[\frac{2}{\epsilon}-2+\gamma_E+\ln\frac{4\pi\mu^2}{(1-y)^2m^2+ya^2}\\ &&-\frac{(-1+4y-y^2)m^2}{(1-y)^2m^2+ya^2}]\\ =&&\frac{e^2}{8\pi^2}\int_0^1dy[(1-y)(\frac{2}{\epsilon}-2+\gamma_E+\ln\frac{4\pi\mu^2}{(1-y)^2m^2+ya^2})-\frac{(1-y)(-1+4y-y^2)m^2}{(1-y)^2m^2+ya^2}]\\ =&&\frac{e^2}{8\pi^2}[\frac{1}{2}(\frac{2}{\epsilon}-2+\gamma_E)+\int_0^1dy((1-y)\ln\frac{4\pi\mu^2}{(1-y)^2m^2+ya^2}-\frac{(1-y)(-1+4y-y^2)m^2}{(1-y)^2m^2+ya^2})]\\ \end{eqnarray}$

如何我们和振幅重整化一下看的话，会得到

$\begin{eqnarray} &&Z_2-1\\ =&&\frac{e^2}{(4\pi)^{2}}\int dx(-2x(\frac{2}{\epsilon}+\gamma_E+\ln\frac{4\pi\mu^2}{xa^2+(1-x)^2m^2}-1)+\frac{4x(1-x)(2-x)m^2}{xa^2+(1-x)^2m^2})\\ =&&\frac{e^2}{8\pi^{2}}[-\frac{1}{2}(\frac{2}{\epsilon}-1+\gamma_E)+\int dx(-x\ln\frac{4\pi\mu^2}{xa^2+(1-x)^2m^2}+\frac{2x(1-x)(2-x)m^2}{xa^2+(1-x)^2m^2})] \end{eqnarray}$

**我们发现两个无穷大抵消掉了**，并且 $Z_2\bar u(p',s')\Gamma^\mu(p',p)u(p,s)$ 整体的修正为

$\delta Z_2(0)+\delta\Gamma_1(0)=0$ 。

实际上这是Ward Identity的要求。上面的无穷大抵消说明了，我们应该考虑所有的可能性，即所有的费曼图。（**注意**：我发现我一直用错了 $\Gamma(x)\approx\frac{1}{x}\color{blue}{-\gamma_E}$ ，**所以讲义里面所有的 $\gamma_E$ 要加一个负号！**）

![]((20241220)量子场论第30讲电子反常磁矩II_Expansion/v2-db5cbfabe46a07c9d4d9991e1fd256bd_1440w.jpg)  

虚光子修正

  
  

---

  


![]((20241220)量子场论第30讲电子反常磁矩II_Expansion/v2-5dcf1d650133388dcb9f5f936e8459b6_1440w.jpg)  
