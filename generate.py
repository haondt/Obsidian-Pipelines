from random import randint
rnd = str(randint(0,100))
rnd2 = str(randint(0,100))
s = """
j1:
  script:
    - echo "todays random number is $RANDINT1"
j2:
  script:
    - echo "todays random number is $RANDINT2"
"""

s = s.replace("$RANDINT1", rnd)
s = s.replace("$RANDINT2", rnd2)

print(s)