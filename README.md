<div id="top"></div>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
<h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>

[![Contributors][contributors-shield]][https://github.com/jakubzolkos][https://github.com/najdamikolaj00]
[![Forks][forks-shield]][https://github.com/jakubzolkos/sobriety-voice-detection/network/members]
[![Stargazers][stars-shield]][https://github.com/jakubzolkos/sobriety-voice-detection/stargazers]
[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/jakub-zolkos-20b0301b7/]


# Sobriety Detection via Voice Analysis

A Python program for determining whether a person is in the state of alcohol intoxication. The model used for classification consists of an ensemble of machine learning techniques such as random forest, categorical boosting, and extreme gradient boosting.  

<!-- TABLE OF CONTENTS -->

  <summary>Table of Contents</summary>
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

According to the data collected by the NHTSA, in 2019 in the United States, 10142 people died as a result of alcohol-impaired driving. A considerably high number of drinking-related road accidents prompts many public authorities to seek legal solutions, such as fines or imprisonment, that would discourage people from driving under the influence. However, those methods frequently yield unsatisfactory results. Our idea is to make a voice-detecting system embedded in a vehicle that would prevent the driver from activating the vehicle's engine if their voice points towards prior alcohol consumption. 

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

The program uses several third-party libraries to perform preprocessing and data classification. They can all be installed si
* npm
  ```sh
  npm install npm@latest -g
  ```

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

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- Feature 1
- Feature 2
- Feature 3
    - Nested Feature

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments 

* []() We would like to express our gratitude to every volunteer who agreed to share their voice for the purpose of our experiment.
* []() 
* []()

<p align="right">(<a href="#top">back to top</a>)</p>


