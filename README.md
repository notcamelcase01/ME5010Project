# ME5010 Project
Math Project

### Logistic Map

$\mathbf{x_{n+1} = rx_n(1-x_n)}$

---

#### Language 
- Python10.+
	Libraries used :
	-  `numpy` : `pip install numpy` (Handling arrays)
	- `matplotlin` : `pip install matplotlib` (Plotting)
	- `numba` : `pip install numba`(Speed optimizer)



#### Code File Description

1) **[`logistic_interactive.py`](https://github.com/notcamelcase01/ME5010Project/blob/master/logistic_interactive.py)**

See how logistic equation progression varies, I have coded two sliders to adjust **r** and **x**.  You can even zoom in the bifurcation map, It's really helpful in tallying what's happening to map with as **r** varies.


<img src="https://raw.githubusercontent.com/notcamelcase01/ME5010Project/master/images/period3ing.png"  width="50%" height="50%" />

---

2) **[`lprandom.py`](https://github.com/notcamelcase01/ME5010Project/blob/master/lprandom.py "lprandom.py")**
Used to generate random number at constant  **r = 4**, here seed is **x**. This file have two functions.

- [`lprandom_real(n,seed = None)`](https://github.com/notcamelcase01/ME5010Project/blob/18b9be4ff058bcdf358a7267cb6970a1daaeb66b/lprandom.py#L54) :
  -  `n` is number of random numbers you want to generate, 
  - `seed`(*optional parameter*) is initial value of **x**, If it's not specified program use epoch time to generate it 
  - It returns **uniformly** distributed array of numbers generated via logistic equation and a seed. `(array,seed)`
  *Sample use case*  : 
 ``` 
 import numpy as np
import lprandom.py as lp
random_number_array,seed = lp.lprandom_real(10000)
```

- [`lprandom_real_un(n,seed = None)`](https://github.com/notcamelcase01/ME5010Project/blob/18b9be4ff058bcdf358a7267cb6970a1daaeb66b/lprandom.py#L62) :
  -  `n` is number of random numbers you want to generate, 
  - `seed`(*optional parameter*) is initial value of **x**, If it's not specified program use epoch time to generate it 
  - It returns array of numbers generated via logistic equation and a seed . `(array,seed)`
  *Sample use case*  : 
 ``` 
 import numpy as np
import lprandom.py as lp
random_number_array,seed = lp.lprandom_real_un(10000)
```

---

3) **[`pseudo_random_gen.py`](https://github.com/notcamelcase01/ME5010Project/blob/master/pseudo_random_gen.py)**
Used to generate random number at constant . This file have one functions. Changes seed after every number generation , `(x,r,N)` all three parameters are seeds.

- [`get_pnr(n)`](https://github.com/notcamelcase01/ME5010Project/blob/18b9be4ff058bcdf358a7267cb6970a1daaeb66b/pseudo_random_gen.py#L26) :
  -  `n` is number of random numbers you want to generate,  
  -  It returns  array of numbers generated via logistic equation 
  *Sample use case*   : 
 ``` 
 import numpy as np
import pseudo_random_gen.py as pn
random_number_array = pn.get_pnr(10000)
```

---

4) **[`spr_traingle.py.py`](https://github.com/notcamelcase01/ME5010Project/blob/master/spr_triangle.py)**
Generate sierpinski traingle.

<img src="https://raw.githubusercontent.com/notcamelcase01/ME5010Project/master/images/ilmtri.png"  width="50%" height="50%" />

---

5) **[`bansli_ferm.py`](https://github.com/notcamelcase01/ME5010Project/blob/master/bansli_ferm.py)**  
Generation of Barnsley Fern.
<img src="https://raw.githubusercontent.com/notcamelcase01/ME5010Project/master/images/goodfern.png"  width="50%" height="50%" />

---

6) **[`cobweb_r_changing.m`](https://github.com/notcamelcase01/ME5010Project/blob/master/cobweb_r_changing.m)**  
Animated cobweb graph for logistic map
<img src="https://raw.githubusercontent.com/notcamelcase01/ME5010Project/master/images/r%3D3.97.png"  width="50%" height="50%" /> 

---
Contributors  :
- TS Rudramani
- Nitesh Singh
- Shyam Sridhar
- Pawan Kumar
- notcamecase01


