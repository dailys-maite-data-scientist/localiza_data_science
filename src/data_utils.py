
import pandas as pd 

def run_data_quality_checks(df):
    """
    Executar diagnostico de integridade dos dados.
    """
    df_quality = pd.DataFrame({
        'Tipo': df.dtypes,
        'Nulos(#)': df.isnull().sum(),
        'Nulos(%)': (df.isnull().sum() / len(df)) * 100,
        'Valores Unicos': df.nunique(),
        'Duplicados(#)': df.duplicated().sum()
    })

    # Flag de alerta para alta cardinalidade ou muitos nulos
    df_quality['Status'] = df_quality.apply(
            lambda x: 'Alerta' if x['Nulos(%)'] > 0 or x['Valores Unicos'] > (len(df) * 0.9)
            else 'OK',
            axis=1
    )

    return df_quality
