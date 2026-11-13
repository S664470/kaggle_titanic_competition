import pandas as pd

class TitanicDataPipline:
    def __init__(self, train_path, test_path):
        #Intiating the class and reading the data pipline
        self.train_df = pd.read_csv(train_path)
        self.test_df = pd.read_csv(test_path)
        pass

    def Explor_data(self):
        #This function to check 
        print("Printing the origunal data befor cleaning")
        print(self.train_df)
        print("Exploring coulumns with missing values")
        print(self.train_df.info())
        print(self.train_df.isnull().sum())


if __name__ == "__main__":
    train_file = "train.csv"

    pipline = TitanicDataPipline(train_path=train_file)
    pipline.Explor_data()