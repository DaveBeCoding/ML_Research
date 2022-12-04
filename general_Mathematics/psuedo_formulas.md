<!-- $_{n+1}$ -->

<!-- ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}) -->

<!-- $$\sum_{i=1}^n X_i$$ -->

<!-- $k_{n+1}$ -->

<p>Recursive Formula</p>

$a_{n}=2*a_{n-1}$

<p>Sequence, each term is dependent on the previous terms.</p>

<hr/>

<p>Explicit Formula</p>

$a_{n}=2^{n-1}$

<hr/>

<!-- <p>Sequence where each term is found by using number of terms</p> -->

<p>Explicit vs Recursive</p>

<!-- ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}) -->

<!-- $$\sum_{i=1}^n X_i$$ -->

$a_{n}=1+2^n$

<!-- $k_{n+1}$ -->

$a_{n} = 2 * a_{n-1}$

$a_{n}=13{n}-{n}^2$


$a_{n}=4*a_{n-1}+5$


$a_{n} =2 * a_{n-1} + 3 * a_{n-2}$

<hr/>
<p>Regression Model formula</p>

$\hat{Y} = b_{0}+b_{1}X_{1}$

<hr/>

<p>GMRES PSUEDO CODE</p>

<p markdown="1">1) Start and Choose,  </p> 


$X_{0}$  <p> and compute</p> $r_{0} = f - Ax_{0}$ 

and 

$v_{1} =  r_{0}/||r_{0}||$

<p>2) iterater: for </p> 

$j = 1,2,3...m$

do: [note: m should be the number of restart interations]

$h_{i,j} = (Av_{j}, v_{i}), i = 1, 2, ..., j,$

$\hat{v}_{j+1}$ = $Av_{j} - \sum_{i=1}^jh_{i}, j{vi},$
