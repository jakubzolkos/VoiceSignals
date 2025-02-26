
# Sobriety Detection via Voice Analysis

A Python program for determining whether a person is in the state of alcohol intoxication. The model used for classification consists of a majority vote ensemble of machine learning algorithms such as random forest, categorical boosting, and extreme gradient boosting.  

<!-- TABLE OF CONTENTS -->

### Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>

<!-- ABOUT THE PROJECT -->
## About The Project

According to the data collected by the NHTSA, in 2019 in the United States, 10142 people died as a result of alcohol-impaired driving. A considerably high number of drinking-related road accidents prompts many public authorities to seek legal solutions, such as fines or imprisonment, that would discourage people from driving under the influence. However, those methods frequently yield unsatisfactory results. Our idea is to make a voice-detecting system embedded in a vehicle that would passively monitor whether the driver's voice suggests prior alcohol consumption. 
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Librosa](https://librosa.org/doc/latest/index.html)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Catboost](https://catboost.ai/en/docs/concepts/python-usages-examples)
* [XGBoost](https://xgboost.readthedocs.io/en/stable/python/python_intro.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
The program utilizes numerous machine learning and preprocessing libraries. For convenience, all the prerequisites have been listed in requirements.txt file and can be simultaneously installed using pip command specified in the installation section.

### Installation

Open the terminal and change the directory to where you would like download the project.

1. Clone the repo
   ```sh
   git clone https://github.com/jakubzolkos/sobriety-voice-detection.git
   ```
2. Install prerequisites
   ```sh
   pip install -r requirements.txt
   ```
3. Run the program with the classification model inside sobriety_detection folder
   ```sh
   python3 main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Inside main.py in sobriety_detection folder initialize preprocessing variable
   ```sh
   data = AudioPreprocessing()
   ```
2. Import a voice recording you wish to analyze
   ```sh
   data.import_audio(PATH)
   ```
3. Extract features from the recording and store them in a .csv file
   ```sh
   data.save_csv(SAVE_PATH)
   ```
4. Perform classification
   ```sh
   X_train, X_test, y_train, y_test = data.model_data_split(test_set_size, random_state, PATH_TO_CSV_FEATURES)
   model = SobrietyClassifier()
   model.fit(X_train, y_train)
   predictions = model.predict(X_test)
   ```
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the GPL 2.0 License. See `LICENSE.md` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments 

* []() We would like to express our gratitude to every volunteer who agreed to share their voice for the purpose of our experiment.
* []() Many thanks to Mikolaj Najda for his substantial work on the project (https://github.com/najdamikolaj00)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
