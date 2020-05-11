double Shifted_Rastrigin( int dim , double* x )
{
    int i;
    double z;
    double F = 0;
    for(i=0;i<dim;i++){  
        z = x[i] - rastrigin[i];
        F = F + ( pow(z,2) - 10*cos(2*pi*z) + 10);
    }
    return F + f_bias[3]; 
}