import math
from Calculos import Calculations


#------------------------------- Complexity -------------------------------------
F = "Fácil"
M = "Medio"
D = "Díficil"


#---------------------------------- Topics --------------------------------------
EQ = "Equilibrio de partículas"


#-------------------------------  Subtopics -------------------------------------
V2D = "Vectores 2D"
V3D = "Vectores 3D"
VU = "Vector unitario"
E2D = "Equilibrio 2D"


#------------------------- Nombres de las respuestas ----------------------------
AX = "Ángulo con el eje X [°]"
AY = "Ángulo con el eje Y [°]"
FX = "Componente con el eje X ${{(F1_x)}}$[kN]"
FY = "Componente con el eje Y ${{(F1_y)}}$[kN]"
Mag = "Magnitud [kN]"
Dir = "Dirección [°]"
Ci = "Componente en X $(i)$"
Cj = "Componente en Y $(j)$"
Ck = "Componente en Z $(k)$" 
A3X = "Ángulo respecto a X $(\\alpha)$ [°]"
A3Y = "Ángulo respecto a Y $(\\beta)$ [°]"
A3Z = "Ángulo respecto a Z $(\\gamma)$ [°]"
CosX = "Coseno con X $(\\theta_x)$"
CosY = "Coseno con Y $(\\theta_y)$"


#----------------------------------- Ayudas --------------------------------------

#EQ_V2D_F
A1 = "¿En cuál cuadrante se encuentra el vector? ¿Por qué esto es importante?"
A2 = "El ángulo con el eje X se puede medir de dos formas: $\\alpha_x$ con respecto al eje X positivo o $180-\\alpha_x$ con respecto al eje X negativo."
A3 = '''
 El ángulo con respecto al eje Y $(\\alpha_y)$ se calcula en función del ángulo con respecto al eje X $(\\alpha_x)$:
 - Primer cuadrante: $\\alpha_y = 90 - \\alpha_x$
 - Segundo cuadrante: $\\alpha_y = \\alpha_x - 90$
 - Tercer cuadrante: $\\alpha_y = 270 - \\alpha_x$
 - Cuarto cuadrante: $\\alpha_y = \\alpha_x - 270$
 '''
A4 = "La componente de un vector a lo largo del eje X es la proyección del vector sobre el eje."
A5 = "La proyección del vector sobre el eje depende de la magnitud del vector y del ángulo entre el vector y el eje."
A6 = "La componente se calcula como la magnitud multiplicada por el coseno del ángulo con respecto al eje."
A7 = """
Calcule la diferencia de las coordenadas en X y en Y:  

$dx = x_{{final}} - x_{{inicial}}$  
$dy = y_{{final}} - y_{{inicial}}$
"""
A8 = "¿Qué representan dx y dy?"
A9 = "Calcule la pendiente como: $m = \\dfrac{{dy}}{{dx}}$. ¿Qué signica el signo?"
A10 = "Calcule la magnitud de F1 como: $|F1| = \\sqrt{dx^2 + dy^2}$."
A11 = "$i$ representa la componente paralela al eje X y $j$ a la componente paralela a Y"
A12 = "Calcule la magnitud como: $\\sqrt{F_x^2 + F_y^2}"
A13 =  """
El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

-Primer cuadrante:  $tan^{-1}\\left(\\dfrac{componente\\hspace{1mm}j}{componente\\hspace{1mm}i}\\right)$  
-Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{componente\\hspace{1mm}j}{componente\\hspace{1mm}i}\\right)$  
-Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{componente\\hspace{1mm}j}{componente\\hspace{1mm}i}\\right)$  
-Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{componente\\hspace{1mm}j}{componente\\hspace{1mm}i}\\right)$  
"""

#EQ_V2D_M
A14 = "Determine las componentes de la fuerza resultante mediante la descomposición de las fuerzas en los ejes x, y o use la ley del paralelogramo. Tenga en cuenta el sentido de cada una de las fuerzas dentro de la sumatoria de las componentes. "
A15 = "Calcula la magnitud como: $\\sqrt{(F_{RX}^2+F_{RY}^2)}$"
A16 = "Calcula la dirección de la fuerza resultante con la función tangente."
A17 = "Realice la sumatoria de fuerzas en X y Y, considere el sentido de cada una de las fuerzas  y a cuánto equivale cada una de las sumatorias."
A18 = "Realice la sumatoria de fuerzas en Y para despejar F2, ¿a cuánto debe igualar la sumatoria?"
A19 = "Para calcular la magnitud de la fuerza resultante realice la sumatoria de fuerzas en X de F1 y F2."
A20 = "La fuerza vertical requerida, equivale a la sumatoria de las componentes en Y de las fuerzas F1 y F2."
A21 = "Para despejar el ángulo, plantee el sistema de ecuaciones y busque formar una ecuación en términos de la fuerza y el ángulo conocido, en donde quede como expresión la tangente del ángulo desconocido. Es decir, reemplace la ecuación de la sumatoria de fuerzas en Y en la ecuación de la sumatoria de fuerzas en X"

#EQ_V2D_D
A22 = "Use la ley del paralelogramo o la regla del triángulo para descomponer una fuerza en dos ejes que no son ortogonales"
A23 = "Para construir el paralelogramo, comience en la cola del vector resultante, en este caso $F$ y trace líneas paralelas que formen el paralelogramo. Los lados del paralelogramo que están sobre los ejes, representan las componentes, $F_u$ y $F_v$. La mitad del paralelogramo ilustra la regla del triángulo. Recuerde que los ángulos internos deben sumar 180°"
A24 = "Use la ley de senos o la ley de cosenos para despejar las componentes"
A25 = "Use la ley de senos o la ley de cosenos para despejar la magnitud y la componente desconocida"
A26 = "Use la ley de senos o la ley de cosenos para despejar la magnitud"
A27 = "Primero, halle el ángulo $\\alpha_2$. Para ello, aplique la regla del triángulo y encuentre una ecuación para calcular F2 utilizando la ley de senos. Luego, analice el ángulo entre F1 y F2 que genera que la fuerza F2 es mínima."
A28 = "F2 es mínima cuando F1 y F2 son perpendiculares."
A29 = "Con la ley de senos halle las magnitudes de F1 y F2"
A30 = "Calcule la magnitud y la dirección de la fuerza resultante entre F1 y F3."
A31 = "La fuerza resultante de las tres fuerzas corresponde a la suma de la resultante entre F1 y F3, y F2. Plantee la regla del triángulo, calcule los ángulos internos de forma que FR sea mínima. ¿Qué ángulo forma la fuerza resultante con uno de los lados del triángulo para ser mínima?."
A32 = "Use la ley de senos o el Teorema de Pitágoras para hallar las magnitudes de las fuerzas."

#EQ_V3D_F/M
A33 = "Para hallar las componentes X y Y, proyecte el vector F en el plano XY"
A34 = "Una vez el vector se encuentre en el plano XY, proyecte el vector hacia los ejes X y Y"
A35 = "Considere el sentido de la fuerza en el cálculo de las componentes"
A36 = "Los ángulos directores coordenados se pueden calcular como el arcocoseno de las componentes del vector divididas por la magnitud del vector F"
A37 = "Para encontrar las componentes X y Y, primero proyecte el vector F en el plano XY y luego realice la proyección sobre cada uno de los ejes."
A38 = "La componente Z se puede proyectar directamente con la información dada"
A39 = "Determine el vector F como un vector cartesiano, esto le permitirá identificar cada una de sus componentes. Tenga en cuenta que el dibujo no está a escala."
A40 = "La magnitud de un vector con 3 componentes (X, Y, Z) se define como: $\\sqrt{F_X^2 + F_Y^2 + F_Z^2}$"
A41 = "Los ángulos directores relacionan directamente al vector F con cada uno de los ejes."
A42 = "$i$ representa la componente paralela al eje X, $j$ a la componente paralela a Y y $k$ a la componente paralela a Z."
A43 = "Calcule las componentes de cada eje como la multiplicación de la fuerza por el coseno del ángulo que forma con dicho eje."

#EQ_V3D_M
A44 = "Iguale las componentes dadas a la sumatoria de fuerzas en dichos ejes para formar un sistema de ecuaciones para despejar las magnitudes F1 y F2."
A45 = "Utilice las coordenadas de cada fuerza para construir un triángulo rectángulo que le permita aplicar el teorema de Pitágoras."
A46 = "Recuerde que, según el teorema de Pitágoras, el coseno de un ángulo $\\alpha$ se define como $cos(\\alpha)=\\dfrac{Cateto adyacente}{Hipotenusa}$. En este caso, el coseno corresponde a $cos(\\alpha)=\\dfrac{Coordenada en X, Y o Z}{Longitud del vector}$"

#EQ_VU_F
A47 = '''
Revise las unidades del ángulo, radianes o grados:  

Para convertir de radianes a grados: $\\alpha_x*\\dfrac{180}{\\pi}$  

Para convertir de grados a radianes: $\\alpha_x*\\dfrac{\\pi}{180}$
'''
A48 = '''
Calcule los ángulos respecto a su eje positivo:  
$\\alpha_x = \\alpha_x$  
$\\alpha_y = \\alpha_x-90°$
'''
A49 = "En un triángulo con un ángulo recto, de lados a y b, la longitud de la hipotenusa se calcula como: $\\sqrt{a^2+b^2}$"
A50 = "Considere que a y b corresponden a los cosenos direccionales"
A51 = "La norma será: $|u| = \\sqrt{(cos(\\alpha_x))^2 + (cos(\\alpha_y))^2)}$."
A52 = "Calcule la longitud de A a B como: $|AB| = \\sqrt{dx^2 + dy^2}$."
A53 = """
Calcule los cosenos direccionales como: 

$cos_x = \\dfrac{{dx}}{{AB}}$  

$cos_y = \\dfrac{{dy}}{{AB}}$
"""
A54 = """
Calcule las componentes como la multiplicación de la magnitud de la fuerza por los cosenos direccionales como: 

$componente i =  \\overrightarrow{{F1}}*\\dfrac{{dx}}{{AB}}$  

$componente j =  \\overrightarrow{{F1}}*\\dfrac{{dy}}{{AB}}$
"""
A55 = "Los ángulos directores coordenados corresponden a los ángulos que relacionan al vector con los ejes x, y, z. Para encontrar estos ángulos, formule el vector unitario en la dirección del vector y determine los cosenos inversos de sus componentes."
A56 = "El vector unitario en la componente del eje (i o j) es equivalente al coseno direccional en dicho eje."
#A57 = "El vector unitario se define como $\\overrightarrow{{u}}=\\dfrac{{(X_2-X_1) + (Y_2-Y_1)}}{{\\sqrt{{(X_2-X_1)^2 + (Y_2-Y_1)^2}}}}$."
A57 = "El vector unitario se define como $\\lambda_u=\\dfrac{{\\overrightarrow{{u}}}}{{|\\overrightarrow{{u}}|}}$."
A58 = "Compruebe que el vector unitario del eje equivale al coseno direccional en dicho eje. Para ello plantee un triángulo rectángulo cuyos lados sean (X2-X1) y (Y2-Y1)."
A59 = "Realice la sumatoria de fuerzas en X y Y. Determine el vector unitario de F1 y F2."
A60 = "Calcule $\\overrightarrow{{u}}$ como un vector cartesiano. Para ello, calcule la diferencia de coordenadas en X, Y y Z."
A61 = "Calcule $|\\overrightarrow{{u}}|$ como la magnitud del vector. La magnitud de un vector con 3 componentes (X, Y, Z) se define como: $\\sqrt{X^2 + Y^2 + Z^2}$"
A62 = "Calcule las componentes X, Y, Z de la fuerza resultante como la suma de las componentes de cada una de las fuerzas."
A63 = "Halle las componentes de cada una de las fuerzas, para ello, multiplique la magnitud de la fuerza por su vector unitario."
A64 = "Encuentre el vector unitario de los cables AB, AC y AD."
A65 = "Plantee la ecuación de la componente $j$ del vector unitario del cable AD."
A66 = "Calcule la componente Y de la fuerza como la multiplicación de la magnitud de la fuerza por el coseno direccional en $y$, es decir, la componente $j$ del vector unitario."
A67 = "Plantee la ecuación de cada una de las componentes de la fuerza como la multiplicación de la magnitud de la fuerza y el vector unitario de dicha componente."
A68 = "¿Qué representa la longitud de la cuerda?"
A69 = "Despeje de cada una de las ecuaciones las distancias en X, Y y Z, según corresponda."

#EQ_V2D_F
A70 = "Para garantizar la condición de equilibrio de una partícula, la sumatoria de las fuerzas en cada uno de los ejes debe ser igual a cero."
A71 = "Plantee las ecuaciones de equilibrio correspondientes a la sumatoria de fuerzas en X y Y."
A72 = "Para facilitar el despeje de las magnitudes, intente formar una tangente de uno de los ángulos, lo cual reducirá el número de términos en el proceso de despeje."
A73 = "Realice el diagrama de cuerpo libre (DCL) de la polea."
A74 = "Realice un corte en las cuerdas que sostiene la polea."
A75 = "Plantee las ecuaciones de equilibrio y resuelva."
A76 = "Realice el diagrama de cuerpo libre (DCL) de la polea."
A77 = "Incluya dentro de la sumatoria las componentes de la fuerza que se debe aplicar y resuelva."
A78 = "Dibuje el diagrama de cuerpo libre (DCL) de cada una de las poleas, identifique correctamente los cambios de cuerda entre las poleas."


#------------------------------------- Textos para las respuestas ---------------------------------------

#EQ_V2D_D
T1 = f"""
        A continuación se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Aplicación de la Ley del paralelogramo o la Regla del triángulo:}}$

        ${{\hspace{{4mm}}\\alpha_3 = 180 - \\alpha_1 - \\alpha_2}}$
    """

T2 = f"""
        A continuación se presenta la solución sugerida para el ejercicio:   

        $\\textbf{{\\small 1. Cálculo del ángulo $\\alpha_2$:}}$

        Primero, se aplica la regla del triángulo y se plantea mediante la ley de senos la ecuación para hallar F2:
    """

T3 = f"""
        A continuación se presenta la solución sugerida para el ejercicio:

        $\\textbf{{\\small 1. Diagrama de cuerpo libre de la polea:}}$
    """




#----------------------------------- Funciones para las respuestas --------------------------------------

def rta_EQ_V2D_F_P2(f, calc, version):
    return f"""
    La descomposición del vector F1 depende de su magnitud y ángulo. Se sugiere el siguiente método para la solución del ejercicio:

    $\\textbf{{\\small 1. Componente de la fuerza con respecto al eje X:}}$

    ${{\hspace{{4mm}}F1_x = |\\overrightarrow{{F1}}| \\cdot \\cos(\\alpha_x) \\text{{ = }}}}{f[0]:.0f}{{\\text{{ kN}}\\hspace{{1mm}}\\cdot\\hspace{{1mm}}}}{calc[f'cos{version}']:.2f}{{\\text{{ = }}}}{f[0]*calc[f'cos{version}']:.2f}{{ \\text{{ kN}}}}$
    
    $\\textbf{{\\small 2. Componente de la fuerza con respecto al eje Y:}}$

    ${{\hspace{{4mm}}F1_y = |\\overrightarrow{{F1}}| \\cdot \\sin(\\alpha_x) \\text{{ = }}}}{f[0]:.0f}{{\\text{{ kN}}\\hspace{{1mm}}\\cdot\\hspace{{1mm}}}}{calc[f'sin{version}']:.2f}{{\\text{{ = }}}}{f[0]*calc[f'sin{version}']:.2f}{{ \\text{{ kN}}}}$
    """

def rta_EQ_V2D_F_P3(ax, ay, bx, by):
    return f"""
    A continuación se presenta la solución sugerida para el ejercicio:

    $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

    ${{\hspace{{4mm}}dx \\text{{ = }}}} {bx:.0f} {{\\text{{ - (}}}} {ax:.2f} {{\\text{{) = }}}} {bx-ax:.0f}$  
    ${{\hspace{{4mm}}dy \\text{{ = }}}} {by:.0f} {{\\text{{ - (}}}} {ay:.2f} {{\\text{{) = }}}} {by-ay:.0f}$ 

    $\\textbf{{\\small 2. Cálculo de la pendiente:}}$
        
    ${{\hspace{{4mm}} m = \\dfrac{{dy}}{{dx}} = \\dfrac{{{by-ay}}}{{{bx-ax}}} = {(by-ay)/(bx-ax):.2f}}}$
    """

def rta_EQ_V2D_F_P4(ax, ay, bx, by):
    return f"""
    A continuación se presenta la solución sugerida para el ejercicio:

    $\\textbf{{\\small 1. Cálculo de la diferencia de coordenadas en X y Y:}}$

    ${{\hspace{{4mm}}dx \\text{{ = }}}} {bx:.0f} {{\\text{{ - (}}}} {ax:.2f} {{\\text{{) = }}}} {bx-ax:.0f}$  
    ${{\hspace{{4mm}}dy \\text{{ = }}}} {by:.0f} {{\\text{{ - (}}}} {ay:.2f} {{\\text{{) = }}}} {by-ay:.0f}$ 

    $\\textbf{{\\small 2. Cálculo de la magnitud:}}$
        
    ${{\hspace{{4mm}} m = \\sqrt{{dx^2+dy^2}} = {math.sqrt((by-ay)**2+(bx-ax)**2):.2f}}}$

    Este resultado implica que el vector cartesiano de F1 es: $\\overrightarrow{{F1}} = ({bx-ax})i + ({by-ay})$ j.
    """
def rta_EQ_V2D_M_P1(F1x, F1y, F2x, F2y, calc, a1,a2):
    return f"""
    La fuerza resultante corresponde a la suma de los dos vectores. Se sugiere para la solución del ejercicio el siguiente método:

    $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

    ${{\hspace{{4mm}} F1_x = F1*cos(\\alpha_1) = {F1x*calc[f'cos{a1}']:.2f} }}$  
    ${{\hspace{{4mm}} F1_y = F1*sen(\\alpha_1) = {F1y*calc[f'sin{a1}']:.2f} }}$  
    ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2) = {F2x*calc[f'cos{a2}']:.2f} }}$  
    ${{\hspace{{4mm}} F2_y = F2*sen(\\alpha_2) = {F2y*calc[f'sin{a2}']:.2f} }}$  
	    
    $\\textbf{{\\small 2. Sumatoria en X y Y:}}$  

    ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}}= F1_x + F2_x = {F1x*calc[f'cos{a1}']+F2x*calc[f'cos{a2}']:.2f} }}$  
    ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y = {F1y*calc[f'sin{a1}']+F2y*calc[f'sin{a2}']:.2f} }}$  
       
    $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

    ${{\hspace{{4mm}} |F_R|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(F1x*calc[f'cos{a1}']+F2x*calc[f'cos{a2}'],F1y*calc[f'sin{a1}']+F2y*calc[f'sin{a2}']):.2f} }}$

    $\\textbf{{\\small 4. Cálculo de la dirección:}}$

    ${{\hspace{{4mm}} \\alpha_R ={Calculations.define_angle(F1x*calc[f'cos{a1}']+F2x*calc[f'cos{a2}'],F1y*calc[f'sin{a1}']+F2y*calc[f'sin{a2}']):.2f} }}$

    El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

    -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
    -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
    -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$  
    -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{\\text{{componente j}}}}{{\\text{{componente i}}}}\\right)$ 
    """

def rta_EQ_V2D_M_P2(F1x, F1y, F2x, F2y, calc, a1,a2):
    return f"""
    La fuerza resultante corresponde a la suma de los dos vectores. Se sugiere para la solución del ejercicio el siguiente método:

    $\\textbf{{\\small 1. Descomposición de los vectores F1 y F2:}}$

    ${{\hspace{{4mm}} F1_x = F1*sen(\\alpha_1) = {F1x*calc[f'sin{a2}']:.2f} }}$  
    ${{\hspace{{4mm}} F1_y = F1*cos(\\alpha_1) = {F1y*calc[f'cos{a2}']:.2f} }}$  
    ${{\hspace{{4mm}} F2_x = F2*cos(\\alpha_2) = {F2x*calc[f'cos{a1}']:.2f} }}$  
    ${{\hspace{{4mm}} F2_y = F2*sen(\\alpha_2) = {F2y*calc[f'sin{a1}']:.2f} }}$  
	    
    $\\textbf{{\\small 2. Sumatoria en X y Y:}}$  

    ${{\hspace{{4mm}} \\sum{{F_x}} = F_{{RX}} = F1_x + F2_x = {F1x*calc[f'sin{a2}']+F2x*calc[f'cos{a1}']:.2f} }}$  
    ${{\hspace{{4mm}} \\sum{{F_y}} = F_{{RY}} = F1_y + F2_y = {F1y*calc[f'cos{a2}']+F2y*calc[f'sin{a1}']:.2f} }}$  
       
    $\\textbf{{\\small 3. Cálculo de la magnitud:}}$

    ${{\hspace{{4mm}} |F_R|=\\sqrt{{F_{{RX}}^2+F_{{RY}}^2}} = {Calculations.magnitude(F1x*calc[f'sin{a2}']+F2x*calc[f'cos{a1}'],F1y*calc[f'cos{a2}']+F2y*calc[f'sin{a1}']):.2f} }}$

    $\\textbf{{\\small 4. Cálculo de la dirección:}}$

     ${{\hspace{{4mm}} \\alpha_R ={Calculations.define_angle(F1x*calc[f'sin{a2}']+F2x*calc[f'cos{a1}'],F1y*calc[f'cos{a2}']+F2y*calc[f'sin{a1}']):.2f} }}$

    El cálculo del ángulo respecto al eje x positivo depende del cuadrante en el que se encuentra el vector:

    -Primer cuadrante:  $tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$  

    -Segundo cuadrante: $180 - tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$  

    -Tercer cuadrante:  $180 + tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$  

    -Cuarto cuadrante:  $360 - tan^{-1}\\left(\\dfrac{{F_{{RY}}}}{{F_{{RX}}}}\\right)$ 
    """

def rta_EQ_V2D_D_P1(f, a, calc):
    return f"""
    $\\textbf{{\\small 2. Aplicación de la Ley de senos para hallar las componentes:}}$  

    $\\underline{{Componente u}}$  

    ${{\hspace{{4mm}} \\dfrac{{F_u}}{{sen(\\alpha_1)}} = \\dfrac{{F}}{{sen(\\alpha_3)}}}}$
    ${{\hspace{{4mm}} F_u = \\dfrac{{F*sen(\\alpha_1)}}{{sen(\\alpha_3)}}}}$
    ${{\hspace{{4mm}} F_u = {(f[0]*calc['sin1'])/Calculations.sine(180-a[0]-a[4]):.2f}}}$

    $\\underline{{Componente v}}$  

    ${{\hspace{{4mm}} \\dfrac{{F_v}}{{sen(\\alpha_2)}} = \\dfrac{{F}}{{sen(180-\\alpha_1-\\alpha_2)}}}}$
    ${{\hspace{{4mm}} F_v = \\dfrac{{F*sen(\\alpha_2)}}{{sen(180-\\alpha_1-\\alpha_2)}}}}$
    ${{\hspace{{4mm}} F_v = {(f[0]*calc['sin5'])/Calculations.sine(180-a[0]-a[4]):.2f}}}$
    """

def rta_EQ_V2D_D_P2(f, a, calc):
    return f"""
    $\\textbf{{\\small 2. Aplicación de la Ley de senos para hallar la magnitud de F y la componente desconocida:}}$  

    $\\underline{{Magnitud F}}$  

    ${{\hspace{{4mm}} \\dfrac{{F}}{{sen(\\alpha_3)}} = \\dfrac{{F_v}}{{sen(\\alpha_2)}}}}$
    ${{\hspace{{4mm}} F = \\dfrac{{F_v*sen(\\alpha_3)}}{{sen(\\alpha_2)}}}}$
    ${{\hspace{{4mm}} F = {(f[0]*Calculations.sine(180-a[0]-a[4]))/calc['sin5']:.2f}}}$

    $\\underline{{Componente $u$}}$  

    ${{\hspace{{4mm}} \\dfrac{{F_u}}{{sen(\\alpha_1)}} = \\dfrac{{F_v}}{{sen(\\alpha_2)}}}}$
    ${{\hspace{{4mm}} F_u = \\dfrac{{F_v*sen(\\alpha_1)}}{{sen(\\alpha_2)}}}}$
    ${{\hspace{{4mm}} F_u = {(f[0]*calc['sin1'])/calc['sin5']:.2f}}}$
    """

def rta_EQ_V2D_D_P3(f, a, calc):
    return f"""
    $\\textbf{{\\small 2. Aplicación de la Ley de senos para hallar la magnitud de F:}}$  

    ${{\hspace{{4mm}} \\dfrac{{F_u}}{{sen(\\alpha_v)}} = \\dfrac{{F}}{{sen(\\alpha_w)}}}}$
    ${{\hspace{{4mm}} F = \\dfrac{{F_u*sen(\\alpha_w)}}{{sen(\\alpha_v)}}}}$
    ${{\hspace{{4mm}} F = {(f[0]*Calculations.sine(180-a[0]-a[9]))/calc['sin10']:.2f}}}$

    $\\textbf{{\\small 3. Cálculo de las componentes X y Y:}}$

    ${{\hspace{{4mm}} F_x = F*sen(\\alpha_Y) = {((f[0]*Calculations.sine(180-a[0]-a[9]))/calc['sin10'])*calc['sin5']:.2f}}}$
    ${{\hspace{{4mm}} F_y = F*cos(\\alpha_Y) = {((f[0]*Calculations.sine(180-a[0]-a[9]))/calc['sin10'])*calc['cos5']:.2f}}}$
    """

def rta_EQ_V2D_D_P4(f, a, calc):
    return f"""
    ${{\hspace{{4mm}} \\dfrac{{FR}}{{sen(\\alpha_3)}} = \\dfrac{{F2}}{{sen(\\alpha_1)}}}}$
    ${{\hspace{{4mm}} F2 = \\dfrac{{FR*sen(\\alpha_1)}}{{sen(\\alpha_3)}}}}$

    Al analizar la fórmula F2 para despejar F2, se observa que a medida que el denominador disminuye, F2 se convierte en un máximo. Por tanto, es necesario maximizar el denominador, en este caso es 1, esto se logra cuando $\\alpha_3$ es 90°. 
    De lo anterior, se concluye que F2 es mínima cuando F1 y F2 son perpendiculares. Teniendo en cuenta esto $\\alpha_3$ se calcula como:

    ${{\hspace{{4mm}} \\alpha_2 = 180° - \\alpha_3 - \\alpha_1 = {180-a[0]-90:.0f}}}$


    $\\textbf{{\\small 2. Cálculo de las magnitudes F1 y F2:}}$  

    $\\underline{{Magnitud F1}}$  

    ${{\hspace{{4mm}} \\dfrac{{F1}}{{sen(\\alpha_2)}} = \\dfrac{{FR}}{{sen(\\alpha_3)}}}}$
    ${{\hspace{{4mm}} F1 = \\dfrac{{FR*sen(\\alpha_2)}}{{sen(90)}}}}$
    ${{\hspace{{4mm}} F1 = {(f[0]*Calculations.sine(180-a[0]-90)):.2f}}}$

    $\\underline{{Magnitud F2}}$  

    ${{\hspace{{4mm}} \\dfrac{{FR}}{{sen(\\alpha_3)}} = \\dfrac{{F2}}{{sen(\\alpha_1)}}}}$
    ${{\hspace{{4mm}} F2 = \\dfrac{{FR*sen(\\alpha_1)}}{{sen(\\alpha_3)}}}}$
    ${{\hspace{{4mm}} F2 = {(f[0]*Calculations.sine(a[0])):.2f}}}$
    """

def rta_EQ_V2D_D_P5_P1(fx1, fy1, a): #Pregunta Equilibrio de partículas, vectores 2D, nivel de complejidad díficil, pregunta 5, parte 1
    return f"""
    A continuación se presenta la solución sugerida para el ejercicio:
    
    $\\textbf{{\\small 1. Cálculo de la magnitud de la fuerza resultante entre F1 y F3:}}$

    ${{\hspace{{4mm}}  |\\overrightarrow{{FR'}}| = \\sqrt{{(F1_x + F3_x)^2+(F1_y + F3_y)^2}}}}$
    ${{\hspace{{4mm}}  |\\overrightarrow{{FR'}}| = {Calculations.magnitude(fx1,fy1):.2f} }}$

    $\\textbf{{\\small 2. Cálculo de la dirección $\\tetha$ de la fuerza resultante entre F1 y F3:}}$

    ${{\hspace{{4mm}} $\\etha$ = tan^{{-1}} \\left(\\dfrac{{F1_y + F3_y}}{{F1_x + F3_x}}\\right)}}$
    ${{\hspace{{4mm}} $\\tetha$ = {Calculations.define_angle(fx1,fy1):.2f}}}$

    $\\textbf{{\\small 3. Construcción de la regla del triángulo:}}$

    Para el cálculo de lo ángulos internos considere que:
    ${{\hspace{{4mm}} $\\tetha_1$ = 180-$\\tetha_2$-$\\tetha_3$}}={180-90-(a[0]+Calculations.define_angle(fx1,fy1)):.0f}°$
    ${{\hspace{{4mm}} $\\tetha_2$ = 90°}} \\text{{. La fuerza resultante mínima es perpendicular a una de las fuerzas de la sumatoria.}}$
    ${{\hspace{{4mm}} $\\tetha_3$ = \\alpha_1 + \\tetha = {a[0]+Calculations.define_angle(fx1,fy1):.0f}}}°$
    """

def rta_EQ_V2D_D_P5_P2(fx1, fy1, a): #Pregunta Equilibrio de partículas, vectores 2D, nivel de complejidad díficil, pregunta 5, parte 2
    return f"""
    $\\textbf{{\\small 4. Cálculo de la magnitud de la fuerza resultante entre F1 y F3:}}$

    ${{\hspace{{4mm}} \\dfrac{{FR}}{{sen(\\tetha_3)}} = \\dfrac{{FR'}}{{sen(\\tetha_2)}}}}$
    ${{\hspace{{4mm}} FR = \\dfrac{{FR'*sen(\\tetha_3)}}{{sen(\\tetha_2)}}}}$
    ${{\hspace{{4mm}} FR = {Calculations.magnitude(fx1,fy1)*Calculations.sine(a[0]+Calculations.define_angle(fx1,fy1)):.2f}}}$

    $\\textbf{{\\small 5. Cálculo de la magnitud de F2:}}$

    ${{\hspace{{4mm}} \\dfrac{{F2}}{{sen(\\tetha_1)}} = \\dfrac{{FR'}}{{sen(\\tetha_2)}}}}$
    ${{\hspace{{4mm}} F2 = \\dfrac{{FR'*sen(\\tetha_1)}}{{sen(\\tetha_2)}}}}$
    ${{\hspace{{4mm}} F2 = {Calculations.magnitude(fx1,fy1)*Calculations.sine(180-90-(a[0]+Calculations.define_angle(fx1,fy1))):.2f}}}$
    """


