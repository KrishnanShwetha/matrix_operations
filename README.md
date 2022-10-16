# matrix_operations
This project implements functions of matrix operations that modify an image

> **_NOTE:_**  Read jupyter notebook to view image manipulation using KMeans on CIFER-10 dataset

functions:
- print_matrix: prints the specified matrix in rectangular form.
- get_matrix: gets a new matrix from the user and returns it
- negate_matrix: negates all of the elements in the specified matrix
- mult_row: multiplies row r of the specified matrix by the specified multiplier m. 
- add_row_into: takes the specified 2-D list matrix and adds each element of the row with index source (the source row) to the corresponding element of the row with index dest (the destination row).
- add_mult_row_into: takes the specified 2-D list matrix and adds each element of row source (the source row), multiplied by m, to the corresponding element of row dest (the destination row).
- create_grid: creates and returns a 2-D list of 0s with the specified dimensions.
- transpose: function transpose(matrix) that takes the specified 2-D list  matrix and creates and returns a new 2-D list that is the transpose of matrix.
- create_uniform_image: creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels have the RGB values given by pixel.
- blank_image: creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels are green.
- brightness: takes a pixel (an [R, G, B] list) and returns a value between 0 and 255 that represents the brightness of that pixel.
- grayscale: takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image that is a grayscale version of the original image.
- fold_diag: takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image in which the original image is “folded” along its diagonal.
- mirror_horiz: takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image in which the original image is “mirrored” horizontally.
- extract: takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list that represents the portion of the original image that is specified by the other four parameters.
