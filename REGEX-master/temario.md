Regex
=====

## Presentación

Las Expresiones Regulares son una herramienta de búsqueda y manipulación de cadenas de caracteres increíblemente potente presente en **todos** los lenguajes de programación. Este curso busca llevar al alumno a entenderlas y darles un uso correcto dentro de sus diferentes aplicaciones.

Algunos puntos de este temario asumen un uso intermedio de la CLI, por lo que se recomienda el curso de "Línea de Comandos".

## Temario

1. Qué es y para qué sirven las expresiones regulares, por ejemplo `/^([a-z\.\+]{4,30})@([a-z\.]+)\.([\w]{2,5})$/`
1. Notas sobre el curso

1. El caracter `.` e introducción a los caracteres especiales y su escapado
    . selcciona todo

1. Las clases predefinidas `\w`, `\d`, `\s` …
    \w - caracteres de palabras
    \d - digitos    
    \s - espacios/invisibles en blanco
   
1. Las clases construidas `[a-zA-Z0-9]`
    [0-9] = \d
    [0-9a-zA-Z] = \w
    
1. Los delimitadores numéricos: `+`, `*`, `?`
    + uno o mas (deben aparecer) 
    * greedy - todo (pueden aparecer)
    ? cero o uno (pueden aparecer)
    Ejemplos 
    \d*[a-z]?s\d+
    \d+[a-z]?s\d+  (buscar un numero determinado)

1. Los contadores `{1,4}`
    En vez de hacer esto \d\d (extrae dos digitos o multiplos de dos)
    \d{2,2}
    \w{3,4}
    \d{2,2}[\-\. ]?     (Buscar por digitos o palabras con contador)
    \d{2,2}\D?         #Otra forma igual (Buscar por digitos o palabras con contador)

1. Not `^`, su uso y sus peligros
    [^a-z0-9]   # \D \W

1. El caso de `?` como delimitador
    \w+[,\n]  
    .+?[,\n] #Otra forma (buscar por comas)

1. Principio (`^`) y final de línea (`$`)
    ^\d$
    ^\d{2,5}$
    ^[^\d].+$

    ^\[LOG.*\[LOG\].*
    ^\[LOG.*\[LOG\].*\[user:@celismx\].*
    ^\[LOG.*\[LOG.*user:@\w+?\].*$

1. Expresiones comunes:
  1. URLS 
    ^https?://.+/.+$
    https?://[\w\.\-]+\.\w{2,5}/?\S*   #bueno Clase
    https?://[www\.]?[a-z]+[\.\w+]+[/?\w+-=]*   #Mas completo 
    [a-zA-Z]*:\/\/[a-z\.@]+\.[a-z]{2,5}[\/]?\S*   #que no sea https
 
  1. mails
    [\w\._]{2,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}    #Completo 
  1. teléfonos
  1. logs
  1. nombres
  1. locaciones
    1. [what three words](https://what3words.com/)
1. Búsqueda y reemplazo
1. Procesadores de texto
1. `grep` y `find` desde consola
1. Regex en
  1. PHP
  1. Javascript
  1. Python
  1. Perl (aunque se burlen)


