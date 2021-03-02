import pandas as pd

class Description():
    def __init__(self, disease):
        self.disease = disease

    def display(self):
        
        description = pd.read_csv('dataset/symptom_Description.csv')
        return list(
            description[description['Disease'] == f'{self.disease}']['Description']
        )[0]

if __name__ == "__main__":
    dis = Description('Migraine')
    print(dis.display())
