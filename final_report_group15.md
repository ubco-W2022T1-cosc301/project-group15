# Group 15 Final Report

## Introduction
Our group decided to perform an analysis on video game data because 

The dataset that we used is data from Steam, a popular online game store. The dataset includes information such as pricing, genre, release date, tags (which includes information on what features the game implements and/or type of game that it is), developer, publisher, languages, achievements, and much more. We obtained this data from Kaggle, an online database that hosts datasets. This data is under the CC0 (public domain) Licence and originally contained over 40 thousand steam games. The data was originally collected in the middle of 2019.

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
