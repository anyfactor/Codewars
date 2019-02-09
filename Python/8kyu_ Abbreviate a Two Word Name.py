## Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
## The output should be two capital letters with a dot seperating them.
 
def abbrevName(name):
    sp= name.split(" ")
    return sp[0][0].upper() + "." + sp[1][0].upper()