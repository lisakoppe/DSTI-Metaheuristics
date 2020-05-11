double Shifted_Ackley( int dim , double* x ){
    int i;
    double z;
    double Sum1 = 0;
    double Sum2 = 0;
    double F = 0;
    for(i=0;i<dim;i++){   
        z = x[i] - ackley[i];
        Sum1 = Sum1 + pow(z , 2 );
        Sum2 = Sum2 + cos(2*pi*z);
    }
    F = -20*exp(-0.2*sqrt(Sum1/dim)) -exp(Sum2/dim) + 20 + e + f_bias[5];

    return F; 
}