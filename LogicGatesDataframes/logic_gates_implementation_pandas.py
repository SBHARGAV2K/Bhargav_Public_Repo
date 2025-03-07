import pandas as pd

def not_gate():
    df = pd.DataFrame(
        {
            'X':[0,1]
        }
    )
    df['NOT X'] = ~df['X'] + 2
    return df

def and_gate():
    df = pd.DataFrame(
        {
            'X':[0,0,1,1],
            'Y':[0,1,0,1]
        }
    )
    df['X AND Y'] = df['X'] & df['Y']
    return df

def or_gate():
    df = pd.DataFrame(
        {
            'X':[0,0,1,1],
            'Y':[0,1,0,1]
        }
    )
    df['X OR Y'] = df['X'] | df['Y']
    return df

def nand_nor_gates():
    df = pd.DataFrame(
        {
            'X':[0,0,1,1],
            'Y':[0,1,0,1]
        }
    )
    df['X NAND Y'] = ~(df['X'] & df['Y']) + 2 #NAND = NOT AND
    df['X NOR Y'] = ~(df['X'] | df['Y']) + 2 #NOR = NOT OR
    return df

def xor_xnor_gates():
    df = pd.DataFrame(
        {
            'X':[0,0,1,1],
            'Y':[0,1,0,1]
        }
    )
    df['X XOR Y'] = df['X'] ^ df['Y']
    df['X XNOR Y'] = ~(df['X'] ^ df['Y']) + 2 #XNOR = NOT XOR
    return df