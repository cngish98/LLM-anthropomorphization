"""Convert and export pandas dataframes as csv files."""


import csv


class ExportCSV:
    def __init__(self, df):
        """Writes a csv file.
        :param df: pandas dataframe with text and label columns
        """
        self.df = df

    def write_df_to_csv(self, filename):
        """

        :param filename: csv file name
        """
        file = open(f"{filename}.csv", "w")
        writer = csv.writer(file)
        writer.writerow(["text", "label"])
        for item in self.df:
            writer.writerow(item.values())
        file.close()
