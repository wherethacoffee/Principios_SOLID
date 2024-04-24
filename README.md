# S.O.L.I.D

Es un acrónimo mnemónico para cinco principios de diseño destinados a hacer que los
diseños de software sean más comprensibles, flexibles y mantenibles. Los principios
son un subconjunto de muchos principios

**Lista de principios**

```
S: single responsability principle.
Establece que un módulo de software debe tener una y solo una razón para
cambiar. Esta razón para cambiar es lo que se entiende por
responsabilidad.
O: open/closed principle.
Este principio nos dice que los módulos de software deben ser abiertos
para su extensión, pero cerrados para su modificación. ¿A qué se refiere
con esto?
Abierto para la extensión: esto significa que el comportamiento del
módulo puede extenderse. A medida que cambian los requisitos de la
aplicación, podemos ampliar el módulo con nuevos comportamientos que
satisfagan esos cambios.
Cerrado por modificación: un módulo estará cerrado si dispone de una
descripción (interface) estable y bien definida. Extender el
comportamiento de un módulo no debería afectar al código ya existente en
el módulo, es decir, el código original del módulo no debería verse
afectado y tener que modificarse.
L: Liskov substitution principle.
La sustitución de Liskov nos dice que los objetos de un programa
deberían ser reemplazables por instancias de sus subtipos sin alterar el
correcto funcionamiento del programa. Básicamente, si en alguna parte de
nuestro código estamos usando una clase, y esta clase es extendida,
tenemos que poder utilizar cualquiera de las clases hijas y que el
programa siga siendo válido
I: Interface segregation principle.
El principio de segregación de interfaces establece que muchas
interfaces cliente específicas son mejores que una interfaz de propósito
general. Cuando los clientes son forzados a utilizar interfaces que no
usan por completo, están sujetos a cambios de esa interfaz. Esto al
final resulta en un acoplamiento innecesario entre los clientes. Dicho
de otra manera, cuando un cliente depende de una clase que implementa
una interfaz, cuya funcionalidad este cliente no usa pero que otros
clientes si, este cliente estará siendo afectado por los cambios que
fuercen otros clientes en la clase en cuestión.
D: Dependency inversion.
El principio de inversión de dependencia nos dice que las entidades de
software deben depender de abstracciones, no de implementaciones. A su
vez, los módulos de alto nivel no deberían depender de los de bajo
nivel. Ambos deberían depender de abstracciones.
```
Hasta aquí, esos fueron los 5 principios que componen una serie principios reconocidos
y seguidos a nivel internacional los cuales se conocen como los "S.O.L.I.D
principles", los siguientes son dos extra que a pesar de que no tienen la relevancia
de los anteriores, si que se deberían seguir de la misma manera.


**Dependency Injection Principle**

```
Este principio se refiere a la técnica de suministrar las dependencias
que un objeto necesita desde el exterior en lugar de que el objeto las
cree internamente. El objetivo es reducir el acoplamiento entre
componentes del software y facilitar la prueba unitaria y la
reutilización del código.
```
**Principle of Least Coupling**

```
Este principio se refiere a la idea de minimizar las interdependencias o
acoplamientos entre los diferentes componentes de un sistema de
software. Un acoplamiento mínimo significa que los componentes son
independientes entre sí y pueden cambiar sin afectar demasiado a otros
componentes. Esto promueve la modularidad y la flexibilidad en el diseño
de software.
```
