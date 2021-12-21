# PFCH_Final
<h2>Final Project for Programming for Cultural Heritage class Fall 2021</h2>

<h3>Project Description</h3>

This project was undertaken as part of an ongoing project of The New School’s Libraries, Collections, and Academic Services department, where I work as a Library Technology Assistant, to redesign our [website](https://library.newschool.edu/). As part of this project, we worked with Institutional Research to conduct a survey of the students and faculty at The New School about what they thought of our current website, and how they use library websites in general. The survey was live on Qualtrics for six weeks, from September 29, 2021 until November 11, 2021, and was sent to 14,817 people via email; 12,433 students and 2,384 faculty. Though data was recorded for 1,265 surveys, only 826 of these were finished, and only these complete results are being included, giving us an overall response rate of 5.6%; 17.7% for faculty (who submitted 422 responses) and 3.2% for students (who submitted 404).

Once the survey was closed, I exported the results as a CSV and stripped the data of all identifying information. I also renamed some of the columns for clarity and to streamline the coding process later. This master file was named SurveyData.csv, and is not included here for privacy reasons. The DatasetParser.py script creates separate csvs from this file for faculty and student responses, then further splits the student responses out into Undergraduate, Graduate, and Continuing Education students. Though the code in this project focuses on the overall results with some investigation into the differences in faculty and overall student responses, further exploration will be done in the future on the differences in responses between different student types.

The rest of the scripts in this project focus on different aspects of the data, which are further explained in the “How to Use this Code” section of this file. Since most of the exported data was in text form, and many of the survey questions utilized a “check all that apply” approach, I used For loops to count specific responses to different questions. Using [pandas](https://pandas.pydata.org/), I then formatted this data  for plotting with [Seaborn](https://seaborn.pydata.org/) and [MatPlotLib](https://matplotlib.org/). I also worked closely with my supervisor, Assistant Director for Library Systems Joshua Dull, to do some text analysis on the short answer questions in the survey. This involved using [Natural Language Toolkit](https://www.nltk.org/) to filter these responses using stopwords and other extraneous words I discovered as I worked with the data. These filtered responses were then analyzed for the most commonly occurring words in each question, as well as the most commonly occurring collocated words, which give us a better sense of the context in which these words are used. In addition to plotting the most commonly used words with seaborn, I also used the [Wordcloud](https://pypi.org/project/wordcloud/) module to generate word clouds for these questions.

This data and the charts it generated, which are included here, will inform the next stages in our website design process, helping us determine what our users want us to prioritize and what changes they would like to see. 

Special thanks to The New School’s Institutional Research office, Joshua Dull, and Allen Jones.

<h3>Survey Questions</h3>
<ol>
<li>How often do you currently visit the library in person? 
<ul><li>Multiple visits per day
  <li>Once a day
  <li>2-3 times per week
  <li>Once a week
  <li>2-3 times per month
  <li>Once per semester
  <li>Never</ul>
<li>How often do you currently visit the library website?    
<ul><li>Multiple visits per day
  <li>Once a day
  <li>2-3 times per week
  <li>Once a week
  <li>2-3 times per month
  <li>Once per semester
  <li>Never</ul>
<li>Why do you come to the library in person? Check all that apply. 
<ul><li>To print or scan documents
  <li>To use the public desktops or circulating laptops
  <li>To use a private/bookable space
  <li>To use a public study area
  <li>To get research help from a library staff member
  <li>To browse the stacks/find resources
  <li>Other</ul>
<li>Why do you use the library website? Check all that apply.  
<ul><li>To find out what technology is available for me to use
  <li>To find library hours
  <li>To reserve study space
  <li>To check on my loans
  <li>To get help from a library staff member
  <li>To find research materials
  <li>To find out about library locations
  <li>Other</ul>
<li>On your last visit to the library website, did you find what you were looking for? 
<ul><li>Yes
  <li>No
  <li>I Don’t Remember
  <li>I Don’t Use the Library Website</ul>
<li>Rate the following aspects of the website: 
  <ul><li>Navigability
  <li>Information Clarity
  <li>Getting Help
  <li>Overall Experience
  <li>Ratings
    <ul><li>Very Poor
      <li>Poor
        <li>Average
          <li>Good
      <li>Excellent</ul></ul>
<li>If you have additional information on your last visit that you would like to share, please do so here.
<li>What do you like about the library's current website?
<li>What do you dislike about the library's current website?
<li>What feature(s) do you wish our website had?
<li>Are there any features of the library website that confuse you? If so, what are they?
<li>What other library websites do you visit? 
<ul><li>New York Public Library
  <li>Brooklyn Public Library
  <li>Queens Public Library
  <li>NYU
  <li>Cooper Union
  <li>Other
  <li>None/Not Applicable</ul>
<li>Why do you use [Other Library]'s website? Check all that apply. 
<ul><li>To find out what technology is available for me to use
  <li>To find library hours
  <li>To find out about library locations
  <li>To reserve study space
  <li>To check on my loans (i.e. fines, due dates, Inter-Library Loan requests, etc.)
  <li>To get help from a library staff member
  <li>To find research materials
  <li>Other</ul>
<li>What do you like about [Other Library]'s website? 
<ul><li>The site is easy to navigate
  <li>The site is well-written with clear information
  <li>It is easy to get help from a staff member if I need it
  <li>Other</ul></ol>


<h3>How to Use this Code</h3>

Per The New School’s Privacy and Data Protection Policy, the dataset used for this project (‘SurveyData.csv’) is not included here. To request access to this data, contact Katie Sweatman at [sweatmak@newschool.edu](mailto:sweatmak@newschool.edu)

To begin analyzing SurveyData.csv, use the script <strong>DatasetParser.py</strong> to separate out faculty and student results as separate CSVs. These will be analyzed later.

The functions of the other script files are outlined below:
<ul>
<li><strong>PieCharts.py</strong>: This file creates pie charts, specifically of the types of respondents to the survey and whether they found what they were looking for on their last visit to The New School Library website. 
<li><strong>Use.py</strong>: This file explores different aspects of patrons’ use of the library and library website, comparing how often they use the website versus the physical library and what they use each for, and comparing the responses of faculty and students. 
<li><strong>Ratings.py</strong>: Respondents were asked in the survey to rate the following aspects of the library website on a 5-point Likert scale: Navigability, Information Clarity, Getting Help, and Overall Experience. This file analyzes those ratings and presents them as stacked percentage bar charts.
<li><strong>OtherLib.py</strong>: Respondents were asked what other library websites they use, why they use them, and what they like about them. This file analyzes those responses.
<li><strong>LanguageParser.py</strong>: Using Natural Language Toolkit, this file filters and analyzes the text responses to the short answer questions in the survey, calculating the most frequently used words and most commonly occurring collocated words. It also generates word clouds for several of these questions using the Wordcloud module.
  </ul>
