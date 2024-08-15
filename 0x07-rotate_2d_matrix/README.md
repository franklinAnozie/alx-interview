## ROTATE A MATRIX ###
The algorithm rotates an N X N matrix in a clockwise direction.
## Here's how ##
 - First, we get the size of the matrix:

        n = len(matrix)

 - We iterate through the layers of the matrix:
        
        for layer in range(n // 2):

    - We only need to go through half the layers because each iteration handles both an outer and inner ring simultaneously.

 - For each layer, we define the boundaries:
        
        first = layer
        last = n - 1 - layer
     - 'first' is the starting index of the current layer, and 'last' is the ending index.


 - We then iterate through each element in the top row of the current layer:
        
        for i in range(first, last):

 - We calculate the offset from the start of the layer:
        
        offset = i - first

 - Now, for each element, we perform a 4-way swap:
    a. Save the top element:  
            top = matrix[first][i]
    b. Move left to top:
            matrix[first][i] = matrix[last - offset][first]
        This takes the element from the left side and puts it on top.
    c. Move bottom to left:
            matrix[last - offset][first] = matrix[last][last - offset]
        This takes the element from the bottom and puts it on the left.
    d. Move right to bottom:
            matrix[last][last - offset] = matrix[i][last]
        This takes the element from the right side and puts it on the bottom.
    e. Move saved top to right:
            matrix[i][last] = top
        This puts the original top element on the right side.

This rotates each set of four elements in their correct positions. By doing this for each element in each layer, we rotate the entire matrix.
