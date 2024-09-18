def response():
    # Function to return user input
    return input()

def symptom(patient, symptom_name):
    # Function to check if the patient has a specific symptom
    reply = input(f"Does {patient} have {symptom_name.replace(  '_' , ' ' )} (y/n)? ")
    # Returns True if the answer is  y , and False if it s  n 
    return reply.lower() ==  'y'

def hypotheses(patient):
    # Function to generate hypotheses about diseases based on symptoms
    # Checks for a set of symptoms to determine the illness

    if (symptom(patient, "fever") and symptom(patient, "cough") and 
        symptom(patient, "conjunctivitis") and symptom(patient, "runny_nose") and 
        symptom(patient, "rash")):
        return "measles"  # Measles
    
    elif (symptom(patient, "fever") and symptom(patient, "headache") and 
          symptom(patient, "runny_nose") and symptom(patient, "rash")):
        return "german measles"  # German Measles
    
    elif (symptom(patient, "fever") and symptom(patient, "headache") and 
          symptom(patient, "body_ache") and symptom(patient, "conjunctivitis") and 
          symptom(patient, "chills") and symptom(patient, "sore_throat") and 
          symptom(patient, "cough") and symptom(patient, "runny_nose")):
        return "flu"  # Influenza
    
    elif (symptom(patient, "headache") and symptom(patient, "sneezing") and 
          symptom(patient, "sore_throat") and symptom(patient, "chills") and 
          symptom(patient, "runny_nose")):
        return "common cold"  # Common Cold
    
    elif (symptom(patient, "fever") and symptom(patient, "swollen_glands")):
        return "mumps"  # Mumps
    
    elif (symptom(patient, "fever") and symptom(patient, "rash") and 
          symptom(patient, "body_ache") and symptom(patient, "chills")):
        return "chicken pox"  # Chicken Pox
    
    elif (symptom(patient, "cough") and symptom(patient, "sneezing") and 
          symptom(patient, "runny_nose")):
        return "whooping cough"  # Whooping Cough
    
    # New diseases
    elif (symptom(patient, "fever") and symptom(patient, "abdominal_pain") and 
          symptom(patient, "diarrhea") and symptom(patient, "headache")):
        return "typhoid"  # Typhoid Fever

    elif (symptom(patient, "fever") and symptom(patient, "joint_pain") and 
          symptom(patient, "rash") and symptom(patient, "bleeding_gums")):
        return "dengue"  # Dengue Fever

    
    elif (symptom(patient, "fever") and symptom(patient, "night_sweats") and 
          symptom(patient, "weight_loss") and symptom(patient, "persistent_cough")):
        return "tuberculosis"  # Tuberculosis

    elif (symptom(patient, "muscle_weakness") and symptom(patient, "difficulty_breathing") and 
          symptom(patient, "fatigue") and symptom(patient, "slurred_speech")):
        return "myasthenia gravis"  # Myasthenia Gravis

    elif (symptom(patient, "joint_pain") and symptom(patient, "stiffness") and 
          symptom(patient, "swelling") and symptom(patient, "fatigue")):
        return "rheumatoid arthritis"  # Rheumatoid Arthritis

    elif (symptom(patient, "chest_pain") and symptom(patient, "shortness_of_breath") and 
          symptom(patient, "dizziness") and symptom(patient, "nausea")):
        return "heart attack"  # Heart Attack

    elif (symptom(patient, "severe_headache") and symptom(patient, "nausea") and 
          symptom(patient, "sensitivity_to_light") and symptom(patient, "vision_problems")):
        return "migraine"  # Migraine

    return None  # If no disease is identified

def go():
    # Starting function to gather patient information
    patient = input("What is the patient s name? ")  # Input patient s name
    disease = hypotheses(patient)  # Get hypothesis based on symptoms
    
    if disease:
        print(f"{patient} probably has {disease}.")  # Print the result
    else:
        print("Sorry, I don t seem to be able to diagnose the disease.")  # If no disease is identified
    input()

if __name__ == "__main__":
    go()  # Start the program