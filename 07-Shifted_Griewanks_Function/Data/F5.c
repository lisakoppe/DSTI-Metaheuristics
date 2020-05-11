double Shifted_Griewank( int dim , double* x ){
    int i;
    double z;
    double F1 = 0;
    double F2 = 1;
    for(i=0;i<dim;i++){       
        z = x[i] - griewank[i];
        F1 = F1 + ( pow(z,2) / 4000 );
        F2 = F2 * ( cos(z/sqrt(i+1)));

    }
    return (F1 - F2 + 1 + f_bias[4]); 
}