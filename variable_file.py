import pickle

values_repository = {'Male' : 1,  'Female' : 0, 'Asymptomatic(ASY)': 0, 'Atypical Angina(ATA)' : 1,
                    'Non-Anginal Pain(NAP)' : 2, 'Typical Angina(TA)' : 3, 'less than 120' : 0,
                    '120 or more' : 1, 'LVH' : 0, 'Normal' : 1, 'ST' :2, 'Yes' : 1, 'No': 0,
                    'Down' : 0, 'Flat' : 1, 'Up' : 2}

sex_list = ['Male', 'Female']

chestPainTypeList = ['Asymptomatic(ASY)', 'Atypical Angina(ATA)', 'Non-Anginal Pain(NAP)', 'Typical Angina(TA)']

fastinBS_list = ['less than 120', '120 or more']

restingECG_list = ['LVH', 'Normal', 'ST']

exerciseAngina_list = ['Yes', 'No']

st_Slope_list = ['Down', 'Flat', 'Up']

classifier_catboost = pickle.load(open('F:/Coding/Python_VS_Code/heart_disease_project/trained_models/trained_categorial_boosting_classifier.sav', 'rb'))
