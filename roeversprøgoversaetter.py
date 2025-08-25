dansksproeg = "Hej Hvordan har du det"

roeversprøg =[s+"o"+s for s in dansksproeg  if s not in "aeiouæøåAEIOUÆØÅ"]

print("".join(roeversprøg))


def map_function(x):
    return x+"o"+x if x not in "aeiouæøåAEIOUÆØÅ" else x


print("".join(map(map_function, dansksproeg)))