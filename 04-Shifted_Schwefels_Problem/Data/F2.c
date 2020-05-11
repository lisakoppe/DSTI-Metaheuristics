double Schwefel_Problem( int dim , double* x ){
    int i;
    double z;
    double F = abss(x[0]);
    for(i=1;i<dim;i++){
    	  z = x[i] - schwefel[i];
        F = max(F , abss(z));
    }
    return F + f_bias[1]; 
}