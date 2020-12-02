# tp_pair
avec Marine
Sujet : implémenter un système de bienvenue
En suivant les méthodologies “TDD”, “CleanCode” et “Pair programming”, vous allez
développer un script de bienvenue en Python. Le principe de ce script est simple : vous allez
lui donner en input une chaîne de caractères, et vous allez obtenir en output un message de
bienvenue.
Pour le pair programming, vous alternerez les rôles à chaque feature. Vous devrez
faire un repository Github public, en communiquant l’url sur Moodle.
Feature 1
Faire une fonction qui prend en paramètre un nom et qui répond “Hello, <nom>”. Par
exemple, si on lui donne “bob”, elle répond “Hello, Bob” (à noter, la majuscule sur le nom).
Feature 2
Gestion du nul en input : si on donne une chaine de caractère vide, nulle ou blanche
(que des espaces), alors répondre “Hello, my friend”. Par exemple, si on donne “ “ =>
“Hello, my friend”.
Feature 3
Gestion des cris. Si on donne une chaîne de caractères en majuscule, alors
répondre en majuscule. Par exemple, si on donne “JERRY”, alors répondre “HELLO, JERRY
!”
Feature 4
Gestion deux noms en input. Si on donne en input 2 noms séparés par des virgules,
alors répondre “Hello, <nom1>, <nom2>”. Par exemple, si on donne en input “Amy,bob”,
alors répondre “Hello, Amy, Bob”
Feature 5
Gestion de plusieurs noms en input. Idem que la feature 4, mais avec un nombre
arbitraire supérieur à 2. Par exemple, si on donne en input “Amy, Bob,Jerry”, alors répondre
“Hello, Amy, Bob, Jerry”
 L2 Informatique - Parcours DIFS
 UE QuaD - Qualité de Développement
Feature 6
Gestion des cris lorsqu’il y a plusieurs noms. Si un nom est écrit en majuscule, alors
séparer le texte en 2 : une partie en minuscule et une partie en majuscule. Par exemple, si
on a “Amy, BOB, Jerry” en input, alors répondre “Hello, Amy, Jerry. AND HELLO, BOB !”.
Feature 7
Gestion des listes avec un “et”. Par exemple, si en input on a “bob, amy, jerry” alors
répondre “Hello, Bob, Amy and Jerry”.
Feature 8
Supprimer les espaces inutiles. Par exemple, si on donne en input “bob , amy”,
alors répondre “Hello, Bob and Amy”
Feature 9
Ignorer les noms commençant par un point d’exclamation. Par exemple, si on donne
“bob, !bob, amy, bob, !jerry”, alors répondre “Hello, Amy”
Feature 10
Indiquer le nombre de fois qu’un nom apparaît dans la chaîne de caractères. Par
exemple, si on donne “bob, amy, bob, !jerry, jerry”, alors répondre “Hello, Bob (x2), and
Amy”.
Feature 11
S’il y a plus de 5 noms différents non ignorés (avec un point d’exclamation devant),
alors répondre “Hello, world !”
Feature 12
S’il y a plus de 5 noms différents non ignorés (avec un point d’exclamation devant),
et tous en majuscule, alors répondre “HELLO, WORLD !”
Feature 13
S’il y a le nom Yoda dans la liste des noms et que Yoda n’est pas ignoré (avec un
point d’exclamation devant), alors inverser la liste des noms et le mot Hello. Par exemple, si
on donne “bob, yoda, amy”, alors répondre “Bob, Yoda, and Amy, Hello”
 L2 Informatique - Parcours DIFS
 UE QuaD - Qualité de Développement
Feature 14
S’il y a plus de 5 noms différents non ignorés, dont 1 étant égal à Yoda, alors
répondre “World, Hello”
Feature 15
S’il y a un nom entre étoiles, alors répondre “our special guest …”. Par exemple, si
on donne en input “bob, *amy*, jerry”, alors répondre “Hello, Bob, our special guest Amy,
and Jerry”.
Feature 16
S’il y a plusieurs noms entre étoiles, alors répondre “our special guests a & b”. Par
exemple, si on donne en input “*bob*, *amy*, jerry”, alors répondre “Hello, our special guests
Bob & Amy, and Jerry”.
Feature 17
Autoriser les virgules dans les noms. Par exemple, si on donne en input “Bob, \”Amy,
Jerry\””, alors répondre Hello, Bob and Amy, Jerry
