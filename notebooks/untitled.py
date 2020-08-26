# Analysing Missing Value

def analyse_na_value(df=None,var_col=None,target_col=None):
    df = df.copy()
    
    # let's make a variable that indicates 1 if the observation was missing or zero otherwise
    df[var_col] = np.where(df[var_col].isnull(), 1, 0)
    
    # let's calculate the mean SalePrice where the information is missing or present
    df.groupby(var_col)[target_col].median().plot.bar()
    plt.title(var_col +" _ medain price")
    plt.show()
    df.groupby(var_col)[target_col].std().plot.bar()
    plt.title(var_col + " _ std price")
    plt.show()
    
    df.groupby(var_col)[target_col].mean().plot.bar()
    plt.title(var_col + " _ mean price")
    plt.show()