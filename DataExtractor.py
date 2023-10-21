class DataExtractor:
    def extract(self,path):
        data_lines = []
        with open(path) as data:
            next(data)
            for row in data:
                lines = row.split()
                data_lines.append(lines)

        return data_lines
