import os
path = r'C:\Users\User\Bucket\ConnectedRepository\Covid19AnalysisInDashboard-Tableau\Images'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))