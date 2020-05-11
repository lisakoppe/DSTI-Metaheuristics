double Shifted_Sphere( int dim , double* x ){
    int i;
    double z;
    double F = 0;
    for(i=0;i<dim;i++){
        z = x[i] - sphere[i];
        F += z*z;
    }
    return F + f_bias[0];
}