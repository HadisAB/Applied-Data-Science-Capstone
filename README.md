# Applied-Data-Science-Capstone
This project is an IBM Data Science complete project.

# Goal
we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch. 


# Results summary:
Based on feature engineering, the most impacted features on predicting a successful landing are Payload mass, Flight number, Booster Version and Orbit.<br/>
With having these feature and using the DecisionTree model with 88.88% accuracy, we can predict the success or failure landing. <br/>

These results are also obtained from the analysis:<br/>
- VLEO has complete success rate for flight number more than 80. HEO has 100% success rate.<br/>
- For the VAFB-SLC launch site there are no rockets launched for heavy payload mass(greater than 10000).<br/>
- For the payload less than 5000, the KSC LC 39A has 100% success rate.<br/>
- KSC LC-39A is the site with the best success rate.<br/>
- ES-L1, GEO, HEO and SSO have the most success rate.<br/>


#### Models accuracy

<img src=https://github.com/HadisAB/Applied-Data-Science-Capstone/blob/main/ModelAccuracy.png />

<br/>

#### Confusion Matrix 
Consiion Matrix of Decision Tree model:

<img src=https://github.com/HadisAB/Applied-Data-Science-Capstone/blob/main/ConfusionMatrix.png />
