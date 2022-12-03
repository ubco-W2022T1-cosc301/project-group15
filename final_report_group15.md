# Group 15 Final Report

## Introduction (+!-!+Incomplete+!-!+)
Our group decided to perform an analysis on video game data because 

The dataset that we used is data from Steam, a popular online game store. The dataset includes information such as pricing, genre, release date, tags (which includes information on what features the game implements and/or type of game that it is), developer, publisher, languages, achievements, and much more. We obtained this data from Kaggle, an online database that hosts datasets. This data is under the CC0 (public domain) Licence and originally contained over 40 thousand steam games. The data was originally collected in the middle of 2019.

## Explorative Data Analysis (+!-!+Incomplete+!-!+)
Our group's EDA mostly consisted of looking at the data manually and figuring out what we can clean up and wrangle in our data pipeline. This was due to the dataset we chose containing a lot of text that needed to be separated out into numerical and boolean values befoe they can be put into use for the analysis.

For example, we separated out the year from the release date and converted it into a numerical value. We also separated out the tags into individual columns and converted them into boolean values. This was done so that we can use the data for our analysis.

In part 2 of the analysis, we also wrote functions to further separate and wrangle large amounts of data which were all crammed into individual cells in the original dataset. The game tags and language columns were the most difficult to wrangle because they contained a lot of data in the form of text.

## Analysis - Part 1
In this part of the data analysis, I attempted to answer some questions on game trends over time. Such as how the game's prices changed, how many games were developed, did more or less games implement online functionalities such as online multiplayer, and did more or less game developers add achievements to their games.

Since the data was originally collected in the middle of 2019, there were a lot of games which were pending release that was not yet added to this dataset, so I decided to cut out all entries from 2019 and onward and only left the years which had a complete list of games.

The dataset also contained a lot of text and missing information. So after filtering out useless columns and rows, I was left with around 2000 entries of good data.
Plotting various values from the filtered data against the release year, we can see some interesting trends in the fields of average price, online multiplayer implementation, games released each year, and achievement implementation.

### Image 1
On the first graph, which is the number of games released each year, we can see that the graph follows an exponential curve. This follows the development trend of technology over those years and from this graph, we can see that the cleaned and wrangled dataset appears to be accurate enough for use in this data analysis.

<img src="images\Final Report Images\Edwin\Games released per year.png">

### Image 2
The second graph that you can see here shows the number of games that implemented online multiplayer over the years. I filtered the tags in the original dataset and marked games which had a tag of both "online" and "multiplayer" to be ones that implemented online multiplayer. We can see from this graph that there were some games which implemented online multiplayer before 2010, but the 2010's are where online multiplayer games really took off. After a bit of searching, I found that just before 2010 is where there was a massive boom in streaming services. Netflix, Hulu, and Amazon Prime Video launched streaming services in 2007, 2008, and 2006 respectively. This boom in streaming services, and the rise of internet connected entertainment in general seems to have kickstarted many developers to start implementing online multiplayer into their games.

<img src="images\Final Report Images\Edwin\Multiplayer games per year.png">

### Image 3
In the third graph, I plotted the average prices of the games and the consumer price index. From here, we can see that despite games becoming more and more complicated and taking more and more money to produce, the average price of games follows closely with the consumer price index. Every 10 points that the consumer price index rises corresponds to about a dollar of the average game price rising. This phenomenon where the average game price follows this closely with the CPI indicates that the gaming industry grew at a steady pace and didn't experience any major disruptions.

<img src="images\Final Report Images\Edwin\Avg price per year vs CPI.png">

### Image 4
The last graph that I have plotted is the number of games that implemented achievements, and the number of achievements in the game year over year. We can see from this graph that a lot more developers have started to implement achievements into their games but there are not that many games that have a huge number of achievements. This graph suggests to me that having an achievement system boosts either the popularity, rating, or money earned by the game. But we can also see that the number of achievements implemented per game remains relatively steady, with most games implementing a maximum of around 150 achievements. This might be because that there is diminishing returns with implementing more achievements into the game so the developers don't bother with it.

<img src="images\Final Report Images\Edwin\Achievement implementation.png">

### Analysis - Part 1 conclusion
From these graphs, we can see how the number of games released matches with the rate of historical technological development, how the rise of internet entertainment has caused developers to make more online games, how prices of games have changed over time while closely following the consumer price index, and how developers have implemented achievements in their games.

## Analysis - Part 2
In the 2nd part of data analysis, I will analysis how many games are in different types of unique genre and game tags with different available languages in games on steam platform in between 1990 to 2018.

There are a lot incomplete and missing data in the dataset. Therefore, after filtering out missing value from columns and rows in the dataset, some data in the graph will show lesser than expected (around 2500 rows of complete data).

### Image 1
On the first graph shows the number of different types of genre from 1990 to 2018. We can see that Indie type is the most used genre tag in steam games, and it is in 107 different games. Along with the second most used genre tag is action type of game

On the first graph, which is the number of games released each year, we can see that the graph follows an exponential curve. This follows the development trend of technology over those years and from this graph, we can see that the cleaned and wrangled dataset appears to be accurate enough for use in this data analysis.

<img src="images\Final Report Images\Adrian\Genre.png">


<img src="images\Final Report Images\Adrian\Genre2018.png">

<img src="images\Final Report Images\Adrian\GameTag.png">

<img src="images\Final Report Images\Adrian\GameTag2018.png">

<img src="images\Final Report Images\Adrian\Language.png">

<img src="images\Final Report Images\Adrian\Language2018.png">

## Analysis - Part 3

## Conclusion (+!-!+Incomplete+!-!+)