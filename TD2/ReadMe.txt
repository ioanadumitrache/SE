J'ai modifié le fichier "bonjour.process" en ajoutant les fils d'éxecution
pour les mesdemoiselles et afin de faire l'affichage correcte, ça veut dire
en ordre: Mesdemoiselles, Madames, Monsieurs. Pour ça, j'ai utilisé des files
d'attente (queues). J'ai utilisé "print" au lieu de logging.info(x) pour que
l'affichage soit fait directemment dans la console et sans utiliser le log.
