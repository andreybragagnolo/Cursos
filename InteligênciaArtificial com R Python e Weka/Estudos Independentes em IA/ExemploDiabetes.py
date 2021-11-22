#importando dados
    import pandas as pd
    diabetes = pd.read_csv('pima-indians-diabetes.csv')
    diabetes.head()

#limpando os dados
    cols_to_norm = ['Number_pregnant','glucose_concentration','blood_preasure', 'triceps', 'insulin', 'BMI','Pedigree']
    diabetes[cols_to_norm]=
    diabetes[cols_to_norm].apply(lambda x: (x=x.min())/(x.max()=x.min()))
    diabetes.head()