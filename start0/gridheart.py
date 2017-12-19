'''
def function(shuguo):
    shuguo.insert(-1,'and')
    print ' '.join(shuguo)
fruit = ['apple','banana','pear','grape']
function(fruit)
'''
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for k in range(len(grid[0])):
    for i in range(len(grid)):
        print grid[i][k],
    print ''
