import pickle
cars=["Audi","Bmw","Maruti Suzuki","Harryti Isuzuki"]
file="myCar.pkl"
fileObj=open(file,"bw")
pickle.dump(cars,fileObj)

fileObj.close()
# read a file from pickle

files=open("myCar.pkl","rb")
myCar=pickle.load(files)
print(myCar)
print(type(myCar))