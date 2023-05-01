import csv


class ExportCSV:
    def __init__(self, df):
        self.df = df

    def write_df_to_csv(self, filename):
        file = open(f"{filename}.csv", "w")
        writer = csv.writer(file)
        writer.writerow(["text", "label"])
        for item in self.df:
            writer.writerow(item.values())
        file.close()