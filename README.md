# final-project

1) PROPOSAL

Team members:
Vanessa Tobar		454455		
Marlene Saint Martin	454351

Objective:

Analyze whether there is a relationship between suicides, violent crimes, and income distribution in New York by county. More specifically, we would like to merge these databases, present the more relevant variables in a table, allow to build summary statistics by county, and run regressions in maps. 

Relevant questions:
	Is there a correlation between “violent” counties and the percentage of suicides?
	Are suicides more probable in poor or rich counties?
	What are the demographics in counties where suicides are more common?
	How have suicide rates changed over the years?
	If suicide rates present a relevant correlation with certain variables i.e. income, group age, ethnicity, could policy makers use this information to conduct a more detailed research for those groups in order to find the underlying causes of suicide and target policies to prevent it?   

Data sources:
https://health.data.ny.gov/Health/Vital-Statistics-Deaths-by-Resident-County-Region-/eyur-mqqm
https://health.data.ny.gov/Health/Vital-Statistics-Suicide-Deaths-by-Age-Group-Race-/j6fz-a4ta
https://data.ny.gov/Public-Safety/Index-Crimes-by-County-and-Agency-Beginning-1990/ca8h-8gjq
https://health.data.ny.gov/Health/New-York-State-Population-Data-Beginning-2003/e9uj-s3sf
https://data.ny.gov/Government-Finance/Average-Income-and-Tax-Liability-of-Full-Year-Resi/2w9v-ejxd

2) MERGING DATA

As seen in data sources above, the data was downloaded as csv files from the data.ny.gov portal. In the file "MERGING.PY" you can follow our steps as we merged all the data by county. In order to do so we had to clean the data first, sliced the dataframes and merged them using two keys (year and county). You can find the csv files we used as well if you are interested in going through the process. The final dataset we end up and that we use in our project is MASTER1.CSV which you can also find in our repository.

3) APPS

We created apps for every main section in our webpage. We had then: "home", "prevention", "Data", "Analysis", and "About us". In each of these apps we have a folder called "templates". In this folder, you can find the skeleton of all the HTML files we used. In home, there is only one html (home.html). In prevention, there are three skeletons (basep.html, risk.html, support.html). In Data, there are three skeletons (baseny.html, data1.html, data2.html). In Analysis, there are two skeletons (analysis.html, crime.html). Finally, in About us there are three skeletons (basea.html, mission.html, team.html). 

4) TEMPLATES - HTML FILES

In our html files we are working with style, format, and a very cool navbar (this is one of the preetiest things we did and it required a lot of time to make it that pretty, please CONSIDER). Also, we are including videos, images, a logo design (not our own but still we had to find one with pretty colors adoc), and hyperlinks. We also worked with forms (YearsForm) to present tables and graphs in the Data Section. 

5) PANDAS: MERGE/TABLES/GRAPHS

We used Pandas a lot. We used it to merge the files (previously mentioned) and then to create the graphs (10 displayed in the by county section in Analysis; 10 displayed in the by year section in Analysis). You can see them in Age Group.ipynb. We customized the format in our graphs by creating a style of colors. The steps that we took to develop the graphs and tables used in our website (Data/data1 and Data/data2) can be found in the file views of the App "Data". Another point mentioning is that our tables and graphs are very pretty (and that took some HOURS). 

6) BONUS - SEXY, OR NOT, REGRESSION TIME

We did a regression using our data in Pandas. You can find the steps in the file Regression.ipynb

7) CONCLUSION

This was hard. VERY. We particularly enjoyed using Pandas and playing with the html skeletons to get a professional/pretty format and information. However there were a lot of things that we didn't know how to do. Our biggest problems were the navbar, making the forms work and connecting the form with our graphs. We spent almost 50 hours working on this final project. We used stackflow (we now can understand discussions YEIII), tutorials you referenced in the slides and even youtube videos to work out things. Still, it was very embarrasing when we took these concerns to you and you were able to solve them in 2 minutes or less. Thus, this course was succesfull in introducing us to the "art" of programming but we still have a long way to go if we want to develop a relationship as close as what you have with Princess Duck. 

Thank you for spending so much of your time in hearing and solving our freak-outs!



