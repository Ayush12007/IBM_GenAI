# MCQ Generator Project

## Description

This project is an MCQ (Multiple Choice Question) generator built using **Streamlit** and **OpenAI** API. It takes a given topic as input and generates multiple-choice questions based on that topic. The application is designed to help users quickly generate questions for quiz creation, study materials, or any educational purpose.

The backend of the project integrates with a **free AI platform** (Hugging Face, OpenAI, etc.) to generate the questions dynamically.

## Features

- Generate multiple-choice questions based on any input topic.
- Use an AI platform to dynamically create MCQs.
- User-friendly interface built with **Streamlit**.
- Easy integration with **OpenAI API** for generating AI-powered questions.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/mcq-generator.git
    cd mcq-generator
    ```

2. **Install dependencies**:

    Ensure you have Python 3.10 or later installed, and then install the necessary libraries.

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment variables**:

    Create a `.env` file in the root directory of the project and add the following variables:

    ```env
    OPENAI_API_KEY=your-openai-api-key
    ```

    Make sure you replace the values with your actual API keys.

4. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

5. Open the URL given by Streamlit in your browser to start generating MCQs.

## Usage

1. Enter a topic for which you want to generate MCQs.
2. Select the number of questions you want to generate.
3. Click on "Generate" and the app will display the generated MCQs.
4. Review the MCQs and use them as required.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and make changes. Open a pull request if you'd like to propose your changes.

## License

This project is licensed under the MIT License.

## Author

**Name**: Ayush Thakare  
**Reg No**: 22BSA10051

## Acknowledgments

- **Streamlit** for building the front-end interface.
- **OpenAI** for the GPT-3 model API for question generation.
- **Hugging Face** for providing other useful models for AI-based projects.

---

Feel free to adjust the details to match your project's specifics. Let me know if you need any modifications or additions to this `README.md` file!
