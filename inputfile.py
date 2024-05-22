from pandas.core.common import flatten
from Model_trainer import ss
import pickle
 
def age_input():
    age = int(input('Enter the age: '))
    return list(ss.fit_transform([[age]]))

def sex_input():
    sex = int(input('Sex(1 for M/0 for F): '))
    return sex

def chestPainType_input():
    chestPainType = int(input('Enter the chestPainType(0 for ASY/1 for ATA/2 for NAP/3 for TA): '))
    return chestPainType

def restingBP_input():
    restingBP = int(input('Enter the restingBP: '))
    return list(ss.fit_transform([[restingBP]]))

def cholesterol_input():
    cholesterol = int(input('Enter the cholesterol: '))
    return list(ss.fit_transform([[cholesterol]]))

def fastingBS_input():
    fastingBS = int(input('Enter the fastingBS(0 if less than 120/ 1 if greater than or equal to 120): '))
    return fastingBS

def restingECG_input():
    restingECG = int(input('Enter the restingECG(0 for LVH/ 1 for Normal/ 2 for ST): '))
    return restingECG

def maxHR_input():
    maxHR = int(input('Enter the maxHR: '))
    return list(ss.fit_transform([[maxHR]]))

def exerciseAngina_input():
    exerciseAngina = int(input('Enter the exerciseAngina(1 for Yes/0 for No): '))
    return exerciseAngina

def sT_Slope_input():
    sT_Slope = int(input('Enter the sT_Slope(0 for Down/1 for Flat/ 2 for Up): '))
    return sT_Slope

def predict_and_generate_output(final_input_list,classifier_lr):
    output_data = classifier_lr.predict([final_input_list])
    return 'The person has a possibility to have a heart disease.' if output_data == 1 else 'The person does not has a possibility to have a heart disease.'

def take_inputs(user_input_list):
    '''
    This method is created for only to take input from the user.
    This method calls a bunch of other methods to take inputs and 
    appends the returned value in the input list provided by the user
    and returns a flattened numpy arrray.
    '''
    print("-------------------------------------------------------------------------")
    user_input_list.append(age_input())
    user_input_list.append(sex_input())
    user_input_list.append(chestPainType_input())
    user_input_list.append(restingBP_input())
    user_input_list.append(cholesterol_input())
    user_input_list.append(fastingBS_input())
    user_input_list.append(restingECG_input())
    user_input_list.append(maxHR_input())
    user_input_list.append(exerciseAngina_input())
    user_input_list.append(sT_Slope_input())
    print("-------------------------------------------------------------------------")
    return list(flatten(user_input_list))

def output_generator():
    
    classifier_lr = pickle.load(open('F:/Python_VS_Code/heart_disease_project/trained_categorial_boosting_classifier.sav', 'rb'))
    user_input_list = list()
    final_input_list = take_inputs(user_input_list)
    message = predict_and_generate_output(final_input_list, classifier_lr)
    print("-------------------------------------------------------------------------")
    print(message)
    print("-------------------------------------------------------------------------")
    
# output_generator()