func rotate(matrix [][]int)  {
    n := len(matrix)-1;
    for i := 0; i<=n; i++{
        for j := 0; j<=n/2; j++{
            placeholder := matrix[i][j];
            matrix[i][j] = matrix[n-i][j];      
            matrix[n-i][j] = placeholder;
        }    
    }
    for i := 0; i<=n; i++{
        for j := 0; j<=i; j++{
            placeholder := matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = placeholder;
        }           
    }
    for i := 0; i<=n; i++{
        for j := 0; j<=n/2; j++{
            placeholder := matrix[i][j];
            matrix[i][j] = matrix[i][n-j];      
            matrix[i][n-j] = placeholder;
        }    
    }
};
