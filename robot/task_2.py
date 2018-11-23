import robot
r = robot.rmap()
r.lm('task2')

r.up()

for _ in range(5):
    r.pt()
    r.right()
    r.up()
    r.pt()
    r.down(2)
    r.pt()
    r.up()
    r.right()
    r.pt()
    r.right()
