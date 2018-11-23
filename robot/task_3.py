import robot
r = robot.rmap()
r.lm('task3')

r.right()

for _ in range(3):
    r.right()
    r.down()
    r.up()
    r.right()

r.right()
