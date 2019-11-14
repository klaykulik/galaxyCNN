import pandas as pd
import glob, os, shutil

path_to_images = "/Users/deepak/Downloads/efigi-1.6/png/"
png_files = glob.glob(path_to_images+"*.png")
labels = ["elliptical", "lenticular", "spiral", "irregular", "dwarf"]
ehs_type_to_labels = {
	"-6": "elliptical",
	"-5": "elliptical",
	"-4": "elliptical",
	"-3": "lenticular",
	"-2": "lenticular",
	"-1": "lenticular",
	"0": "spiral",
	"1": "spiral",
	"2": "spiral",
	"3": "spiral",
	"4": "spiral",
	"5": "spiral",
	"6": "spiral",
	"7": "spiral",
	"8": "spiral",
	"9": "spiral",
	"10": "irregular",
	"11": "dwarf"
}

efigi_attributes = pd.read_csv("EFIGI_attributes.txt", delimiter="\t", skiprows=81)

for label in labels:
	os.makedirs("./images/"+label, exist_ok = True)

for file_path in png_files:
	ehs_type = efigi_attributes.loc[efigi_attributes.PGCname == file_path.split("/")[-1].split(".")[0]]["T"].values[0]
	shutil.copy(file_path, "./images/"+ehs_type_to_labels[str(ehs_type)]+"/")
