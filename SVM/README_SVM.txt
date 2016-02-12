Setup::
1. Install Weka 3.6 (setup/weka-3-6-13jre-x64.exe)
2. Unzip SVM Library(setup/libsvm-3.20.zip)
3. Add Environment Variable in system
	a. New System variable:
	b. Variable Name: CLASSPATH
	c. Variable Value: ...setup\libsvm-3.20\java\libsvm.jar

Run:
1. Open Weka 3.6
2. Open Application->Explorer
3. In tab "Preprocess":
	a. Choose 'Open file...' to open csv file of raw data.
	b. In 'Filters', Choose weka->filters->unsupervised->attribute->NumerictoNominal
	c. Apply filter
4. In tab "Classify": 
	a. In Classifier, Choose weka->classifier->function->LibSVM
	b. Choose Test options radio button with FOLDS:5
	c. Start

NOTE:
Preprocess:
1. Make sure your data has unique attribute names.
2. Attribute names are in first row of the csv file.
3. Add Class labels to the data file itself.
4. Last column in the csv file is the Class label.

Results:
1. Summary shows Accuracy.
2. 'Detailed Accuracy By Class' shows the computed results of each attribute.
3. 'Confusion Matrix' shows the predicted class vs the correct labels. 
