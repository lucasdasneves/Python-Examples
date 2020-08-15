#encurtador.com.br/AIU15

def reg_simp(x,y):
    import numpy as np
    from scipy.stats.stats import pearsonr 
    
    #calculos necessários
    np.array(x)
    np.array(y)
    avg_x = np.mean(x)
    avg_y = np.mean(y)
    corr = pearsonr(x,y)
    std_x = np.std(x)
    std_y = np.std(y)
    
    #define B1
    B1 = round(corr[0] * (std_y/std_x),3)
    
    #define B0
    B0 = round(avg_y - (B1*avg_x),3)
    
    print ("O coeficiente B1 é: {}".format(B1))
    print ("O coeficiente B0 é: {}".format(B0))
    print("A equação fica definida como Y ={} + {} * X".format(B1,B0))

x = [1,2,4,3,8,9]
y = [1,3,3,2,5,6]

reg_simp(x,y)