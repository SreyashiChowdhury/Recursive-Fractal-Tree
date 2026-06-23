import turtle
t = turtle.Turtle()

def draw_tree(branch_len, angle):
    # Base case: stop when the branch is too short to draw
    if branch_len < 5:
        return

    t.forward(branch_len)       # draw current branch

    t.right(angle)              # turn right — right child
    draw_tree(branch_len * 0.75, angle)

    t.left(angle * 2)           # swing left past center — left child
    draw_tree(branch_len * 0.75, angle)

    t.right(angle)              # return to original heading
    t.backward(branch_len)     # retrace this branch