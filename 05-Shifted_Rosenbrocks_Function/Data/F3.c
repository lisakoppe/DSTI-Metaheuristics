double Shifted_Rosenbrock( int dim , double* x ){
    int i;
    double z[dim];
    double F = 0;

    for(i=0;i<dim;i++) z[i] = x[i] - rosenbrock[i] + 1;   

    for(i=0;i<dim-1;i++){    
        F = F + 100*( pow((pow(z[i],2)-z[i+1]) , 2) ) + pow((z[i]-1) , 2);
    }
    return F + f_bias[2]; 
}