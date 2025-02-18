"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import os
import pandas as pd


def clean_text(columnilla):
    return columnilla.str.lower().str.replace("-", " ").str.replace("_", " ").str.strip()


def fechas(dts):
    fechas = pd.to_datetime(dts, dayfirst=True, errors="coerce")
    fechas = fechas.fillna(
        pd.to_datetime(dts, format="%Y/%m/%d", errors="coerce")
    )
    return fechas


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    inp = "files/input/solicitudes_de_credito.csv"
    oup = "files/output/solicitudes_de_credito.csv"

    dfp = pd.read_csv(inp, sep=";", index_col=0)

    dfp.drop_duplicates(inplace=True)
    dfp.dropna(inplace=True)

    dfp["sexo"] = dfp["sexo"].str.lower()
    dfp["tipo_de_emprendimiento"] = dfp["tipo_de_emprendimiento"].str.lower()
    dfp["barrio"] = dfp["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    columnillas = [
        "idea_negocio",
        "línea_credito",
    ]
    for columnilla in columnillas:
        dfp[columnilla] = clean_text(dfp[columnilla])

    dfp["monto_del_credito"] = (
        dfp["monto_del_credito"]
        .str.strip()
        .str.replace("$", "")
        .str.replace(",", "")
        .str.replace(".00", "")
        .astype(int)
    )
    dfp["fecha_de_beneficio"] = fechas(dfp["fecha_de_beneficio"])

    dfp.drop_duplicates(inplace=True)

    if os.path.exists(oup):
        os.remove(oup)

    os.makedirs(os.path.dirname(oup), exist_ok=True)
    dfp.to_csv(oup, sep=";")

    print(dfp["sexo"].value_counts())
    print(dfp["barrio"].value_counts())


pregunta_01()